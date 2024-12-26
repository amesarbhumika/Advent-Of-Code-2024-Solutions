import re


def read():
    with open("input3.txt", "r") as reader:
        l = reader.readlines()
    return " ".join(l)


def first_problem(l):
    pattern = r"mul\((\d+),(\d+)\)"

    matches = re.findall(pattern, l)
    # print(matches)

    sum_x = sum(int(x) * int(y) for x, y in matches)
    return sum_x


def second_problem(l):
    safe = True
    sum_x = 0

    matches = re.findall(r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))", l)

    for el in matches:
        if "do()" in el[0]:
            safe = True
        elif "don't()" in el[0]:
            safe = False
        elif safe:
            x, y = int(el[1]), int(el[2])
            sum_x += x * y

    return sum_x


def main():
    l = read()
    print(first_problem(l))
    print(second_problem(l))


if __name__ == "__main__":
    main()