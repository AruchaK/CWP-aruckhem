import sys

def downcase_all(string):
    return string.lower()

if len(sys.argv) < 2:
    print("none")
else:
    for param in sys.argv[1:]:
        print(downcase_all(param))