import processing.serial.*;
Serial myPort;

void setup() {
  size(300, 300);
  println("Available serial ports:");
  println(Serial.list());
  myPort = new Serial(this, Serial.list()[2], 9600);
}

void draw() {
  background(120);
  ellipse(75, 75, 55, 55);
  ellipse(225, 75, 55, 55);
  ellipse(75, 225, 55, 55);
  ellipse(225, 225, 55, 55);
}
