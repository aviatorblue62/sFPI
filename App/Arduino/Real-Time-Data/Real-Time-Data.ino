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
 *
 * Version: 2.0
 *
 * Description:  This program takes real time data from
 * 
 */

const int PIN         = A0; // Connected to Photodiode Circuit
const int SIN         = A1; // Connected to sFPI-Driver Circuit
const int TGR         = 9;  // Trigger pin for data
const int DLY         = 60; // Delay between data samples
boolean   run         = false;

// Number of points taken per interrupt
unsigned const int PTS         = (4096*3); // Number of points (3 cycles)
unsigned const int ARRAY_LEN   = PTS+1;     // Length of the data array

unsigned int data_port1[ARRAY_LEN];
unsigned int data_port2[ARRAY_LEN];

void setup()
{
    Serial.begin(115200); // Enable Serial communication 
    pinMode(PIN, INPUT);  // Enable PIN for input
    pinMode(SIN, INPUT);  // Enable SIN for input
    
    // Create interrput based on master clock
    attachInterrupt(TGR, TakeData, RISING);   
}

void loop() { 
// Do Nothing  
}

void TakeData() {
    for (int i = 0; i < PTS; i++) {
        data_port1[i] = analogRead(PIN); // read from PIN ADC
        delayMicroseconds(60);           // Wait for ADC to reset
        data_port2[i] = analogRead(SIN); // read from SIN ADC      
      }
  
    SendData(data_port1);
    SendData(data_port2);
}

void SendData(unsigned int data[]) {
    // send 512 bytes of data over serial interface
    // this is probably slowest of everything
    
    for (int i=0; i<256; i++) {
        Serial.write(byte(0x00FF & data[i]));
        Serial.write(byte(data[i] >> 8));
    }
}

