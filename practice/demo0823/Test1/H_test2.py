#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random


def getRandomSet(bits):
    num_set = [chr(i) for i in range(48, 58)]
    char_set = [chr(i) for i in range(97, 123)]
    total_set = num_set + char_set

    value_set = "".join(random.sample(total_set, bits))

    return value_set


if __name__ == '__main__':
    strings = getRandomSet(16)
    print(strings)
