import sys, re, math, random, collections as C, unicodedata
from rapidfuzz.distance import Levenshtein as Lv
sys.argv=['x','Latein']
exec(open('opt.py').read().split("lang=sys.argv[1]")[0])
NW=12000
def loc(ws,n=60000,seed=0):
    r=random.Random(seed); ws=[cuva(w) for w in ws]; N=len(ws); a=[0,0,0]; b=[0,0,0]
    for _ in range(n):
        i=r.randrange(8,N); j=i-r.randint(1,8); k=r.randrange(N)
        for (x,y),acc in (((ws[i],ws[j]),a),((ws[i],ws[k]),b)):
            acc[0]+=1
            if len(x)>=3 and len(y)>=3:
                e=Lv.distance(x,y); acc[1]+=e==1; acc[2]+=e==0
    return (a[1]/max(b[1],1)), (a[2]/max(b[2],1))
def full(ws):
    m=metrics(ws); m['near'],m['iden']=loc(ws); return m
TT=full(V[:NW])
SC2=dict(SC, near=.15, iden=.3)
def loss2(m): return sum(((m[k]-TT[k])/SC2[k])**2 for k in SC2)+(sum(abs(x-y) for x,y in zip(m['ld'],TT['ld']))/.05)**2
def show(m): return ' | '.join(f"{k} {m[k]:.2f}" for k in ['h2','wl','typ','rep','pur','mi','near','iden'])
