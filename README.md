# Novtrois_attendance_system
We have created an automated attendance system where the student can enter his or her attendance with their ID-card and face recognition.

We have used python and various python modules to make this happen.

## Requirements
The user has to note that his/her's camera should have adequate resolution for the bar code to be clear.
In case the bar code is unclear or the camera is not working, the program will prompt the user to align the ID card correctly.

## Functioning of attendance system
At the beginning of the day, the system is started. Initially the tutor must give details of current day timetable(such as start time, end time, course code, email ID of subject teacher and tutor's). The attendance.py is initiated.
It asseses the current time using datetime module. The start time of a period is assesed for the time pool of 10 minutes where the barcode and faces are scanned and attendance is recorded. End time is assesed to stop scanning and a mail having a list of absentees is sent to the repsective teachers and tutor's mail ID. This happens for each period.
At 10PM(2200) the program ends

## Attendance.py
Currently, the attendance.py is the parent file of test.py. In these files the bar code is scanned and the roll number is displayed. The program will prompt at each step.
To run these files it is enough to run attendance.py
In the attendance.py, the time is compared using datetime module. 

## timetable input test.py
The timetable input test.py stores the timetable. It will prompt the repsective teacher to enter the start time, end time of a period(in 24 hour format), course code/subject, and his/her email id for each period. The time should be given in the form of HHMM(eg: 830 means 8:30AM)

## face2.py
The face2.py is where the real magic happens! It is a simple algorithm which just compares 2 images. It's not foolproof but it's still in it's toddler's phase as we have not implemented machine learning due to the time constraint and the lack of suitable pre-trained models.

## Procedure to run the program
This is to note that currently attendance.py and test.py were tested in python 3.8.0, face2.py was tested in python 3.6.6(due to the lack of face_recognition in the later flavours of python) and "timetable input test.py" in python 3.10. But we believe that the code should be stable in Windows 10 and python 3.6.6. You should also have visual studio tools installed for smooth functioning of program.
First, you have to run the timetable input test.py file to input the timetable with details and tutor's mail, and then attendance.py should be run after this.

### Disclaimer
>In case the files in the final folder are not working, you can try running the attendance.py, timetable input test.py and face2.py in the proto folder. They are not linked but are working models. 😅

You need to install face_recongition, dlib, opencv-python, tkinter, pyzbar and pickle modules. 
