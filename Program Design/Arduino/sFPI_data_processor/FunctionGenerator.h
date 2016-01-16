#ifndef _FunctionGenerator_h_
#define _FunctionGenerator_h_

#include <Arduino.h>

#define maxWaveform 256
#define maxSamplesNum 9
#define numpins 13

class aset
{
  public:
    aset();
    int pin_assgin[numpins];
    boolean inout[numpins];
    boolean initial[numpins];
    void setPins();
};

class Waveforms
{
  // user-accessible "public" interface
  public:
        int waveformsTable[maxWaveform][maxSamplesNum]; 
        Waveforms();
        //boolean value;
	int ReturnTableValues(int i, int j);  	
};

#endif
