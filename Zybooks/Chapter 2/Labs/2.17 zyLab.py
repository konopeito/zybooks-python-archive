# 2.17.1: LAB: Musical note frequencies
import math
base_frequency = float(input())
r= math.pow(2.0,(1.0/12.0))
one_key_up= base_frequency * (math.pow(r,1))
two_keys_up= base_frequency * (math.pow(r,2))
three_keys_up= base_frequency * (math.pow(r,3))
four_keys_up= base_frequency * (math.pow(r,4))
print(f'{base_frequency:.2f} {one_key_up:.2f} {two_keys_up:.2f} {three_keys_up:.2f} {four_keys_up:.2f}')