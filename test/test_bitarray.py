import pytest

from bit_array import BitArray


def helper(size):
    t = BitArray(size)
    
    # set every other bit to 1, starting with position 0
    for i in range(size):
        if i % 2 == 0:
            t[i] = 1
        else:
            t[i] = 0

    # verify that the even bits are 1 and odds are 0
    for i in range(size):
        if i % 2 == 0:
            assert(t[i] == 1), "Assert failed for index %d" %(i)
        else:
            assert(t[i] == 0), "Assert failed for index %d" %(i)


    # clear the bits, then make sure all are zero
    for i in range(size):
        t[i] = 0
        assert(t[i] == 0), "Assert failed for index %d" %(i)


    # now do opposite bit pattern, evens 0, odds 1
    for i in range(size):
        if i % 2 != 0:
            t[i] = 1
            
    # verify
    for i in range(size):
        if i % 2 != 0:
            assert(t[i] == 1), "Assert failed for index %d" %(i)
        else:
            assert(t[i] == 0), "Assert failed for index %d" %(i)

    # clear and verify again
    for i in range(size):
        t[i] = 0
        assert(t[i] == 0), "Assert failed for index %d" %(i)


@pytest.mark.parametrize("size", [int(pow(2, x)) for x in range(4, 20)])
def test_size(size):
    helper(size) 
