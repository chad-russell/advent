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
        elif label in boxes[boxnr]:
            del boxes[boxnr][label]
            
    answer = sum((boxnr + 1) * (slotnr + 1) * box[slot] for boxnr, box in enumerate(boxes) for slotnr, slot in enumerate(box))
    # assert(answer == 243747)
    return answer

print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
