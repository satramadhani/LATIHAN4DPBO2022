# Saya [Muhammad Satria Ramadhani - 2005128] mengerjakan evaluasi [Latihan
# Praktikum 04] dalam mata kuliah [Desain dan Pemrograman Berorientasi Objek]
# untuk keberkahan-Nya, maka saya tidak melakukan kecurangan seperti yang
# telah dispesifikasikan. Aamiin.

# Import vehicles class.
from Vehicle import Vehicle
from Ship import Ship
from Airplane import Airplane

# Import persons class.
from Person import Person
from Job import Job
from Driver import Driver


# Hardcode input for Ship data. #

ship = [Ship("Aldian Coast", 3, "Transport Ship", "Biofuel", 65535, "Japan"),
        Ship("Binsar Tour", 1, "Entertainment Ship", "Diesel", 1024, "Indonesia"),
        Ship("Carla Entertainment", 2, "Entertainment Ship", "Biofuel", 1024, "France"),
        Ship("Ellona", 4, "Transport Ship", "Solar", 2048, "Italy"),
        Ship("Lunox Beauty", "Entertainment Ship", "Biofuel", 512, "USA")]

# Hardcode input for Airplane data. #

airplane = [Airplane("Aldian Flight", 3, "Transport Airplane", "Aftur", 384, 48),
            Airplane("Hanliszt Symphony", 4, "Cargo Airplane", "Aftur", 2, 8),
            Airplane("Rainview Plane", 1, "Private Airplane", "Aftur", 8, 16),
            Airplane("Ripkysan", 2, "Transport Airplane", "Aftur", 256, 46),
            Airplane("Techi Darkplane", 1, "Private Airplane", "Aftur", 4, 10)]

# Hardcode input for Person/Driver data. # 

driver = [Driver('C', 2022, "Motorcycle"),
          Driver('C', 2023, "Motorcycle"),
          Driver('A', 2024, "Car"),
          Driver('B', 2025, "Truck"),
          Driver('A', 2026, "Car")]

driver[0].setNIK(2000514)
driver[0].setName("Satlight")
driver[0].setGender('M')
driver[0].setNIP(123456789)
driver[0].setCompanyName("Universitas Pendidikan Indonesia")
driver[0].setPosition("Third-Class Employee")

driver[1].setNIK(2001123)
driver[1].setName("Rainchivo")
driver[1].setGender('M')
driver[1].setNIP(234567890)
driver[1].setCompanyName("Moonton Indonesia")
driver[1].setPosition("Third-Class Employee")

driver[2].setNIK(2001531)
driver[2].setName("Hanlizst")
driver[2].setGender('M')
driver[2].setNIP(345678901)
driver[2].setCompanyName("Beethoven Melodies")
driver[2].setPosition("Second-Class Employee")

driver[3].setNIK(2001680)
driver[3].setName("Handicki")
driver[3].setGender('M')
driver[3].setNIP(456789012)
driver[3].setCompanyName("Pertamina")
driver[3].setPosition("First-Class Employee")

driver[4].setNIK(2005128)
driver[4].setName("Techiknight")
driver[4].setGender('M')
driver[4].setNIP(567890123)
driver[4].setCompanyName("Keyakizaka46 Seed & Flower")
driver[4].setPosition("First-Class Employee")

# Output. #

# Print Ship data.
print("= = = Ship Data = = =")
print("")

for i in range(5):
    print("Name      :", ship[i].getName())
    print("Age       :", ship[i].getAge())
    print("Type      :", ship[i].getType())
    print("Fuel Type :", ship[i].getFuelType())
    print("Max Pass. :", ship[i].getMaxPassengers())
    print("Country   :", ship[i].getCountryOfManufacture())
    
    ship[i].start()
    ship[i].move()
    ship[i].stop()
    print("")

# Print Airplane data.
print("= = = Airplane Data = = =")
print("")

for i in range(5):
    print("Name         :", airplane[i].getName())
    print("Age          :", airplane[i].getAge())
    print("Type         :", airplane[i].getType())
    print("Fuel Type    :", airplane[i].getFuelType())
    print("Max Pass.    :", airplane[i].getMaxPassengers())
    print("Wings Length :", airplane[i].getWingsLength())
    
    airplane[i].start()
    airplane[i].move()
    airplane[i].stop()
    print("")

# Print Person/Driver data.
print("= = = Driver Data = = =")
print("")

for i in range(5):
    print("NIK            :", driver[i].getNIK())
    print("Name           :", driver[i].getName())
    if(driver[i].getGender() == 'M'):
        print("Gender         : Male")
    else:
        print("Gender         : Female")
    print("NIP            :", driver[i].getNIP())
    print("Company        :", driver[i].getCompanyName())
    print("Position       :", driver[i].getPositon())
    print("License ID     :", driver[i].getLicenseID())
    print("- Active Until :", driver[i].getActiveUntil())
    print("- Vehicle Type :", driver[i].getVehicleType())
    
    driver[i].sleep()
    driver[i].wake()
    driver[i].walk()
    print("")