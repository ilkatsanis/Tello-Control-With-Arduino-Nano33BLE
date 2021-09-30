// library to take inertial measurements
#include <Arduino_LSM9DS1.h>
// library to detect gestures
#include <Arduino_APDS9960.h>

float x, y, z;

int plusThreshold = 90;
int minusThreshold = -90;

void setup() {
  Serial.begin(9600);
  // change led color for each gesture
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(LEDR, OUTPUT);
  pinMode(LEDG, OUTPUT);
  pinMode(LEDB, OUTPUT);

  while(!Serial); // wait for an active serial connection
  // check gesture sensor
  if (!APDS.begin()) {
    Serial.println("Error initializing sensor");
  }
  else {
    Serial.println("Initialize Sensor");
  }

  Serial.println("Detecting Gestures");
  digitalWrite(LEDR, HIGH);
  digitalWrite(LEDG, HIGH);
  digitalWrite(LEDB, HIGH);

  // check IMU
  if (!IMU.begin()) {
    Serial.println("Error initializing IMU");
  }

  Serial.print("Gyroscope sample rate = ");
  Serial.print(IMU.gyroscopeSampleRate());
  Serial.println(" Hz");
  Serial.println();
  Serial.println("Gyroscope in degrees/second");

}

void loop() {
  if (IMU.gyroscopeAvailable()) {
    IMU.readGyroscope(x, y, z);
  }

  /*This setup is when we hold the board 
   * with the cable on the left of the wrist
   */
  if (x > plusThreshold) {
    Serial.println("Moving back");
    delay(1800);
  }

  if (x < minusThreshold) {
    Serial.println("Moving front");
    delay(1800);
  }

  if (y > plusThreshold) {
    Serial.println("Move left");
    delay(1800);
  }

  if (y < minusThreshold) {
    Serial.println("Move right");
    delay(1800);
  }

  /*
   * This setup is when we hold the board
   * with the cable in front of us
   * 
   * if (y > plusThreshold) {
    Serial.println("Moving back");
    delay(1500);
  }

  if (y < minusThreshold) {
    Serial.println("Moving forward");
    delay(1500);
  }

  if (x < minusThreshold) {
    Serial.println("Move left");
    delay(1500);
  }

  if (x > plusThreshold) {
    Serial.println("Move right");
    delay(1500);
  }
   */

  // detect, read and print gesture to serial monitor
  if (APDS.gestureAvailable()) {
    int gesture = APDS.readGesture();

    /* 
       *  cases for two gestures
       *  1 sec delay allowing the drone to react properly
       *  up gesture --> red led on
       *  down gesture --> green led on
       */
       
    switch (gesture) {
      // to make UP GESTURE, pass the hand up and right of the board
      case GESTURE_UP:
      Serial.println("UP GESTURE detected");
      digitalWrite(LEDR, LOW);
      delay(1000);
      digitalWrite(LEDR, HIGH);
      break;

      // to make DOWN GESTURE, pass the hand up and left of the board
      case GESTURE_DOWN:
      Serial.println("DOWN GESTURE detected");
      digitalWrite(LEDG, LOW);
      delay(1000);
      digitalWrite(LEDG, HIGH);
      break;

      default:
      break;
    }
  }
}
