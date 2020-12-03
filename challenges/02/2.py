import sys
sys.path.insert(1, 'util')
import aoc
import re

def part1 (pwd, l, mn, mx):
    return (pwd.count(l) >= mn) and (pwd.count(l) <= mx)

def part2 (pwd, l, mn, mx):
    return ((pwd[mn - 1] == l) and (pwd[mx - 1] != l)) or ((pwd[mn - 1] != l) and (pwd[mx - 1] == l))

def main ():
    res = [0, 0]
    
    f = aoc.read_file('02')
    for l in f:
        lower = int(re.findall(r"\d{1,}", l)[0])
        upper = int(re.findall(r"\d{1,}", l)[1])
        letter = re.findall("[a-z]", l)[0]
        pwd = re.findall("[a-z]{2,}", l)[0]
        
        res[0] += part1(pwd, letter, lower, upper)
        res[1] += part2(pwd, letter, lower, upper)
    
    print(f"Part 1 = {res[0]}\nPart 2 = {res[1]}")

main()