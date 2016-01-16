int state1 = 0; // state of the output1; 0 --> OFF, 1 --> ON
unsigned long currentMillis = millis(); // derive actual timestamp
unsigned long startMillis = millis(); // derive actual timestamp
unsigned long pulsewidth_1 = 10;
int pin_out = 3;

void setup() {                
  // initialize the digital pin as an output.
  pinMode(3, OUTPUT);     
  pinMode(13, OUTPUT);  
  Serial.begin(9600); 
  
  digitalWrite(3, LOW);    // turn the output off 
  currentMillis = millis(); // derive actual timestamp
  startMillis = millis(); // derive actual timestamp

}
   /////////////////////////////
   
void loop() {

  if(currentMillis - startMillis <= pulsewidth_1) {
    state1 = HIGH;
  }
  
  // Create the pulsewidth. Read Analog POT at A0, contraint (limit) the amount to maximum periode, more wouldnt make sense
  if (currentMillis - startMillis >= constrain(analogRead(A0), 5, analogRead(A1))) 
  {
        state1 = LOW;
  }
  
  // Create the periode (hz). Read Analog POT at A1, contraint (limit) the amount to minimum 10ms
  if (currentMillis - startMillis >= constrain((analogRead(A1)*1.5),10,20000 )) 
  {
        state1 = LOW;
        startMillis = millis();  
  }
  
    digitalWrite(3, state1);
    currentMillis = millis();

}
