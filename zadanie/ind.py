#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # X = (A\B) /\ ( C u D)     Y = (A /\ not(B)) u (C\D)
    U = set("abcdefghijklmnopqrstuvwxyz")
    a = {'c', 'e', 'h', 'n'}
    b = {'e', 'f', 'k', 'n', 'x'}
    c = {'b', 'c', 'h', 'p', 'r', 's'}
    d = {'b', 'e', 'g'}
    print('X =', (a - b) & (c | d))
    print('Y =', (c - d) | (a & (U - b)))
