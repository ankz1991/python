filename = "sample.txt"
file = None
try:
    file = open(filename, 'r')
    printFile = file.read()
    print("Reading File Content :")
    print(printFile)
except FileNotFoundError:
    print("Error : The file", filename, " not found")
finally:
    if file:
        file.close()
