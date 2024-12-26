from collections import defaultdict
from itertools import pairwise


def f(s):
    s = s ^ s << 6 & 0xFFFFFF
    s = s ^ s >> 5 & 0xFFFFFF
    return s ^ s << 11 & 0xFFFFFF


ans1, ans2 = 0, defaultdict(int)

for s in map(int, open('input22.txt')):
    nums = [s] + [s:=f(s) for _ in range(2000)]
    ans1 += nums[-1]

    diffs = [b%10-a%10 for a,b in pairwise(nums)]

    seen = set()
    for i in range(len(nums) - 4):
        pat = tuple(diffs[i:i+4])
        if pat not in seen:
            seen.add(pat)
            ans2[pat] += nums[i+4] % 10

print(ans1,max(ans2.values()))