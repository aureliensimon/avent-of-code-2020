import sys
import time
sys.path.insert(1, 'util')
import aoc

def part1 (a, t):
    for i in range(len(a)):
        for j in range(i, len(a)):
            if (a[i] + a[j] == t):
                return a[i] * a[j]

def part2 (a, t):
    for i in range(len(a)):
        for j in range(i, len(a)):
            for k in range(j, len(a)):
                if (a[i] + a[j] + a[k] == t):
                    return a[i] * a[j] * a[k]


def main ():
    f = aoc.read_file('01')
    a = [int(l) for l in f]
    res = [part1(a, 2020), part2(a, 2020)]

    print(f"Part 1 = {res[0]}\nPart 2 = {res[1]}")
    print("%s ms" % round((time.time() - start_time) * 1000))

start_time = time.time()
main()
