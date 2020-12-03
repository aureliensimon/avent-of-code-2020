def read_file (name, strip = True):
    with open('input/' + name + '.in') as f:
        content = f.readlines()
    if strip:
        return [x.strip() for x in content]
    return content