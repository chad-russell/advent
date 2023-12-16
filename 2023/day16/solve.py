input = open(0).read().splitlines()

class Beam:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

RIGHT = [0, 1]
LEFT = [0, -1]
DOWN = [1, 0]
UP = [-1, 0]

def energized_tiles(initial_position, initial_velocity):
    history = set()
    beams = [Beam(position=initial_position, velocity=initial_velocity)]
    new_beams = []

    def out_of_bounds(beam):
        if beam.position[0] < 0 or beam.position[0] >= len(input):
            return True
        if beam.position[1] < 0 or beam.position[1] >= len(input[0]):
            return True
        return False

    def push_new_beam(beam):
        beam.position[0] += beam.velocity[0]
        beam.position[1] += beam.velocity[1]
        new_beams.append(beam)

    def process_beam(beam):
        if out_of_bounds(beam):
            return

        # Avoid cycles
        hkey = (beam.position[0], beam.position[1], beam.velocity[0], beam.velocity[1])
        if hkey in history:
            return
        history.add(hkey)

        cur = input[beam.position[0]][beam.position[1]]

        if cur == '/':
            if beam.velocity == RIGHT:
                beam.velocity = UP
            elif beam.velocity == LEFT:
                beam.velocity = DOWN
            elif beam.velocity == UP:
                beam.velocity = RIGHT
            elif beam.velocity == DOWN:
                beam.velocity = LEFT
            push_new_beam(beam)

        elif cur == '\\':
            if beam.velocity == RIGHT:
                beam.velocity = DOWN
            elif beam.velocity == LEFT:
                beam.velocity = UP
            elif beam.velocity == UP:
                beam.velocity = LEFT
            elif beam.velocity == DOWN:
                beam.velocity = RIGHT
            push_new_beam(beam)

        elif cur == '-':
            if beam.velocity == RIGHT or beam.velocity == LEFT:
                push_new_beam(beam)
            else:
                s1 = Beam(position=[beam.position[0], beam.position[1]], velocity=[beam.velocity[0], beam.velocity[1]])
                s2 = Beam(position=[beam.position[0], beam.position[1]], velocity=[beam.velocity[0], beam.velocity[1]])

                s1.velocity = LEFT
                s2.velocity = RIGHT

                push_new_beam(s1)
                push_new_beam(s2)

        elif cur == '|':
            if beam.velocity == UP or beam.velocity == DOWN:
                push_new_beam(beam)
            else:
                s1 = Beam(position=[beam.position[0], beam.position[1]], velocity=[beam.velocity[0], beam.velocity[1]])
                s2 = Beam(position=[beam.position[0], beam.position[1]], velocity=[beam.velocity[0], beam.velocity[1]])

                s1.velocity = UP
                s2.velocity = DOWN

                push_new_beam(s1)
                push_new_beam(s2)

        else:
            push_new_beam(beam)

    while beams:
        for beam in beams:
            process_beam(beam)

        beams = new_beams
        new_beams = []

    return len(set((h[0], h[1]) for h in history))

def part1():
    answer = energized_tiles([0, 0], RIGHT)
    # assert(answer == 8112)
    return answer

def part2():
    answer = 0

    for col in range(len(input[0])):
        # Top row, heading down
        e = energized_tiles([0, col], DOWN)
        answer = max(answer, e)

        # Bottom row, heading up
        e = energized_tiles([len(input) - 1, col], UP)
        answer = max(answer, e)

    for row in range(len(input)):
        # Left row, heading right
        e = energized_tiles([row, 0], RIGHT)
        answer = max(answer, e)

        # Right row, heading left
        e = energized_tiles([row, len(input) - 1], LEFT)
        answer = max(answer, e)

    # assert(answer == 8314)
    return answer  

print(f'part 1: {part1()}')
print(f'part 2: {part2()}')
