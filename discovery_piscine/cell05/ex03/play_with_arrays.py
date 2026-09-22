x = [2, 8, 9, 48, 8, 22, -12, 2]
print("Original array: " + str(x))
print("New array: " + str(set([i + 2 for i in set(x) if i > 5])))