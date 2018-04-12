import matplotlib.pyplot as plt
import numpy as np

savePlots = 0
showPlots = 1

t1,theta1,phi1,psi1,x1,y1,z1,K1,V1,E1,C11,C21= np.genfromtxt("../data/lagrange1fwd.dat",unpack=True)
t2,theta2,phi2,psi2,x2,y2,z2,K2,V2,E2,C12,C22= np.genfromtxt("../data/lagrange2fwd.dat",unpack=True)
t3,theta3,phi3,psi3,x3,y3,z3,K3,V3,E3,C13,C23= np.genfromtxt("../data/lagrange3fwd.dat",unpack=True)
t4,theta4,phi4,psi4,x4,y4,z4,K4,V4,E4,C14,C24= np.genfromtxt("../data/lagrange4fwd.dat",unpack=True)
data1= np.genfromtxt("../data/lagrange1dense.dat",unpack=True)
data2= np.genfromtxt("../data/lagrange2dense.dat",unpack=True)
data3= np.genfromtxt("../data/lagrange3dense.dat",unpack=True)
data4= np.genfromtxt("../data/lagrange4dense.dat",unpack=True)
print()
for i in range(len(t1)):
    theta1[i] -= np.floor(theta1[i]/np.pi)*np.pi
    phi1[i] -= np.floor(phi1[i]/(2*np.pi))*2*np.pi
    phi2[i] -= np.floor(phi2[i]/(2*np.pi))*2*np.pi
    phi3[i] -= np.floor(phi3[i]/(2*np.pi))*2*np.pi
    phi4[i] -= np.floor(phi4[i]/(2*np.pi))*2*np.pi
    data1[3,i] -= np.floor(data1[3,i]/(2*np.pi))*2*np.pi
    data2[3,i] -= np.floor(data2[3,i]/(2*np.pi))*2*np.pi
    data3[3,i] -= np.floor(data3[3,i]/(2*np.pi))*2*np.pi
    data4[3,i] -= np.floor(data4[3,i]/(2*np.pi))*2*np.pi

plt.figure("theta1")
plt.plot(t1,theta1,label=r"$\theta$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-theta-1.pdf")
plt.figure("phi1")
plt.plot(t1,phi1,label="$\phi$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-phi-1.pdf")
plt.figure("psi1")
plt.plot(data1[0,0:340],data1[3,0:340],'-',label="$\psi$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-psi-1.pdf")
plt.figure("constants of motion1")
plt.plot(t1,(E1-E1[0])/E1[0],label="Total Energy")
plt.plot(t1,(C11-C11[0])/C11[0],'--',label="Eq. (18)")
plt.plot(t1,(C21-C21[0])/C21[0],'-.',label="Eq. (20)")
plt.xlabel("Time")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-const-1.pdf")
plt.figure("thetadot1")
plt.plot(t1,x1,label=r"$\dot{\theta}$")
plt.xlabel("Time")
plt.ylabel("Angular velocity [rad/s]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-thetadot-1.pdf")
plt.figure("phidot1")
plt.plot(t1,y1,label=r"$\dot{\phi}$")
plt.xlabel("Time")
plt.ylabel("Angular velocity [rad/s]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-phidot-1.pdf")
plt.figure("psidot1")
plt.plot(t1,z1,label=r"$\dot{\psi}$")
plt.xlabel("Time")
plt.ylabel("Angular velocity [rad/s]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-psidot-1.pdf")


plt.figure("theta2")
plt.plot(t2,theta2,label=r"$\theta$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-theta-2.pdf")
plt.figure("phi2")
plt.plot(t2,phi2,label="$\phi$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-phi-2.pdf")
plt.figure("psi2")
plt.plot(data2[0,0:340],data2[3,0:340],'-',label="$\psi$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-psi-2.pdf")
plt.figure("constants of motion2")
plt.plot(t2,(E2-E2[0])/E2[0],label="Total Energy")
plt.plot(t2,(C12-C12[0])/C12[0],'--',label="Eq. (18)")
plt.plot(t2,(C22-C22[0])/C22[0],'-.',label="Eq. (20)")
plt.xlabel("Time")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-const-2.pdf")
plt.figure("thetadot2")
plt.plot(t1,x2,label=r"$\dot{\theta}$")
plt.xlabel("Time")
plt.ylabel("Angular velocity [rad/s]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-thetadot-2.pdf")
plt.figure("phidot2")
plt.plot(t1,y2,label=r"$\dot{\phi}$")
plt.xlabel("Time")
plt.ylabel("Angular velocity [rad/s]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-phidot-2.pdf")
plt.figure("psidot2")
plt.plot(t1,z2,label=r"$\dot{\psi}$")
plt.xlabel("Time")
plt.ylabel("Angular velocity [rad/s]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-psidot-2.pdf")

plt.figure("theta3")
plt.plot(t3,theta3,label=r"$\theta_3$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-theta-3.pdf")
plt.figure("phi3")
plt.plot(t3,phi3,label="$\phi$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-phi-3.pdf")
plt.figure("psi3")
plt.plot(data3[0,0:340],data3[3,0:340],'-',label="$\psi$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-psi-3.pdf")
plt.figure("constants of motion3")
plt.plot(t3,(E3-E3[0])/E3[0],label="Total Energy")
plt.plot(t3,(C13-C13[0])/C13[0],'--',label="Eq. (18)")
plt.plot(t3,(C23-C23[0])/C23[0],'-.',label="Eq. (20)")
plt.xlabel("Time")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-const-3.pdf")
plt.figure("thetadot3")
plt.plot(t1,x3,label=r"$\dot{\theta}$")
plt.xlabel("Time")
plt.ylabel("Angular velocity [rad/s]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-thetadot-3.pdf")
plt.figure("phidot3")
plt.plot(t1,y3,label=r"$\dot{\phi}$")
plt.xlabel("Time")
plt.ylabel("Angular velocity [rad/s]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-phidot-3.pdf")
plt.figure("psidot3")
plt.plot(t1,z3,label=r"$\dot{\psi}$")
plt.xlabel("Time")
plt.ylabel("Angular velocity [rad/s]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-psidot-3.pdf")

plt.figure("theta4")
plt.plot(t4,theta4,label=r"$\theta_4$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-theta-4.pdf")
plt.figure("phi4")
plt.plot(t4,phi4,label="$\phi$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-phi-4.pdf")
plt.figure("psi4")
plt.plot(data4[0,0:340],data4[3,0:340],'-',label="$\psi$")
plt.xlabel("Time")
plt.ylabel("Angle [rad]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-psi-4.pdf")
plt.figure("constants of motion4")
plt.plot(t4,(E4-E4[0])/E4[0],label="Total Energy")
plt.plot(t4,(C14-C14[0])/C14[0],'--',label="Eq. (18)")
plt.plot(t4,(C24-C24[0])/C24[0],'-.',label="Eq. (20)")
plt.xlabel("Time")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-const-4.pdf")
plt.figure("thetadot4")
plt.plot(t1,x4,label=r"$\dot{\theta}$")
plt.xlabel("Time")
plt.ylabel("Angular velocity [rad/s]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-thetadot-4.pdf")
plt.figure("phidot4")
plt.plot(t1,y4,label=r"$\dot{\phi}$")
plt.xlabel("Time")
plt.ylabel("Angular velocity [rad/s]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-phidot-4.pdf")
plt.figure("psidot4")
plt.plot(t1,z4,label=r"$\dot{\psi}$")
plt.xlabel("Time")
plt.ylabel("Angular velocity [rad/s]")
plt.legend()
if savePlots:
    plt.savefig("../figs/lag-psidot-4.pdf")

if showPlots:
    plt.show()


t,theta,phi,psi,x,y,z,K,V,E,C1,C2= np.genfromtxt("../data/lagrangeback.dat",unpack=True)

#0.1745329252, 0, 0, 0, 0, 414.69023028
print(t[-1])
print(0.1745329252-theta[-1])
print(phi[-1])
print(psi[-1])
print(x[-1])
print(y[-1])
print(414.69023028-z[-1])
