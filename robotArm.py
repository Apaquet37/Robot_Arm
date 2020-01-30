import board #pylint: disable-msg=import-error
import time
import busio #pylint: disable-msg=import-error
import pulseio #pylint: disable-msg=import-error
from analogio import AnalogIn #pylint: disable-msg=import-error
from adafruit_motor import servo #pylint: disable-msg=import-error
from digitalio import DigitalInOut, Direction, Pull #pylint: disable-msg=import-error


pwm1 = pulseio.PWMOut(board.A2, duty_cycle=2**15, frequency = 50)
pwm2 = pulseio.PWMOut(board.A3, duty_cycle=2**15, frequency = 50)
pwm3 = pulseio.PWMOut(board.A4, duty_cycle=2**15, frequency = 50) 
pwm4 = pulseio.PWMOut(board.D3, duty_cycle=2**15, frequency = 50)
servo1 = servo.Servo(pwm1) 
servo2 = servo.Servo(pwm2)
servo3 = servo.Servo(pwm3) 
servo4 = servo.Servo(pwm4)

dial1 = AnalogIn(board.D5)
dial2 = AnalogIn(board.D6)
dial3 = AnalogIn(board.D7)
dial4 = AnalogIn(board.D8)

switch = DigitalInOut(board.D13)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

if switch.value:
    controlToggle = 0

def get_voltage(pin):
    return(pin.value*180)/65536

while True:
    time.sleep(.1)
    myDial1 = get_voltage(dial1)
    myDial2 = get_voltage(dial2)
    myDial3 = get_voltage(dial3)
    myDial4 = get_voltage(dial4)
    servo1.angle = myDial1
    servo2.angle = myDial2
    servo3.angle = myDial3
    servo4.angle = myDial4