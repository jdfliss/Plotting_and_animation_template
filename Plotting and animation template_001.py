# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 13:27:58 2022

@author: Jordan
"""

#del dir([])

#locals()
#gc.collect()

#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FFMpegWriter as MW
#from matplotlib.animation import PillowWriter as MW
import random as Rdm

plt.rcParams['animation.ffmpeg_path'] = 'C:\\Program Files (x86)\\ffmpeg\\bin\\ffmpeg.exe'
  
#%% 
N=500
x=np.linspace(0, N, num=N+1)
y=np.zeros(N+1)

r=0
for r in range(N+1):
    plt.clf()
    if r==0 :
        r
    else:
        #y[r]=(y[r-1]+Rdm.randint(-5, 5)) #psuedo random walk
        y[r]=(y[r-1]+Rdm.randint(-2, 2))+Rdm.randint(30, 100)/100*6*np.sin(5*r) #psuedo random walk + Sine influence
    r+=1

#Video Setup
metadata = dict(title='Gud Movie', artist='yo mama')
Vid=MW(fps=15,metadata=metadata)


#%% Create sequential plots for animation
step_size=1
plot_limits=max(y),min(y)
plot_limits=np.ceil(abs(plot_limits[abs(max(y))<abs(min(y))]))


p1=plt.figure(300)
r=0
with Vid.saving(p1, "test3.mp4",300):
#anim.save(f, writer=writermp4)
    for r in range(N): #growing function (N+1)
        if r%1==0: #skip frames
            p1=plt.figure(300)
            temp_domain=np.array([np.linspace(0,r,r+1)])
            temp_domain=temp_domain.astype(int)
            x_plotted=x[temp_domain]
            y_plotted=y[temp_domain]
            c_plotted=np.round(abs(y[temp_domain]/plot_limits),decimals=2)
            #plt.xlabel=[]
            #plt.ylabel=[]
            #plt.xticks=[]
            #plt.yticks=[]
            #plt.linestyles=[]
            #plt.linewidths=[]
            #plt.xscale=[]
            #plt.yscale=[]
            #plt.GridSpec()
            
            p1=plt.scatter(x_plotted,y_plotted, s=5, c=c_plotted ,marker='o',)
            p1.axes.set_xlim(0,N)
            p1.axes.set_ylim(-np.ceil(plot_limits/10)*10,np.ceil(plot_limits/10)*10)
            p1.axes.yaxis.set_visible(False)
            p1.axes.xaxis.set_visible(False)
            p1.axes.set_aspect('equal')
            #p1.set_linewidth(0.5)
            #p1.set_=12
    
            #rotating line or smart lines
            if r%2==0 and r>step_size: #skip lines
                #domain=np.linspace(0,[r*pi/16])
                #domain=round(domain[],2)
                a=np.array([5])
                k=10
                #xpos=a*sin(k*r*3.14/100)
                #ypos=a*cos(k*r*3.14/2/100)
                xpos=r
                ypos=y_plotted[0][r]
                #x1=np.linspace(-a*np.cos(k*r*3.14/100),a*np.cos(k*r*3.14/100))+N/2+xpos
                #y1=np.linspace(-a*np.sin(k*r*3.14/100),a*np.sin(k*r*3.14/100))+ypos
                #plt.plot(x1,y1)
                
                OffSet=0.0
                #x2=np.linspace(-a*np.cos(k*(r-OffSet)*3.14/100),a*np.cos(k*(r-OffSet)*3.14/100))+N/2+xpos
                #y2=np.linspace(-a*np.sin(k*(r-OffSet)*3.14/100),a*np.sin(k*(r-OffSet)*3.14/100))+ypos
                #plt.plot(x2,y2)
                
                #step_size=5
                #np.size(np.diff(y_plotted[1]))
                slope=(y_plotted[0][r]-y_plotted[0][r-step_size])/step_size
                slope=-1/(slope)
                for ii in range(1):
                    #xii=np.linspace(-a*np.cos(k*ii/5*(r-OffSet*ii)*3.14/100),a*np.cos(k*(r-OffSet*ii)*3.14/100))+N/2+xpos
                    #yii=np.linspace(-a*np.sin(k*ii/5*(r-OffSet*ii)*3.14/100),a*np.sin(k*(r-OffSet*ii)*3.14/100))+ypos
                    theta=atan(slope)
                    xii=np.linspace(-a*cos(theta),a*cos(theta))+xpos
                    yii=np.linspace(-a*sin(theta),a*sin(theta))+ypos
                    
                    #xii=np.linspace(-a*np.cos(k*ii/5*(r-OffSet*ii)),a*np.cos(k*(r-OffSet*ii)*3.14/100))+xpos
                    #yii=np.linspace(-a*np.sin(k*ii/5*(r-OffSet*ii)),a*np.sin(k*(r-OffSet*ii)*3.14/100))+ypos
                    plt.plot(xii,yii,'k')
        Vid.grab_frame()
        r+=1
    plt.pause(0.001)
    
    
        
        #plt.show()

#%%










#%%

dir(p1)
dir(np)

dir(p1.axes.yaxis.set_visible(False)

plot.axes.get_linewidths()