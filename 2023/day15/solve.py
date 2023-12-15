input = open(0).read().strip().split(',')

def hash(s):
    cv = 0
    for ch in s:
        cv += ord(ch) # ascii value
        cv *= 17
        cv %= 256
    return cv

def part1():
    answer = sum(hash(item) for item in input)
    # assert(answer == 505427)
    return answer

def part2():
    boxes = [{} for _ in range(256)]
    for item in input:
        label, rest = item.split('=') if '=' in item else item.split('-')
        boxnr = hash(label)
        if '=' in item:
            boxes[boxnr][label] = int(rest)
        else:
            boxes[boxnr].pop(label, None)
            
    answer = sum(boxnr * slotnr * box[slot] for boxnr, box in enumerate(boxes, 1) for slotnr, slot in enumerate(box, 1))
    # assert(answer == 243747)
    return answer

print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
