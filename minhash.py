#!/usr/bin/python

import hashlib

def h_md5(key):
    h = hashlib.md5()
    h.update(key)
    return long(h.hexdigest(), 16)
def h_sha1(key):
    h = hashlib.sha1()
    h.update(key)
    return long(h.hexdigest(), 16)
def minhash_map(a_set):
    '''mapping a set to a smaller space with minhash'''
    hash_func = [h_md5, h_sha1]
    ret = []
    for func in hash_func:
        ret.append(min([func(a_set) for v in a_set]))

    return ret

def sim(set1_mapped, set2_mapped):
    '''calculate the similarity betweet two mapped set(using minhash'''
    same = 0
    for v1, v2 in zip(set1_mapped, set2_mapped):
        if v1 == v2:
            same += 1
    return float(same) / len(set1_mapped)
