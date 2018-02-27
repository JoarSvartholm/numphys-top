import matplotlib.pyplot as plt
import numpy as np

savePlots = 0
showPlots = 1

top1= np.genfromtxt("../data/top1.dat",unpack=True)

plt.figure("Top 1")
plt.plot(np.linspace(0,5,51),top1)
if savePlots:
    plt.savefig("../figs/Top1.pdf")

top2= np.genfromtxt("../data/top2.dat",unpack=True)

plt.figure("Top 2")
plt.plot(np.linspace(0,5,51),top2)

top3= np.genfromtxt("../data/top3.dat",unpack=True)

plt.figure("Top 3")
plt.plot(np.linspace(0,5,51),top3)

top4= np.genfromtxt("../data/top4.dat",unpack=True)

plt.figure("Top 4")
plt.plot(np.linspace(0,5,51),top4)

rho1= np.genfromtxt("../data/rho1.dat",unpack=True)

plt.figure("Rho 1")
plt.plot(np.linspace(0,5,51),rho1)
if savePlots:
    plt.savefig("../figs/rho1.pdf")

rho2= np.genfromtxt("../data/rho2.dat",unpack=True)

plt.figure("Rho 2")
plt.plot(np.linspace(0,5,51),rho2)

rho3= np.genfromtxt("../data/rho3.dat",unpack=True)

plt.figure("Rho 3")
plt.plot(np.linspace(0,5,51),rho3)

rho4= np.genfromtxt("../data/rho4.dat",unpack=True)

plt.figure("Rho 4")
plt.plot(np.linspace(0,5,51),rho4)

err,est = np.genfromtxt("../data/erroranalysis.dat",unpack=True)
xx = 10**-2*2.**np.array([0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14])
plt.figure("error analysis")
h1,=plt.loglog(xx,np.abs(err[0:15]),'*-',label="Error")
h2,=plt.loglog(xx,est[0:15],'*-',label="Estimated error")
plt.legend(handles=[h2,h1])
if savePlots:
    plt.savefig("../figs/absErr.pdf")

plt.figure("error relerr")
h1,=plt.loglog(xx,np.abs(err[15:]),'*-',label="Error")
h2,=plt.loglog(xx,est[15:],'*-',label="Estimated error")
plt.legend(handles=[h2,h1])
if savePlots:
    plt.savefig("../figs/relErr.pdf")


if showPlots:
    plt.show()

print(0.25*np.pi*2.5*9+0.3*0.3*np.pi*2.5*2)
print((0.25*3**4/4+0.3**2*8)/(0.25*9+0.3**2*2))
print(2.5*np.pi/2*(0.5**4*3**5/5+0.3**4*2))
print(2.5*np.pi*((0.5**2+0.5**4/4)*3**5/5+0.3**2/3*(5**3-3**3)+0.5*0.3**4))
