import numpy as np
from numpy.ma.core import argsort


def obj(X): # amaç fonksiyonu
    return sum(X**2)
N = 20 # ajan sayısı
T = 100 # iterasyon sayısı
lb = -5
ub = 5
D = 2
X = np.random.rand(N,D)*(ub-lb)+lb
t = 0
fit = np.empty(N)
fval=[]
fitbest=np.inf

while (t<T):
    for i in range(N):
        X[i] = np.clip(X[i], lb, ub)
        fit[i] = obj(X[i])
        if fit[i]<fitbest:
            fitbest = fit[i].copy()
            F = X[i].copy()
    c1 = 2*np.exp(-(4*t/T)**2)

    for i in range(N):
        for j in range(D):
            if i==0:
                c3=np.random.rand()
                c2=np.random.rand()
                if c3 >=.5:
                   X[0][j] = F[j]+c1*(c2*(ub-lb)+lb)
                else:
                    X[0][j] = F[j]-c1*(c2*(ub-lb)+lb)
            else:
                X[i][j] = (X[i][j]+X[i-1][j])/2

    t=t+1
    fval.append(fitbest)

print(fitbest,F)