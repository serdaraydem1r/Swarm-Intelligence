#%%
from glob import iglob

import numpy as np
np.random.seed(12)
def obj(X):
    top = (1/4000)*sum(X**2) + 1
    c=1
    for j in range(len(X)):
        c=c*np.cos(X[j]/np.sqrt(j+1))
    return (top-c)
#%% başlangıç değerleri
N = 50
Dim = 30
ub = 600
lb = -600
C = 0.1
T = 200
t = 0
R = lb+(ub-lb)*np.random.rand(N,Dim) # popülasyon oluşturma
fit = np.empty(N)
fitbest = np.inf
temp = R.copy()
Rr = R.copy()
#%%
while(t<T):
    for i in range(N): # limit kontrolü
        R[i] = np.clip(R[i],lb,ub)
        fit[i]=obj(R[i])
        if fit[i] <fitbest:
            fitbest=fit[i].copy()
            Rbest = R[i].copy()
    if t == 0:
        Rpre = R.copy()
    else :
        Rpre= temp.copy()
        temp = R.copy()
    for i in range(N):
         Ratt=R[i]+(R[i]-Rpre[i])*np.random.randn()
         fit_att = obj(Ratt)
         if fit[i]<fit_att:
             H = np.random.randint(0,2)
             if H == 0:
                 D=abs(Rbest-R[i])
                 a = -(1+t/T)
                 alpha = np.random.rand()*(a-1)+1
                 R[i] = D*np.exp(a)*np.cos(2*np.pi*alpha)+R[i]
             else:
                Rrand = R[np.random.randint(0,N)].copy()
                R[i] = Rbest-(np.random.rand()*((Rbest+Rrand)/2)-Rrand)
         else:
            V = 2*(1-t/T)
            B = 2*V*np.random.rand()-V
            A = B*(R[i]-C*Rbest)
            R[i]=R[i]+A
    t = t+1
print(fitbest)




