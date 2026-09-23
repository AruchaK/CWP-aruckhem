import sys


def shrink(string):
    return string[:8]

def enlarge(string):
    return string + "Z" * (8 - len(string))

def main():
    if len(sys.argv) < 2:
        print("none")
    else:
        for param in sys.argv[1:]:
            if len(param) == 8:
                print(param)
            elif len(param) < 8:
                print(enlarge(param))
            elif len(param) > 8:
                print(shrink(param))

main()


