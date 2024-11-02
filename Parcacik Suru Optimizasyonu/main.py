import numpy as np
def obj(X):
    return sum(X**2)

# kısıtlar
lb = -5.12
ub = 5.12
D = 2
N=30
c1 = 2
c2 = 2
T = 100
w = .8

X = np.random.rand(N,D)*(ub-lb)+lb # X'ler ub ve lb arasına getirdik.
F = np.empty([N,1],dtype=float)
for i in range(N):
    F[i]=obj(X[i])

v = np.zeros([N,D])
pbest = X.copy()
pbest_obj = F.copy()
gbest = X[np.argmin(F)]
gbest_obj = np.min(F)

for t in range(T):
    r1 = np.random.rand()
    r2 = np.random.rand()
    v = w*v+c1*r1*(pbest-X) + c2*r2*(gbest-X)
    X = X+v
    X=np.clip(X,lb,ub) # sınırları sağlamayan değerler varsa kontrol eder ve düzenler.
    for i in range(N):
        F[i] = obj(X[i])
        if F[i] < pbest_obj[i]:
            pbest_obj[i] = F[i].copy()
            pbest[i] = X[i].copy()
        if F[i] < gbest_obj:
            gbest_obj = F[i].copy()
            gbest = X[i].copy()

print(gbest)
print(gbest_obj)



