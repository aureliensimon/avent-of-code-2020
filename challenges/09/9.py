import sys
import time
sys.path.insert(1, 'util')
import aoc

def getNumbers (fc):
    return [int(n) for n in fc]

def part1 (numbers, maxPreamble):
    nb = 0
    preamble = []
    sumpairs = []

    lower = 0
    upper = maxPreamble

    for ns in numbers[maxPreamble:]:
        preamble = numbers[lower:upper]

        for i in range(len(preamble)):
            for j in range(i, len(preamble)):
                sumpairs.append(preamble[i] + preamble[j])

        if ns not in sumpairs:
            return ns

        lower += 1
        upper += 1
        sumpairs = []

def part2 (numbers, maxPreamble):
    p1 = part1(numbers, maxPreamble)
    contiguous = []

    for i in range(len(numbers)):
        j = i + 1
        sum = numbers[i]

        while j <= len(numbers) - 1:
            sum += numbers[j]
            if (sum == p1):
                contiguous.append(numbers[i] + numbers[j - 1])
            j += 1

    return contiguous[0]

def main ():
    f = aoc.read_file('09')
    preambleSize = 25
    numbers = getNumbers(f)

    res = [part1(numbers, preambleSize), part2(numbers, preambleSize)]
    print(f"Part 1 = {res[0]}\nPart 2 = {res[1]}")
    print("%s ms" % round((time.time() - start_time) * 1000))

start_time = time.time()
main()
