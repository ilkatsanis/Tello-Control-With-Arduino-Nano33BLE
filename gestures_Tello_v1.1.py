# CLOSE ARDUINO'S SERIAL MONITOR TO CONTROL THE DRONE
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
# print drone's battery state
print("Battery is: " + tello.get_battery())

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
            
        # while the drone is in the air, it will go up 40 cm
        elif 'UP' in decoded_bytes and flying:
            tello.move_up(40)
            print("Drone is going up")
        # while the drone is in the air, it will go down 40 cm
        elif 'DOWN' in decoded_bytes and flying:
            tello.move_down(40)
            print("Drone is going down")
        elif 'LEFT' in decoded_bytes and flying:
            tello.move_left(40)
            print("Drone moved left")
        elif 'RIGHT' in decoded_bytes and flying:
            tello.move_right(40)
            print("Drone moved right")
        # the drone will land automatically after 30 seconds from the first gesture
        if time.time()-start>40:
            tello.land()
            print("Drone is landing")
    # the drone will land if you shut down the .py script
    except:
        print("Keyboard Interrupt")
        tello.land()
        print("Drone is landing")
        break
