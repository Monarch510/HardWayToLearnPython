cites = {"ca": "san francisco", "mi": "detroit", "fl": "jacksonville"}
cites["ny"] = "new york"
cites["or"] = "portland"


def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "not found"


cites["find"] = find_city
while True:
    print("state?(enter to quit)")
    state = input(">")
    if not state:
        break
    cite_found = cites["find"](cites, state)
    print(cite_found)
