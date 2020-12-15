import sys
import time
sys.path.insert(1, 'util')
import aoc

def part1 (nbs):
    spokenNumbers = []
    [spokenNumbers.append(n) for n in nbs]

    while len(spokenNumbers) != 2020:
        lastSpoken = spokenNumbers[-1]
        if (lastSpoken not in spokenNumbers) or (len(spokenNumbers) <= 3):
            spokenNumbers.append(0)
            lastSpoken = spokenNumbers[-1]
        else:
            index = [i for i, v in enumerate(spokenNumbers) if v == lastSpoken]
            index = index[::-1]

            if (len(index) >= 2):
                spokenNumbers.append(index[0] - index[1])
            else:
                spokenNumbers.append(0)

    return spokenNumbers[-1]

def part2 (nbs):
        spokenNumbers = []
        [spokenNumbers.append(n) for n in nbs]

        lastSeen = {}

        for i, v in enumerate(nbs):
            lastSeen[v] = i

        while len(spokenNumbers) != 30000000:
            lastSpoken = spokenNumbers[-1]

            if lastSpoken in lastSeen:
                spokenNumbers.append(len(spokenNumbers) - lastSeen[lastSpoken] - 1)
            else:
                spokenNumbers.append(0)

            lastSeen[lastSpoken] = len(spokenNumbers) - 2

        return spokenNumbers[-1]

def main ():
    with open('input/15.in', 'r') as file:
        content = file.read().splitlines()
        numbers = [int(x) for x in content[0].split(',')]

    res = [part1(numbers), part2(numbers)]
    print(f"Part 1 = {res[0]}\nPart 2 = {res[1]}")
    print("%s ms" % round((time.time() - start_time) * 1000))

start_time = time.time()
main()
