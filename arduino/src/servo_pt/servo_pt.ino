#include <Servo.h>
Servo servo;
const int button = 2;
int angle = 0;
int count = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo.attach(9);
  servo.write(0);
  pinMode(button, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  count++;
  if (digitalRead(button) == HIGH && count % 1000 == 0) {
    angle++;
    if (angle >= 180) {
      angle = 0;
      servo.write(angle);

    }
    if (count > 10000) {
      count = 1;
    }
    
    servo.write(angle);
    Serial.println(angle);
    
    
  }





  // while (Serial.available() > 0) {
  //   Serial.println("----");
  //   String input_str = Serial.readStringUntil('\n');
  //   float tmp = input_str.toFloat();
    
  //   Serial.println(tmp);
  //   servo.write(tmp);
    
  // }
}
