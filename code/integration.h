
double integrate(int type, double (*rho)(double x),double (*y)(double x),double a,double b);

double integrate_error(int type, double (*rho)(double x),double (*y)(double x),double a,double b,double epsabs,double epsrel,double *error);

double integrate_qag(int type, double (*rho)(double x),double (*y)(double x),double a,double b);

double integrate_qagp(int type, double (*rho)(double x),double (*y)(double x),double a,double b);
