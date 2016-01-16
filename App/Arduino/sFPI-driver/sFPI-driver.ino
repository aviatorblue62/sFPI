/*  sFPI Driver version 1.5
    Copyright (c) 2015 David Miles Houston
    
    This sketch uses the following associated
    pins in conjunction with the ,
    for the use of a sawtooth signal generator.

    Developers Note: Current Pin out is as follows
     
    Pin Name      Pin Location
    ---------    --------------
      SDA            A5
      SCL            A4 
*/

#include <Wire.h>
#include "Adafruit_MCP4725.h"

// use layout from the Adafruit Header File
Adafruit_MCP4725 dac;

#define bitres 1024;
// Number of tunable bits at one time
const int numbits = 1024; 
// Number of bits in the period of the signal
const int wave_bits = 4096; 
const int DP1 = 9;
//Number of bits to skip each time to increase speed
uint32_t skip = 1;

// Setup Loop
void setup()
{
  // Setup for Serial Communication
  // Pin Assignments
  pinMode(DP1,OUTPUT);
  dac.begin(0x62);
}

// Infinite Loop
void loop()
{ 
        digitalWrite(DP1,HIGH);
	for (uint32_t i = 0; i < wave_bits-1; i = i + skip) {
		dac.setVoltage(i,false);
                if (i==0) {
                  digitalWrite(DP1,LOW);
                }
  	}
        
}
