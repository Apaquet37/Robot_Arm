import processing.serial.*;
Serial myPort;

void setup() {
  size(300, 400);
  println("Available serial ports:");
  println(Serial.list());
  myPort = new Serial(this, Serial.list()[2], 9600);
}

void draw() {
  background(120, 0, 250);
}
