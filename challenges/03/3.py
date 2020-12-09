import sys
import time
sys.path.insert(1, 'util')
import aoc

def part1 (m):
    x = 0
    y = 0
    xmax = len(m) - 1
    ymax = len(m[x])
    trees = 0

    while x < xmax:
            x += 1
            y += 3

            if (m[x][y % ymax] == '#'):
                trees += 1

    return trees

def part2 (m):
    s = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    total = 1

    for (dy, dx) in s:
        trees = 0
        x = 0
        y = 0
        xmax = len(m) - dx
        ymax = len(m[x])

        while x < xmax:
            x += dx
            y += dy

            if (m[x][y % ymax] == '#'):
                trees += 1

        total *= trees

    return total

def main ():
    mp = []

    f = aoc.read_file('03')
    for l in f:
        mp.append(list(l))

    res = [part1(mp), part2(mp)]
    print(f"Part 1 = {res[0]}\nPart 2 = {res[1]}")
    print("%s ms" % round((time.time() - start_time) * 1000))

start_time = time.time()
main()
