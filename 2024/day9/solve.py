input = list(open(0).read().strip())

def part1():
    id = 0
    disk = []
    for i in range(len(input)):
        if i % 2 == 0:
            disk += [id] * int(input[i])
            id += 1
        else:
            disk += ['.'] * int(input[i])

    first_empty = disk.index('.')
    moving_from = len(disk) - 1
    while moving_from > first_empty:
        if disk[moving_from] == '.':
            moving_from -= 1
            continue
        if disk[first_empty] != '.':
            first_empty += 1
            continue
        disk[first_empty], disk[moving_from] = disk[moving_from], disk[first_empty]
        moving_from -= 1

    return sum(i * j for i, j in enumerate(disk) if j != '.')

def part2():
    id = 0
    disk = []
    free_list = dict()
    for i in range(len(input)):
        if i % 2 == 0:
            if input[i] != '0':
                disk.append([id] * int(input[i]))
            id += 1
        elif input[i] != '0':
            if int(input[i]) in free_list:
                free_list[int(input[i])].append(len(disk))
            else:
                free_list[int(input[i])] = [len(disk)]
            disk.append(['.'] * int(input[i]))

    max_free_length = max(free_list.keys())

    to_move = len(disk) - 1
    while to_move > 0:
        if '.' in disk[to_move]:
            to_move -= 1
            continue
        
        len_to_move = len(disk[to_move])
        trying = len_to_move

        found_any = False
        placing_at = 999999999
        min_trying = 999999999
        while trying <= max_free_length:
            if trying in free_list and len(free_list[trying]) > 0 and free_list[trying][0] < placing_at:
                found_any = True
                placing_at = free_list[trying][0]
                min_trying = trying
            trying += 1

        if not found_any or placing_at >= to_move:
            to_move -= 1
            continue

        trying = min_trying

        free_list[trying] = free_list[trying][1:]
        if len(free_list[trying]) == 0:
            free_list.pop(trying)
        index_of_first_dot = disk[placing_at].index('.')
        for i in range(len(disk[to_move])):
            disk[placing_at][index_of_first_dot + i] = disk[to_move][i]
            disk[to_move][i] = '.'
        if trying > len_to_move:
            if trying - len_to_move in free_list:
                free_list[trying - len_to_move].append(placing_at)
                free_list[trying - len_to_move].sort()
            else:
                free_list[trying - len_to_move] = [placing_at]

        to_move -= 1

    total = 0
    position = 0
    for d in disk:
        for dd in d:
            if dd != '.':
                total += position * int(dd)
            position += 1
    return total

print(f'part 1: {part1()}') # 6398608069280
print(f'part 2: {part2()}') # 6427437134372