#include <gsl/gsl_integration.h>
#include "integration.h"


typedef struct{
  double (*rho)(double);
  double (*y)(double);
} parameters;

double mass_integrand(double x,void *params){
  parameters pars = *(parameters *)params;

  return pars.rho(x)*M_PI*pars.y(x)*pars.y(x);
}

double com_integrand(double x,void *params){
  parameters pars = *(parameters *)params;

  return pars.rho(x)*M_PI*pars.y(x)*pars.y(x)*x;
}

double I3_integrand(double x,void *params){
  parameters pars = *(parameters *)params;

  return 0.5*M_PI*pars.rho(x)*pow(pars.y(x),4);
}

double I1_integrand(double x,void *params){
  parameters pars = *(parameters *)params;

  return M_PI*pars.rho(x)*pars.y(x)*pars.y(x)*x*x + 0.25*M_PI*pars.rho(x)*pow(pars.y(x),4);
}

double integrate(int type, double (*rho)(double x),double (*y)(double x),double a,double b){
  double epsabs = 1e-8;
  double epsrel = 1e-12;

  parameters pars;
  pars.rho = rho;
  pars.y = y;


  gsl_integration_workspace *w = gsl_integration_workspace_alloc(1000);
  double result,error;

  gsl_function F;
  F.params = &pars;

  if(type == 1)   F.function = &mass_integrand;
  else if(type ==2)   F.function = &com_integrand;
  else if(type == 3)   F.function = &I3_integrand;
  else   F.function = &I1_integrand;


  gsl_integration_qags(&F,a,b,epsabs,epsrel,1000,w,&result,&error);

  gsl_integration_workspace_free(w);

  return result;
}


double integrate_error(int type, double (*rho)(double x),double (*y)(double x),double a,double b,double epsabs,double epsrel,double *error){

  parameters pars;
  pars.rho = rho;
  pars.y = y;


  gsl_integration_workspace *w = gsl_integration_workspace_alloc(1000);
  double result;

  gsl_function F;
  F.params = &pars;

  if(type == 1)   F.function = &mass_integrand;
  else if(type ==2)   F.function = &com_integrand;
  else if(type == 3)   F.function = &I3_integrand;
  else   F.function = &I1_integrand;


  gsl_integration_qags(&F,a,b,epsabs,epsrel,1000,w,&result,error);

  gsl_integration_workspace_free(w);

  return result;
}

double integrate_qag(int type, double (*rho)(double x),double (*y)(double x),double a,double b){
  double epsabs = 1e-8;
  double epsrel = 1e-12;

  parameters pars;
  pars.rho = rho;
  pars.y = y;


  gsl_integration_workspace *w = gsl_integration_workspace_alloc(1000);
  double result,error;

  gsl_function F;
  F.params = &pars;

  if(type == 1)   F.function = &mass_integrand;
  else if(type ==2)   F.function = &com_integrand;
  else if(type == 3)   F.function = &I3_integrand;
  else   F.function = &I1_integrand;


  gsl_integration_qag(&F,a,b,epsabs,epsrel,1000,31,w,&result,&error);

  gsl_integration_workspace_free(w);

  return result;
}

double integrate_qagp(int type, double (*rho)(double x),double (*y)(double x),double a,double b){
  double epsabs = 1e-8;
  double epsrel = 1e-12;
  double I[3];

  parameters pars;
  pars.rho = rho;
  pars.y = y;


  gsl_integration_workspace *w = gsl_integration_workspace_alloc(1000);
  double result,error;

  gsl_function F;
  F.params = &pars;
  I[0]=a;
  I[1]=3;
  I[2]=b;

  if(type == 1)   F.function = &mass_integrand;
  else if(type ==2)   F.function = &com_integrand;
  else if(type == 3)   F.function = &I3_integrand;
  else   F.function = &I1_integrand;


  gsl_integration_qagp(&F,I,3,epsabs,epsrel,1000,w,&result,&error);

  gsl_integration_workspace_free(w);

  return result;
}
