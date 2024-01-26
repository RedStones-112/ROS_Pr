const int ECHO = 8;
const int TRIG = 9;
const int LED_R = 3;
const int LED_G = 5;
const int LED_B = 6;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);


}
void loop() {
  ////put your main code here, to run repeatedly:
  long duration, distance;
  char input;
  digitalWrite(TRIG, LOW); // 파형발생
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);


  duration = pulseIn(ECHO, HIGH); 
  distance = duration * 17 / 1000;
  Serial.println(duration);
  Serial.print("\nDIstance : ");
  Serial.print(distance);
  Serial.println(" cm");

  if (Serial.available() > 0){
    input = Serial.read();
    Serial.println(input);
  }

  if (input == 'R'){
    analogWrite(LED_R, map(distance, 0, 300, 0, 255));
    analogWrite(LED_G, 0);
    analogWrite(LED_B, 0);
    Serial.println("test");
  }
  if (input == 'G'){
    analogWrite(LED_R, 0);
    analogWrite(LED_G, map(distance, 0, 300, 0, 255));
    analogWrite(LED_B, 0);
    
  }
  if (input == 'B'){
    analogWrite(LED_R, 0);
    analogWrite(LED_G, 0);
    analogWrite(LED_B, map(distance, 0, 300, 0, 255));
    
  }

  delay(100);
}