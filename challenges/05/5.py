import sys
sys.path.insert(1, 'util')
import aoc

def part1 (code):
    row = code[:-3]
    col = code[-3:]
    range_row = [0, 127]
    for b in row:
        if (b == 'F'):
            range_row[1] -= -(-(range_row[1] - range_row[0]) // 2)
        elif (b == 'B'):
            range_row[0] += -(-abs(range_row[0]-range_row[1]) // 2)

    row = range_row[0] if range_row[0] < range_row[1] else range_row[1]

    range_col = [0, 7]
    for b in col:
        if (b == 'L'):
            range_col[1] -= -(-(range_col[1] - range_col[0]) // 2)
        elif (b == 'R'):
            range_col[0] += -(-abs(range_col[0]-range_col[1]) // 2)

    col = range_col[0] if range_col[0] < range_col[1] else range_col[1]

    return row * 8 + col

def part2 (ids):
    myid = 0
    ids = sorted(ids)
    last = ids[0]
    i = 0
    for id in range(1, len(ids)):
        col = id - 5
        row = id / 8
        if (row != 0 and row != 127):
            if (last + 1 != ids[id]):
                myid = last + 1
                break
            else:
                last = ids[id]

    return myid

def main ():
    f = aoc.read_file('05')

    ids = []
    for l in f:
        ids.append(part1(l))

    res = [max(ids), part2(ids)]
    print(f"Part 1 = {res[0]}\nPart 2 = {res[1]}")

main()
