
/*
 * Sketch to control stepper motors via serial interface
 *
 * Commands implemented with examples:
 * - V:500 : Set motor speed to 500 steps/second
 * - M:-1000:50 : Move motor 1 to position -1000 and motor 2 to 50
 * - S : Stop (release) motors
 * - Q : Query software ID
 * - P : Query position of motors
 * - R : Query whether motors are running
 */

#include <stdio.h>
/* Adafruit Motor Shield v. 2.3 */
#include <AccelStepper.h>
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"
#include <MultiStepper.h>

Adafruit_MotorShield AFMS(0x60);
Adafruit_StepperMotor *motor1 = AFMS.getStepper(200, 1);
Adafruit_StepperMotor *motor2 = AFMS.getStepper(200, 2);

/* String I/O */
const int bufsize = 32;
char cmd[bufsize];    // command string
int len = 0;

/* flags */
boolean command_ready = false; // command string received
boolean is_running = false;    // true if steppers are running

/* motor positions (steps) */
long n1 = 0;
long n2 = 0;

/* Motor configuration */
void forwardstep1() {
  motor1->onestep(FORWARD, DOUBLE);
}

void backwardstep1() {
  motor1->onestep(BACKWARD, DOUBLE);
}

void forwardstep2() {
  motor2->onestep(FORWARD, DOUBLE);
}

void backwardstep2() {
  motor2->onestep(BACKWARD, DOUBLE);
}

AccelStepper stepper1(forwardstep1, backwardstep1);
AccelStepper stepper2(forwardstep2, backwardstep2);
MultiStepper steppers;

void set_speed() {
  float v;
  
  if (len < 2) {
    return;
  }
  sscanf(cmd, "V:%f", &v);
  stepper1.setMaxSpeed(v);
  stepper2.setMaxSpeed(v);
}

void move_to() {
  long target[2];
  
  if (len < 2) {
    return;
  }
  sscanf(cmd, "M:%ld:%ld", &n1, &n2);
  target[0] = n1;
  target[1] = n2;
  steppers.moveTo(target);
}

void release_motors() {
  motor1->release();
  motor2->release();
}

void query_identity() {
  Serial.println("acam2");
}

void query_position() {
  n1 = stepper1.currentPosition();
  n2 = stepper2.currentPosition();
  Serial.print('P');
  Serial.print(':');
  Serial.print(n1);
  Serial.print(':');
  Serial.println(n2);
}

void query_isrunning() {
  Serial.print('R');
  Serial.print(':');
  Serial.println(is_running);
}

/* Dispatch commands */
void parse_command() {
  switch (cmd[0]) {
    case 'P':
      query_position();
      break;
    case 'R':
      query_isrunning();
      break;
    case 'M':
      move_to();
      break;
    case 'V':
      set_speed();
    case 'S':
      release_motors();
      break;
    case 'Q':
      query_identity();
      break;
    default:
      break;
  }
  command_ready = false;
}

void debug_command() {
  Serial.print("debug: ");
  Serial.println(cmd);
}

void setup() {
    Serial.begin(9600, SERIAL_8N1); // Serial Port at 9600 baud
    while (!Serial) {
      ;                     // Wait for serial port to connect
    }
    Serial.setTimeout(100);
    
    AFMS.begin();           // AccelStepper setup
    TWBR = ((F_CPU / 800000l) - 16) / 2; // i2C clock 800kHz
    stepper1.setMaxSpeed(500.0);
    stepper2.setMaxSpeed(500.0);
    stepper1.setCurrentPosition(0);	
    stepper2.setCurrentPosition(0);
    steppers.addStepper(stepper1);
    steppers.addStepper(stepper2);
}

void loop() {
    if (command_ready) {
      parse_command();
    }
    is_running = steppers.run();
}

void serialEvent() {
  char c;

  while (Serial.available() > 0 && command_ready == false) {
    c = Serial.read();
    if (c == '\n') {
      cmd[len] = '\0';
      len = 0;
      command_ready = true;
    } else {
      cmd[len++] = c;
      if (len >= bufsize) {
        len = bufsize - 1;
      }
    }
  }
}
