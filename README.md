# Novtrois_attendance_system
We have created an automated attendance system where the student can enter his or her attendance with their ID-card and face recognition.

We have used python and various python modules to make this happen.

## Requirements
The user has to note that his/her's camera should have adequate resolution for the bar code to be clear.
In case the bar code is unclear or the camera is not working, the program will prompt the user to align the ID card correctly.

## Attendance.py
Currently, the attendance.py is the parent file of test.py. In these files the bar code is scanned and the roll number is displayed. The program will prompt at each step.
To run these files it is enough to run attendance.py

## timetable input test.py
The timetable input test.py stores the timetable. It will prompt the repsective teacher to enter the start time, end time of a period, course code/subject, and his/her email id for each period. 

## face2.py
The face2.py is where the real magic happens! It is a simple algorithm which just compares 2 images. It's not foolproof but it's still in it's toddler's phase as we have not implemented machine learning due to the time constraint and the lack of suitable pre-trained models.

## Procedure to run the program
This is to note that currently attendance.py and test.py were tested in python 3.8.0, face2.py was tested in python 3.6.6(due to the lack of face_recognition in the later flavours of python) and "timetable input test.py" in python 3.10. But we believe that the code should be stable in Windows 10 and python 3.6.6. You should also have visual studio tools installed for smooth functioning of program.
