import sys

if len(sys.argv) != 3:
    print("none")
else:
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    if start <= end:
        numbers = list(range(start, end + 1))
    else:
        numbers = list(range(end, start + 1))

    print(numbers)