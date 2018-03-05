import matplotlib.pyplot as plt
import numpy as np

savePlots = 0
showPlots = 1

t1,theta1,phi1,psi1,pth1,H1= np.genfromtxt("../data/hamilton1fwd.dat",unpack=True)
t2,theta2,phi2,psi2,pth2,H2= np.genfromtxt("../data/hamilton2fwd.dat",unpack=True)
t3,theta3,phi3,psi3,pth3,H3= np.genfromtxt("../data/hamilton3fwd.dat",unpack=True)
t4,theta4,phi4,psi4,pth4,H4= np.genfromtxt("../data/hamilton4fwd.dat",unpack=True)
data1= np.genfromtxt("../data/hamilton1dense.dat",unpack=True)
data2= np.genfromtxt("../data/hamilton2dense.dat",unpack=True)
data3= np.genfromtxt("../data/hamilton3dense.dat",unpack=True)
data4= np.genfromtxt("../data/hamilton4dense.dat",unpack=True)
print()
for i in range(len(t1)):
    theta1[i] -= np.floor(theta1[i]/np.pi)*np.pi
    phi1[i] -= np.floor(phi1[i]/(2*np.pi))*2*np.pi
    data1[3,i] -= np.floor(data1[3,i]/(2*np.pi))*2*np.pi
    data2[3,i] -= np.floor(data2[3,i]/(2*np.pi))*2*np.pi
    data3[3,i] -= np.floor(data3[3,i]/(2*np.pi))*2*np.pi
    data4[3,i] -= np.floor(data4[3,i]/(2*np.pi))*2*np.pi

plt.figure("theta1")
plt.plot(t1,theta1,'-',label=r"$\theta$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/ham-theta-1.pdf")
plt.figure("phi1")
plt.plot(t1,phi1,'-',label="$\phi$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/ham-phi-1.pdf")
plt.figure("psi1")
plt.plot(data1[0,0:340],data1[3,0:340],'-',label="$\psi$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/ham-psi-1.pdf")
plt.figure("H1")
plt.plot(t1,(H1-H1[0])/H1[0],'-',label="$H$")
plt.xlabel("Time")
plt.legend()
if savePlots:
    plt.savefig("../figs/ham-const-1.pdf")
plt.figure("pth1")
plt.plot(t1,pth1,label=r"$p_{\theta}$")
plt.xlabel("Time")
plt.ylabel("momentum [g $\cdot$ cm$^2$ rad/s]")
plt.legend()
if savePlots:
    plt.savefig("../figs/ham-pth-1.pdf")


plt.figure("theta2")
plt.plot(t2,theta2,'-',label=r"$\theta$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/ham-theta-2.pdf")
plt.figure("phi2")
plt.plot(t2,phi2,'-',label="$\phi$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/ham-phi-2.pdf")
plt.figure("psi2")
plt.plot(data2[0,0:340],data2[3,0:340],'-',label="$\psi$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/ham-psi-2.pdf")
plt.figure("H2")
plt.plot(t2,(H2-H2[0])/H2[0],'-',label="$H$")
plt.xlabel("Time")
plt.legend()
if savePlots:
    plt.savefig("../figs/ham-const-2.pdf")
plt.figure("pth2")
plt.plot(t1,pth2,label=r"$p_{\theta}$")
plt.xlabel("Time")
plt.ylabel("momentum [g $\cdot$ cm$^2$ rad/s]")
plt.legend()
if savePlots:
    plt.savefig("../figs/ham-pth-2.pdf")


plt.figure("theta3")
plt.plot(t3,theta3,'-',label=r"$\theta$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/ham-theta-3.pdf")
plt.figure("phi3")
plt.plot(t3,phi3,'-',label="$\phi$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/ham-phi-3.pdf")
plt.figure("psi3")
plt.plot(data3[0,0:340],data3[3,0:340],'-',label="$\psi$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/ham-psi-3.pdf")
plt.figure("H3")
plt.plot(t3,(H3-H3[0])/H3[0],'-',label="$H$")
plt.xlabel("Time")
plt.legend()
if savePlots:
    plt.savefig("../figs/ham-const-3.pdf")
plt.figure("pth3")
plt.plot(t1,pth3,label=r"$p_{\theta}$")
plt.xlabel("Time")
plt.ylabel("momentum [g $\cdot$ cm$^2$ rad/s]")
plt.legend()
if savePlots:
    plt.savefig("../figs/ham-pth-3.pdf")

plt.figure("theta4")
plt.plot(t4,theta4,'-',label=r"$\theta$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/ham-theta-4.pdf")
plt.figure("phi4")
plt.plot(t4,phi4,'-',label="$\phi$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/ham-phi-4.pdf")
plt.figure("psi4")
plt.plot(data4[0,0:340],data4[3,0:340],'-',label="$\psi$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/ham-psi-4.pdf")
plt.figure("H4")
plt.plot(t4,(H4-H4[0])/H4[0],'-',label="$H$")
plt.xlabel("Time")
plt.legend()
if savePlots:
    plt.savefig("../figs/ham-const-4.pdf")
plt.figure("pth4")
plt.plot(t1,pth4,label=r"$p_{\theta}$")
plt.xlabel("Time")
plt.ylabel("momentum [g $\cdot$ cm$^2$ rad/s]")
plt.legend()
if savePlots:
    plt.savefig("../figs/ham-pth-4.pdf")


if showPlots:
    plt.show()


t,theta,phi,psi,pth,H= np.genfromtxt("../data/hamiltonback.dat",unpack=True)

#0.1745329252, 0, 0, 0, 0, 414.69023028
print(t[-1])
print(0.1745329252-theta[-1])
print(phi[-1])
print(psi[-1])
print(pth[-1])
