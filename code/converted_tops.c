#include "converted_tops.h"
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

double rho_top1(double x){
  return top_rho(1,x);
}

double y_top2(double x){
  return top_y(2,x);
}

double rho_top2(double x){
  return top_rho(2,x);
}

double y_top3(double x){
  return top_y(3,x);
}

double rho_top3(double x){
  return top_rho(3,x);
}

double y_top4(double x){
  return top_y(4,x);
}

double rho_top4(double x){
  return top_rho(4,x);
}
