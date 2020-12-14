import sys
import time
sys.path.insert(1, 'util')
import aoc
import re
from itertools import product

def findChar (s, c):
    return [i for i, l in enumerate(s) if l == c]

def part1 (fa):
    memory = {}

    for l in fa:
        if (l[:4] == 'mask'):
            mask = l.split()[2]
            maskand = int(mask.replace('X', '1'), 2)
            maskor = int(mask.replace('X', '0'), 2)
        else:
            adress = int(re.findall("\[([0-9]*?)\]", l)[0])
            value = int(l.split()[2])

            value &= maskand
            value |= maskor

            memory[adress] = value

    return sum(memory.values())

def part2 (fb):
    memory = {}

    for l in fb:
        if (l[:4] == 'mask'):
            mask = l.split()[2]
        else:
            adress = int(re.findall("\[([0-9]*?)\]", l)[0])
            value = int(l.split()[2])

            adressbin = ('0' * (36 - len(str(bin(adress))[2:]))) + str(bin(adress))[2:]

            for i, c in enumerate(adressbin):
                if (mask[i] != '0'):
                    adressbin = adressbin[:i] + mask[i] + adressbin[i + 1:]

            combs = list(product(range(2), repeat=adressbin.count('X')))

            indexes = findChar(adressbin, 'X')
            adressbincopy = list(adressbin)

            for comb in combs:
                for (index, replacement) in zip(indexes, comb):
                    adressbincopy[index] = str(replacement)

                newadress = int(''.join(adressbincopy), 2)
                memory[newadress] = value

    return sum(memory.values())

def main ():
    f = aoc.read_file('14')

    res = [part1(f), part2(f)]
    print(f"Part 1 = {res[0]}\nPart 2 = {res[1]}")
    print("%s ms" % round((time.time() - start_time) * 1000))

start_time = time.time()
main()
