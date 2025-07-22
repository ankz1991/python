fileName="Output.txt"
file = None
try:
    file = open(fileName, "r+")
    file.write(input("Enter text to write to the file : ")+ "\n")
    print("Data Successfully Written to ",fileName)
    file.write(input("Enter additional text to append : ")+ "\n")
    print("Data Successfully appended.")
    # Move file pointer to beginning before reading
    file.seek(0)
    print("Final Content of ",fileName)
    content = file.read()
    print(content)
finally:
    if file:
        file.close()