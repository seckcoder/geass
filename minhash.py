#!/usr/bin/python

import random

def next_highest(v):
    v-=1
    v |= v >> 1
    v |= v >> 2
    v |= v >> 4
    v |= v >> 8
    v |= v >>16
    v+=1
    return v

def naive_sim(set1, set2):
    return float(len(set1.intersection(set2))) / len(set1.union(set2))
class MinHash(object):
    def __init__(self, init_hash_func, universe_size):
        self.hash_funcs = []
        self.universe_size = universe_size
        self.hash_size = next_highest(universe_size) - 1
        for i in range(init_hash_func):
            self.add_hash_func();
        self.min_hash_sets = []
    def add_hash_func(self):
        a = random.randint(self.universe_size)
        b = random.randint(self.universe_size)
        c = random.randint(self.universe_size)
        def qhash(x):
            int_x = int(x)
            return abs((a * (int_x >> 4) + b *x + c) & self.hash_size)
        self.hash_funcs.append(qhash)
        for offset, min_hash_struct in enumerate(self.min_hash_sets):
            the_set, hash_values = min_hash_struct["set"], min_hash_struct["v"]
            hash_values.append(self.apply_hash(self.hash_funcs[-1], the_set))

    def add_set(self, the_set):
        hash_values = []
        for hash_func in self.hash_funcs:
            hash_values.append(self.apply_hash(hash_func, the_set))
        
        self.min_hash_sets.append({
            "set": the_set,
            "v": hash_values
        })
    def apply_hash(self, hash_func, the_set):
        min_v = self.hash_size
        for v in the_set:
            min_v = min(hash_func(v), min_v)

    def cal_simmilarity(self, min_hash_set1, min_hash_set2):
        return naive_sim(min_hash_set1["v"], min_hash_set2["v"])
