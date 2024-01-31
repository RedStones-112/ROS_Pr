const int LED_R = 3;
const int LED_G = 5;
const int LED_B = 6;
char status;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  while (Serial.available() > 0) {
    
    char input = Serial.read();
    if (input != '\n') {
      Serial.println("-----------");
      Serial.println(input);
      status = input;
    }
  }
  


  for (int i = 0; i < 255; i++) {
    if (status == 'R') {
      analogWrite(LED_R, i);
      analogWrite(LED_G, 0);
      analogWrite(LED_B, 0);
    }
    else if (status == 'G') {
      analogWrite(LED_G, i);
      analogWrite(LED_R, 0);
      analogWrite(LED_B, 0);
    }
    else if (status == 'B') {
      analogWrite(LED_B, i);
      analogWrite(LED_R, 0);
      analogWrite(LED_G, 0);
    }
    
    delay(10);
  }
}
