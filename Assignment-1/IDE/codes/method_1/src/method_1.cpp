#include <Arduino.h>
int X=0,Y=0,Z=1;
int F;
void setup()
{
    pinMode(13, OUTPUT);
}

void loop()
{
  F=(!X||Y)||(Y&&!Z);
  digitalWrite(13, F);
}
