#!/usr/bin/env python
#-*- coding=utf-8 -*-
#
# Copyright 2013 Jike Inc. All Rights Reserved.
# Author: liwei@jike.com


# Douch National Flag algorithm for 4 colors

# for dnf2 and dnf3, refer to http://www.csse.monash.edu.au/~lloyd/tildeAlgDS/Sort/Flag/

def dnf4(seq):
    n = len(seq)
    l0 = l1 = 0
    l2 = l3 = n - 1

    # assumes:
    #       seq[0...l0-1] = 0
    #       seq[l0...l1-1] = 1
    #       seq[l1, l2] = unknown
    #       seq[l2+1, l3] = 2
    #       seq[l3+1, n-1] = 3
    while l1 <= l2:
        if seq[l1] == 0:
            seq[l0], seq[l1] = seq[l1], seq[l0]
            l0 += 1
            l1 += 1
        elif seq[l1] == 1:
            l1 += 1
        elif seq[l1] == 2:
            seq[l1], seq[l2] = seq[l2], seq[l1]
            l2 -= 1
        elif seq[l1] == 3:
            # What we actually do here is:
            #   translate seq[l2+1,l3] one cell left and then swap(l3, l1),
            #   which is equivalent to two swap
            seq[l1], seq[l2] = seq[l2], seq[l1]
            seq[l2], seq[l3] = seq[l3], seq[l2]

            l2 -= 1
            l3 -= 1

import random
seq = []
for i in xrange(1000):
    seq.append(random.randint(0, 3))

print seq
dnf4(seq)
print seq
