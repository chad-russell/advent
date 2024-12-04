def print_x(min_x, max_x, min_z, max_z, bricks):
    rows = []
    for z in range(min_z, max_z + 1):
        row = ''
        for x in range(min_x, max_x + 1):
            rowchar = []
            for bn, b in enumerate(bricks):
                bx, _, bz = b
                if z in bz and x in bx:
                    rowchar.append(str(bn))
            match len(rowchar):
                case 0:
                    row += '.'
                case 1:
                    row += rowchar[0]
                case _:
                    row += '?'
        rows.append(row)

    rows.reverse()
    for row in rows:
        print(row)

def print_y(min_y, max_y, min_z, max_z, bricks):
    rows = []
    for z in range(min_z, max_z + 1):
        row = ''
        for y in range(min_y, max_y + 1):
            rowchar = []
            for bn, b in enumerate(bricks):
                _, by, bz = b
                if z in bz and y in by:
                    rowchar.append(str(bn))
            match len(rowchar):
                case 0:
                    row += '.'
                case 1:
                    row += rowchar[0]
                case _:
                    row += '?'
        rows.append(row)

    rows.reverse()
    for row in rows:
        print(row)
