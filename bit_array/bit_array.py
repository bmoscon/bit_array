'''

Copyright (c) 2016 Bryant Moscon - bmoscon@gmail.com

See LICENSE file for the terms and conditions
associated with this software.

'''

import array
from math import ceil


class BitArray(object):
    def __init__(self, bits):
        # L = 4 bytes minimum, but could be 8 bytes. No need to waste all that space
        # so lets look up the size of L on this machine
        self.elem_size = array.array('L').itemsize * 8
        self.elem_mask =  self.elem_size - 1
        
        if isinstance(bits, list):
            data = list(bits)
            bits = len(data)
        else:
            data = None   
        size = int(ceil(float(bits) / float(self.elem_size)))
        self.size = bits
        self.bits = array.array('L', (0,) * size)
        if data is not None:
            index = 0
            for i in xrange(0, len(data), self.elem_size):
                self.bits[index] = int("".join(str(x) for x in data[i:i+self.elem_size])[::-1],2)
                index += 1

    def __len__(self):
        return self.size

    def __str__(self):
        pad = self.size % self.elem_size
        arr_len = len(self.bits)
        return '0b' + ''.join([bin(self.bits[i])[2:].zfill(pad)[::-1] for i in range(arr_len)])

    def __repr__(self):
        return self.__str__() 

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
            return BitArray([self[x] for x in range(*index.indices(len(self)))])
        else:
            if index >= self.size:
                raise IndexError
            array_index = index >> self.elem_size
            bit_position = index & self.elem_mask
            mask = 1 << bit_position
            return 1 if self.bits[array_index] & mask else 0

