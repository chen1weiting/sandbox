from Week6.guitar import Guitar

def main():
    """Testing Guitar class"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    print(f"\n{guitar.name:>35}\n")
    print(f"{guitar.name}get_age() - Expected {98}.Got{guitar.get_age()}")
    print(f"{guitar.name}is_vintage() - Expected {False}. Got{guitar.is_vintage()}")

    guitar_two = Guitar("Martin D-45", 1933, 135000.00)# Year changed from 2013to 1933
    print(f"\n{guitar_two.name:>35}\n")
    print(f"{guitar_two.name}get_age() - Expected {89}.Got{guitar_two.get_age()}")
    print(f"{guitar_two.name}is_vintage() - Expected {True}. Got{guitar_two.is_vintage()}")

 if __name__ == '__main__':
    main()