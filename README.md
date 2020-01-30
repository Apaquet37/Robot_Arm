# Robot Arm Planning

#### Goal
- Construct a Metro-controlled robot arm from materials in the sigma lab.

#### Resources/Materials
- 4-6 servos
- Metro Express
- 9V battery pack
- Gears made out of 3mm acrylic
- 5 mm LEDs
- Switch (for power)
- Potentiometers (for controlling servos) 
- Photo interrupters
- 3D printer and laser cutter

#### Ideas
- Each servo corresponds to the moving parts of the arm (left/right, up/down, open/close)
 - Potentiometers on the base of the arm will control each direction
- Labels will be printed to indicate what servo it corresponds to
- The base of the arm is just a box, containing the arduino and battery pack
- One side of the box will be able to open with a hinge/knob, in order to allow easy access if the wiring or batteries    had to be changed
- It will use continuous rotation servos, but will the range will be limited by a photo interrupter so the moving parts don’t hit other parts of the arm
- Approximate size of box: length = 150 mm, width = 100 mm, height = 80 mm

#### Overview
- *Solidworks*
  1. Base of the arm
     - Box connected by corner tabs
     - Properly dimensioned holes for screws, arduino, led, switch
      - Hinge for one side of the box
  2. "Claw” that picks up the object
     - Each side has gears on one end, when they are connected it makes the claws open and close together when only one         of them is being controlled by the servo
      - The other side has “teeth”
     - The ridges make it less slippery and less likely to drop the object
  3. Servo holders 
      - Material surrounding the base of the servo and connects to the acrylic
      
- *Wiring/Code*
  1. Power switch to led and battery
      - Switch should turn on the entire thing, and the led should indicate when it is on
  2. Potentiometers
  3. Servos
  
#### Schedule
1/31 - finished plan & sitting together.

2/7 - rough dimensions figured out on solidworks, 4 servos with potentiometers coded on circuitpython.

2/14 - servos and dials wired, processing gui started
