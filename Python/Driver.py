import imp
from Person import Person
from Job import Job

# Class Driver, with class Person AND Job used as it's parents.
class Driver(Person, Job):

    # Driver attributes.
    __licenseID = ''
    __activeUntil = 0
    __vehicleType = ""

    # Constructor. #

    def __init__(self, licenseID = '', activeUntil = 0, vehicleType = ""):
        self.__licenseID = licenseID
        self.__activeUntil = activeUntil
        self.__vehicleType = vehicleType
    
    # Getter and Setter. #
    
    # Get license ID.
    def getLicenseID(self):
        return self.__licenseID
    
    # Get "active until" attribute.
    def getActiveUntil(self):
        return self.__activeUntil
    
    # Get vehicle type.
    def getVehicleType(self):
        return self.__vehicleType
    
    # Set license ID.
    def setLicenseID(self, licenseID):
        self.__licenseID = licenseID
    
    # Set "active until" attribute.
    def setActiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil
    
    # Set vehicle type.
    def setVehicleType(self, vehicleType):
        self.__vehicleType = vehicleType