import os
import urllib.request
import gzip
import sys
from time import time

def progress(count, blocksize, total_size):
    global start
    if count ==0:
        start = time()
    sys.stdout.write('\rDownloaded {}% of {}MB -- ETA {}m'.format(int(100*count * blocksize / total_size), total_size // (1024*1024), int((time() - start) * total_size / (count * blocksize + 1)/60)))
    sys.stdout.flush()

class Avianbase:
    def __init__(self, filename='links1.txt', out_dir='./tmp', cache=False):
        super().__init__()
        self.links = self._load_links(filename)
        self.tmp_dir = out_dir
        self.cache = cache # Whether to keep genomes on disk in tmp folder

    def _load_links(self, filename):
        return open(filename).readlines()

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i >= len(self.links):
            raise StopIteration
        
        if not self.cache:
            try:
                os.removedirs(self.tmp_dir)
            except:
                pass

        # Download genome
        os.makedirs('./tmp', exist_ok=True)
        fname = os.path.join(self.tmp_dir, '{}.gz'.format(self.i))
        if not os.path.exists(fname):
            url = self.links[self.i]
            print('Downloading genome ', url)
            urllib.request.urlretrieve(url, fname, progress)
        self.i += 1
        
        return self.links[self.i - 1], gzip.open(fname)