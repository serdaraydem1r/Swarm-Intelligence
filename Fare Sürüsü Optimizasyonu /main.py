import numpy as np
def obj(X): # amaç fonksiyonu
    return sum(X**2)
N = 30 # ajan sayısı
T = 100  # iterasyon sayısı
lb = -5
ub = 5
D = 2
P = np.random.rand(N,D)*(ub-lb)+lb
t = 0
fit = np.empty(N)
fval=[]
fitbest=np.inf

for t in range(T):
    for i in range(N):
        P[i]=np.clip(P[i],lb,ub)
        fit[i] = obj(P[i])
        if fit[i]<fitbest:
            fitbest=fit[i].copy()
            Pr =P[i].copy()
    R = 4*np.random.rand()+1
    A = R-t*R/T
    for i in range(N):
        for j in range(D):
            c = 2 * np.random.rand()
            Pd = A*P[i][j]+c*(Pr[j]-P[i][j])
            P[i][j] = Pr[j]-Pd
    fval.append(fitbest)
print(fitbest,Pr)
