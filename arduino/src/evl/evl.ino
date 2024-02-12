int floor_status[3] = {0,0,0};
float evl_loc = 1;
int stop_count = 0;
int pop[3] = {0,0,0};
int red_LED = 2;
int yellow_LED[4] = {8, 9, 10, A0};
int pushed_buttons = 0;
int count_time = 0;




void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  for (int i = 2; i <= 10; i++) { // LED
    pinMode(i, OUTPUT);
  }
  pinMode(A0, OUTPUT);
  
}


bool button(int button_num) {
  static bool old_status[3] = {0,0,0};
  bool button = digitalRead(button_num);
  bool click;


  if (button == HIGH && old_status[button_num-11] == LOW) {
    click = 1;
  }
  else {
    click = 0;
  }


  old_status[button_num-11] = button;
  return click;
}


void call_evl_LED() {
  for (int i = 0; i <= 2; i++) {

    if (floor_status[i] >= 1) {
      digitalWrite(red_LED + i, HIGH);
    }
    else {
      digitalWrite(red_LED + i, LOW);
    }
  }
}







void end_cancel_button(int num) {
  for (int i = 0; i <= 2; i++) {
    if (num < floor_status[i]) {
      floor_status[i]--;
    }
    else if (num == floor_status[i]) {
      floor_status[i] = 0;
    }
  }
}


int min_floor_status() { // 가장 빠르게 누른층과 그사이층 반환
  int result = 3;
  int min_floor = 0;
  for (int i = 0; i <= 2; i++) {
    if (result > floor_status[i] && floor_status[i] != 0) {
      result = floor_status[i];

      min_floor = i + 1;
    }
  }

  return min_floor;
}


void move_evl() {
  static int target = 0;
  float sub_target = 0;

  if (target == 0) {
    target = min_floor_status();
  }
  else if (floor_status[0] + floor_status[1] + floor_status[2] == 0) {
    target = 0;
  }

  for (int i = 1; i <= 3; i++) { //GREEN_LED
    if (i - 0.01 < evl_loc && evl_loc < i + 0.01) {
      
      digitalWrite(i + 4, HIGH);
      if (target - 0.01 < evl_loc && evl_loc < target + 0.01) {
        pushed_buttons--;
        end_cancel_button(floor_status[target - 1]);
        target = 0;
        count_time = 0;
      }
    }
    else {
      digitalWrite(i + 4, LOW);
    }
  }
  

  for (int i = 0; i <= 3; i++) {
    if (1.01 + (0.5 * i) < evl_loc && evl_loc < 1.49 + (0.5 * i)) { // YELLOW_LED
      digitalWrite(yellow_LED[i], HIGH);
    }
    else {
      digitalWrite(yellow_LED[i], LOW);
    }
  }

  


  
  if (target != 0 && count_time >= 500) {
    if (evl_loc - target > 0.01) { /// 엘리베이터 운행 방향
      evl_loc = evl_loc - 0.1;
      stop_count = 0;
    }
    else if (evl_loc - target < -0.01) {
      evl_loc = evl_loc + 0.1;
      stop_count = 0;
    }

  }
  else {
    stop_count++;
  }


}

void move_pop() {
  float max_loc = -1.0;
  int max_index = 0;
  int max_num = 0;

  for (int i = 0; i <= 2; i++) {
    if (pop[i] > max_num) {
      max_num = pop[i];
      max_index = i;
      max_loc = static_cast<float>(i);
    }
  }


  
  if (evl_loc != max_loc + 1.0) {
    pushed_buttons++;
    floor_status[max_index] = pushed_buttons;
  }

  stop_count = 0;
}


void loop() {
  // put your main code here, to run repeatedly:
  for (int i = 11; i <= 13; i++) {// button
    if (button(i)) {
      if (floor_status[i-11] != 0) {
        pushed_buttons--;
        end_cancel_button(floor_status[i-11]);
        pop[i-11]--;
      }
      else {
        pushed_buttons++;
        floor_status[i-11] = pushed_buttons;
        pop[i-11]++;
      }
    }
  }
  call_evl_LED();


  if (count_time % 10 == 0) { //반복속도 1 / 10
    move_evl();
  }


  if (stop_count == 100 and count_time % 10 == 0) {
    move_pop();
  }


  //Serial.println(stop_count);

  // Serial.print(pushed_buttons);  
  // Serial.print("  ");
  // Serial.print(floor_status[0]);
  // Serial.print("  ");
  // Serial.print(floor_status[1]);
  // Serial.print("  ");
  // Serial.println(floor_status[2]);


  count_time++;

  


  delay(10);


}
