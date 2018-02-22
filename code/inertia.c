#include <stdio.h>
#include "integration.h"
#include <math.h>

double rho_cyl(double x){
  return 1;
}

double y_cyl(double x){
  return 1;
}

int main(int argc, char const *argv[]) {
  double M,Ml;

  M = integrate(1,rho_cyl,y_cyl,0,1);
  Ml = integrate(2,rho_cyl,y_cyl,0,1);

  printf("Mass of unit cylinder is %f\n",M );
  printf("analytical value: %f\n", M_PI );

  printf("COM of unit cylinder is %f\n",Ml );
  printf("analytical value: %f\n", .5);

  return 0;
}
