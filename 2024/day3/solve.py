import re

input = open(0).read()

RE_MUL = r"mul\((\d{1,3}),(\d{1,3})\)"
RE_DONT = r"(don't\(\))"
RE_DO = r"(do\(\))"

def part1():
    found = re.findall(RE_MUL, input)
    return sum(int(a) * int(b) for a, b in found)

def part2():
    found = re.findall(f"{RE_DO}|{RE_DONT}|{RE_MUL}", input)
    enabled = True
    answer = 0
    for do, dont, a, b in found:
        if do: enabled = True
        elif dont: enabled = False
        elif a and b and enabled: answer += int(a) * int(b)
    return answer

print(f'part 1: {part1()}') # 173529487
print(f'part 2: {part2()}') # 99532691
