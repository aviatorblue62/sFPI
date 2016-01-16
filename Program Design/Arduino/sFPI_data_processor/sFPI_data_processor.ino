/*  sFPI Processor version 1.0
    Copyright (c) 2015 David Miles Houston
    
    This sketch uses the following assoicated
    pins in conjunction with the MCP4725 DAC,
    for use with the output manipulation of the
    sFPI Driver program and with data collection,
    storage, and processing. It uses I2C to com-
    muicate with the DAC and its associated
    libraries. This data will be sent to a computer 
    via usb interface every cycle of the wave and 
    processed through an interactive GUI.
    
    Pin Name      Pin Location
    ---------    --------------
      SCL              A4
      SDA              A5
      Data_IN          A0
      Wave_IN          A1
      Signal_AT_1      A2
      Signal_AT_2      A3     
*/

#define bitres 1025

int photodiode_data[bitres];
int ramp_function[bitres];
int data[2];
int max_count = 1025;
int counter = 0;
boolean transmit;
int recieved = 87456;

void setup() {
  Serial.begin(9600);
  // Set A0, A1, A2 for analog inputs. 
  // A5 and A4 have already been set in the Adafruit Header File as SCL and SDA. 
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(13, OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  
  analogWrite(13, 255);
  digitalWrite(8,HIGH);
  
}
 
void loop(){
  
    if (counter < max_count-2) {
      digitalWrite(8,HIGH);
      photodiode_data[counter] = analogRead(A0);
      ramp_function[counter] = analogRead(A1);
      counter++;
    }
    
    else {
      counter = 0;
      transmit = true;
      digitalWrite(9,HIGH);
      digitalWrite(8,LOW);
      photodiode_data[max_count-1] = recieved;
      ramp_function[max_count-1] = recieved;
      data[0] = *photodiode_data;
      data[1] = *ramp_function;
    }
    
    if (transmit == true){
      while (true){
        digitalWrite(10,HIGH);
        digitalWrite(9,LOW);
        if (Serial.available() > 0){
          for (int j = 0; j < 2; j++){
            for (int i = 0; i < max_count-1; i++){
              int * output = &data[j];
              Serial.print("Cool");  
            }
          }
        }
      }
    }  
}
  
    
    

