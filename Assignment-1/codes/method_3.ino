//Declaring all variables as integers
int X,Y,Z;
void writing(int D)
{
  digitalWrite(13, D); 
}
// the setup function runs once when you press reset or power the board
void setup() {
    pinMode(13, OUTPUT);  
    pinMode(3, INPUT);
    pinMode(4, INPUT);
    pinMode(5, INPUT);
}

// the loop function runs over and over again forever
void loop() {
    
X = digitalRead(3);  
Y = digitalRead(4);  
Z = digitalRead(5);//MSB  

D = (!X||Y);
writing(D);  
}
