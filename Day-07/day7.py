from re import findall
from functools import reduce
from operator import add, mul

parse = lambda l: map(int, findall(r'\d+', l))
cat = lambda x, y: int(str(x) + str(y))

for ops in (add, mul), (add, mul, cat):
    f = lambda X, y: [op(x, y) for x in X for op in ops]
    print(sum(t for t, x, *X in map(parse, open('input7.txt'))
                if t in reduce(f, X, [x])))