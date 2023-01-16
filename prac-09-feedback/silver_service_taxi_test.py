from silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Hummer", 200, 2)
taxi.drive(18)
print(taxi.get_fare()) # Expected output: 48.78
print(taxi)
# Expected output: Hummer, fuel=200, odo=18, 18km on current fare, $9.84/km plus flagfall of $4.50