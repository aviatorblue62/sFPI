//
//  Arduino_setup.h
//  Ardunio Simulation
//
//  Created by Miles Houston on 4/21/15.
//  Copyright (c) 2015 Miles Houston. All rights reserved.
//

#ifndef __Ardunio_Simulation__Arduino_setup__
#define __Ardunio_Simulation__Arduino_setup__

#include <stdio.h>
#include <string>

using namespace std;

class generate {
public:
    string * generateList();
    void writetoPins(int i, float scale);
    void setVoltage(int analog0, int analog1);
private:
    
};

// Variables

int dc_value,v_peak,multiplier; // Int Variables
float scalar,dc_read,magnitude,vpp,ramp_wave_max; // Float Variables

#endif /* defined(__Ardunio_Simulation__Arduino_setup__) */
