import board #pylint: disable-msg=import-error
import time
import busio #pylint: disable-msg=import-error
import pulseio #pylint: disable-msg=import-error
from analogio import AnalogIn #pylint: disable-msg=import-error
from adafruit_motor import servo #pylint: disable-msg=import-error
from digitalio import DigitalInOut, Direction, Pull #pylint: disable-msg=import-error

uart = busio.UART(board.TX, board.RX, baudrate = 9600)

pwm1 = pulseio.PWMOut(board.D3, duty_cycle=2**15, frequency = 50)
pwm2 = pulseio.PWMOut(board.D4, duty_cycle=2**15, frequency = 50)
pwm3 = pulseio.PWMOut(board.D5, duty_cycle=2**15, frequency = 50) 
pwm4 = pulseio.PWMOut(board.D6, duty_cycle=2**15, frequency = 50)
servo1 = servo.Servo(pwm1) 
servo2 = servo.Servo(pwm2)
servo3 = servo.Servo(pwm3) 
servo4 = servo.Servo(pwm4)
servoState = 0

dial1 = AnalogIn(board.A1)
dial2 = AnalogIn(board.A2)
dial3 = AnalogIn(board.A3)
dial4 = AnalogIn(board.A4)

switch = DigitalInOut(board.D12)
switch.direction = Direction.INPUT
switch.pull = Pull.UP
controlToggle = 0

print("go")
#myStr = "445678|180"
#print(myStr.index("|"))

def get_voltage(pin):
    return(pin.value*180)/65536

while True:
    print(switch.value)
    if switch.value:
        controlToggle = 0
    else:
        controlToggle = 1
    if controlToggle == 0:
        time.sleep(.1)
        myDial1 = get_voltage(dial1)
        myDial2 = get_voltage(dial2)
        myDial3 = get_voltage(dial3)
        myDial4 = get_voltage(dial4)
        servo1.angle = myDial1
        servo2.angle = myDial2
        servo3.angle = myDial3
        servo4.angle = myDial4
        print(myDial1)
    
    elif controlToggle == 1:
        print("switch")
        x = uart.read(5)
        if x is not None:
            try:
                myData = x.decode("utf-9")
                print("yes")
                print(myData)
                if myData.index("$")==1:
                    print("hi")    
                    servoState = myData[0]
                    print(servoState)
                    if servoState == "1":
                        angle1 = myData[2:]
                        servo1.angle = angle1
                        print(angle1)
                    if servoState == "2":
                        angle2 = myData[2:]
                        servo2.angle = angle2
                    if servoState == "3":
                        angle3 = myData[2]
                        servo3.angle = angle3
                    if servoState == "4":
                        angle4 = myData[2:]
                        servo4.angle = angle4
            except:
                print("unicode error")

                