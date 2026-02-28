//C - Supporting code for calculation of theoretical non-dim. temperatures values  
#include <math.h>
#include <stdio.h>
#define PII 3.1415926535897932384626433832795028841971693993751058209749445923  
 
double nonDimTemp(double x, double L, double y, double W, int steps){
	double sum = 0;
	double temp = 0;
	
	for (int n = 1; n<steps;n++){	
		temp = ( ( pow(-1,n+1) + 1 ) / n ) * ( sin(n*PII*x/L)*sinh(n*PII*y/L) ) / ( sinh(n*PII*W/L) );
		if (temp >= 0 || temp < 0 ){ sum = sum + temp;}
		else{
			sum = sum + 0;
		}
	}
	temp = sum * 2/PII;
	if (temp > 0.99999999999999){ return 1; }
	else { return temp; }
}