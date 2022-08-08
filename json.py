import json

print("                             Welcome to file viewer simulator!")
print("What would you like to do?")
print("1. Create File\n2. View File\n")
userChoice = int(input("Enter your choice: "))

while True:
    if userChoice == 1:
        fileName = input("What would you like your file name to be? ")
        fileName =  fileName + ".json"
        datadict = {

        }

        dataAmt = int(
            input("How much data (in the form of keys and values) would you like to enter?(Enter a number): "))
        while dataAmt != 0:
            key = input("Enter your data(key): ")
            value = input("Enter the value for the key " + key + ": ")
            if key == "" or value == "":
                print("Please enter your data with it's value again. (Error: Invalid data or its value)")
            else:
                datadict[key] = value
                dataAmt -= 1
        dumper = json.dumps(datadict)
        with open(fileName, "w") as f:
            f.write(dumper)
        break
    elif userChoice == 2:
        fileName = input("Enter the file name you want to view: ")
        try:
            f = open(fileName+".json", "r")
            reader = json.reads(f)
            print(reader)
        except:
            print("File doesnt exist")
            break
