G = {i+j*1j: c for i,r in enumerate(open('input6.txt'))
               for j,c in enumerate(r.strip())}

start = min(p for p in G if G[p] == '^')

def walk(G, part=1):
    pos, dir, seen = start, -1, set()
    while pos+dir in G and (pos,dir) not in seen:
        seen |= {(pos,dir)}
        while G[pos+dir] == "#":
            dir *= -1j
        pos += dir
    if part: return (pos,dir) in seen
    else: return {pos for pos,_ in seen}

path = walk(G, 0)
print(len(path)+1)
print(sum(walk(G | {o:'#'}) for o in path))