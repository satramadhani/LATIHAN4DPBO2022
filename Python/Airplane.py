from Vehicle import Vehicle

# Class Airplane, with class Vehicle used as it's parent. 
class Airplane(Vehicle):

    # Airplane attributes.
    __wingsLength = 0.0

    # Constructor. #

    # Constructor with airplane data.
    def __init__(self, name = "", age = 0, vehicleType = "", fuelType = "", maxPassengers = 0, wingsLength = 0.0):
        super().__init__(name, age, vehicleType, fuelType, maxPassengers)
        self.__wingsLength = wingsLength
    
    # Getter and Setter. #

    # Get wings length.
    def getWingsLength(self):
        return self.__wingsLength
        
    # Set wings length.
    def setWingsLength(self, wingsLength):
        self.__wingsLength = wingsLength
    
    # Public Methods. #

    # Start airplane.
    def start(self):
        print("The pilot ready to take-off, the", super().getName(), "starts flying.")
    
    # Stop airplane.
    def stop(self):
        print("The pilot feels enough, the", super().getName(), "stops flying.")