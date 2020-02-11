import processing.serial.*;
Serial myPort;
int x1 = 75;
int x2 = 225;
int y1 = 75;
int y2 = 225;
int w = 55;
int servoState = 0;
//boolean oldButtonState = false;

void setup() {
  size(300, 300);
  println("Available serial ports:");
  println(Serial.list());
  myPort = new Serial(this, Serial.list()[2], 9600);
  background(120);
  fill(255, 255, 255);
  ellipse(x1, y1, 55, 55);
  ellipse(x2, y1, 55, 55);
  ellipse(x1, y2, 55, 55);
  ellipse(x2, y2, 55, 55);
  textSize(15);
  fill(0, 100, 175, 270);
  text("Servo 1", 50, 80);
  text("Servo 2", 200, 80);
  text("Servo 3", 50, 230);
  text("Servo 4", 200, 230);
}

void draw() {
  if(mousePressed /*&& oldButtonState == false*/){
    if(mouseX > x1 && mouseX < x1+w && mouseY > y1 && mouseY < y1+w){
      println("Servo 1");
      servoState = 1;
      //oldButtonState = true;
      delay(100);
    }
    if(mouseX > x2 && mouseX < x2+w && mouseY > y1 && mouseY < y1+w){
      println("Servo 2");
      servoState = 2;
      //oldButtonState = true;
      delay(100);
    }
    if(mouseX > x1 && mouseX < x1+w && mouseY > y2 && mouseY < y2+w){
      println("Servo 3");
      servoState = 3;
      //oldButtonState = true;
      delay(100);
    }
    if(mouseX > x2 && mouseX < x2+w && mouseY > y2 && mouseY < y2+w){
      println("Servo 4");
      servoState = 4;
      //oldButtonState = true;
      delay(100);
    }
  }
  //oldButtonState = false;
}

void keyPressed(){
  if(key == CODED){
    if(keyCode == UP){
      if(servoState == 1){
        
      }
      else if(servoState == 2){
        
      }
      else if(servoState == 3){
        
      }
      else if(servoState == 4){
        
      }
    }
  }
}
