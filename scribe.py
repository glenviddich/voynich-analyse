import re, random, collections as C
from rapidfuzz.distance import Levenshtein as Lv
exec(open('qtest.py').read().split("isq=lambda")[0])
def cuva(w):
    for a,b in [('cth','T'),('ckh','K'),('cph','P'),('cfh','F'),('ch','C'),('sh','S'),('iin','M'),('in','N')]: w=w.replace(a,b)
    return w
byH=C.defaultdict(list); bySec=C.defaultdict(list)
for l in L:
    byH[(l[3],l[2])]+=[cuva(w) for w in l[5]]
def twins(ws,K=10,n=None):
    a=t=0
    for i in range(K,len(ws)):
        if len(ws[i])<3: continue
        t+=1; a+=any(len(p)>=3 and Lv.distance(ws[i],p)==1 for p in ws[i-K:i])
    return a/t*100
r=random.Random(0)
print('Schreiber | Abschnitt | Wörter | Fast-Zwilling-Überschuss (echt − gemischt) | Bootstrap-Spanne')
rows=[]
for (h,s),ws in sorted(byH.items()):
    if len(ws)<1500: continue
    sh=ws[:]; r.shuffle(sh); obs=twins(ws)-twins(sh)
    bs=[]
    for _ in range(30):
        i=r.randrange(0,len(ws)-1200); seg=ws[i:i+1200]; sg=seg[:]; r.shuffle(sg); bs.append(twins(seg)-twins(sg))
    bs.sort(); print(f'   {h}         {s}          {len(ws):5d}   {obs:+5.1f}   [{bs[2]:+.1f} … {bs[27]:+.1f}]')
