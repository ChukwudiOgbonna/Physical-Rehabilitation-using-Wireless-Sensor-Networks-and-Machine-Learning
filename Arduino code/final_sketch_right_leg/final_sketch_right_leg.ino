#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
#include <SoftwareSerial.h> 
SoftwareSerial MyBlue(3, 2); // RX | TX 
Adafruit_MPU6050 mpu;
// response from our application
char response;
int count;
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


const int sensorPin= A2;
void setup() {
Serial.begin(19200);
  // power pins for force sensors
  pinMode(8,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(sensorPin, INPUT);

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
  MyBlue.begin(9600); 

}

float calibrateMotion(){
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);
  while(count<10){
    reading=g.gyro.y;
    totalreading+=reading;
    count++;
  }
  totalreading=totalreading/count;
  Serial.println(totalreading);
  return totalreading;
}

float exerciseMotion(){
   sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);
  while(count<70){
    reading=a.acceleration.y;
    totalreading+=reading;
    count++;
    delay(500);
  }
  totalreading=totalreading/count;
  return totalreading;
 }
 
float calibrateForce(){
  //turn on power
  digitalWrite(8,HIGH);
  digitalWrite(6,HIGH);
  digitalWrite(4,HIGH);

  while(count<10){
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
    totalFsrForce+=fsrForce;
    count++;
    delay(50);
}
averageFsrForce= totalFsrForce/count;
Serial.println(fsrForce);
return fsrForce;
}

float exerciseForce(){
  //turn on power
  digitalWrite(8,HIGH);
  digitalWrite(6,HIGH);
  digitalWrite(4,HIGH);

  while(count<70){
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
    totalFsrForce+=fsrForce;
    count++;
    delay(500);
}
averageFsrForce= totalFsrForce/count;
return averageFsrForce;
  
}
void loop() {
  // put your main code here, to run repeatedly:
   if (MyBlue.available()>0){
    while(MyBlue.available()){
   response = (char)MyBlue.read(); 
 if (response == 'a') 
 { 
  data=calibrateForce();
   MyBlue.println(data);
 }else if(response=='b'){
  data=calibrateMotion();
  MyBlue.println(data);
 }else if(response=='c'){
  data=exerciseForce();
  MyBlue.println(data);
 }else if(response=='d'){
  data=exerciseMotion();
  MyBlue.println(data);
 }
 }
}
}
