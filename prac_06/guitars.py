from Week6.guitar import Guitar

def main():
    """Start of program"""
    print("My guitars!")
    name = input("Name: ")
    guitars = []
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)guitars.append(guitar)
        print(guitar, " added.")
        name = input("\nName: ")

    if guitars:
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            if guitar.is_vintage():
                print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} (vintage)")
            else:print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}")
    else:
        print("\nNo guitars :( Quick, go and buy one!")

if __name__ == '__main__':
    main()