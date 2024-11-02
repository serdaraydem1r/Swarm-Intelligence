import numpy as np
np.random.seed(0)
def obj(X):
    return (X[0]-5)**2+(X[1]-2)**2
Run = 30
BestF = np.empty([Run,1])
for run in range(Run):
    np.random.seed(run)
    N = 20
    T = 100
    ub = 10
    lb = -10
    D = 2
    X = lb+np.random.rand(N,D)*(ub-lb)
    F = np.empty([N,1])
    for i in range(N):
        F[i] = obj(X[i]) # amaç değerlerini hesaplıyoruz
    idx = np.argsort(F,0)

    X_alpha =X[idx[0]].reshape(-1)
    F_alpha = F[idx[0]].reshape(-1)

    X_beta = X[idx[1]].reshape(-1)
    F_beta = F[idx[1]].reshape(-1)

    X_delta = X[idx[2]].reshape(-1)
    F_delta = F[idx[2]].reshape(-1)

    for t in range(T):
        a = 2-2*(t/T)
        for i in range(N):
            for j in range(D):
                r1 = np.random.rand()
                A1= 2*a*r1-a
                r2 = np.random.rand()
                C1 =2*r2

                # alpha kurt
                D_alpha = abs(C1*X_alpha[j]-X[i][j])
                P1 = X_alpha[j]-A1*D_alpha

                # beta kurt
                r1 = np.random.rand()
                A2= 2*a*r1-a
                r2 = np.random.rand()
                C2 = 2*r2
                D_beta = abs(C2*X_beta[j]-X[i][j])
                P2 = X_beta[j]-A2*D_beta

                # delta kurt
                r1 = np.random.rand()
                A3= 2*a*r1-a
                r2 = np.random.rand()
                C3 = 2*r2
                D_delta = abs(C3*X_delta[j]-X[i][j])
                P3 = X_delta[j]-A3*D_delta
                X[i][j] = (P1+P2+P3)/3
        for i in range(N):
            X[i] = np.clip(X[i],lb,ub)
            F[i] = obj(X[i])
            if F[i] < F_alpha:
                X_alpha = X[i].copy()
                F_alpha = F[i].copy()
            if F[i] > F_alpha and F[i]<F_beta:
                X_beta = X[i].copy()
                F_beta = F[i].copy()
            if F[i] > F_beta and F[i]<F_delta:
                X_delta = X[i].copy()
                F_delta = F[i].copy()
    BestF[run]=F_alpha.copy()
    print(X_alpha,F_alpha)
ort = np.mean(BestF)
std = np.std(BestF,ddof=1)

print(ort,std)