#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = ('a bc     d f')
    k = 0
    max = 0
    for character in s:
        if character == ' ':
            k += 1
        else:
            if k > max:
                max = k
                k = 0
    print(max)



