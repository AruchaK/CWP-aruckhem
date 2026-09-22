import sys

if len(sys.argv) != 2:
    print("none")
else:
    param = sys.argv[1]
    print("Good job!" if param == str(input("What was the parameter? ")) else "Nope, sorry...")