from enum import Enum
import math
from collections import deque

input = open(0).read().splitlines()

class Pulse(Enum):
    LOW = 0
    HIGH = 1

class Module(Enum):
    BROADCASTER = 2
    FLIPFLOP = 3
    CONJUNCTION = 4

modules = {}

# Parse
for line in input:
    src, dst = line.split(' -> ')
    dst = list(dst.split(', '))

    if src == 'broadcaster':
        modules[src] = { 'ty': Module.BROADCASTER, 'dst': dst }
    elif src[0] == '%':
        modules[src[1:]] = { 'ty': Module.FLIPFLOP, 'dst': dst, 'state': Pulse.LOW }
    else:
        assert(src[0] == '&')
        modules[src[1:]] = { 'ty': Module.CONJUNCTION, 'dst': dst, 'states': {} }

leads_to_rx = None
conjunctions = []
first_seen_conjunctions = {}

# Fill in the initial states for each conjunction module
# Pull out the list of modules which lead to `rx`
for mk in modules.keys():
    m = modules[mk]
    if m['ty'] == Module.CONJUNCTION:
        sources = [smk for smk in modules.keys() if mk in modules[smk]['dst']]
        m['states'] = {s: Pulse.LOW for s in sources}
    if 'rx' in m['dst']:
        leads_to_rx = mk

# Pull out anything which leads to something in leads_to_rx
conjunctions = [mk for mk, m in modules.items() if leads_to_rx in m['dst']]

high_pulses = 0
low_pulses = 0
button_presses = 0

def push_button():
    global high_pulses, low_pulses, button_presses

    button_presses += 1
    
    pulse_list = deque([])
    pulse_list.append(('button', 'broadcaster', Pulse.LOW))

    while pulse_list:
        src, dst, pulse = pulse_list.popleft()

        # pulse_desc = "low" if pulse == LOW else "high"
        # print(f'{src} -{pulse_desc}-> {dst}')

        if pulse == Pulse.LOW and dst in conjunctions and dst not in first_seen_conjunctions:
            first_seen_conjunctions[dst] = button_presses

        if pulse == Pulse.HIGH:
            high_pulses += 1
        else:
            low_pulses += 1

        if dst not in modules:
            continue

        module = modules[dst]
        match module['ty']:
            case Module.BROADCASTER:
                for d in module['dst']:
                    pulse_list.append((dst, d, pulse))
            case Module.FLIPFLOP:
                if pulse == Pulse.HIGH:
                    continue
                module['state'] = Pulse.HIGH if module['state'] == Pulse.LOW else Pulse.LOW
                for d in module['dst']:
                    pulse_list.append((dst, d, module['state']))
            case _:
                assert(module['ty'] == Module.CONJUNCTION)
                module['states'][src] = pulse
                new_pulse = Pulse.HIGH
                if all(a == Pulse.HIGH for a in module['states'].values()):
                    new_pulse = Pulse.LOW
                for d in module['dst']:
                    pulse_list.append((dst, d, new_pulse))

def part1():
    for _ in range(0, 1000):
        push_button()

    answer = low_pulses * high_pulses
    # assert(answer == 834323022)
    return answer

def part2():
    while len(first_seen_conjunctions) != len(conjunctions):
        push_button()
    answer = math.lcm(*first_seen_conjunctions.values())
    # assert(answer == 225386464601017)
    return answer


print(f'part 1: {part1()}')
print(f'part 2: {part2()}')

