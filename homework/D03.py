import numpy as np
#1.正常的談話的聲壓為20000微巴斯卡，請問多少分貝?
#請寫下程式
V1 = 20000
V0 = 20
GdB = 20*np.log10(V1/V0)
print(int(GdB),"分貝")
#2.30分貝的聲壓會是50分貝的幾倍?
#公式移項過後可以得到 V1 = ?
#請寫下程式
GdB30 = (V1/np.log10((V1)))*(30/20+np.log10(V0))
GdB50 = (V1/np.log10(V1))*(50/20+np.log10(V0))
print(GdB30/GdB50,"倍")