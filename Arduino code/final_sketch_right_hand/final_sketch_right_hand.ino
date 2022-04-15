#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
#include <SoftwareSerial.h> 
SoftwareSerial MyBlue(3, 2); // RX | TX 
// response from our application
char response;

Adafruit_MPU6050 mpu;

const int sensorPin= A0;
const int sensorPin1= A1;
const int sensorPin2= A2;
const int sensorPin3= A3;
const int sensorPin4= A6;
float ADCflex;
float Vflex;
float Rflex;
float angle;
float averageangle;
float totalaverageangle;
float totalaverageFsrForce;
float count;
float reading;
float totalreading;
float fsrReading;
float fsrVoltage;
float fsrResistance;
float fsrConductance;
float fsrForce;
float totalFsrForce;
float averageFsrForce;
float data;
float totalfsrForce;
float totalangle;
const float VCC=5;
const float R_DIV= 8000;
const float flatResistance = 25000.0; // resistance when flat
const float bendResistance = 100000.0;  // resistance at 90 deg

void setup() {
  // initialize serial monitor
  Serial.begin(19200);
  // initialize sensor pins for flex and force
  pinMode(13,OUTPUT);
  pinMode(12,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(sensorPin, INPUT);
  pinMode(sensorPin1, INPUT);
  pinMode(sensorPin2, INPUT);
  pinMode(sensorPin3, INPUT);
  pinMode(sensorPin4, INPUT);

   // Try to initialize mpu
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
  Serial.println("MPU6050 Found!");

  // set accelerometer range to +-8G
  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);

  // set gyro range to +- 500 deg/s
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);

  // set filter bandwidth to 21 Hz
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

  delay(100);
  
  // initialize bluetooth module
  MyBlue.flush();
  MyBlue.begin(9600); 

}
 float exerciseForce(){
   //turn off power pins for flex sensors
  digitalWrite(13,LOW);
  digitalWrite(11,LOW);
  digitalWrite(9,LOW);
  digitalWrite(7,LOW);
  digitalWrite(5,LOW);
  
  // turn on power pins for force sensor
  digitalWrite(12,HIGH);
  digitalWrite(10,HIGH);
  digitalWrite(8,HIGH);
  digitalWrite(6,HIGH);
  digitalWrite(4,HIGH);
while(count<70){
//read sensor 1
  fsrReading= analogRead(sensorPin);
  fsrVoltage = map(fsrReading, 0, 1023, 0, 5000);
  fsrResistance = 5000 - fsrVoltage;     // fsrVoltage is in millivolts so 5V = 5000mV
  fsrResistance *= 8200;                // 8K resistor
  fsrResistance /= fsrVoltage;
  fsrConductance = 1000000;           // we measure in micromhos so 
  fsrConductance /= fsrResistance;
  if (fsrConductance <= 1000) {
      fsrForce = fsrConductance / 80;
    } else {
      fsrForce = fsrConductance - 1000;
      fsrForce /= 30; 
    }
    
    totalfsrForce+=fsrForce;

    // read sensor 2
  fsrReading= analogRead(sensorPin1);
  fsrVoltage = map(fsrReading, 0, 1023, 0, 5000);
  fsrResistance = 5000 - fsrVoltage;     // fsrVoltage is in millivolts so 5V = 5000mV
  fsrResistance *= 8200;                // 10K resistor
  fsrResistance /= fsrVoltage;
  fsrConductance = 1000000;           // we measure in micromhos so 
  fsrConductance /= fsrResistance;
  if (fsrConductance <= 1000) {
      fsrForce = fsrConductance / 80;
    } else {
      fsrForce = fsrConductance - 1000;
      fsrForce /= 30; 
    }
     totalfsrForce+=fsrForce;

     // read sensor 3
      fsrReading= analogRead(sensorPin2);

  fsrVoltage = map(fsrReading, 0, 1023, 0, 5000);
  fsrResistance = 5000 - fsrVoltage;     // fsrVoltage is in millivolts so 5V = 5000mV
  fsrResistance *= 8200;                // 10K resistor
  fsrResistance /= fsrVoltage;
  fsrConductance = 1000000;           // we measure in micromhos so 
  fsrConductance /= fsrResistance;
  if (fsrConductance <= 1000) {
      fsrForce = fsrConductance / 80;
    } else {
      fsrForce = fsrConductance - 1000;
      fsrForce /= 30; 
    }
    totalfsrForce+=fsrForce;

       // read sensor 4
      fsrReading= analogRead(sensorPin3);

  fsrVoltage = map(fsrReading, 0, 1023, 0, 5000);
  fsrResistance = 5000 - fsrVoltage;     // fsrVoltage is in millivolts so 5V = 5000mV
  fsrResistance *= 8200;                // 10K resistor
  fsrResistance /= fsrVoltage;
  fsrConductance = 1000000;           // we measure in micromhos so 
  fsrConductance /= fsrResistance;
  if (fsrConductance <= 1000) {
      fsrForce = fsrConductance / 80;
    } else {
      fsrForce = fsrConductance - 1000;
      fsrForce /= 30; 
    }
     totalfsrForce+=fsrForce;
     
     // read sensor 5
      fsrReading= analogRead(sensorPin3);

  fsrVoltage = map(fsrReading, 0, 1023, 0, 5000);
  fsrResistance = 5000 - fsrVoltage;     // fsrVoltage is in millivolts so 5V = 5000mV
  fsrResistance *= 8200;                // 10K resistor
  fsrResistance /= fsrVoltage;
  fsrConductance = 1000000;           // we measure in micromhos so 
  fsrConductance /= fsrResistance;
  if (fsrConductance <= 1000) {
      fsrForce = fsrConductance / 80;
    } else {
      fsrForce = fsrConductance - 1000;
      fsrForce /= 30; 
    }
    totalfsrForce+=fsrForce;
    averageFsrForce=totalFsrForce/5;
    totalaverageFsrForce=+averageFsrForce;
    count++;
    delay(500);
}
   totalaverageFsrForce=totalaverageFsrForce/count;
   return totalaverageFsrForce;
  
 }

 float exerciseFlex(){
   //turn off power pins for force sensors
  digitalWrite(12,LOW);
  digitalWrite(10,LOW);
  digitalWrite(8,LOW);
  digitalWrite(6,LOW);
  digitalWrite(4,LOW);
  
  // turn on power pins for flex sensor
  digitalWrite(13,HIGH);
  digitalWrite(11,HIGH);
  digitalWrite(9,HIGH);
  digitalWrite(7,HIGH);
  digitalWrite(5,HIGH);
while(count<70){
   // read sensor 1
  ADCflex = analogRead(sensorPin);
   Vflex = ADCflex * VCC / 1023.0;
   Rflex = R_DIV * (VCC / Vflex - 1.0);

  // Use the calculated resistance to estimate the sensor's bend angle:
   angle = map(Rflex, flatResistance, bendResistance, 0, 90.0);

  totalangle+=angle;
  // read sensor 2
  ADCflex = analogRead(sensorPin1);
   Vflex = ADCflex * VCC / 1023.0;
  Rflex = R_DIV * (VCC / Vflex - 1.0);

  // Use the calculated resistance to estimate the sensor's bend angle:
  angle = map(Rflex, flatResistance, bendResistance, 0, 90.0);
  totalangle+=angle;

  // read sensor 3
   ADCflex = analogRead(sensorPin2);
   Vflex = ADCflex * VCC / 1023.0;
   Rflex = R_DIV * (VCC / Vflex - 1.0);

  // Use the calculated resistance to estimate the sensor's bend angle:
   angle = map(Rflex, flatResistance, bendResistance, 0, 90.0);
  totalangle+=angle;

  // read sensor 4
   ADCflex = analogRead(sensorPin3);
   Vflex = ADCflex * VCC / 1023.0;
   Rflex = R_DIV * (VCC / Vflex - 1.0);

  // Use the calculated resistance to estimate the sensor's bend angle:
   angle = map(Rflex, flatResistance, bendResistance, 0, 90.0);
  totalangle+=angle;

  // read sensor 5
  ADCflex = analogRead(sensorPin4);
   Vflex = ADCflex * VCC / 1023.0;
   Rflex = R_DIV * (VCC / Vflex - 1.0);

  // Use the calculated resistance to estimate the sensor's bend angle:
   angle = map(Rflex, flatResistance, bendResistance, 0, 90.0);
  totalangle+=angle;
  averageangle=totalangle/5;
  totalaverageangle+=averageangle;
  count++;
  delay(500);
}
totalaverageangle=totalaverageangle/count;
return totalaverageangle;
  
 }

 float exerciseMotion(){
   sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);
  while(count<70){
    reading=g.gyro.y;
    totalreading+=reading;
    count++;
    delay(500);
  }
  totalreading=totalreading/count;
  return totalreading;
 }
float calibrateForce(){
  
  //turn off power pins for flex sensors
  digitalWrite(13,LOW);
  digitalWrite(11,LOW);
  digitalWrite(9,LOW);
  digitalWrite(7,LOW);
  digitalWrite(5,LOW);
  
  // turn on power pins for force sensor
  digitalWrite(12,HIGH);
  digitalWrite(10,HIGH);
  digitalWrite(8,HIGH);
  digitalWrite(6,HIGH);
  digitalWrite(4,HIGH);
while(count<10){
//read sensor 1
  fsrReading= analogRead(sensorPin);
  fsrVoltage = map(fsrReading, 0, 1023, 0, 5000);
  fsrResistance = 5000 - fsrVoltage;     // fsrVoltage is in millivolts so 5V = 5000mV
  fsrResistance *= 8200;                // 8K resistor
  fsrResistance /= fsrVoltage;
  fsrConductance = 1000000;           // we measure in micromhos so 
  fsrConductance /= fsrResistance;
  if (fsrConductance <= 1000) {
      fsrForce = fsrConductance / 80;
    } else {
      fsrForce = fsrConductance - 1000;
      fsrForce /= 30; 
    }
    Serial.println(fsrForce);
    
    totalfsrForce+=fsrForce;

    // read sensor 2
  fsrReading= analogRead(sensorPin1);
  fsrVoltage = map(fsrReading, 0, 1023, 0, 5000);
  fsrResistance = 5000 - fsrVoltage;     // fsrVoltage is in millivolts so 5V = 5000mV
  fsrResistance *= 8200;                // 10K resistor
  fsrResistance /= fsrVoltage;
  fsrConductance = 1000000;           // we measure in micromhos so 
  fsrConductance /= fsrResistance;
  if (fsrConductance <= 1000) {
      fsrForce = fsrConductance / 80;
    } else {
      fsrForce = fsrConductance - 1000;
      fsrForce /= 30; 
    }
     totalfsrForce+=fsrForce;

     // read sensor 3
      fsrReading= analogRead(sensorPin2);

  fsrVoltage = map(fsrReading, 0, 1023, 0, 5000);
  fsrResistance = 5000 - fsrVoltage;     // fsrVoltage is in millivolts so 5V = 5000mV
  fsrResistance *= 8200;                // 10K resistor
  fsrResistance /= fsrVoltage;
  fsrConductance = 1000000;           // we measure in micromhos so 
  fsrConductance /= fsrResistance;
  if (fsrConductance <= 1000) {
      fsrForce = fsrConductance / 80;
    } else {
      fsrForce = fsrConductance - 1000;
      fsrForce /= 30; 
    }
    totalfsrForce+=fsrForce;

       // read sensor 4
      fsrReading= analogRead(sensorPin3);

  fsrVoltage = map(fsrReading, 0, 1023, 0, 5000);
  fsrResistance = 5000 - fsrVoltage;     // fsrVoltage is in millivolts so 5V = 5000mV
  fsrResistance *= 8200;                // 10K resistor
  fsrResistance /= fsrVoltage;
  fsrConductance = 1000000;           // we measure in micromhos so 
  fsrConductance /= fsrResistance;
  if (fsrConductance <= 1000) {
      fsrForce = fsrConductance / 80;
    } else {
      fsrForce = fsrConductance - 1000;
      fsrForce /= 30; 
    }
     totalfsrForce+=fsrForce;
     
     // read sensor 5
      fsrReading= analogRead(sensorPin3);

  fsrVoltage = map(fsrReading, 0, 1023, 0, 5000);
  fsrResistance = 5000 - fsrVoltage;     // fsrVoltage is in millivolts so 5V = 5000mV
  fsrResistance *= 8200;                // 10K resistor
  fsrResistance /= fsrVoltage;
  fsrConductance = 1000000;           // we measure in micromhos so 
  fsrConductance /= fsrResistance;
  if (fsrConductance <= 1000) {
      fsrForce = fsrConductance / 80;
    } else {
      fsrForce = fsrConductance - 1000;
      fsrForce /= 30; 
    }
    totalfsrForce+=fsrForce;
    averageFsrForce=totalFsrForce/5;
    totalaverageFsrForce=+averageFsrForce;
    count++;
}
   totalaverageFsrForce=totalaverageFsrForce/count;
   Serial.println(totalaverageFsrForce);
   return totalaverageFsrForce;
}

float calibrateFlex(){

  //turn off power pins for force sensors
  digitalWrite(12,LOW);
  digitalWrite(10,LOW);
  digitalWrite(8,LOW);
  digitalWrite(6,LOW);
  digitalWrite(4,LOW);
  
  // turn on power pins for flex sensor
  digitalWrite(13,HIGH);
  digitalWrite(11,HIGH);
  digitalWrite(9,HIGH);
  digitalWrite(7,HIGH);
  digitalWrite(5,HIGH);
while(count<10){
   // read sensor 1
   ADCflex = analogRead(sensorPin);
   Vflex = ADCflex * VCC / 1023.0;
  Rflex = R_DIV * (VCC / Vflex - 1.0);

  // Use the calculated resistance to estimate the sensor's bend angle:
   angle = map(Rflex, flatResistance, bendResistance, 0, 90.0);

  totalangle+=angle;
  // read sensor 2
   ADCflex = analogRead(sensorPin1);
   Vflex = ADCflex * VCC / 1023.0;
   Rflex = R_DIV * (VCC / Vflex - 1.0);

  // Use the calculated resistance to estimate the sensor's bend angle:
   angle = map(Rflex, flatResistance, bendResistance, 0, 90.0);
  totalangle+=angle;

  // read sensor 3
   ADCflex = analogRead(sensorPin2);
    Vflex = ADCflex * VCC / 1023.0;
   Rflex = R_DIV * (VCC / Vflex - 1.0);

  // Use the calculated resistance to estimate the sensor's bend angle:
   angle = map(Rflex, flatResistance, bendResistance, 0, 90.0);
  totalangle+=angle;

  // read sensor 4
   ADCflex = analogRead(sensorPin3);
   Vflex = ADCflex * VCC / 1023.0;
   Rflex = R_DIV * (VCC / Vflex - 1.0);

  // Use the calculated resistance to estimate the sensor's bend angle:
   angle = map(Rflex, flatResistance, bendResistance, 0, 90.0);
  totalangle+=angle;

  // read sensor 5
   ADCflex = analogRead(sensorPin4);
  Vflex = ADCflex * VCC / 1023.0;
   Rflex = R_DIV * (VCC / Vflex - 1.0);

  // Use the calculated resistance to estimate the sensor's bend angle:
   angle = map(Rflex, flatResistance, bendResistance, 0, 90.0);
  totalangle+=angle;
  averageangle=totalangle/5;
  totalaverageangle+=averageangle;
  count++;
  delay(500);
}
totalaverageangle=totalaverageangle/count;
return totalaverageangle;
}

float calibrateMotion(){
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);
  while(count<10){
    reading=g.gyro.y;
    totalreading+=reading;
    count++;
    delay(500);
  }
  totalreading=totalreading/count;
  return totalreading;
}
void loop() {
  if (MyBlue.available()>0){
   response = (char)MyBlue.read(); 
 if (response == 'a') 
 { 
  data=calibrateForce();
  Serial.println(data);
   MyBlue.println(data);
 } 
 else if (response == 'b') 
 { 
 data=calibrateFlex();
 MyBlue.println(data);
 } 
 else if(response=='c'){
  data=calibrateMotion();
  MyBlue.println(data);
 }
 else if(response=='d'){
  data= exerciseForce();
  MyBlue.println(data);
 }
 else if(response=='e'){
  data= exerciseFlex();
  MyBlue.println(data);
 }
 else if(response=='f'){
  data=exerciseMotion();
  MyBlue.println(data);
 }
 
}  
delay(500);
}
