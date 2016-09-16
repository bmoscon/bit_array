from bit_array import BitArray


def test(size):
    t = BitArray(size)
    
    # set every other bit to 1, starting with position 0
    for i in range(size):
        if i % 2 == 0:
            t.set(i)

    # verify that the even bits are 1 and odds are 0
    for i in range(size):
        if i % 2 == 0:
            assert(t.bit(i) == 1), "Assert failed for index %d" %(i)
        else:
            assert(t.bit(i) == 0), "Assert failed for index %d" %(i)


    # clear the bits, then make sure all are zero
    for i in range(size):
        t.clear(i)
        assert(t.bit(i) == 0), "Assert failed for index %d" %(i)


    # now do opposite bit pattern, evens 0, odds 1
    for i in range(size):
        if i % 2 != 0:
            t.set(i)
            
    # verify
    for i in range(size):
        if i % 2 != 0:
            assert(t.bit(i) == 1), "Assert failed for index %d" %(i)
        else:
            assert(t.bit(i) == 0), "Assert failed for index %d" %(i)

    # clear and verify again
    for i in range(size):
        t.clear(i)
        assert(t.bit(i) == 0), "Assert failed for index %d" %(i)



if __name__ == '__main__':
    for i in range (4, 20):
        size = int(pow(2, i))
        print("Testing with size %d . . . " %(size))
        test(size)

    print("All tests pass")
        
