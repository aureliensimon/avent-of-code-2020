import sys
sys.path.insert(1, 'util')
import aoc

def run2(cmds):
    acc = 0
    i = 0

    while True:
        if (i == len(cmds)) or cmds[i][2]:
            break
        elif not cmds[i][2]:
            cmds[i][2] = True

        if (cmds[i][0] == 'nop'):
            i += 1
        elif (cmds[i][0] == 'acc'):
            acc += cmds[i][1]
            i += 1
        elif (cmds[i][0] == 'jmp'):
            i = (i + cmds[i][1])

    return acc if i == (len(cmds)) else 0

def run (commands):
    acc = 0
    i = 0

    while True:
        if commands[i][2]:
            return acc
        else:
            commands[i][2] = True

        if (commands[i][0] == 'nop'):
            i = (i + 1) % len(commands)
        elif (commands[i][0] == 'acc'):
            acc += commands[i][1]
            i = (i + 1) % len(commands)
        elif (commands[i][0] == 'jmp'):
            i = (i + commands[i][1]) % len(commands)

def getCommands (fc):
    commands = []

    for l in fc:
        cmd = l[:3]
        val = l[5:]
        sign = l[4]
        if (sign == '+'):
            commands.append([cmd, int(val), False])
        elif (sign == '-'):
            commands.append([cmd, int(val) * -1, False])

    return commands

def part1 (fa):
    commands = getCommands(fa)
    return run(commands)

def part2 (fb):
    acc = 0
    aa = 0
    commands = getCommands(fb)

    for i in range(len(commands)):
        newcommands = [p[:] for p in commands]
        end = 0
        if newcommands[i][0] == 'jmp':
            newcommands[i][0] = 'nop'
            acc = run2(newcommands)
        elif newcommands[i][0] == 'nop':
            newcommands[i][0] = 'jmp'
            acc = run2(newcommands)
            newcommands[i][0] = 'nop'

        if (acc): return acc


def main ():
    f = aoc.read_file('08')

    res = [part1(f), part2(f)]
    print(f"Part 1 = {res[0]}\nPart 2 = {res[1]}")

main()
