from bisect import bisect_left

data = open("input18.txt").read()
data=[tuple(int(n) for n in line.split(",")) for line in data.split("\n")]

DIRS=[(1,0), (0,1), (-1,0), (0,-1)]
def bfs(delay=1024, W=70):
    blocks = set(data[:delay])

    boundary, target = set([(0,0)]), (W, W)
    step, seen = 0, set()
    while boundary:
        newb = set()
        while boundary: 
            y, x = boundary.pop()
            if (y,x) in seen: continue
            if (y,x) == target: return step
            seen.add((y,x))

            for dy, dx in DIRS:
                ny, nx = y+dy, x+dx
                if 0<=y<=W and 0<=x<=W and (y,x) not in blocks:
                    newb.add((ny, nx))
        boundary = newb
        step += 1
    return 0

print(bfs())
print(*data[bisect_left(range(len(data)), True, key=lambda i: bfs(i)==0)-1], sep=",")