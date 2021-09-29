// include this library to detect the gestures
#include <Arduino_APDS9960.h>

void setup() {
  Serial.begin(9600);
  // change led color for each gesture
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(LEDR, OUTPUT); // red led
  pinMode(LEDG, OUTPUT); // led green
  pinMode(LEDB, OUTPUT); // led blue

  // if the sensor is not being detected, print error message
  while(!Serial); // wait for an active serial connection
  if (APDS.begin()) {
    Serial.println("Initialize sensor");
  }
   else {
    Serial.println("Fail to initialize sensor");
   }

  Serial.println("Detecting Gestures");
  digitalWrite(LEDR, HIGH);
  digitalWrite(LEDG, HIGH);
  digitalWrite(LEDB, HIGH);

}

void loop() {
  // start the sensor to detect gestures
  if (APDS.gestureAvailable()) {
    int gesture = APDS.readGesture();
    
     /* 
       *  cases for each gesture
       *  1 sec delay allowing the drone to react properly
       *  up gesture --> red led on
       *  down gesture --> green led on
       *  left gesture --> blue led on
       *  right gesture --> builtin led on
       */
       
    switch (gesture) {
      case GESTURE_UP:
      Serial.println("UP gesture detected");
      digitalWrite(LEDR, LOW);
      delay(1000); 
      digitalWrite(LEDR, HIGH);
      break;

      case GESTURE_DOWN:
      Serial.println("DOWN gesture detected");
      digitalWrite(LEDG, LOW);
      delay(1000);
      digitalWrite(LEDG, HIGH);
      break;

      case GESTURE_LEFT:
      Serial.println("LEFT gesture detected");
      digitalWrite(LEDB, LOW);
      delay(1000);
      digitalWrite(LEDB, HIGH);
      break;

      case GESTURE_RIGHT:
      Serial.println("RIGHT gesture detected");
      digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
      digitalWrite(LED_BUILTIN, LOW);
      break;

      default:
      break;
    }
  }
}
