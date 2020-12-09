import sys
import time
import re
sys.path.insert(1, 'util')
import aoc

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def validate_infos (passport):
    validation_infos = True

    byr = passport['byr']
    iyr = passport['iyr']
    eyr = passport['eyr']
    hgt = passport['hgt']
    hcl = passport['hcl']
    ecl = passport['ecl']
    pid = passport['pid']

    # date check
    if (not number_is_between(1920, 2002, byr)) or (not number_is_between(2010, 2020, iyr)) or (not number_is_between(2020, 2030, eyr)):
        validation_infos = False

    # regex check
    if not re.search('^#[0-9a-f]{6}$', hcl) or (not re.search('^[0-9]{9}$', pid)):
        validation_infos = False

    # exist in array
    if ecl not in eye_colors:
        validation_infos = False

    # unit and height check
    unit = hgt[-2:]
    if (unit == 'in'):
        if not number_is_between(59, 76, hgt[:-2]):
            validation_infos = False
    elif (unit == 'cm'):
        if not number_is_between(150, 193, hgt[:-2]):
            validation_infos = False
    else:
        validation_infos = False


    return validation_infos

def number_is_between(lower, upper, number):
    return lower <= int(number) <= upper

def part1 (fa):
    t = 0
    passport = {}

    for l in fa:
        l = l.strip()

        if l:
            infos = l.split()
            for info in infos:
                category, value = info.split(':')
                passport[category] = value
        else:
            t += all([fd in passport for fd in fields])
            passport = {}

    t += all([fd in passport for fd in fields])

    return t

def part2 (fb):
    t = 0
    passport = {}

    for l in fb:
        l = l.strip()

        if l:
            infos = l.split()
            for info in infos:
                category, value = info.split(':')
                passport[category] = value
        else:
            all_infos = all([fd in passport for fd in fields])

            if all_infos:
                t += validate_infos(passport)

            # reset passport
            passport = {}

    t += validate_infos(passport)

    return t

def main ():
    f = aoc.read_file('04')

    res = [part1(f), part2(f)]
    print(f"Part 1 = {res[0]}\nPart 2 = {res[1]}")
    print("%s ms" % round((time.time() - start_time) * 1000))

start_time = time.time()
main()
