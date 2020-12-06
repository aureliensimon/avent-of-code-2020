import sys
sys.path.insert(1, 'util')
import aoc

def part1 (fa):
    questions = ''
    count = 0

    for l in fa:
        l = l.strip()
        if l:
            questions += l
        else:
            count += len(set(questions))
            questions = ''

    # last part
    u = set(questions)
    count += len(u)

    return count

def part2 (fb):
        questions = []
        count = 0

        for l in fb:
            l = l.strip()
            if l:
                questions.append(l)
            else:
                count += len(list(set.intersection(*map(set, questions))))
                questions = []

        # last part
        u = list(set.intersection(*map(set, questions)))
        count += len(u)

        return count

def main ():
    f = aoc.read_file('06')

    res = [part1(f), part2(f)]
    print(f"Part 1 = {res[0]}\nPart 2 = {res[1]}")

main()
