import subprocess
import datetime

def download_input ():
    year, day = datetime.datetime.today().strftime('%Y-%#d').split('-')
    session = open('.session', 'r').readline()
    cmd = f'curl https://adventofcode.com/{year}/day/{day}/input --cookie "session={session}"'
    output = subprocess.check_output(cmd, shell=True)

    f = open('input/' + ('0' if (int(day) < 10) else '') + day + '.in', 'w+')
    f.write(output.decode('utf-8'))

download_input()
