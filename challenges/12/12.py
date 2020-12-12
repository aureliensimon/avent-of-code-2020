import sys
import time
sys.path.insert(1, 'util')
import aoc

N = 0
W = 90
S = 180
E = 270

def part1 (fa):
    distance = [0, 0]
    facing = E

    for l in fa:
        direction = l[0]
        units = int(l[1:])

        if (direction == 'E'):
            distance[0] += units
        elif (direction == 'S'):
            distance[1] += units
        elif (direction == 'N'):
            distance[1] -= units
        elif (direction == 'W'):
            distance[0] -= units
        elif (direction == 'F'):
            if (facing == E):
                distance[0] += units
            elif (facing == S):
                distance[1] += units
            elif (facing == N):
                distance[1] -= units
            elif (facing == W):
                distance[0] -= units
        elif (direction == 'L'):
            facing = (facing + units) % 360
        elif (direction == 'R'):
            facing = (facing - units) % 360

    return abs(distance[0]) + abs(distance[1])

def part2 (fb):
    waypoint = [10, 1]
    distance = [0, 0]

    for l in fb:
        direction = l[0]
        units = int(l[1:])

        if (direction == 'E'):
            waypoint[0] += units
        elif (direction == 'S'):
            waypoint[1] -= units
        elif (direction == 'N'):
            waypoint[1] += units
        elif (direction == 'W'):
            waypoint[0] -= units
        elif (direction == 'F'):
            for i in range(units):
                distance[0] += waypoint[0]
                distance[1] += waypoint[1]
        elif (direction == 'L'):
            for i in range(int(units / 90)):
                tmp = -waypoint[1]
                waypoint[1] = waypoint[0]
                waypoint[0] = tmp
        elif (direction == 'R'):
            for i in range(int(units / 90)):
                tmp = -waypoint[0]
                waypoint[0] = waypoint[1]
                waypoint[1] = tmp

    return abs(distance[0]) + abs(distance[1])

def main ():
    f = aoc.read_file('12')

    res = [part1(f), part2(f)]
    print(f"Part 1 = {res[0]}\nPart 2 = {res[1]}")
    print("%s ms" % round((time.time() - start_time) * 1000))

start_time = time.time()
main()
