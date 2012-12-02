import random
def trailing_zeroes(num):
    if num == 0:
        return 32;
    p = 0;
    while (num >> p) &1 == 0:
        p += 1;
    return p

def estimate_cardinality(values, k):
    num_buckets = 2**k
    max_zeros = [0] * num_buckets
    for v in values:
        h = hash(v)
        bucket = h & ( num_buckets - 1)
        bucket_hash = h >> k
        max_zeros[bucket] = max(max_zeros[bucket], trailing_zeroes(bucket_hash))
    return 2 ** (float(sum(max_zeros)) / num_buckets) * num_buckets * 0.79402

n = 100000
print [n/estimate_cardinality([random.random() for i in range(n)], 10) for j in range(10)]
