import processing.serial.*;
Serial myPort;
int x1 = 75;
int x2 = 225;
int y1 = 75;
int y2 = 225;
int w = 100;
int r = w/2;
int angle1 = 0;
int angle2 = 0;
int angle3 = 0;
int angle4 = 0;
int servoAngle = 0;

int servoState = 0;
//boolean oldButtonState = false;
String message = "";

void setup() {
  size(300, 350);
  println("Available serial ports:");
  println(Serial.list());
  myPort = new Serial(this, Serial.list()[1], 9600);
  background(120);
  fill(255, 255, 255);
  ellipse(x1, y1, w, w); 
  ellipse(x2, y1, w, w);
  ellipse(x1, y2, w, w);
  ellipse(x2, y2, w, w);
  textSize(15);
  fill(0, 100, 175, 270);
  text("Servo 1", 50, 80);
  text("Servo 2", 200, 80);
  text("Servo 3", 50, 230);
  text("Servo 4", 200, 230);
  text("Select a servo and then use up and down", 0, 325);
  text("arrows to control angle.", 60, 340);
}

void draw() {
  if(mousePressed /*&& oldButtonState == false*/){
    if(mouseX > x1-r && mouseX < x1+r && mouseY > y1-r && mouseY < y1+r){
      println("Servo 1");
      servoState = 1;
      //oldButtonState = true;
      delay(100);
    }
    if(mouseX > x2-r && mouseX < x2+r && mouseY > y1-r && mouseY < y1+r){
      println("Servo 2");
      servoState = 2;
      //oldButtonState = true;
      delay(100);
    }
    if(mouseX > x1-r && mouseX < x1+r && mouseY > y2-r && mouseY < y2+r){
      println("Servo 3");
      servoState = 3;
      //oldButtonState = true;
      delay(100);
    }
    if(mouseX > x2-r && mouseX < x2+r && mouseY > y2-r && mouseY < y2+r){
      println("Servo 4");
      servoState = 4;
      //oldButtonState = true;
      delay(100);
    }
  }
  //oldButtonState = false;
  //keyPressed();
  println("go");
  println(servoState);
}

void keyPressed(){
  if((key == CODED) && (servoAngle <= 180) && (servoAngle >= 0)){
    if(keyCode == UP){
      if(servoState == 1 && angle1 < 180){
        angle1 = angle1+1;
        println(angle1);
        println("go1");
        servoAngle = angle1;
      }
      else if(servoState == 2 && angle2 < 180){
        angle2 = angle2+1;
        println(angle2);
        servoAngle = angle2;
      }
      else if(servoState == 3 && angle3 < 180){
        angle3 = angle3+1;
        println(angle3);
        servoAngle = angle3;
      }
      else if(servoState == 4 && angle4 < 180){
        angle4 = angle4+1;
        println(angle4);
        servoAngle = angle4;
      }
    }
    if(keyCode == DOWN){
      if(servoState == 1 && angle1 > 0){
        angle1 = angle1-1;
        println(angle1);
        println("go1");
        servoAngle = angle1;
      }
      else if(servoState == 2 && angle2 > 0){
        angle2 = angle2-1;
        println(angle2);
        servoAngle = angle2;
      }
      else if(servoState == 3 && angle3 > 0){
        angle3 = angle3-1;
        println(angle3);
        servoAngle = angle3;
      }
      else if(servoState == 4 && angle4 > 0){
        angle4 = angle4-1;
        println(angle4);
        servoAngle = angle4;
      }
    }
    // write "4|180"
    message = servoState+"$"+nf (servoAngle, 3);
    println(message);
    myPort.write(message);
  }
}
