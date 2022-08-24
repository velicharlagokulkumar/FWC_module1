#include <Arduino.h>
//Declaring all variables as integers
int X=0,Y=0,Z=1;
int F;
// the setup function runs once when you press reset or power the board
void setup()
{
    pinMode(13, OUTPUT);
}

// the loop function runs over and over again forever
void loop()
{
  F=(!X||Y)||(Y&&!Z);
  digitalWrite(13, F);
}
