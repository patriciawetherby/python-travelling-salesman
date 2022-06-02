# Patricia Wetherby, Student ID: 000768032
# main

# Imports
import csv
from hashTable import ChainingHashTable
from CSV import loadPackageData
import datetime as dt

# Load Packages into Chaining HashTable

packageHash = ChainingHashTable()
loadPackageData('packages.csv', packageHash)


# Complexity : O(N)
def getPackageData():
    # Fetch data from Hash Table
    for i in range(len(packageHash.table)):
        print("Key: {} and Value: {}".format(i + 1, packageHash.search(i + 1)))


distanceArray = []

# Get distance data


# Complexity : O(N)
def loadDistanceData(fileName):
    with open(fileName) as distances:
        distanceFile = csv.reader(distances, delimiter=',')
        for row in distanceFile:
            distanceArray.append(row)
        # print(distanceArray)


# Get address data

addressData = {
    "4001 South 700 East (HUB)": "0",
    "1060 Dalton Ave S": "1",
    "1330 2100 S": "2",
    "1488 4800 S": "3",
    "177 W Price Ave": "4",
    "195 W Oakland Ave": "5",
    "2010 W 500 S": "6",
    "2300 Parkway Blvd": "7",
    "233 Canyon Rd": "8",
    "2530 S 500 E": "9",
    "2600 Taylorsville Blvd": "10",
    "2835 Main St": "11",
    "300 State St": "12",
    "3060 Lester St": "13",
    "3148 S 1100 W": "14",
    "3365 S 900 W": "15",
    "3575 W Valley Central Station bus Loop": "16",
    "3595 Main St": "17",
    "380 W 2880 S": "18",
    "410 S State St": "19",
    "4300 S 1300 E": "20",
    "4580 S 2300 E": "21",
    "5025 State St": "22",
    "5100 South 2700 West": "23",
    "5383 S 900 East #104": "24",
    "600 E 900 South": "25",
    "6351 S 900 East": "26"
}


# Lookup address using a string address
# Complexity: O(N)
def addressLookup(stringAddress):
    for key, value in addressData.items():
        if stringAddress == key:
            return value


# Lookup position on distanceArray
# Complexity: O(1)
def distanceBetween(address1, address2):
    return distanceArray[int(addressLookup(address1))][int(addressLookup(address2))]


# Calculate distance for mileage
# Complexity: O(1)
def convertDistanceToTime(distance):
    return distance / mph


# Nearest Neighbor Algorithm:
# Calculate nearest address from the truck's current position
# Complexity: O(N)
def nearestNeighbor(currAddress, truckLoad):
    minDistance = 1000
    nearestAddress = ''
    nearestPackage = ''
    # Cycle through packages in truck
    for pkg in truckLoad:
        package = packageHash.search(int(pkg))
        packageAddress = package.address
        # Calculate distance between addresses using the distanceArray lookup
        distance = float(distanceBetween(currAddress, packageAddress))
    # Remember smallest distance and nearest package
        if distance < minDistance:
            minDistance = distance
            nearestPackage = pkg
            nearestAddress = packageAddress
    package = packageHash.search(int(nearestPackage))
    return nearestAddress, package

# Main Algorithm

# Initialize variables


# Manually load all the trucks
truck1_load = ['1', '2', '13', '14', '15', '16', '19', '20', '29', '30', '31', '34', '35', '40']
truck2_load = ['3', '6', '8', '10', '12', '18', '21', '23', '25', '27', '36', '37', '38', '39']
truck3_load = ['4', '5', '7', '9', '11', '17', '22', '24', '26', '28', '32', '33']

# Set mileage of each trucks to 0
t1Miles = 0
t2Miles = 0
t3Miles = 0

# Load distances into distanceArray
loadDistanceData('distances.csv')

# Delivery One

# Set current address at Hub
currentAddress = "4001 South 700 East (HUB)"
addressVisited = []
currentPackage = ""

# Clock to emulate time passing
mph = 18 / 60  # 18 mph

# Set Truck 1 departure time to 8:00 am
truck1Time = dt.datetime(2021, 2, 28, 8, 0, 0)
timeElapsed = dt.timedelta(minutes=0)

# Set Truck 1 packages departure time
# Complexity: O(N)
for p in truck1_load:
    (packageHash.search(int(p))).departure = (dt.datetime(2021, 2, 28, 8, 0, 0).strftime("%H:%M"))

# Move to new address and deliver packages
# Complexity: O(N^2)
while len(truck1_load) > 0:
    # Find next address
    nextAddress, currentPackage = nearestNeighbor(currentAddress, truck1_load)
    # print("Current Address: " + currentAddress)
    # print("Next Address: " + nextAddress)
    # Calculate distance traveled
    miles = float(distanceBetween(currentAddress, nextAddress))
    t1Miles += miles
    # Convert distance to time using mph
    timeElapsed += dt.timedelta(minutes=(convertDistanceToTime(miles)))
    deliveryTime = truck1Time + timeElapsed
    # Timestamp package for drop off
    currentPackage.timestamp = (deliveryTime.strftime("%H:%M"))
    # print(currentPackage)
    # Drop off package
    truck1_load.remove(str(currentPackage.packageID))
    # Move to next address
    currentAddress = nextAddress

# return to Hub and calculate mileage
t1Miles += float(distanceBetween(currentAddress, "4001 South 700 East (HUB)"))
currentAddress = "4001 South 700 East (HUB)"

# Delivery Two

# Set Truck 2 delivery to 9:05 am and reset timeElapsed
truck2Time = dt.datetime(2021, 2, 28, 9, 5, 0)
timeElapsed = dt.timedelta(minutes=0)

# Set Truck 2 packages departure time
# Complexity: O(N)
for q in truck2_load:
    (packageHash.search(int(q))).departure = (dt.datetime(2021, 2, 28, 9, 5, 0).strftime("%H:%M"))

# Move to new address and deliver packages
# Complexity: O(N^2)
while len(truck2_load) > 0:
    # Find next address
    nextAddress, currentPackage = nearestNeighbor(currentAddress, truck2_load)
    # print("Current Address: " + currentAddress)
    # print("Next Address: " + nextAddress)
    # Calculate distance traveled
    miles = float(distanceBetween(currentAddress, nextAddress))
    t1Miles += miles
    # Convert distance to time using mph
    timeElapsed += dt.timedelta(minutes=(convertDistanceToTime(miles)))
    deliveryTime = truck2Time + timeElapsed
    # Timestamp package for drop off
    currentPackage.timestamp = (deliveryTime.strftime("%H:%M"))
    # Drop off package
    truck2_load.remove(str(currentPackage.packageID))
    # Move to next address
    currentAddress = nextAddress

# return to Hub and calculate mileage
t2Miles += float(distanceBetween(currentAddress, "4001 South 700 East (HUB)"))
currentAddress = "4001 South 700 East (HUB)"

# Delivery Three

# Change time for Truck 3 and reset timeElapsed
truck3Time = dt.datetime(2021, 2, 28, 11, 0, 0)
timeElapsed = dt.timedelta(minutes=0)

# Fix Address Error on Package 9 and address changes
(packageHash.search(int(9))).address = '410 S State St'
(packageHash.search(int(9))).notes = "Address corrected"

# Set Truck 3 packages departure time
# Complexity: O(N)
for r in truck3_load:
    (packageHash.search(int(r))).departure = (dt.datetime(2021, 2, 28, 11, 0, 0).strftime("%H:%M"))

# Move to new address and deliver packages
# Complexity: O(N^2)
while len(truck3_load) > 0:
    # Find next address
    nextAddress, currentPackage = nearestNeighbor(currentAddress, truck3_load)
    # print("Current Address: " + currentAddress)
    # print("Next Address: " + nextAddress)
    # Calculate distance traveled
    miles = float(distanceBetween(currentAddress, nextAddress))
    t1Miles += miles
    # Convert distance to time using mph
    timeElapsed += dt.timedelta(minutes=(convertDistanceToTime(miles)))
    deliveryTime = truck3Time + timeElapsed
    # Timestamp package for drop off
    currentPackage.timestamp = (deliveryTime.strftime("%H:%M"))
    # Drop off package
    truck3_load.remove(str(currentPackage.packageID))
    # Move to next address
    currentAddress = nextAddress
# return to Hub
t3Miles += float(distanceBetween(currentAddress, "4001 South 700 East (HUB)"))

# print(t1Miles)
# print(t2Miles)
# print(t3Miles)

# Calculate Total Miles
totalMiles = t1Miles + t2Miles + t3Miles
# print(totalMiles)

# Deliveries Completed!!!

# Control GUI

print('-------------------------------------------')
print('WGUPS Delivery System')
print('-------------------------------------------')
print('Route was completed in {} miles'.format(totalMiles))

print('1 = Enter time')
print('2 = Print All Packages')
print('3 = Lookup User Package')
print('4 = End')
# Receive user input
num = input('Enter a number: ')


if num == '1':
    try:
        # Receive input time from user
        input_time = input('Enter a time in 24 hour format (HH:MM): ')
        (hr, mn) = input_time.split(':')
        convertInputTime = dt.timedelta(hours=int(hr), minutes=int(mn))

        # Convert timestamps for comparison
        # Complexity: O(N)
        for count in range(1, 41):
            t = packageHash.search(count)
            inTransit = t.departure
            time = t.timestamp
            (hr, mn) = inTransit.split(':')
            convertInTransitTime = dt.timedelta(hours=int(hr), minutes=int(mn))
            (hr, mn) = time.split(':')
            convertDeliveredTime = dt.timedelta(hours=int(hr), minutes=int(mn))

            # If time entered is before delivery
            if convertInputTime <= convertInTransitTime:
                print('Package ID: ' + str(t.packageID) + ' at HUB')
                print('Leaves at: ' + inTransit)
                print('-----------------')

            # If time entered is on truck after in transit
            elif convertInputTime >= convertInTransitTime:
                # If time entered is after delivery
                if convertInputTime < convertDeliveredTime:
                    print('Package ID: ' + str(t.packageID) + ' In Transit')
                    print('Left at: ' + inTransit)
                    print('-----------------')
                else:
                    print('Package ID: ' + str(t.packageID) + ' Delivered')
                    print('Delivered at: ' + time)
                    print('-----------------')

    except IndexError:
        print(IndexError)
        exit()
    except ValueError:
        print('Invalid entry')
        exit()

elif num == '2':
    # Print all package data
    getPackageData()
elif num == '3':
    package_input = input('Enter the Package ID: ')
    # Print package that matches ID
    print(packageHash.search(int(package_input)))
elif num == '4':
    # Exit Program
    print('Exiting now...')
    exit(0)
else:
    print("Please enter valid number")
