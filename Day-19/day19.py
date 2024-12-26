from functools import cache

P, _,*T = open('input19.txt').read().split('\n')

@cache
def count(t):
    return t == '' or sum(count(t.removeprefix(p))
        for p in P.split(', ') if t.startswith(p))

for cast in bool, int:
    print(sum(map(cast, map(count, T))))