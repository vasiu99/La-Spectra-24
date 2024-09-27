#include <Servo.h>

Servo baseM1;        // 0 - 180
Servo horM2;         //20 - 120
Servo verM3;         //60 - 150
Servo pickM4;        //60 - 150

int baseM1_val;
int horM2_val;
int verM3_val;
int pickM4_val;

int CLOSE_ANGLE = 40;

void setup() {
Serial.begin(9600);

  baseM1.attach(13);
  horM2.attach(12);
  verM3.attach(11);
  pickM4.attach(9);

}

void Move_Shoot_Position(){

  baseM1.write(90);
  horM2.write(110);
  verM3.write(140);
  pickM4.write(100);

}

void Pickup_Object(){

  baseM1.write(90);
  horM2.write(80);
  delay(1000);
  verM3.write(60);
  delay(1000);
  horM2.write(120);
  delay(1000);
  pickM4.write(CLOSE_ANGLE);
  delay(1000);

  verM3.write(120);

}

void Place_Red(){

  horM2.write(120);
  delay(100);
  baseM1.write(180);
  delay(1000);
  verM3.write(80);
  delay(1000);
  pickM4.write(100);
  delay(1000);
  verM3.write(120);
  delay(200);
  baseM1.write(90);

}

void Place_Blue(){

  horM2.write(120);
  delay(100);
  baseM1.write(0);
  delay(1000);
  verM3.write(80);
  delay(1000);
  pickM4.write(100);
  delay(1000);
  verM3.write(120);
  delay(200);
  baseM1.write(90);


}

void Place_Green(){

  horM2.write(120);
  delay(100);
  baseM1.write(90);
  delay(500);
  horM2.write(70);
  delay(200);
  verM3.write(60);
  delay(1000);
  pickM4.write(100);
  delay(1000);

  horM2.write(120);
  
}

void Move_To_Rest(){

  baseM1.write(90);
  horM2.write(100);
  verM3.write(70);
  pickM4.write(100);
}

void Test_pickup()
{
    pickM4.write(CLOSE_ANGLE);
  delay(2000);
  pickM4.write(100);
   delay(2000);
  pickM4.write(CLOSE_ANGLE);
   delay(2000);
  pickM4.write(100);
   delay(2000);
  pickM4.write(CLOSE_ANGLE);
   delay(2000);
  pickM4.write(100);
   delay(2000);
  pickM4.write(CLOSE_ANGLE);
   delay(2000);
  pickM4.write(100);
   delay(2000);
  pickM4.write(CLOSE_ANGLE);
   delay(2000);
  pickM4.write(100);
}

void loop() {

  if (Serial.available() > 0){
    String msg = Serial.readString();

     if (msg == "rest"){
      Move_To_Rest();
    }

    if (msg == "shoot"){
      Move_Shoot_Position();
    }

     if (msg == "test"){
      Test_pickup();
    }

      if (msg == "pick"){
      Pickup_Object();
    }

    if (msg == "Red"){
      Place_Red();
    }

    else if (msg == "Blue"){
      Place_Blue();
    }

    else if (msg == "Green"){
      Place_Green();
    }
    else{}
    }
  else{}

}
