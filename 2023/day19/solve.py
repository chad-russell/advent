import math

workflows, parts = open(0).read().strip().split('\n\n')

def parse_workflow(w):
    name, rest = w.split('{}'[0]) # awful hack to ensure balanced curly braces, for the formatter
    rest = rest[:-1]
    rest = rest.split(',')
    rules = []
    for r in rest:
        if '>' in r:
            target, rest = r.split('>')
            value, result = rest.split(':')
            rules.append(('>', target, int(value), result))
        elif '<' in r:
            target, rest = r.split('<')
            value, result = rest.split(':')
            rules.append(('<', target, int(value), result))
        else:
            rules.append((r,))
    return { 'name': name, 'rules': rules }

def parse_part_value(pv):
    return int(pv.split('=')[1])

def parse_part(p):
    parts = p[1:-1].split(',')
    x, m, a, s = list(map(parse_part_value, parts))
    return (x, m, a, s)

workflows = list(map(parse_workflow, workflows.split('\n')))
workflows = { w['name']: w['rules'] for w in workflows }

parts = list(map(parse_part, parts.split('\n')))

def apply(part, wf):
    wf = workflows[wf]

    for rule in wf:
        if len(rule) == 1:
            return rule[0]
        
        assert(len(rule) == 4)
        target_index = 'xmas'.index(rule[1])
        target = part[target_index]

        value = rule[2]

        if rule[0] == '<':
            if target < value:
                return rule[3]
        else:
            assert(rule[0] == '>')
            if target > value:
                return rule[3]

def part1():
    answer = 0

    for part in parts:
        wfname = 'in'
        while wfname not in ['A', 'R']:
            wfname = apply(part, wfname)
        if wfname == 'A':
            answer += sum(part)

    # assert(answer == 383682)

    return answer


def narrow(r, op, n):
    if op == '<':
        return ((r[0], min(r[1], n - 1)), (max(r[0], n), r[1]))

    assert(op == '>')
    return ((max(r[0], n + 1), r[1]), (r[0], min(r[1], n)))

seen = set()
ranges = []

def mag(r):
    # Using len(range(...)) here automatically accounts
    # for the case when the end of the range is <= the start
    return len(range(r[0], r[1])) + 1

def range_combinations(r):
    return math.prod(map(mag, r))

def visit(wfname, xmas):
    global ranges

    if wfname == 'A':
        ranges.append(xmas)
        return

    if wfname == 'R':
        return

    if wfname in seen:
        return

    seen.add(wfname)

    wf = workflows[wfname]
    for rule in wf:
        if len(rule) == 1:
            visit(rule[0], xmas)
        else:
            assert(len(rule) == 4)

            xi = 'xmas'.index(rule[1])
            taken, not_taken = narrow(xmas[xi], rule[0], rule[2])

            xmas[xi] = taken
            visit(rule[-1], list(xmas))
            xmas[xi] = not_taken

    seen.discard(wfname)

def part2():
    visit('in', [(1, 4000)] * 4)

    answer = 0

    for r in ranges:
        answer += range_combinations(r)

    # assert(answer == 117954800808317)

    return answer

print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
