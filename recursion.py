#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 14, fibonnaci sequence"""

def fibonnaci(n):
    if n<= 1 :
        return 0
    if n== 2:
        return 1

    a = fibonnaci( n-1 )
    b = fibonnaci( n-2 )
    result = a + b
    return result

def gcd(a,b):
    if b > a:
        return gcd(b,a)
    if a%b == 0:
        return b
    return gcd(b, a%b)

def compareTo(s1,s2):
    if s1==s2:
        return 0
    if s1<s2:
        return -1
    if s1>s2:
        return 1
    return compareTo(s1,s2)

