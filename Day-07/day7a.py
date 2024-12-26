from re import findall
from operator import add, mul

cat = lambda x,y: int(str(x) + str(y))

ans = 0
for line in open('input7.txt'):
    tgt, x, *Y = map(int, findall(r'\d+', line))

    X = [x]
    for y in Y:
        X = [op(x,y) for x in X for op in (add,mul,cat)]

    if tgt in X: ans += tgt

print(ans)