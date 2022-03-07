# Class Person, used as one of "base" parent of profession (multiple-type). 
class Person:

    # Person attributes.
    __nik = 0
    __name = ""
    __gender = ''
    
    # Constructor. #

    def __init__(self, nik = 0, name = "", gender = ''):
        self.__nik = nik
        self.__name = name
        self.__gender = gender
    
    # Getter and Setter. #

    # Get NIK attribute.
    def getNIK(self):
        return self.__nik
    
    # Get name attribute.
    def getName(self):
        return self.__name
    
    # Get gender attribute.
    def getGender(self):
        return self.__gender
    
    # Set NIK attribute.
    def setNIK(self, nik):
        self.__nik = nik
    
    # Set name attribute.
    def setName(self, name):
        self.__name = name
    
    # Set gender attribute.
    def setGender(self, gender):
        self.__gender = gender
    
    # Public Methods. #

    # Person sleep.
    def sleep(self):
        print(self.__name, "feels sleepy, they start sleeping.")
    
    # Person wake up.
    def wake(self):
        print(self.__name, "feels enough, they wake up.")
    
    # Person walk.
    def walk(self):
        print(self.__name, "is walking.")