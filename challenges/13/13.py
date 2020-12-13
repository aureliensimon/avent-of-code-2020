import sys
import time
sys.path.insert(1, 'util')
import aoc

def part1 (bus, timestamp):
    possiblesbus = []

    for t in bus:
        if (t != 'x'):
            possiblesbus.append(int(t))

    for i in range(timestamp, timestamp + 1000):
        for b in possiblesbus:
            if not (i % b):
                minuts = i - timestamp
                return b * minuts

def part2 ():
    # https://www.dcode.fr/restes-chinois
    pass

def main ():
    with open('input/13.in', 'r') as file:
        content = file.read().splitlines()

        timestamp = int(content[0])
        bus = content[1].split(',')

    res = part1(bus, timestamp)
    print("Part 1 = {}".format(res))
    print("%s ms" % round((time.time() - start_time) * 1000))

start_time = time.time()
main()
