const int ECHO = 8;
const int TRIG = 9;

const int LED_1 = 3;
const int LED_2 = 5;
const int LED_3 = 6;
const int LED_4 = 7;
const int LED_5 = 8;
const int LED_6 = 9;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

  pinMode(LED_1, OUTPUT);
  pinMode(LED_2, OUTPUT);
  pinMode(LED_3, OUTPUT);
  pinMode(LED_4, OUTPUT);
  pinMode(LED_5, OUTPUT);
  pinMode(LED_6, OUTPUT);

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

  if (distance < 100){
    digitalWrite(LED_1, HIGH);
  }
  if (100 < distance) {
    digitalWrite(LED_2, HIGH);
  }
  else {
    digitalWrite(LED_2, LOW);
  }
  if (200 < distance) {
    digitalWrite(LED_3, HIGH);
  }
  else {
    digitalWrite(LED_3, LOW);
  }
  if (300 < distance) {
    digitalWrite(LED_4, HIGH);
  }
  else {
    digitalWrite(LED_5, LOW);
  }
  if (400 < distance) {
    digitalWrite(LED_5, HIGH);
  }
  else {
    digitalWrite(LED_5, LOW);
  }
  if (500 < distance) {
    digitalWrite(LED_6, HIGH);
  }
  else {
    digitalWrite(LED_6, LOW);
  }

  delay(100);
}