#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "integration.h"
#include "converted_tops.h"
#include "top.h"


int main(int argc, char const *argv[]) {
  double M,Ml,I3,I1;

  if(argc < 2){
    printf("--- Running test on unit cylinder and cone ---\n" );

    M = integrate(1,rho_cyl,y_cyl,0,1);
    Ml = integrate(2,rho_cyl,y_cyl,0,1);

    printf("Mass of unit cylinder is %f\n",M );
    printf("analytical value: %f\n", M_PI );
    printf("COM of unit cylinder is %f\n",Ml/M );
    printf("analytical value: %f\n", .5);
    M = integrate(1,rho_cyl,y_cone,0,1);
    Ml = integrate(2,rho_cyl,y_cone,0,1);

    printf("Mass of unit cone is %f\n",M );
    printf("analytical value: %f\n", M_PI/3 );
    printf("COM of unit cone is %f\n",Ml/M);
    printf("analytical value: %f\n", .75);
  }else if(atoi(argv[1])==1){
    M = integrate(1,rho_top1,y_top1,0,5);
    Ml = integrate(2,rho_top1,y_top1,0,5);
    I3 = integrate(3,rho_top1,y_top1,0,5);
    I1 = integrate(4,rho_top1,y_top1,0,5);

    printf("Mass of unit top 1 is %f\n",M );
    printf("COM of unit top 1 is %f\n",Ml/M);
    printf("I3 of top 1 is %f\n",I3);
    printf("I1 of top 1 is %f\n",I1);
  }else if(atoi(argv[1])==2){

    M = integrate(1,rho_top2,y_top2,0,5);
    Ml = integrate(2,rho_top2,y_top2,0,5);
    I3 = integrate(3,rho_top2,y_top2,0,5);
    I1 = integrate(4,rho_top2,y_top2,0,5);

    printf("Mass of unit top 2 is %f\n",M );
    printf("COM of unit top 2 is %f\n",Ml/M);
    printf("I3 of top 2 is %f\n",I3);
    printf("I1 of top 2 is %f\n",I1);
  }else if(atoi(argv[1])==3){
    M = integrate(1,rho_top3,y_top3,0,5);
    Ml = integrate(2,rho_top3,y_top3,0,5);
    I3 = integrate(3,rho_top3,y_top3,0,5);
    I1 = integrate(4,rho_top3,y_top3,0,5);

    printf("Mass of unit top 3 is %f\n",M );
    printf("COM of unit top 3 is %f\n",Ml/M);
    printf("I3 of top 3 is %f\n",I3);
    printf("I1 of top 3 is %f\n",I1);
  }else if(atoi(argv[1])==4){
    M = integrate(1,rho_top4,y_top4,0,5);
    Ml = integrate(2,rho_top4,y_top4,0,5);
    I3 = integrate(3,rho_top4,y_top4,0,5);
    I1 = integrate(4,rho_top4,y_top4,0,5);

    printf("Mass of unit top 4 is %f\n",M );
    printf("COM of unit top 4 is %f\n",Ml/M);
    printf("I3 of top 4 is %f\n",I3);
    printf("I1 of top 4 is %f\n",I1);
  }else if (atoi(argv[1])==5){
    for(int i = 0;i<=50;i++){
      printf("%f\n", top_y(atoi(argv[2]),(double)i/10.));
    }
  }else if (atoi(argv[1])==6){
    for(int i = 0;i<=50;i++){
      printf("%f\n", top_rho(atoi(argv[2]),(double)i/10.));
    }
  }else if(atoi(argv[1])==7){

    double ana = 124.51250878559192;
    double error;
  for(int i = 0;i<15;i++){

    I1 = integrate_error(4,rho_top1,y_top1,0,5,1e-2*pow(2,-i*2),1e-15,&error);
    printf("%.20f %.20f\n",(ana-I1) , error);
  }

  for(int i=0;i<15;i++){

    I1 = integrate_error(4,rho_top1,y_top1,0,5,1e-10,1e-2*pow(2,-i*3),&error);
    printf("%.20f %.20f\n",(ana-I1) , error);

  }

}else if(atoi(argv[1])==8){
  double ana = 124.51250878559192;

  I1 = integrate_qag(4,rho_top1,y_top1,0,5);
  double I2 = integrate_qagp(4,rho_top1,y_top1,0,5);
  I3 = integrate(4,rho_top1,y_top1,0,5);

  printf("QAG gives error: %e\n",(I1-ana)/ana );
  printf("QAGP gives error: %e\n",(I2-ana)/ana );
  printf("QAGS gives error: %e\n",(I3-ana)/ana );
}else printf("Not a valid test case\n" );

  return 0;
}
