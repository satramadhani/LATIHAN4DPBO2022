# Class Job, used as one of "base" parent of profession (multiple-type). 
class Job:

    # Job attributes.
    __nip = 0
    __companyName = ""
    __position = ""

    # Constructor. #

    def __init__(self, nip = 0, companyName = "", position = ""):
        self.__nip = nip
        self.__companyName = companyName
        self.__position = position
    
    # Getter and Setter. #

    # Get NIP attribute.
    def getNIP(self):
        return self.__nip
    
    # Get company name.
    def getCompanyName(self):
        return self.__companyName
    
    # Get position attribute.
    def getPositon(self):
        return self.__position
    
    # Set NIP attribute.
    def setNIP(self, nip):
        self.__nip = nip
    
    # Set company name.
    def setCompanyName(self, companyName):
        self.__companyName = companyName
    
    # Set position attribute.
    def setPosition(self, position):
        self.__position = position