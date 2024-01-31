#include <Servo.h>

Servo servo;
int deg = 28;
int count1 = 0;
int flag = 0;
float light1 = 0;
bool status = 0;
float old_data = 0;
int old_data2 = 0;
int time = 500;
int TH1 = 640;
int TH2 = 120;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo.attach(9);
  servo.write(0);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  count1++;
  light1 = analogRead(A0);
  //Serial.println(light1);
  
  if (time <= 50) {
    time = 50;
  }  
  if (abs(light1 - old_data) > 80 && 120 < light1 < 630) {  
    delay(time); 
    servo.write(deg);
    count1 = 0; 
    time -= 8;
    
  }


  if (count1 == 2000) {
    servo.write(0);
  }

  old_data = light1;
  
}




// #include <Servo.h>

// Servo servo;
// int deg = 28;
// int count1 = 0;
// int count2 = 0;
// int light1 = 0;
// bool status = 0;
// int old_data = 0;
// int old_data2 = 0;
// int time = 500;
// int TH1 = 630;
// int TH2 = 90;

// void setup() {
//   // put your setup code here, to run once:
//   Serial.begin(9600);
//   servo.attach(9);
//   servo.write(0);
  
// }

// void loop() {
//   // put your main code here, to run repeatedly:
//   count1++;
//   light1 = analogRead(A0);
//   //Serial.println(light1);
  
//   if (time <= 0) {
//     time = 0;
//   }
//   if (light1 <= TH1 && old_data > TH1 && status == 0) {
//     delay(time);
//     servo.write(deg);
//     count1 = 0;
//     time -= 12;
//   }

//   else if (light1 >= TH2 && old_data < TH2 && status == 1) {
//     delay(time);
//     servo.write(deg);
//     count1 = 0;
//     time -= 12;
//   }



//   if (light1 <= TH2 && status == 0) { //낮 밤 감지
//     count2 += 1;
//   }

//   else if (light1 > TH1 && status == 1) {
//     count2 -= 1;
//   }

//   else {
//     count2 = 0;
//   }



//   if (count2 >= 2000) {
//     status = 1;
//   }
//   else if (count2 <= -2000) {
//     status = 0;
//   }



//   if (count1 == 2500) {
//     servo.write(0);
//   }

  

//   old_data = light1;
  
// }