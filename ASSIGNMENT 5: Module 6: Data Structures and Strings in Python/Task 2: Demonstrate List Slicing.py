#Creates a list of numbers from 1 to 10.
listNumbers = list(range(1,11))
print("Original List : ",listNumbers)
#Extracts the first five elements from the list.
ExtractFirstFive=listNumbers[0:5]
print("Extract First Five elements",ExtractFirstFive)
ReverseExtractedList= ExtractFirstFive[::-1]
print("Reversed Extracted Elements : ",ReverseExtractedList)
