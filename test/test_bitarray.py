'''

Copyright (c) 2016 Bryant Moscon - bmoscon@gmail.com

See LICENSE file for the terms and conditions
associated with this software.

'''

import pytest

from bit_array import BitArray


def helper(size):
    t = BitArray(size)
    
    # set every other bit to 1, starting with position 0
    for i in range(len(t)):
        if i % 2 == 0:
            t[i] = 1
        else:
            t[i] = 0

    # verify that the even bits are 1 and odds are 0
    for i in range(len(t)):
        if i % 2 == 0:
            assert(t[i] == 1), "Assert failed for index %d" %(i)
        else:
            assert(t[i] == 0), "Assert failed for index %d" %(i)


    # clear the bits, then make sure all are zero
    for i in range(len(t)):
        t[i] = 0
        assert(t[i] == 0), "Assert failed for index %d" %(i)


    # now do opposite bit pattern, evens 0, odds 1
    for i in range(len(t)):
        if i % 2 != 0:
            t[i] = 1
            
    # verify
    for i in range(len(t)):
        if i % 2 != 0:
            assert(t[i] == 1), "Assert failed for index %d" %(i)
        else:
            assert(t[i] == 0), "Assert failed for index %d" %(i)

    # clear and verify again
    for i in range(len(t)):
        t[i] = 0
        assert(t[i] == 0), "Assert failed for index %d" %(i)


@pytest.mark.parametrize("size", [int(pow(2, x)) for x in range(4, 20)])
def test_size(size):
    helper(size)


@pytest.mark.parametrize("size", [int(pow(2, x))+1 for x in range(4, 20)])
def test_sizes_non_power2(size):
    helper(size)


@pytest.mark.parametrize("size", [x for x in range(1, 257)])
def test_size_linear(size):
    helper(size)

