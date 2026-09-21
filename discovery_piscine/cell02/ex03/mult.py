x, y = (int(input("Enter the first number:\n")), int(input("Enter the second number:\n")))
print(f"{x} x {y} = {x * y}")
print("The result is positive." if x * y > 0 else "The result is negative." if x * y < 0 else "The result is positive and negative.")