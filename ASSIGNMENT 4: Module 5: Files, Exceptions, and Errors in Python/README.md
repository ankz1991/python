# Python Task Submission
# Module 5: Files, Exceptions, and Errors in Python



This repository contains two Python programs that perform basic tasks using user input.

## Task 1: Read a File and Handle Errors

### Problem Statement
Write a Python program that:
1. Attempts to open and read the contents of a file named `sample.txt`.
2. Handles the case where the file does not exist by displaying an appropriate error message.
3. Ensures the file is properly closed after reading, even if an error occurs.

## Explanation
This program demonstrates file handling and exception management in Python. It tries to open `sample.txt` for reading. If the file is found, it prints its contents. If the file is not found, it catches the `FileNotFoundError` and prints an error message. The `finally` block ensures the file is closed if it was successfully opened.

## Expected Output
If `sample.txt` exists:
```
Reading File Content :
Line 1: This is a sample text file.
Line 2: It contains multiple lines.
```
If `sample.txt` does not exist:
```
Error : The file sample.txt  not found
```

## How to Run
1. Make sure Python is installed.
2. Place a file named `sample.txt` in the same directory as the script (or test the error handling by omitting the file).
3. Open a terminal and navigate to the project directory.
4. Run the script using:
   ```bash
   python "Task 1: Read a File and Handle Errors.py"
   ```

## File Included
- `Task 1: Read a File and Handle Errors.py` – Code to read a file and handle errors if the file






## Task 2: Write and Append Data to a File

### Problem Statement
Write a Python program that:
1. Opens a file named `Output.txt` for reading and writing.
2. Prompts the user to enter text, writes this text to the file, and confirms the action.
3. Prompts the user to enter additional text, appends this text to the file, and confirms the action.
4. Reads and displays the final content of the file.
5. Ensures the file is properly closed after all operations.

## Explanation
This program demonstrates how to write to, append to, and read from a file in Python. It uses the `r+` mode to allow both reading and writing. The program first writes user input to the file, then appends more input, and finally reads and prints the entire file content. The file is closed safely at the end.

## Expected Output
```
Enter text to write to the file : Hello, Python!
Data Successfully Written to  Output.txt
Enter additional text to append : Learning file handling in Python.
Data Successfully appended.
Final Content of  Output.txt
Hello, Python!
Learning file handling in Python.
```

## How to Run
1. Make sure Python is installed.
2. Open a terminal and navigate to the project directory.
3. Run the script using:
   ```bash
   python "Task 2: Write and Append Data to a File.py"
   ```

## File Included
- `Task 2: Write and Append Data to a File.py` – Code to write, append, and read data from a file.
