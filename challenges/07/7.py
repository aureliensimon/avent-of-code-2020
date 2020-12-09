import sys
import time
sys.path.insert(1, 'util')
import aoc
import re

def createTree (d):
    tree = {}

    for l in d:
        type = re.findall('.+?(?=bags)', l)[0].strip()
        res = re.findall('\d.+?(?=bags|bag)', l)
        tree[type] = []
        for r in res:
            tree[type].append({
                'name': r[2:].strip(),
                'weight': int(r[0])
            })

    return tree

def findColorInTree (t, c, target):
    if c == target: return True

    contain = False
    for e in t[c]:
        e = e['name']
        contain |= findColorInTree(t, e, target)

    return contain

def findColorWithWeights (t, c):
    if not len(t[c]): return 1

    sum = 1
    for e in t[c]:
        sum += e['weight'] * findColorWithWeights(t, e['name'])
    return sum

def part1 (tree, target):
    colors = []

    for e in tree:
        if findColorInTree(tree, e, target) and e != target:
            colors.append(e)

    return len(colors)

def part2 (tree, target):
    return findColorWithWeights(tree, target) - 1

def main ():
    f = aoc.read_file('07')

    t = createTree(f)
    target = 'shiny gold'

    res = [part1(t, target), part2(t, target)]
    print(f"Part 1 = {res[0]}\nPart 2 = {res[1]}")
    print("%s ms" % round((time.time() - start_time) * 1000))

start_time = time.time()
main()
