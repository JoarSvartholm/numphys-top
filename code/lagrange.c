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
  double h = 0.01;
  double epsabs = 1e-8;
  double epsrel = 1e-12;

if(argc<2) {fprintf(stderr, "Wrong number of input parameters\n" ); exit(1);}
if(atoi(argv[1])==1){
  pars.Ml = integrate(2,rho_top1,y_top1,0,5);
  pars.I3 = integrate(3,rho_top1,y_top1,0,5);
  pars.I1 = integrate(4,rho_top1,y_top1,0,5);
} else if(atoi(argv[1])==2){
  pars.Ml = integrate(2,rho_top2,y_top2,0,5);
  pars.I3 = integrate(3,rho_top2,y_top2,0,5);
  pars.I1 = integrate(4,rho_top2,y_top2,0,5);
} else if(atoi(argv[1])==3){
  pars.Ml = integrate(2,rho_top3,y_top3,0,5);
  pars.I3 = integrate(3,rho_top3,y_top3,0,5);
  pars.I1 = integrate(4,rho_top3,y_top3,0,5);
} else if(atoi(argv[1])==4){
  pars.Ml = integrate(2,rho_top4,y_top4,0,5);
  pars.I3 = integrate(3,rho_top4,y_top4,0,5);
  pars.I1 = integrate(4,rho_top4,y_top4,0,5);
}else {fprintf(stderr, "Wrong input parameter\n" ); exit(1);}

  gsl_odeiv2_system sys = {func,jac,6,&pars};

  gsl_odeiv2_driver *d = gsl_odeiv2_driver_alloc_y_new(&sys,gsl_odeiv2_step_rkf45,h,epsabs,epsrel);

  double t0=0.,t1=5.;
  double y[6] = {0.1745329252, 0, 0, 0, 0, 414.69023028};
  //double y[6] = {0.175078, 0.357448, 1658.408940, 0.014379, 0.124736, 414.567401};

  for(double ti=t0;ti<=t1;ti+=h){

    int status = gsl_odeiv2_driver_apply(d,&t0,ti,y);

    if(status != GSL_SUCCESS){
      printf("Error code: %d\n",status );
      break;
    }

    double K = pars.I1*0.5*(y[3]*y[3]+y[4]*y[4]*sin(y[0])*sin(y[0])) + pars.I3*0.5*(y[5]+y[4]*cos(y[0]))*(y[5]+y[4]*cos(y[0]));
    double V = pars.Ml*9.82*cos(y[0]);

    double C1 = pars.I1*y[4]*sin(y[0])*sin(y[0]) + pars.I3*cos(y[0])*(y[5]+y[4]*cos(y[0]));
    double C2 = y[5] + y[4]*cos(y[0]);
    printf("%e %e %e %e %e %e %e %.10e %.10e %.20e %.20e %.20e\n", t0, y[0], y[1], y[2], y[3], y[4], y[5], K, V, K+V, C1, C2 );
  }

  gsl_odeiv2_driver_free(d);

  return 0;
}
