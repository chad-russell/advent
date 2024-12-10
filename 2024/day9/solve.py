input = list(open(0).read().strip())

def part1():
    id = 0
    disk = []
    is_block = True
    for i in range(len(input)):
        if is_block:
            disk += [str(id)] * int(input[i])
            id += 1
        else:
            disk += ['.'] * int(input[i])
        is_block = not is_block

    first_empty = disk.index('.')
    moving_from = len(disk) - 1
    while moving_from > first_empty:
        if disk[moving_from] == '.':
            moving_from -= 1
            continue
        disk[first_empty] = disk[moving_from]
        disk[moving_from] = '.'
        moving_from -= 1
        while first_empty < len(disk) and disk[first_empty] != '.':
            first_empty += 1
        # print(''.join(disk))

    return sum(i * int(j) for i, j in enumerate(disk) if j != '.')

def compact_free(disk):
    i = 0
    while i < len(disk) - 1:
        if '.' in disk[i] and '.' in disk[i + 1]:
            disk[i] += disk[i + 1]
            disk = disk[:i + 1] + disk[i + 2:]
        i += 1
    return disk

def part2():
    id = 0
    disk = []
    is_block = True
    for i in range(len(input)):
        if is_block:
            if input[i] != '0':
                disk.append([str(id)] * int(input[i]))
            id += 1
        elif input[i] != '0':
            disk.append('.' * int(input[i]))
        is_block = not is_block

    to_move = len(disk) - 1
    while to_move > 0:
        if '.' in disk[to_move]:
            to_move -= 1
            continue

        slot_index = 0
        moved = False
        while (not moved) and (slot_index < to_move):
            if '.' not in disk[slot_index]:
                slot_index += 1
                continue

            ldsi = len(disk[slot_index])
            ldtm = len(disk[to_move])
            if ldsi < ldtm:
                slot_index += 1
            elif ldsi == ldtm:
                disk[slot_index], disk[to_move] = disk[to_move], disk[slot_index]
                moved = True
            elif ldsi > ldtm:
                disk[slot_index] = disk[to_move]
                disk[to_move] = '.' * ldtm
                disk.insert(slot_index + 1, '.' * (ldsi - ldtm))
                to_move += 1
                moved = True

        to_move -= 1

    total = 0
    id = 0
    position = 0
    for d in disk:
        if '.' in d:
            position += len(d)
            continue
        for dd in d:
            total += position * int(dd)
            position += 1
    return total

print(f'part 1: {part1()}') # 6398608069280
print(f'part 2: {part2()}') # 6427437134372
