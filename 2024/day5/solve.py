input = open(0).read().splitlines()

newline_index = input.index('')
orderings = [list(map(int, e.split('|'))) for e in input[:newline_index]]
updates = [list(map(int, e.split(','))) for e in input[newline_index+1:]]

already_correct = [u for u in updates if all(u.index(o[0]) < u.index(o[1]) for o in orderings if o[0] in u and o[1] in u)]

def part1():
    return sum(u[len(u) // 2] for u in already_correct)

def order_swap(u, i0, i1):
    if i0 < i1: return False
    u[i0], u[i1] = u[i1], u[i0]
    return True

def midpoint_of_ordered(u):
    relevant_orderings = [o for o in orderings if o[0] in u and o[1] in u]
    while any([order_swap(u, u.index(o0), u.index(o1)) for o0, o1 in relevant_orderings]): pass
    return u[len(u) // 2]

def part2():
    return sum(midpoint_of_ordered(u) for u in updates if u not in already_correct)

print(f'part 1: {part1()}') # 3608
print(f'part 2: {part2()}') # 4922
