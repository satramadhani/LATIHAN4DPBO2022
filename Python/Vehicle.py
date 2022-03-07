# Class Vehicle, used as a single "base" of another vehicle (hierarchical-type).
class Vehicle:

    # Vehicle attributes.
    __name = ""
    __age = 0
    __vehicleType = ""
    __fuelType = ""
    __maxPassengers = 0

    # Constructor. #

    # Constructor with vehicle data.
    def __init__(self, name = "", age = 0, vehicleType = "", fuelType = "", maxPassengers = 0):
        self.__name = name
        self.__age = age
        self.__vehicleType = vehicleType
        self.__fuelType = fuelType
        self.__maxPassengers = maxPassengers

    # Getter and Setter. #

    # Get name attribute.
    def getName(self):
        return self.__name

    # Get age attribute.
    def getAge(self):
        return self.__age

    # Get type attribute.
    def getType(self):
        return self.__vehicleType
    
    # Get fuel type.
    def getFuelType(self):
        return self.__fuelType
    
    # Get max passengers.
    def getMaxPassengers(self):
        return self.__maxPassengers
    
    # Set name attribute.
    def setName(self, name):
        self.__name = name

    # Set age attribute.
    def setAge(self, age):
        self.__age = age
    
    # Set type attribute.
    def setType(self, type):
        self.__vehicleType = type

    # Set fuel type.
    def setFuelType(self, fuelType):
        self.__fuelType = fuelType
    
    # Set max passengers.
    def setMaxPassengers(self, maxPassengers):
        self.__maxPassengers = maxPassengers

    # Public Methods. #

    # Move vehicles.
    def move(self):
        print("The", self.__name, "is moving.")