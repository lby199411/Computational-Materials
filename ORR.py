import matplotlib.pyplot as plt
import numpy as np
def FEE(s1,s2,s3,s4,s5,s6,s7,s8,s9,u1,u2):
    x=[[0,1.2],[2,3.2],[4,5.2],[6,7.2],[8,9.2]]
    xx=[[1.2,2.0],[3.2,4.0],[5.2,6.0],[7.2,8.0]]
    y1=[[s1-4*u1,s1-4*u1],[s2-3*u1,s2-3*u1],[s3-2*u1,s3-2*u1],[s4-u1,s4-u1],[s5,s5]]
    yy1=[[s1-4*u1,s2-3*u1],[s2-3*u1,s3-2*u1],[s3-2*u1,s4-u1],[s4-u1,s5]]
    y2=[[s6-4*u2,s6-4*u2],[s7-3*u2,s7-3*u2],[s8-2*u2,s8-2*u2],[s9-u2,s9-u2],[s5,s5]]
    yy2=[[s6-4*u2,s7-3*u2],[s7-3*u2,s8-2*u2],[s8-2*u2,s9-u2],[s9-u2,s5]]


    font = {'family' : 'normal',
            'weight' : 'bold',
            'size'   : 40}

    plt.rc('font', **font)
    plt.rcParams['lines.linewidth']=5
    plt.figure(figsize=(18,12))
# main lines
    for i in range(0,len(x)):
        line1,=plt.plot(x[i],y1[i],'b-',label='site1')
        line2,=plt.plot(x[i],y2[i],'r-',label='site2')
        
    plt.legend(handles=[line1,line2])

    plt.text(8.1,s5+0.08, '2H$_2$O')
    plt.text(0.2,s1-4*u1+0.08, 'O$_2$')
    plt.text(2.0,s2-3*u1+0.08, '*OOH')
    plt.text(4.2,s3-2*u1+0.08, '*O')
    plt.text(6.2,s4-u1+0.08, '*OH')
    plt.text(0.1,3.7, 'U=0.68V')
#dash line
    for i in range(0,len(xx)):
        plt.plot(xx[i],yy1[i],'b--',)
        plt.plot(xx[i],yy2[i],'r--',)

#bash line
    xxx=[0,9.2]
    yyy=[0,0]
    plt.plot(xxx,yyy,'k--')
    plt.ylim([-1,4.0])
    plt.xlim([0,9.2])
    plt.tick_params('both')

    plt.gca().xaxis.set_major_locator(plt.NullLocator())

    plt.xlabel('Reaction Coordinates',fontsize=40,fontweight='bold')
    plt.ylabel('Free Energy(eV)',fontsize=40,fontweight='bold')
    plt.savefig('a.png')

    plt.show()

FEE(4.92,3.76,1.59,0.58,0,4.92,3.68,1.54,0.57,0.58,0.58)
