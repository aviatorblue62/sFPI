/*
 * Arduino program to control the TSL1402R
 *
 * The pixels are exposed for (240+EXTRA_CYCLES)*CLOCK_TIME microseconds
 *
 * If the computer sends a byte of data to the Arduino, then these pixels
 * are digitized and then sent serially over USB to the computer.
 *
 * VERSION C
 *
 * Scott Prahl, November 2013
 */

const int AO1_PIN = A0;     // Arduino Pin A0 connected to AO1 on TSL1402
const int CLOCK_PIN = 7;    // Arduino Pin  7 connected to CLK on TSL1402
const int SI_PIN = 8;       // Arduino Pin  8 connected to SI1 on TSL1402
const int CLOCK_TIME = 30;   // Between 10 and 400 microseconds
const int PULSE = CLOCK_TIME/2 - 4;
const int EXTRA_CYCLES = 0; // Integration time is (240+EXTRA_CYCLES)*CLOCK_TIME
                            // Integration time must be less than 100,000 us
unsigned int data[257];

void setup()
{
    Serial.begin(57600);
    pinMode(CLOCK_PIN, OUTPUT);
    pinMode(SI_PIN, OUTPUT);
}

void loop()
{
    // Start signal integration
    digitalWrite(SI_PIN, HIGH);

    // 18+239 = 256+1 clocks to clear buffer
    // plus EXTRA_CYCLES to increase integration time
    
    for (int i=0; i<257+EXTRA_CYCLES; i++) {
        digitalWrite(CLOCK_PIN, HIGH);
        delayMicroseconds(PULSE);
        if (i==0) digitalWrite(SI_PIN, LOW);  // Drop SI after first cycle
        digitalWrite(CLOCK_PIN, LOW);
        delayMicroseconds(PULSE);
    }
    
    // Stop integration
    digitalWrite(SI_PIN, HIGH);     

    // If data is requested by computer
    if (Serial.available() > 0) {
        int incomingByte = Serial.read();
        Serial.flush();
        
        // Convert pixels and store in as an array of 2-byte integers
        // This requires about 257*100 microseconds for the A/D conversion
        // and then 257*PULSE microseconds waiting
        for (int i=0; i<257; i++) {
            digitalWrite(CLOCK_PIN, HIGH);
            data[i] = analogRead(AO1_PIN);
            if (i==0) digitalWrite(SI_PIN, LOW);  // Drop SI after first point
            digitalWrite(CLOCK_PIN, LOW);
            delayMicroseconds(PULSE);
        }

        // send 512 bytes of data over serial interface
        // this is probably slowest of everything
        for (int i=0; i<256; i++) {
            Serial.write(byte(0x00FF & data[i]));
            Serial.write(byte(data[i] >> 8));
        }
    }
}
