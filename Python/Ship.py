from Vehicle import Vehicle

# Class Ship, with class Vehicle used as it's parent. 
class Ship(Vehicle):

    # Ship attributes.
    __countryOfManufacture = ""

    # Constructor. #

    # Constructor with ship data.
    def __init__(self, name = "", age = 0, vehicleType = "", fuelType = "", maxPassengers = 0, countryOfManufacture = ""):
        super().__init__(name, age, vehicleType, fuelType, maxPassengers)
        self.__countryOfManufacture = countryOfManufacture
    
    # Getter and Setter. #
    
    # Get country of manufacture.
    def getCountryOfManufacture(self):
        return self.__countryOfManufacture
    
    # Set country of manufacture.
    def setCountryOfManufacture(self, countryOfManufacture):
        self.__countryOfManufacture = countryOfManufacture
    
    # Public Methods. #

    # Start ship.
    def start(self):
        print("The wind blows to the East, the", super().getName(), "starts sailing.")
    
    # Stop ship.
    def stop(self):
        print("The journey ends here, the", super().getName(), "ship stops sailing.")
