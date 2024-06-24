#!/usr/bin/python3
"""UTF-8 VDT"""


def get_leading_set_bits(num):
    """return  number"""
    st_bits = 0
    helper = 1 << 7
    while helper & num:
        st_bits  += 1
        helper = helper >> 1
    return  st_bits


def validUTF8(data):
    """ UTF-8 encoding"""
    bits_count = 0
    for iter in range(len(data)):
        if bits_count == 0:
            bits_count = get_leading_set_bits(data[iter])
            '''1-byte'''
            if bits_count == 0:
                continue
            '''a character in UTF-8'''
            if bits_count == 1 or bits_count > 4:
                return False
        else:
            '''checks if current byte has the right format'''
            if not (data[iter] & (1 << 7) and not (data[iter] & (1 << 6))):
                return False
        bits_count -= 1
    return bits_count == 0
