#include <Arduino.h>
int X,Y,Z;
int D;
void writing(int D)
{
  digitalWrite(13, D); 
}
void setup() {
    pinMode(13, OUTPUT);  
    pinMode(3, INPUT);
    pinMode(4, INPUT);
    pinMode(5, INPUT);
}
void loop() {
    
X = digitalRead(3);  
Y = digitalRead(4);  
Z = digitalRead(5);  
D = (!X||Y);
writing(D);  
}