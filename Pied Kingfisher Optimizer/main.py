"""
2023 Yılında Çıkmıştır.

Tüneme ve havada asılı kalma stratejisi (keşif) -> Dalış Stratejisi(sömürü) ->Ortakçılık aşaması  yerel optimumdan kaçma

1. Başlangıç popülasyonu rastgele oluştururulur.
        X = lb + rand.(ub-lb)
2. Tüneme ve havada asılı kalma stratejisi
        Xinew = Xi(t)*a*t*(Xj(t)-Xi(t))
            a = 2*randn(1,D)-1
            T parametresi algoritmaa önemli bir yol oynar.

3. Tüneme Stratejisi
    T = (e-e**(t-1/Tmax)**1/BF).cos(CA)
        CA = 2*pi*rand
        BF -> Kanat çırpma faktörü = 8
        CA : İbik Açısı
4. Havada Asılı Kalma Stratejisi
    T = BR*(t/Tmax)**1/BF
    BR = rand*(fitj/fiti)
5. Dalış Stratejisi
    Xinew = Xi(t) + HA*o*a(b-Xbest)
    b = Xi(t)+(o**2)*randn*Xbest
    HA = rand*(fiti/fitbest)
    o = e**(-t/Tmax)**2
6. Ortakçılık Aşaması

            Xm(t)+o*a*|Xi(t)-Xn(t)| rand > (1-PE)
    Xinew =
            Xi(t)                   dd

    PE = PEmax-(PEmax-PEmin)*(t/Tmax)
"""

#%%
import numpy as np
def obj(X):
    return sum(X**2)
N = 20
Tmax = 500
Dim = 2
BF = 8
ub = 10
lb=-10

X = np.random.randn(N,Dim)*(ub-lb)+lb
f = np.empty(N)
for i in range (N):
    f[i] = obj(X[i])
idx = np.argmin(f)
Xbest = X[idx]
fbest = f[idx]

Xnew = np.empty([N,Dim])
fnew = np.empty(N)

t = 1

while (t<Tmax):
    o = np.exp((-t / Tmax) ** 2)
    PE = .5-(.5-0)*(t/Tmax)
    for i in range (N):
        if np.random.rand()<.8:
            alpha = 2 * np.random.randn(Dim) - 1
            j = np.random.randint(0,N)
            while (j==i):
                j = np.random.randint(0,N)
            if np.random.random()>.5:
                CA = 2*np.pi*np.random.rand()
                T = np.exp(1)-np.exp((((t-1)/Tmax)**(1/BF)))*np.cos(CA)
                Xnew[i] = X[i]+alpha*T*(X[j]-X[i])
            else :
                BR = np.random.rand()*(f[j]/f[i])
                T = BR*(t/Tmax)**(1/BF)
                Xnew[i] = X[i] + alpha*T*(X[j]-X[i])

        else:
            alpha = 2 * np.random.randn(Dim) - 1
            HA = np.random.rand()*f[i]/fbest
            b = X[i]+o**2*np.random.rand()*Xbest
            Xnew[i] = X[i]+HA*o*alpha*(b-Xbest)
    for i in range (N):
        Xnew[i] = np.clip(Xnew[i],lb,ub)
        fnew[i] = obj(Xnew[i])
        if fnew[i]<f[i]:
            f[i] = fnew[i].copy()
            X[i] = Xnew[i].copy()
        if f[i]<fbest:
            fbest = f[i].copy()
            Xbest = X[i].copy()

    for i in range (N):
        if np .random.rand()>(1-PE):
            alpha = 2 * np.random.randn(Dim) - 1
            m = np.random.randint(0,N)
            n = np.random.randint(0,N)
            Xnew[i] = X[m]+o*alpha*abs(X[i]-X[n])
        else :
            Xnew[i] = X[i].copy()

    for i in range (N):
        Xnew[i] = np.clip(Xnew[i],lb,ub)
        fnew[i] = obj(Xnew[i])
        if fnew[i]<f[i]:
            f[i] = fnew[i].copy()
            X[i] = Xnew[i].copy()
        if f[i]<fbest:
            fbest = f[i].copy()
            Xbest = X[i].copy()

    t = t+1

print(Xbest,fbest)

