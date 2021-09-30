from djitellopy import Tello
import time
import serial
#import sys

ser = serial.Serial('/dev/cu.usbmodem1401')
ser_bytes = ser.readline()

# activate the drone with any gesture
ser.flushInput()

tello = Tello()

# connect to drone
tello.connect()

print("Starting drone")

# receive drone's battery state
print("Battery is: " + tello.get_battery())

# flag for flying
flying = False

start = time.time()

while True:
    try:
        # read from board's (Arduino's) serial output
        ser_bytes = ser.readline()
        # characters need to be decoded.
        decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
        
        if 'UP' in decoded_bytes and not flying:
            tello.takeoff()
            print("Drone takes-off")
            flying = True
            print()
            
        elif 'UP' in decoded_bytes and flying:
            tello.move_up(40)
            print("Drone is going up")
            print()
            
        elif 'DOWN' in decoded_bytes and flying:
            tello.move_down(40)
            print("Drone is going down")
            print()
            
        elif 'front' in decoded_bytes and flying:
            tello.move_forward(30)
            print("Drone moves front")
            print()
            
        elif 'back' in decoded_bytes and flying:
            tello.move_back(30)
            print("Drone moves back")
            print()
            
        elif 'right' in decoded_bytes and flying:
            tello.move_right(30)
            print("Drone moves right")
            print()
            
        elif 'left' in decoded_bytes and flying:
            tello.move_left(30)
            print("Drone moves left")
            print()
            
        # the drone will land after 40 secs from the first command
        if time.time() - start >= 45:
            print("DRONE WILL LAND IN...")
            print()
            for i in range(3, 0, -1):
                print(i)
                time.sleep(1)
            tello.land()
            flying = False
    except:
        print("Keyboard Interrupt")
        tello.land()
        break
