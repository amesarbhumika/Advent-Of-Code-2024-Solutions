def read():
    with open("input2.txt", "r") as reader:
        l = reader.readlines()
    l = [el.replace('\n', '') for el in l]
    return l


def first_problem(l):
    temp = None
    count = 0
    for i in range(len(l)):
        temp = [int(num) for num in l[i].split(" ")]
        value = compare(temp)
        if value:
            count += 1
    return count


def compare(l):
    # all should be increasing or all should be decreasing by atleast one and atmost 3
    # should not be equal
    status = None
    if l[0] < l[1]:
        status = "inc"
    elif l[0] > l[1]:
        status = "dec"
    for i in range(1, len(l)):
        if l[i-1] == l[i]:
            return False
        if status == "inc":
            if not (1 <= l[i]-l[i-1] <= 3):
                return False
        elif status == "dec":
            if not (1 <= l[i-1]-l[i] <= 3):
                return False
    return True

# if discrepancy found then True, else False
# brute force it :sob:


def has_discrepancy(l):
    for i in range(len(l)):
        modified_list = l[:i] + l[i+1:]
        if compare(modified_list):
            return True
    return False


def second_problem(l):
    temp = None
    count = 0
    for i in range(len(l)):
        temp = [int(num) for num in l[i].split(" ")]
        if compare(temp) or has_discrepancy(temp):
            count += 1
    return count


def main():
    input = read()
    print("first problem", first_problem(input))
    print("second problem", second_problem(input))


if __name__ == "__main__":
    main()