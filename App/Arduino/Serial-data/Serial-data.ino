/*
 * Title: Data Collection for sFPI
 * Authors: Scott Prahl & David Houston
 * Version: 1.0
 * Date: November 2015
 * 
 * Description:  This program accepts a byte of data 
 * from the computer and then determines what ADC 
 * pin to sample data from. It then sends the 512 bytes 
 * to the computer via USB.
 */
 
// Arduino Pin A0 connected to photodiode output
const int PIN = A0;     
// Arduino Pin A1 connected to ramp function output
const int SIN = A1;
// Pin connected to the other Arduino for communication
const int DP1 = 9;
const int PULSE = 10;
boolean run = false;
unsigned int data[257];

void setup()
{
    Serial.begin(57600);
    pinMode(PIN, INPUT);
    pinMode(SIN, INPUT);
    pinMode(DP1, INPUT);
}

void loop()
{    
    // If data is requested by computer
    if (Serial.available() > 0) {   
        char incomingByte = Serial.read();
        Serial.flush();
       /* 
        while (run != true) {
          if (digitalRead(DP1) == HIGH){
            run = true;
          }
        }*/
        
        if (incomingByte == '0') {
          TakeData(SIN);
        }
        else
        {
          TakeData(PIN);
        }                     
    }
}

void TakeData(const int P)
{
    for (int i=0; i<256; i++) {
        data[i] = analogRead(P);      
      }

    // send 512 bytes of data over serial interface
    // this is probably slowest of everything
    for (int i=0; i<256; i++) {
        Serial.write(byte(0x00FF & data[i]));
        Serial.write(byte(data[i] >> 8));
    }
}

