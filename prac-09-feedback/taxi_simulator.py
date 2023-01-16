class Taxi:
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def drive(self, distance):
        cost = distance * 1.23
        self.odometer += distance
        self.fuel -= distance / 10
        return cost

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}, {self.odometer}km on current fare, $1.23/km"

class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness_factor):
        super().__init__(name, fuel)
        self.fanciness_factor = fanciness_factor
        self.flagfall = 4.50

    def drive(self, distance):
        cost = distance * (1.23 * self.fanciness_factor) + self.flagfall
        self.odometer += distance
        self.fuel -= distance / 10
        return cost

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}, {self.odometer}km on current fare, $2.46/km plus flagfall of $4.50"

    def main():
        taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
        current_taxi = None
        bill = 0.00

        while True:
            print("q)uit, c)hoose taxi, d)rive")
            user_input = input()
            if user_input == "q":
                break
            elif user_input == "c":
                # display list of taxis and prompt user to choose one
                for i, taxi in enumerate(taxis):
                    print(f"{i} - {taxi}")
                choice = int(input("Choose taxi: "))
                if choice < 0 or choice >= len(taxis):
                    print("Invalid taxi choice")
                else:
                    current_taxi = taxis[choice]
                    print(f"Bill to date: ${bill:.2f}")
            elif user_input == "d":
                if current_taxi is None:
                    print("You need to choose a taxi before you can drive")
                else:
                    # prompt user for distance and drive the taxi
                    distance = int(input("Drive how far? "))
                    cost = current_taxi.drive(distance)
                    bill += cost
                    print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
                    print(f"Bill to date: ${bill:.2f}")
            else:
                print("Invalid option")
                print(f"Bill to date: ${bill:.2f}")
        print(f"Total trip cost: ${bill:.2f}")