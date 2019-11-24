import avianbase
from io import StringIO, BytesIO
from minhash import minhash

def test_avianbase():
    a = avianbase.Avianbase(cache=True)

    for url, g in a:
        with g as f:
            print(f.readline())

def test_kmers_from_file():
    fstring = b"ABC\nABC\nABC"
    f = BytesIO(fstring)
    k = avianbase.kmers_from_file(f, 3)
    kmers = set([b'ABC',b'BCA',b'CAB'])
    assert set(k) == kmers

    fstring = b'>comment\nHELLO>comment\n'
    f = BytesIO(fstring)
    k = avianbase.kmers_from_file(f, 3)
    kmers = set([b'HEL',b'ELL',b'LLO'])
    assert set(k) == kmers

# def test_kmers_avianbase():
#     a = avianbase.Avianbase(cache=True)

#     for url, g in a:
#         stream = avianbase.kmers_from_file(g, 3)
#         m = minhash(stream, 1000)
#         print(m)


# test_kmers_avianbase()
# test_avianbase()