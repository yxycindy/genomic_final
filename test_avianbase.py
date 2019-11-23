import avianbase

def test_avianbase():
    a = avianbase.Avianbase(cache=True)

    for g in a:
        print(g)

test_avianbase()