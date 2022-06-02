# For handling package classes and importing
import csv


# Create a package class that includes the 8 fields from the package.csv file + delivery status
class Package:
    def __init__(self, packageID, address, city, state, zipcode, deadline, massKg, notes, departure, timestamp):
        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.massKg = massKg
        self.notes = notes
        self.departure = departure
        self.timestamp = timestamp

    def __str__(self):  # overwrite print(package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.packageID, self.address, self.city, self.state,
            self.zipcode, self.deadline, self.massKg, self.notes, self.departure, self.timestamp)


# Use csvreader to extract package data
# Complexity: O(N)
def loadPackageData(fileName, packageHash):
    with open(fileName) as packages:
        packageData = csv.reader(packages, delimiter=',')
        next(packageData)  # skip header
        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = package[4]
            pDeadline = package[5]
            pMassKg = package[6]
            pNotes = package[7]
            pDeparture = package[8]
            pTimestamp = package[9]

            # Create a package object
            package = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pMassKg, pNotes, pDeparture, pTimestamp)

            # Add the package object to the hash table using the insert() function
            packageHash.insert(pID, package)
