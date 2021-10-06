# Tello-control-with-arduino-nano-33-ble-sense
Controlling dji Tello drone with Arduino nano 33 ble Sense.
Using microcontroller's gesture sensor and the Inertial Measurement Unit (IMU) we are able to fly the drone in 4 + 2 directions: UP, DOWN, LEFT, RIGHT, FRONT & BACK
Python and Arduino code is available.
# Important!
Using the serial port in Python means that we cannot have the two programs opened at the same port.
While running the .py program, the serial monitor of Arduino should be closed.
# This repo contains:
- the detect_Gestures.ino file is the code of detecting gestures from microcontroller
- detect_gestures_IMU.ino file with the code of cotrolling the drone using gesture and IMU libraries
- the gestures_Tello.py file is the python script of controlling the drone from the detected gestures
- the gestures_Tello_v1.1.py is an updated version with UP and DOWN gestures to move the drone up and down
and land after a certain time
- the gestures_Tello_IMU.py file with the code to control the drone using Arduino's inertial measurement unit
