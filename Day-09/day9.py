import sys

easy = "input9.txt"
hard = "input9.txt"

def checksum(disk):
    sum = 0
    for idx, val in enumerate(disk):
        if val > -1:
            sum += idx * val
    return sum

def checksum2(file_intervals):
    sum = 0
    for file_index, start, end in file_intervals:
        for i in range(start, end):
            sum += file_index * i
    return sum

def is_compacted(disk):
    is_empty = False
    for i in disk:
        if i == -1:
            is_empty = True
        if i != -1 and is_empty:
            return False
    return True

def part_one(file):
    line = file.read()
    disk = []
    empties = []

    is_file = True
    file_index = 0

    for num in line.strip():
        if is_file:
            # print("file of size", int(num))
            disk.extend([file_index for _ in range(int(num))])
            file_index += 1
        else:
            disk.extend([-1 for _ in range(int(num))])
        is_file = not is_file

    for idx, d in enumerate(disk):
        if d == -1:
            empties.append(idx)

    # print("".join([str(i) if i != -1 else "." for i in disk]))

    empty_pointer = 0
    disk_end = len(disk) - 1

    while not is_compacted(disk):
        # print("".join([str(i) if i != -1 else "." for i in disk]))
        disk[empties[empty_pointer]], disk[disk_end] = disk[disk_end], disk[empties[empty_pointer]]
        empty_pointer += 1
        while disk[disk_end] == -1:
            disk_end -= 1

    print(checksum(disk))

def merge_empties(empty_intervals):
    i = 0
    while i < len(empty_intervals) - 1:
        if empty_intervals[i][1] == empty_intervals[i+1][0]:
            to_replace = empty_intervals[i+1]
            del empty_intervals[i+1]
            empty_intervals[i] = (empty_intervals[i][0], to_replace[1])
        else:
            i += 1
    return empty_intervals

def part_two(file):
    # store intervals of empties and files
    # if an empty interval can store a file, pop the interval, fragment it,
    # and put it back in the same place (if not delete it.).
    # calculate checksum for each interval.
    line = file.read()

    file_intervals = []
    empty_intervals = []

    is_file = True
    file_index = 0
    current_index = 0
    for num in line.strip():
        if is_file:
            file_intervals.append((file_index, current_index, current_index+int(num)))
            file_index += 1
        else:
            empty_intervals.append((current_index, current_index+int(num)))
        is_file = not is_file
        current_index += int(num)

    # print(file_intervals)
    # print(empty_intervals)

    disk_end = len(file_intervals) - 1
    while disk_end > 0:
        # print(file_intervals[disk_end])
        file_size = file_intervals[disk_end][2] - file_intervals[disk_end][1]
        empty_to_modify = -1
        for idx, e in enumerate(empty_intervals):
            if e[1] - e[0] >= file_size and e[0] < file_intervals[disk_end][1]:
                empty_to_modify = idx
                break

        if empty_to_modify != -1:
            interval = empty_intervals[empty_to_modify]
            if interval[1] - interval[0] == file_size:
                # remove interval
                del empty_intervals[empty_to_modify]
                empty_intervals.append((file_intervals[disk_end][1], file_intervals[disk_end][2]))
                file_intervals[disk_end] = (file_intervals[disk_end][0], interval[0], interval[1])
            else:
                empty_intervals[empty_to_modify] = (interval[0]+file_size, interval[1])
                empty_intervals.append((file_intervals[disk_end][1], file_intervals[disk_end][2]))
                file_intervals[disk_end] = (file_intervals[disk_end][0], interval[0], interval[0] + file_size)

            empty_intervals = merge_empties(sorted(empty_intervals))

        # print(file_intervals[disk_end], empty_to_modify)
        disk_end -= 1

    print(file_intervals)
    print(sorted(empty_intervals))
    print(checksum2(file_intervals))


if __name__ == "__main__":
    command = "easy"
    if len(sys.argv) >= 2:
        command = sys.argv[1]

    if command.find("easy") > -1:
        print("part one:")
        with open(easy) as file:
            part_one(file)
        print("part two:")
        with open(easy) as file:
            part_two(file)
    else:
        print("part one:")
        #with open(hard) as file:
            #part_one(file)
        print("part two:")
        with open(hard) as file:
            part_two(file)
