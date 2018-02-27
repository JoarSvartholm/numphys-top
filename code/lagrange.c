#include <stdio.h>
#include "math.h"
#include "converted_tops.h"
#include "integration.h"
#include <gsl/gsl_errno.h>
#include <gsl/gsl_odeiv2.h>

typedef struct{
  double M,Ml,l,I1,I3;
} parameters;

int func(double t, const double y[],double dydt[], void *params){
  (void)(t);
  parameters pars = *(parameters *)params;
  double g = 9.82;

  dydt[0] = y[3];
  dydt[1] = y[4];
  dydt[2] = y[5];
  dydt[3] = pars.Ml*g/pars.I1*sin(y[0]) + y[4]*y[4]*sin(y[0])*cos(y[0]) - pars.I3/pars.I1*(y[5]+y[4]*cos(y[0]))*y[4]*sin(y[0]);
  dydt[4] = pars.I3/pars.I1*(y[4]*y[3]*cos(y[0])/sin(y[0])+y[5]*y[3]/sin(y[0])) - 2*y[3]*y[4]/tan(y[0]);
  dydt[5] = y[4]*y[3]*sin(y[0]) + 2*y[3]*y[4]*cos(y[0])/tan(y[0]) - pars.I3/pars.I1*(y[3]*y[4]*cos(y[0])/tan(y[0])+y[3]*y[5]/tan(y[0]));

  return GSL_SUCCESS;
}

int jac(double t, const double y[],double *dfdy,double dfdt[],void *params){

  return GSL_SUCCESS;
}

int main(int argc, char const *argv[]) {

  parameters pars;
  double hstart = 0.01;
  double epsabs = 1e-8;
  double epsrel = 1e-12;

  pars.Ml = integrate(2,rho_top1,y_top1,0,5);
  pars.I3 = integrate(3,rho_top1,y_top1,0,5);
  pars.I1 = integrate(4,rho_top1,y_top1,0,5);

  gsl_odeiv2_system sys = {func,jac,6,&pars};

  gsl_odeiv2_driver *d = gsl_odeiv2_driver_alloc_y_new(&sys,gsl_odeiv2_step_rkf45,hstart,epsabs,epsrel);

  double t0=.0,t1=5.;
  double y[6] = {0.1745329252, 0, 0, 0, 0, 414.69023028};

  for(int i=0;i<=100;i++){
    double t = (t1-t0)*i/100 + t0;
    int status = gsl_odeiv2_driver_apply(d,&t0,t,y);

    if(status != GSL_SUCCESS){
      printf("Error code: %d\n",status );
      break;
    }

    printf("%f %f %f %f %f %f %f\n", t, y[0], y[1], y[2], y[3], y[4], y[5] );
  }

  gsl_odeiv2_driver_free(d);

  return 0;
}
