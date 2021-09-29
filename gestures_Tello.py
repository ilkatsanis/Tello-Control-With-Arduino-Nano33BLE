# import the necessary packages
from djitellopy import Tello
import time
import serial

"""
The detected gestures need to be read
from microcontroller's serial output
to the laptop and then pass them to drone
"""
ser = serial.Serial('/dev/cu.usbmodem1101') # declare the serial port
ser_bytes = ser.readline() # read from port
"""
Prevent any random UP gestures causing the drone to take off.
The drone will take off only on the second gesture (UP).
The first gesture could be anything.
"""
ser.flushInput()

# initialize tello object
tello = Tello()

# connect to tello drone
tello.connect()
#print(tello.get_current_state())
print("Starting...")

# flag for flying set to false
flying = False

start = time.time()
while True:
    try:
        # read from board's (Arduino's) serial output
        ser_bytes = ser.readline()
        """
        The drone needs to understand what is coming out
        from Arduino's serial output.
        Characters need to be decoded
        """
        decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
        # drone take off
        if 'UP' in decoded_bytes and not flying:
            tello.takeoff()
            print("Drone is taking off")
            flying = True # set flag to true - Drone is in the air
        elif 'DOWN' in decoded_bytes and flying:
            tello.land()
            print("Drone is landing")
        elif 'LEFT' in decoded_bytes and flying:
            tello.move_left(40)
            print("Drone moved left")
        elif 'RIGHT' in decoded_bytes and flying:
            tello.move_right(40)
            print("Drone moved right")
        if time.time()-start>40:
            tello.land()
            print("Drone is landing")
            flying = False
    except:
        print("Keyboard Interrupt")
        tello.land()
        print("Drone is landing")
        break
