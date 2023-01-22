CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

# Print all the states and names neatly lined up with string formatting
for code, name in CODE_TO_NAME.items():
    print("{:3s} is {}".format(code, name))

while True:
    # Prompt for a state code and convert it to uppercase
    state_code = input("Enter short state: ").upper()

    # Check if the input is a valid state code using the EAFP approach
    try:
        # If the code is valid, print the state name
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        # If the code is invalid, print an error message and prompt for another code
        print("Invalid short state")
        continue

    # If the input is blank, stop the loop
    if state_code == "":
        break