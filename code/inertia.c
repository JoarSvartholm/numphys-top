#include <stdio.h>
#include <math.h>
#include "integration.h"
#include "top.h"

double rho_cyl(double x){
  return 1;
}

double y_cyl(double x){
  return 1;
}

double y_cone(double x){
  return x;
}

double y_top1(double x){
  return top_y(1,x);
}

int main(int argc, char const *argv[]) {
  double M,Ml;

  M = integrate(1,rho_cyl,y_top1,0,1);
  Ml = integrate(2,rho_cyl,y_cone,0,1);

  printf("Mass of unit cylinder is %f\n",M );
  printf("analytical value: %f\n", M_PI/3 );

  printf("COM of unit cylinder is %f\n",Ml );
  printf("analytical value: %f\n", .5);

  return 0;
}
