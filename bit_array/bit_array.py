'''

Copyright (c) 2016 Bryant Moscon - bmoscon@gmail.com

See LICENSE file for the terms and conditions
associated with this software.

'''

import array
from math import log

class BitArray(object):
    def __init__(self, bits):
        # L = 4 bytes minimum, but could be 8 bytes. No need to waste all that space
        # so lets look up the size of L on this machine
        self.elem_size = int(log(array.array('L').itemsize * 8, 2))
        self.elem_mask =  int(pow(2, self.elem_size) - 1)
        if isinstance(bits, list):
            data = list(bits)
            bits = len(data)
        else:
            data = None   
        size = bits >> self.elem_size;
        if bits & self.elem_mask:
            size += 1
        print size
        self.size = bits
        self.bits = array.array('L', (0,) * size)
        if data is not None:
            for i in xrange(0, len(data), self.elem_size):
                print i, self.elem_size
                print data[i:i+self.elem_size]     
       
    def __len__(self):
        return self.size

    def __setitem__(self, index, value):
        if index > self.size:
            raise IndexError
        array_index = index >> self.elem_size
        bit_position = index & self.elem_mask
        mask = 1 <<  bit_position
        if value:
            self.bits[array_index] |= mask
        else:
            mask = ~mask
            self.bits[array_index] &= mask

    def __getitem__(self, index):
        if isinstance(index, slice):
            return [self[x] for x in xrange(*index.indices(len(self)))]
        else:
            if index >= self.size:
                raise IndexError
            array_index = index >> self.elem_size
            bit_position = index & self.elem_mask
            mask = 1 << bit_position
            return 1 if self.bits[array_index] & mask else 0

