import array
from math import log

class BitArray(object):
    def __init__(self, bits):
        # L = 4 bytes minimum, but could be 8 bytes. No need to waste all that space
        # so lets look up the size of L on this machine
        self.elem_size = int(log(array.array('L').itemsize * 8, 2))
        self.elem_mask =  int(pow(2, self.elem_size) - 1)
        size = bits >> self.elem_size;
        if bits & self.elem_mask:
            size += 1
        
        self.bits = array.array('L', (0,) * size)

    def __getitem__(self, index):

    def __setitem__(self, index, value)
        array_index = index >> self.elem_size
        bit_position = index & self.elem_mask
        mask = 1 <<  bit_position
        if value:
            mask = ~mask
            self.bits[array_index] &= mask
        else:
            self.bits[array_index] |= mask


    def __getitem__(self, index)
        array_index = index >> self.elem_size
        bit_position = index & self.elem_mask
        mask = 1 << bit_position
        return 1 if self.bits[array_index] & mask else 0

