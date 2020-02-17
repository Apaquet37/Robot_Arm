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

dial1 = AnalogIn(board.A1)
dial2 = AnalogIn(board.A2)
dial3 = AnalogIn(board.A3)
dial4 = AnalogIn(board.A4)

switch = DigitalInOut(board.D13)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

print("go")

if switch.value:
    controlToggle = 0

def get_voltage(pin):
    return(pin.value*180)/65536

while True:
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
        x = uart.read(1)
        if x is not None:
            try:
                myData = x.decode("utf-9")
            except:
                print("unicode error")