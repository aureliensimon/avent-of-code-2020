import sys
import time
sys.path.insert(1, 'util')
import aoc

def getNumbers (fc):
    nbs = []
    nbs.append(0)
    for l in fc:
        nbs.append(int(l))
    nbs.append(max(nbs) + 3)
    nbs.sort()
    return nbs

def part1 (fa):
    differences = []
    seen = []

    nbs = getNumbers(fa)

    for n in range(len(nbs)):
        for d in range(n + 1, len(nbs)):
            if (nbs[d] - nbs[n] <= 3 and nbs[n] not in seen):
                differences.append(nbs[d] - nbs[n])
                seen.append(nbs[n])

    return (differences.count(1) + 1) * (differences.count(3) + 1)

def part2 (fb):
    nbs = getNumbers(fb)

    routes = [0] * (max(nbs) + 1)
    routes[0] = 1

    for i in nbs:
        routes[i] += sum(routes[i - j] for j in range(1, 4))

    return routes[len(routes) - 1]

def main ():
    f = aoc.read_file('10')

    res = [part1(f), part2(f)]
    print(f"Part 1 = {res[0]}\nPart 2 = {res[1]}")
    print("%s ms" % round((time.time() - start_time) * 1000))


start_time = time.time()
main()
