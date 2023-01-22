class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __lt__(self, other):
        return self.year < other.year


guitars = [Guitar("Fender Stratocaster", 2014, 765.4),
           Guitar("Gibson L-5 CES", 1922, 16035.4),
           Guitar("Line 6 JTV-59", 2010, 1512.9),
           Guitar("Martin Grand J12-16GTE", 2015, 2199),
           Guitar("Taylor PS10ce", 2014, 9318),
           Guitar("Gretsch 6120 Chet Atkins", 1956, 10999.99)]

guitars.sort()

for guitar in guitars:
    print(guitar.name, guitar.year, guitar.cost)

    guitars = []  # initialize empty list

    while True:
        name = input("Enter the name of the guitar (or 'q' to quit): ")
        if name == 'q':
            break
        year = int(input("Enter the year of the guitar: "))
        cost = float(input("Enter the cost of the guitar: "))
        guitars.append(Guitar(name, year, cost))

with open('guitars.csv', 'w') as f:
    for guitar in guitars:
        f.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
