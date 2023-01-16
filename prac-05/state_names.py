CODE_TO_NAME = {"qld": "Queensland", "nsw": "New South Wales", "nt" : "Northern Territory", "wa" : "Western Australia",
"act": "Australian Capital Territory", "vic": "Victoria", "tas": "Tasmania"}

print("List of state codes and names:")
for code, name in CODE_TO_NAME.items():
    print("{} is {}".format(code.upper(), name))

while True:
    state_code = input("Enter short state (or press enter to stop): ").strip().lower()
    if state_code == "":
        break
    try:
        print("{} is {}".format(state_code.upper(), CODE_TO_NAME[state_code]))
    except KeyError:
        print("Invalid short state")
