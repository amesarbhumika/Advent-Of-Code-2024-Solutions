data = open('input20.txt').read().strip().split('\n')

grid = {}
cnt = 2
for r,l in enumerate(data):
    for c,v in enumerate(l):
        grid[(r,c)] = v
        if v == 'S': start = (r,c)
        if v == 'E': end = (r,c)
        if v == '.': cnt += 1

ds = ((1,0),(-1,0),(0,1),(0,-1))
def bfs(p):
    distMap = {p:0}
    queue = [p]
    for r,c in queue:
        d = distMap[(r,c)]
        for dr,dc in ds:
            nr,nc = r+dr,c+dc
            if (nr,nc) not in distMap and grid[(nr,nc)] != '#':
                queue.append((nr,nc))
                distMap[(nr,nc)] = d+1
    return distMap
    
startMap = bfs(start)

def Cheats():
    cheats = {}
    for r,c in startMap:
        for dr,dc in ds:
            nr,nc = r+2*dr,c+2*dc
            if (nr,nc) in startMap:
                if startMap[(r,c)] > startMap[(nr,nc)]:
                    nn =  startMap[(r,c)] - startMap[(nr,nc)] -2  
                    if nn > 0:
                        cheats[((r,c),(nr,nc))] = nn
    return cheats
    
cheats = Cheats()
p1 = 0
for i in cheats:
    n = cheats[i]
    if n >= 100:p1 += 1
print(p1)

def Cheats():
    cheats = {}
    for r,c in startMap:
        for i in range(-20,21,1):
            for j in range(-20,21,1):
                if abs(i)+abs(j) <= 20:
                    nr,nc = r+i,c+j
                    if (nr,nc) in startMap:
                        if startMap[(r,c)] > startMap[(nr,nc)]:
                            nn =  startMap[(r,c)] - startMap[(nr,nc)] - abs(i)-abs(j) 
                            if nn > 0:
                                cheats[((r,c),(nr,nc))] = nn
    return cheats

cheats = Cheats()
p2 = 0
for i in cheats:
    n = cheats[i]
    if n >= 100:p2 += 1
print(p2)