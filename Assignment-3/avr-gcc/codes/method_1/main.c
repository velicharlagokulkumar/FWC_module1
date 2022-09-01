#include <avr/io.h>
#include <stdbool.h>
int main (void)
{

	 bool X=1,Y=1,Z=1,F=0;
	  DDRB =  0b00100000;  
	   F = ((!X|Y)|(Y&(!Z)));
	    PORTB |= (F<< 5);
	     return 0;
}
