#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите слово: ")
    k = int(input("Введите номер буквы для удаления: "))
    s = s.replace(s[3], '')
    s = s.replace(s[k], '')
    print(s)


