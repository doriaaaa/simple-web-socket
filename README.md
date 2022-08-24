# simple-web-socket
IERG3310 web socket project

The project consists of two parts: 
student.py 
robot.py

How to run the program
Run Robot.py before running student.py

Special remarks
In student.py, if two machines are required to test the program, eg. Machine A is for student.py and Machine B is for Robot.py, the host name needs to be changed manually in student.py main(). User can comment line 78, which is the code that allows robot.py and student.py to run locally. User needs to input the IP of Machine B (with robot.py) to locate the connection by uncommenting line 79 and input the IP address there.
Apart from testing for two machines, user can go to student.py to adjust the TCP buffer size in s3() and the time required to send the message. User can amend the buffer size in line 47 by inputting their own buffer size. In line 53, user can adjust the time required to test the input in there. The default time will be 30 seconds.
