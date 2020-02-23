import glob
import sys
from os import listdir
from os.path import isfile, join

path = 'functions'
commentated = False


def get_function(name):
    with open(join(path, name), 'r') as f:
        content = f.read()
        content = content.replace('\n', '')
        content = content.replace(' ', '')
        if commentated:
            content = f'% {name};\n{content}'
        return content


def load_functions():
    fnnames = [f for f in listdir(path) if isfile(join(path, f))]
    print(fnnames)
    functions = {
        fnname: get_function(fnname)
        for fnname in fnnames
    }
    return functions


def replace_functions(source, functions):
    with open(join(source), 'r') as f:
        code = f.read()
    for name, fn in functions.items():
        code = code.replace(name, fn)
    return code


def main():
    if len(sys.argv) is not 2:
        print('Use: combine <path to program>')
        exit(1)
    program = sys.argv[1]
    if not isfile(program):
        print(f'Could not find program: {program}')
        exit(1)

    functions = load_functions()
    parsed = replace_functions(program, functions)
    with open(join(program + '_gen'), 'w') as f:
        f.write(parsed)


if __name__ == '__main__':
    main()
