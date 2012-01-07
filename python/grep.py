import re
import argparse

def grep(regex, path, inverted = False):
    prog = re.compile(regex)
    
    with open(path) as file_in:
        if inverted:
            for line in file_in:
                if not prog.search(line):
                    print line
        else:
            for line in file_in:
                if prog.search(line):
                    print line

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A basic grep utility")

    parser.add_argument("-v", action="store_true")
    parser.add_argument("regex")
    parser.add_argument("file", nargs="+")

    args = parser.parse_args()

    for f in args.file:
        grep(args.regex, f, args.v)
