#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
#for a radiating element with 6dBi Gain and symmetric (AZ / EL) shape
#Planarphasedarraywith tapering along xz plane (origin = CENTER)
plt.close(1)
fc = 3.6e9;
c = 3*np.exp(8);
lamda = c / fc;
dx = 0.5 * lamda;
dz = 0.5 * lamda;
Teta = np.arange(0, 181,1);
Phi = np.arange(0,181,1);
Nx = 8;
Nz = 8;
Axn = np.ones((Nx,1));
Azn = np.ones((Nz,1));
nx = np.arange(-(Nx-1) / 2,(Nx) / 2,1,dtype = 'float');
nz = np.arange(-(Nz - 1) / 2,(Nz) / 2,1,dtype = 'float');
Teta_vec = np.zeros(len(Teta) * len(Phi));
for i in  range(len(Teta)):
    Teta_vec[len(Phi)*i:len(Phi)*(i+1)]=Teta[i]*np.ones(len(Phi));
Phi_vec=np.tile(Phi,[1,len(Teta)]);
Phi_vec = Phi_vec.T;
Teta_vec=Teta_vec.reshape(len(Teta_vec),1);
print(Teta_vec)
# Antenna gain
AFx = np.zeros((len(Phi_vec),len(nx)));
for ind in range(len(nx)):
   A= (1/np.sqrt(Nx)* Axn[ind]* np.exp(1j* nx[ind] * (2* np.pi / lamda)* dx *(np.sin(Teta_vec*np.pi/180)* np.cos(Phi_vec*np.pi/180))));
   AFx[:, ind] = A.T;
AFx=np.sum(AFx,axis=1);
print(AFx[0:10])
AFz = np.zeros((len(Teta_vec),len(nz)));
print()
for ind in range(len(nz)):
    B = (1/np.sqrt(Nz)* Azn[ind]* np.exp(1j* nz[ind] * (2* np.pi / lamda)* dz *( np.cos(Teta_vec*np.pi/180))));
    AFz[:, ind]=B.T;
AFz=np.sum(AFz,axis=1);
Gain_EL = AFx * AFz;
Gain_EL_matrix=Gain_EL.reshape((len(Phi),len(Teta)))
Gain_EL_matrix_dB=20*(np.log(abs(Gain_EL_matrix.T))/np.log(10));
Gain_EL_matrix_dB[Gain_EL_matrix_dB<-50]= -50
phi,theta =np.meshgrid(Phi,Teta);
fig= plt.figure()
ax1 = plt.axes(projection ='3d')
ax1.plot_surface(phi,theta ,Gain_EL_matrix_dB,rstride=1,cstride=1,cmap='rainbow')
#ax1.view_init(0,0)
plt.xlim(180,0)
plt.xlabel('Azimuth angle [deg]',loc='left')
#y轴文本
plt.ylabel('Elevation angle [deg]',loc = 'center')
#标题
plt.title('Beam Gain [dB]')
plt.show()
Gx=abs(Gain_EL/np.max(abs(Gain_EL))) *np.sin(Teta_vec*np.pi/180)* np.cos(Phi_vec*np.pi/180);
Gy=abs(Gain_EL/np.max(abs(Gain_EL)))*np.sin(Teta_vec*np.pi/180)*np.sin(Phi_vec*np.pi/180);
Gz=abs(Gain_EL/max(abs(Gain_EL)))*np.cos(Teta_vec*np.pi/180);
fig2= plt.figure()
ax2 =plt.axes(projection ='3d')
ax2.scatter(Gx.T,Gy.T,Gz.T,cmap='Blues')
plt.xlabel('y');
plt.xlim(-1 ,1);
plt.ylabel('x');
plt.ylim(-1,1);
plt.show()