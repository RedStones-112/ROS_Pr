const int button_num = 13;

int numbers[10][7] {
  {1,1,1,1,1,1,0}, // digit 0
  {0,1,1,0,0,0,0}, // digit 1
  {1,1,0,1,1,0,1}, // digit 2
  {1,1,1,1,0,0,1}, // digit 3
  {0,1,1,0,0,1,1}, // digit 4
  {1,0,1,1,0,1,1}, // digit 5
  {1,0,1,1,1,1,1}, // digit 6
  {1,1,1,0,0,0,0}, // digit 7
  {1,1,1,1,1,1,1}, // digit 8
  {1,1,1,1,0,1,1} // digit 9
};
int count = 0;
void display(int num) {
  for (int i = 0; i < 7; i++) {
    digitalWrite(i+2, numbers[num][i]);
  }
}

bool button() {
  static bool old_status = 0;
  bool button = digitalRead(button_num);
  bool click;

  if (button == HIGH && old_status == LOW) {
    click = 1;
  }
  else {
    click = 0;
  }
  old_status = button;
  return click;
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  for (int i = 2; i < 9; i++){
    pinMode(i,OUTPUT);
  }
  pinMode(13,INPUT);
}

void loop() {
  static bool status = 0;
  // put your main code here, to run repeatedly:
  bool click = 0;


  click = button();
  Serial.println(click);

  if (status == 0 && click == HIGH) {
    count++;
  }
  else if (status == 1 && click == HIGH) {
    count--;
  }


  if (count == 9) {
    status = 1;
  }
  else if (count == 0) {
    status = 0;
  }

  
  display(count);

}
