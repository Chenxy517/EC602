# Copyright 2022 XingyuChen chxy517@bu.edu
# Copyright 2022 ShenyouFan syffan@bu.edu

import numpy as np
import time

def show_integer_properties():
    Table = "{:<6} {:<22} {:<22} {:<22}"
    print(Table.format('Bytes','Largest Unsigned Int','Minimum Signed Int','Maximum Signed Int'))
    for i in range(1, 9):
        byte = i * 8
        unsigned_int = 2 ** byte - 1
        max_signed_int = (unsigned_int - 1) // 2
        min_signed_int = max_signed_int - unsigned_int
        print(Table.format(i,unsigned_int,min_signed_int,max_signed_int))
     
def estimate_wrap_around():
    start_time = time.time()
    m = np.array([1],dtype= np.int16)
    while m[0]>0: 
        m[0] += 1
    time_16 = (time.time() - start_time) * 1000
    time_8 = time_16 * (10**6) / (2**8)
    time_32 = time_16 * (2**16) / (10**3)
    time_64 = time_32 * (2**32) / (60 * 60 * 24 * 365)
    print("estimated 8-bit time (nanoseconds): %s" %(time_8))
    print("measured 16-bit time (microseconds): %s" %(time_16))
    print("estimated 32-bit time (seconds): %s" %(time_32))
    print("estimated 64-bit time (years): %s" %(time_64))

def maximum_consecutive_int_value(float_type):
    i = int(0)
    f = float(0)
    while i == f:
        i += 1
        if float_type == np.float16:
            f = int(np.float16(i))
        elif float_type == np.float32:
            f = int(np.float32(i))
        elif float_type == np.float64:
            f = int(np.float64(i))
        elif float_type == np.float128:
            f = int(np.float128(i))
    return i

def largest_double():
    fraction = 1
    for i in range(1, 24):
        fraction += 2 ** (-i)
    largest_double = (2 ** 127) * fraction
    return largest_double

def smallest_double():
    smallest_double = 2 ** (-1074)
    return smallest_double

def largest_single():
    fraction = 1
    for i in range(1, 53):
        fraction += 2 ** (-i)
    largest_double = (2 ** 1023) * fraction
    return largest_double

def smallest_single():
    smallest_single = 2 ** (-149)
    return smallest_single

def breakdown_float(f):
    if f > 0:
        sign = 0
    elif f < 0:
        sign = 1
    elif f == 0:
        return {'sign': 1, 'fraction': 0, 'exponent': 0, 'subnormal': True}
    if type(f) == float:
        f = np.float64(f)
    f_byte = f.tobytes()
    bin_str = bin(int.from_bytes(f.tobytes(), byteorder='little'))
    bin_len = len(bin_str)
    if type(f) == np.float16:
        bin_str = '0' * (18 - bin_len) + bin_str[2:]
        if sign == 0:
            exponent_str = bin_str[:6]
            fraction_str = bin_str[6:]
        else:
            exponent_str = bin_str[1:6]
            fraction_str = bin_str[6:]
    elif type(f) == np.float32:
        bin_str = '0' * (34 - bin_len) + bin_str[2:]
        if sign == 0:
            exponent_str = bin_str[:9]
            fraction_str = bin_str[9:]
        else:
            exponent_str = bin_str[1:9]
            fraction_str = bin_str[9:]
    elif type(f) == np.float64:
        bin_str = '0' * (66 - bin_len) + bin_str[2:]
        if sign == 0:
            exponent_str = bin_str[:12]
            fraction_str = bin_str[12:]
        else:
            exponent_str = bin_str[1:12]
            fraction_str = bin_str[12:]
    if exponent_str == '':
        exponent = 0
    else:
        exponent = int(exponent_str, 2)
    if fraction_str == '':
        fraction = 0
    else:
        fraction = int(fraction_str, 2)
    if exponent == 0:
        subnormal = True
    else:
        subnormal = False
    dict = {'sign': sign, 'fraction': fraction, 'exponent': exponent, 'subnormal': subnormal}
    return dict

def construct_float(float_parms, float_type):
    sign = float_parms.get('sign')
    fraction = float_parms.get('fraction')
    exponent = float_parms.get('exponent')
    subnormal = False
    subnormal = float_parms.get('subnormal')
    exponent_str = bin(exponent)[2:]
    fraction_str = bin(fraction)[2:]
    if float_type == np.float16:
        if len(exponent_str) > 5 or len(fraction_str) > 10:
            raise ValueError("Can't construct float.")
        exponent_str = '0' * (5 - len(exponent_str)) + exponent_str
        fraction_str = '0' * (10 - len(fraction_str)) + fraction_str
    elif float_type == np.float32:
        if len(exponent_str) > 8 or len(fraction_str) > 23:
            raise ValueError("Can't construct float.")
        exponent_str = '0' * (8 - len(exponent_str)) + exponent_str
        fraction_str = '0' * (23 - len(fraction_str)) + fraction_str
    elif float_type == np.float64 or float_type == float:
        if len(exponent_str) > 11 or len(fraction_str) > 52:
            raise ValueError("Can't construct float")
        exponent_str = '0' * (11 - len(exponent_str)) + exponent_str
        fraction_str = '0' * (52 - len(fraction_str)) + fraction_str
    float_str = str(sign) + exponent_str + fraction_str
    float_int = int(float_str, 2)
    float_byte = float_int.to_bytes(10, byteorder="little")
    return float_type(np.frombuffer(float_byte, count = 1, dtype = float_type))




def get_next_float(start_float, index):
    if type(start_float) not in {float, np.float16, np.float32, np.float64}:
        raise TypeError("Invalid start_float type")
    if index <= 0:
        raise ValueError("Index must be positive")
    if type(index) != int:
        raise TypeError("Invalid index type")
    dict = breakdown_float(start_float)
    fraction = dict.get('fraction')
    fraction = fraction + index
    dict['fraction'] = fraction
    return construct_float(dict, type(start_float))
