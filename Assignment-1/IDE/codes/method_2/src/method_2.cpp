#include <Arduino.h>
int X=1,Y=0,Z=0;
int F;
void setup()
{
    pinMode(13, OUTPUT);
}

void loop()
{
  F =(!X || Y);
  digitalWrite(13, F);
}