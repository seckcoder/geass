#!/usr/bin/python

import random
import hashlib
import pyhash

def h_fnv1_32(key):
    return pyhash.fnv1_32()(key)
def h_murmur3(key):
    return pyhash.murmur3_32()(key)
def h_lookup3(key):
    return pyhash.lookup3()(key)
def h_superfasthash(key):
    return pyhash.super_fast_hash()(key)
def h_md5(key):
    h = hashlib.md5()
    h.update(key)
    return long(h.hexdigest(), 16)
def h_sha1(key):
    h = hashlib.sha1()
    h.update(key)
    return long(h.hexdigest(), 16)
def h_sha224(key):
    h = hashlib.sha224()
    h.update(key)
    return long(h.hexdigest(), 16)
def minhash_map(a_set):
    '''mapping a set to a smaller space with minhash'''
    hash_func = [h_md5, h_sha1, h_superfasthash, h_murmur3, h_fnv1_32, h_lookup3,
                 h_sha224]
    ret = []
    for func in hash_func:
        ret.append(min([func(v) for v in a_set]))

    return ret

def sim(set1_mapped, set2_mapped):
    '''calculate the similarity betweet two mapped set(using minhash'''
    same = 0
    for v1, v2 in zip(set1_mapped, set2_mapped):
        if v1 == v2:
            same += 1
    return float(same) / len(set1_mapped)

if __name__ == '__main__':
    set1 = set()
    set2 = set()
    for i in xrange(100):
        set1.add(str(random.randint(0, 200)))
        set2.add(str(random.randint(0, 200)))
    set1_mapped = minhash_map(set1)
    set2_mapped = minhash_map(set2)
    print sim(set1_mapped, set2_mapped)
