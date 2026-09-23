def greetings(string="noble stranger"):
    if not isinstance(string, str):
        print("Error! It was not a name.")
    else:
        print(f"Hello, {string}.")

greetings("Alexandra")
greetings("Wil")
greetings()
greetings(42)