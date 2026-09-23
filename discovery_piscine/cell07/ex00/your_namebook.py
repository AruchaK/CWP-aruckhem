def array_of_names(dict):
    return [f"{key} {value}" for key, value in dict.items()]

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))
