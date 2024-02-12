
const int PIR = 2;
const int LED = 13;
int count = 0;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(PIR, INPUT);
  pinMode(LED, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(count);
  Serial.print("  ");
  Serial.println(digitalRead(PIR));
  delay(100);
  int PIR_val = digitalRead(PIR)


  count++;
  if (PIR_val == HIGH) {
    digitalWrite(LED, 255);
    count = 0;
  }


  if (count >= 50) {
    digitalWrite(LED, 0);
  }




  if (count >= 10000) { 
    count = 0;
  }
}
