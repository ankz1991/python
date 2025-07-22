student_marks ={"Alice":85,
                "Bob":90,
                "David":70,
                "Eve":60,
                "Fred":55,
                "Marks":80,
                "Samson":60,
                "Thomas":60}

sudentName=input("Enter the student's name : ")

if sudentName in student_marks:
    mark=student_marks[sudentName]
    print("{}'s marks : {}".format(sudentName,mark))
else:
    print("Student not found.")