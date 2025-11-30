"""
This module demonstrates working with composite data types in Python:
a List that contains Dictionary objects, populated from a CSV file.
It uses the csv and copy modules for file handling and deep copying.
"""
import csv
import copy

# 1. Definisi Dictionary Template
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# Demonstrasi Loop pada Dictionary Template
print("--- Dictionary Template ---")
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))

# 2. Definisi List Inventaris Kosong
myInventoryList = []

# 3. Membaca Data dari CSV ke Memori (List of Dictionaries)
print("\n--- Processing CSV Data ---")
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            # Baris Header
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            # Baris Data
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            
            # Membuat Deep Copy dari template untuk setiap baris
            currentVehicle = copy.deepcopy(myVehicle)  
            
            # Memetakan nilai dari baris CSV ke Dictionary
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            
            # Menambahkan Dictionary yang telah diisi ke List
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')

# 4. Mencetak Inventaris Mobil Lengkap (List of Dictionaries)
print("\n--- Final Car Inventory ---")
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
    print("-----")