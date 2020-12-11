import sys
import time
sys.path.insert(1, 'util')
import aoc

def createMaps (fc):
    map = []
    for l in fc:
        map.append(list(l))

    mapCopy = [[map[x][y] for y in range(len(map[0]))] for x in range(len(map))]

    return map, mapCopy

def getNeighbours (i, j, m, n):
    neighours = []
    if (i > 0):
        neighours.append((i - 1, j))
        if (j > 0):
            neighours.append((i - 1, j - 1))
        if (j + 1 < n):
            neighours.append((i - 1, j + 1))

    if (i + 1 < m):
        neighours.append((i + 1, j))
        if (j > 0):
            neighours.append((i + 1, j - 1))
        if (j + 1 < n):
            neighours.append((i + 1, j + 1))

    if (j > 0):
        neighours.append((i, j - 1))

    if (j + 1 < n):
        neighours.append((i, j + 1))

    return neighours

def findVisible (map, x, y, dx, dy):
    point = map[x][y]

    while (point == '.'):
        if (x + dx > len(map) - 1 or x + dx < 0) or (y + dy > len(map[0]) - 1 or y + dy < 0):
            break
        else:
            x += dx
            y += dy
            point = map[x][y]

    return (x, y)

def part1 (fa):
    map, mp = createMaps(fa)

    moving = True

    while moving:
        moving = False
        for i in range(len(map)):
            for j in range(len(map[i])):
                adj = getNeighbours(i, j, len(map), len(map[i]))
                nbs = 0
                for m, n in adj:
                    if (map[m][n] == '#'):
                        nbs += 1

                if (map[i][j] == 'L') and not nbs:
                    mp[i][j] = '#'
                    moving = True
                elif (map[i][j] == '#') and nbs >= 4:
                    mp[i][j] = 'L'
                    moving = True

        map = [[mp[x][y] for y in range(len(mp[0]))] for x in range(len(mp))]

    return (sum(x.count('#') for x in map))

def part2 (fb):
    map, mp = createMaps(fb)

    moving = True

    while moving:
        moving = False
        for i in range(len(map)):
            for j in range(len(map[i])):
                adj = getNeighbours(i, j, len(map), len(map[i]))
                nbs = 0
                for m, n in adj:
                    x, y = findVisible(map, m, n, m - i, n - j)
                    if (map[x][y] == '#'):
                        nbs += 1

                if (map[i][j] == 'L') and not nbs:
                    mp[i][j] = '#'
                    moving = True
                elif (map[i][j] == '#') and nbs >= 5:
                    mp[i][j] = 'L'
                    moving = True


        map = [[mp[x][y] for y in range(len(mp[0]))] for x in range(len(mp))]

    return (sum(x.count('#') for x in map))

def main ():
    f = aoc.read_file('11')
    tc = aoc.read_file('test')

    res = [part1(f), part2(f)]
    print(f"Part 1 = {res[0]}\nPart 2 = {res[1]}")
    print("%s ms" % round((time.time() - start_time) * 1000))

start_time = time.time()
main()
