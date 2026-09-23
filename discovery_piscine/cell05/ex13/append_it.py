import sys
print("none") if len(sys.argv) == 1 else [print(word + "ism") for word in sys.argv[1:] if not word.endswith("ism")]
