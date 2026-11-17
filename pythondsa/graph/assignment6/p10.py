from collections import OrderedDict 
cap = int(input()) 
if cap < 0:
    raise SystemExit("Cache capacity cannot be negative.")
requests = list(map(int, input().split())) 
cache = OrderedDict() 
hits = misses = 0 
for key in requests: 
    if key in cache: 
        hits += 1 
        cache.move_to_end(key) 
        print(key, "Cache Hit") 
    else: 
        misses += 1 
        print(key, "Cache Miss") 
        cache[key] = key 
        if len(cache) > cap: 
            old, _ = cache.popitem(last=False) 
            print("Evicted:", old) 
print("Hits:", hits) 
print("Misses:", misses) 
print("Cache LRU to MRU:", list(cache.keys()))