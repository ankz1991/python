# Python Task Submission
# Module 6: Data Structures and Strings in Python



This repository contains two Python programs that perform basic tasks using user input.

## Task 1: Create a Dictionary of Student Marks

## Problem Statement
Write a Python program that:
1. Stores student names and their marks in a dictionary.
2. Prompts the user to enter a student's name.
3. Checks if the student exists in the dictionary.
4. If found, displays the student's marks; otherwise, displays a "Student not found" message.

## Explanation
This program demonstrates the use of dictionaries in Python to store and retrieve data. It allows the user to look up a student's marks by name. If the entered name matches a key in the dictionary, the program prints the corresponding marks; otherwise, it notifies the user that the student was not found.

## Expected Output
If the user enters a name present in the dictionary:
```
Enter the student's name : Alice
Alice's marks : 85
```
If the user enters a name not present in the dictionary:
```
Enter the student's name : John
Student not found.
```

## How to Run
1. Make sure Python is installed.
2. Open a terminal and navigate to the project directory.
3. Run the script using:
   ```bash
   python "Task 1: Create a Dictionary of Student Marks.py"
   ```

## File Included
- `Task 1: Create a Dictionary of Student Marks.py` – Code to store and retrieve student marks using






## Task 2: Demonstrate List Slicing

## Problem Statement
Write a Python program that:
1. Creates a list of numbers from 1 to 10.
2. Extracts the first five elements from the list using slicing.
3. Reverses the extracted elements using slicing.
4. Prints the original list, the extracted elements, and the reversed extracted elements.

## Explanation
This program demonstrates how to use list slicing in Python. It first creates a list of numbers from 1 to 10. It then uses slicing to extract the first five elements (`listNumbers[0:5]`) and reverses this sublist (`ExtractFirstFive[::-1]`). The results are printed at each step.

## Expected Output
```
Original List :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extract First Five elements [1, 2, 3, 4, 5]
Reversed Extracted Elements :  [5, 4, 3, 2, 1]
```

## How to Run
1. Make sure Python is installed.
2. Open a terminal and navigate to the project directory.
3. Run the script using:
   ```bash
   python "Task 2: Demonstrate List Slicing.py"
   ```

## File Included
- `Task 2: Demonstrate List Slicing.py` – Code to demonstrate list slicing and reversing in
