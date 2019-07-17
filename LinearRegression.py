import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn

f = pd.read_csv("F.csv")
ge = pd.read_csv("GE.csv")
coke = pd.read_csv("COKE.csv")
dji = pd.read_csv("^DJI.csv")

def calculate():
    f_val = list(f.Open)
    ge_val = list(ge.Open)
    coke_val = list(coke.Open)
    dji_val = list(dji.Open)

    fm,fb,fr,fp,fstderr = stats.linregress(f_val,dji_val)
    fn = len(f_val)
    fr2 = fr**2
    fsse = fstderr**2 * (fn - 1)
    fsst = sum((dji_val - np.mean(dji_val))**2)
    fssr = fsst - fsse

    plt.title('F residual plot')
    seaborn.residplot(f_val,dji_val)
    plt.show()

    plt.title('GE residual plot')
    seaborn.residplot(ge_val,dji_val)
    plt.show()

    plt.title('COKE residual plot')
    seaborn.residplot(coke_val,dji_val)
    plt.show()
    
    plt.plot(f_val,dji_val,'ko',markersize=2)
    plt.xlabel('F')
    plt.ylabel('DJIA')
    plt.title('F vs DJI')
    plt.show()

    gm,gb,gr,gp,gstderr = stats.linregress(ge_val,dji_val)
    gn = len(ge_val)
    gr2 = gr**2
    gsse = gstderr**2 * (gn - 1)
    gsst = sum((dji_val - np.mean(dji_val))**2)
    gssr = gsst - gsse
    
    plt.plot(ge_val,dji_val,'ko',markersize=2)
    plt.xlabel('GE')
    plt.ylabel('DJIA')
    plt.title('GE vs DJI')
    plt.show()

    cm,cb,cr,cp,cstderr = stats.linregress(coke_val,dji_val)
    gn = len(coke_val)
    cr2 = cr**2
    csse = cstderr**2 * (gn - 1)
    csst = sum((dji_val - np.mean(dji_val))**2)
    cssr = csst - csse

    plt.plot(coke_val,dji_val,'ko',markersize=2)
    plt.xlabel('F')
    plt.ylabel('DJIA')
    plt.title('COKE vs DJI')
    plt.show()

    print("Ford:")
    print("R\u00b2 = ",fr2)
    print("SSE = ",fsse)
    print("SST = ",fsst)
    print("SSR = ",fssr)
    print("y = ",fm, "x + ",fb)

    print("\nGE:")
    print("R\u00b2 = ",gr2)
    print("SSE = ",gsse)
    print("SST = ",gsst)
    print("SSR = ",gssr)
    print("y = ",gm, "x + ",gb)

    print("\nCoke:")
    print("R\u00b2 = ",cr2)
    print("SSE = ",csse)
    print("SST = ",csst)
    print("SSR = ",cssr)
    print("y = ",cm, "x + ",cb)


calculate()
