#!/usr/bin/env python
# -*- coding: utf-8 -*-

def find_first_repeating_char(l):
    for i in range(len(l)):
       for j in range(i, len(l)):
           if l[i] == l[j]:
               return l[i]

print(find_first_repeating_char([1,3,5,7,8,3,1,4,3]))

