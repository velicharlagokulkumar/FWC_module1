#include <avr/io.h>
#include <stdbool.h>
int main (void)
{

	 bool X=0,Y=0,Z=0,F=0;
	  DDRB =  0b00100000;  
	   DDRD =  0b11000111;
	    PORTD = 0b00111000;   

	    while(1)
	    {  
		    X = (PIND & (1 << PIND3)) == (1 << PIND3);
		    Y = (PIND & (1 << PIND4)) == (1 << PIND4);
		    Z = (PIND & (1 << PIND5)) == (1 << PIND5);
		    F = ((!X)|(Y));
		    PORTB |= (F<< 5);
	    }
	    return 0;
}
