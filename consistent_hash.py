#!/usr/bin/python

import hashlib
class ConsistentHash:
    def __init__(self, replica):
        self.replica = replica
        self.ring = dict()
        self.sorted_keys = []

    def get_node(self, string_key):
        if not self.ring:
            return None, None
        key = self.gen_key(string_key)

        for offset, node in enumerate(self.sorted_keys):
            if key <= node:
                return self.ring[node], offset
        return self.ring[self.sorted_keys[0]], 0
    def add_node(self, node):
        for i in xrange(self.replica):
            key = self.gen_key('%s:%s' % (node, i))
            self.ring[key] = node
            self.sorted_keys.append(key)
        self.sorted_keys.sort()
    def remove_node(self, node):
        for i in xrange(0, self.replica):
            key = self.gen_key('%s:%s' % (node, i))
            del self.ring[key]
            self._sorted_keys.remove(key)
    def gen_key(self, key):
        m = hashlib.md5()
        m.update(key)
        return long(m.hexdigest(), 16)


c_hash = ConsistentHash(10)
c_hash.add_node(1)
c_hash.add_node(2)
c_hash.add_node(3)


stat = dict()
for i in xrange(0, 1000):
    #stat.add(c_hash.get_node('%s' % i)[0])
    node = c_hash.get_node('%s' %i)[0]
    stat.setdefault(node, 0)
    stat[node] += 1

for key, value in stat.items():
    print key, ':', value
