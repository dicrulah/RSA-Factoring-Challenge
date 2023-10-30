#!/usr/bin/env python3
""" Factors """
from sys import argv
from math import sqrt


def open_read_file(file_name):
    """read from file
    only
    """
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
    num_to_factor = []
    for line in lines:
        num_to_factor.append(int(line))
    return num_to_factor


def find_and_times(n):
    """factor the
    n given
    """
    for i in range(1, n):
        if n == ((n // i) * i):
            print("{}={}*{}".format(n, (n // i), i))
            break


def fac_list(ls):
    """factor each
    num in ls
    """
    for i in ls:
        find_and_times(i)


if len(argv) == 2:
    fac_list(open_read_file(argv[1]))
