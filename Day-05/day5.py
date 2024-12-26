data = [x.strip().split('\n') for x in open("input5.txt").read().strip().split("\n\n")]
reqs = list(map(lambda x: [int(y) for y in x],list(map(lambda x: x.split('|'), data[0]))))
updates = list(map(lambda x: [int(y) for y in x],[x.split(',') for x in data[1]]))
p1,p2,rels = 0,0,dict((k[0],{'b':[], 'a':[]}) for k in reqs) | dict((k[1],{'b':[], 'a':[]}) for k in reqs)

for (x,y) in reqs:
    rels[x]['b'].append(y)
    rels[y]['a'].append(x)

for u in updates:
    valid = True
    for i in range(len(u)): 
        if not (valid := all([u[i] in x for x in [rels[b]['b'] for b in u[:i]]] + [u[i] in x for x in [rels[a]['a'] for a in u[i+1:]]])): break
    if valid: p1 += u[len(u)//2]
    else:
        build = []
        while len(build) != len(u):
            left = u[:]
            for b in build: left.pop(left.index(b))
            while len(left) != 0:
                l = left.pop()
                if all(item in rels[l]['b'] for item in left) and (len(build) == 0 or all(item in rels[l]['a'] for item in build)):
                    build.append(l)
                    break
        p2 += build[len(build)//2]

print(f"{p1=} || {p2=}")