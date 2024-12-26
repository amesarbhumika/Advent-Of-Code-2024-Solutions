from math import floor, log10

with open("input11.txt") as file:
    stones = [int(stone) for stone in next(file).split()]
    stones = {stone: stones.count(stone) for stone in stones}

for i in range(75):
    new_stones = {}
    for stone, n in stones.items():
        if stone != 0:
            n_digits = floor(log10(stone)) + 1
        if stone == 0:
            new_stones[1] = n + new_stones.get(1, 0)
        elif n_digits % 2 == 0:
            left = stone // 10 ** (n_digits // 2)
            right = stone - left * 10 ** (n_digits // 2)
            new_stones[left] = n + new_stones.get(left, 0)
            new_stones[right] = n + new_stones.get(right, 0)
        else:
            new_stones[2024 * stone] = n + new_stones.get(2024 * stone, 0)
    stones = new_stones
    if i == 24:
        print(sum(n for n in stones.values()))

print(sum(n for n in stones.values()))