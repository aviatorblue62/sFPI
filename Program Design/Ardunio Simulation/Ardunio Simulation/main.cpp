//
//  main.cpp
//  Ardunio Simulation
//
//  Created by Miles Houston on 4/21/15.
//  Copyright (c) 2015 Miles Houston. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <string.h>
#include <cstring>
#include <math.h>
#include <iostream>
#include <fstream>

using namespace std;

// Constants
const int wave_bits = 4096;
int DB0 = 1,
DB1 = 2,
DB2 = 3,
DB3 = 4,
DB4 = 5,
DB5 = 6,
DB6 = 7,
DB7 = 8,
A0 = 9,
A1 = 10,
LDAC = 11,
WR = 12,
CS = 13; // Which is tide to SS on the Uno so might need to change things around

const float initial_wave = 34; // Volts
const int numbits = 1024; // Number of tunable bits at one time
const int step = 4; // different numbers of steps for a perfect signal
const int dac_reset_time = 1; // us
const int time_step = 500; // microseconds
const int discharge_time =  5000; // mircoseconds

// Variables

int dc_value,v_peak,multiplier; // Int Variables
float scalar,dc_read,magnitude,vpp,ramp_wave_max; // Float Variables
int LIST[4];
int daca,dacb;


int * makeTT(int);
float setVoltage();
void writetoPins(int, float);

int main(int argc, const char * argv[]) {
    
    // Generate Truth Tables
    for (int AA = 0; AA < 4; AA++) {
        for (int DB = 0; DB < wave_bits-1; DB++) {
            LIST[AA] = *makeTT(DB);
            cout << LIST[AA];
        }
    }
    
    daca = *makeTT(2);
    dacb = *makeTT(2);
    
    scalar = setVoltage();
    
    for (int i = 0; i < 4095; i++){
        writetoPins(i, scalar);
    }
    
    return 0;
}


// Set Voltage Function
float setVoltage() {

    int multiplier;
    int v_peak;
    cout << "Enter Multiplier: ";
    cin >> multiplier;
    cout << "\nEnter VPP (in Volts): ";
    cin >> v_peak;
    
    int magnitude = step*(multiplier)/(numbits-1); //Magnitude has four stages for a max bit resolution of 4096 bits
    float vpp = (v_peak)/(numbits-1); // Vpp max out at 5 V/div (i.e. the higest output will be 34 V or 1/1 for the MDAC)
    
    // Decode to specific readable values for the MDAC
    
    // Create table of values to access for iterrative loop
    float ramp_wave_max = vpp + float(magnitude);
    float scalar = wave_bits * ramp_wave_max/initial_wave;
    return scalar;
}


void writetoPins(int i, int scale) {// This is for 1 value
    
    // First write LSB to list (0-7) while A0 = 1, A1 = 0, WR = 1, LDAC = 1, CS = 0 (This generates first intial value of the rampfunction)
    
    for (int j = 0; j < 2; j++) {
        
        // Multiplex DAC A
        
        cout << "A0" + daca[j];  // A0
        cout << "A1: 0";  // A1
        cout << "CS: LOW";
        cout << "WR: LOW";

		if (j == 0){
            cout << "DB0" + LIST[i][DB0]; // DATA SET BITS
			cout << "DB1" + LIST[i][DB1];
			cout << "DB2" + LIST[i][DB2];
			cout << "DB3" + LIST[i][DB3];
			cout << "DB4" + LIST[i][DB4];
			cout << "DB5" + LIST[i][DB5];
			cout << "DB6" + LIST[i][DB6];
			cout << "DB7" + LIST[i][DB7];
		}

		else {
			cout << "DB0" + LIST[i][DB0]; // DATA SET BITS
			cout << "DB1" + LIST[i][DB1];
			cout << "DB2" + LIST[i][DB2];
			cout << "DB3" + LIST[i][DB3];
		}
        
        cout << "LDAC: LOW";// ~LDAC
        cout << "LDAC: HIGH";// ~LDAC
    }
    
    cout << "CS:  HIGH";
    cout << "WR: HIGH";
    
    for (int j = 0; j < 2; j++) {
        
        // Multiplex DAC B
        cout << "A0" + dacb[j];  // A0
        cout << "A1: HIGH";  // A1
        cout << "CS: LOW";
        cout << "WR: LOW";

		if (j == 0){
			cout << "DB0" + LIST[scale][DB0]; // DATA SET BITS
			cout << "DB1" + LIST[scale][DB1];
			cout << "DB2" + LIST[scale][DB2];
			cout << "DB3" + LIST[scale][DB3];
			cout << "DB4" + LIST[scale][DB4];
			cout << "DB5" + LIST[scale][DB5];
			cout << "DB6" + LIST[scale][DB6];
			cout << "DB7" + LIST[scale][DB7];
		}

		else {
			cout << "DB0" + LIST[scale][DB0]; // DATA SET BITS
			cout << "DB1" + LIST[scale][DB1];
			cout << "DB2" + LIST[scale][DB2];
			cout << "DB3" + LIST[scale][DB3];
		}
        
        cout << "LDAC: LOW";// ~LDAC
        cout << "LDAC: HIGH";// ~LDAC
    }
    
    cout << "CS: HIGH";
    cout << "WR: HIGH";
}


int * makeTT(int val) {
    int list[4096];
    unsigned int mask = 1 << (sizeof(int) * 8 - 1);
    for(int i = 0; i < sizeof(int) * 8; i++)
    {
        if( (val & mask) == 0 )
            list[i] = 1 ;
        else
            list[i] = 0 ;
        
        mask  >>= 1;
    }
    return list[];
}

