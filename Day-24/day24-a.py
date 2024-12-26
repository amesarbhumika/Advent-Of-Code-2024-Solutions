inps, gates = open('input24.txt').read().strip().split('\n\n')
vals = {}
for l in inps.split("\n"):
	gate, val = l.split(": ")
	vals[gate] = int(val)
gatez = {}
for gate in gates.split("\n"):
	gatez[gate.split(" -> ")[1]] = gate.split(" -> ")[0]
outs = list(set(list(vals.keys()) + list(gatez.keys())))
outs = [x for x in outs if x[0] == 'z']

def eval(g):
	if g in vals:
		return vals[g]
	a, op, b = gatez[g].split(" ")
	if op == "AND":
		return eval(a) & eval(b)
	if op == "OR":
		return eval(a) | eval(b)
	if op == "XOR":
		return eval(a) ^ eval(b)

ret = ""
for x in sorted(outs):
	ret += str(eval(x))
print(int(ret[::-1], 2))

def shouldBe(inp1, inp2, outShould):
	for x in range(46):
		vals["x" + str(x).zfill(2)] = (inp1 >> x) & 1
		vals["y" + str(x).zfill(2)] = (inp2 >> x) & 1
	for z in range(46):
		if eval("z" + str(z).zfill(2)) != (outShould >> z) & 1:
			print("misbatch at bit", z)
			break

for testBit in range(46):
	i = 1 << testBit
	shouldBe(i,i,i+i)
