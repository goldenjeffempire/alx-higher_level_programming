#!/usr/bin/python3
import sys
arguments = sys.argv[1:]
sum_result = sum(int(arg) for arg in arguments)
print("Sum of the arguments:", sum_result)
