exec(open('local.py').read().split("out={k:curve")[0])
def band(ws,ds,n=400000):
    N=len(ws); near=same=k=0
    for _ in range(n):
        i=r.randrange(N); d=r.choice(ds) if ds else None; j=i-d if d else r.randrange(N)
        if j<0 or j==i: continue
        k+=1; a,b=ws[i],ws[j]
        if len(a)<3 or len(b)<3: continue
        e=Lv.distance(a,b); near+=e==1; same+=e==0
    return near/k*100, same/k*100
print(f"{'':40s} {'fast gleich nah':>16} {'fern/gemischt':>14} {'Faktor':>7} | {'identisch nah':>14} {'fern':>6} {'Faktor':>7}")
rows=[('Voynich echt','Voynich gemischt in Abschnitt+Dialekt'),('Latein echt','Latein gemischt'),('Deutsch echt','Deutsch gemischt'),('Tschechisch echt','Tschechisch gemischt')]
for a,b in rows:
    n1,s1=band(series[a],[1,2,3,4,5,6,7,8]); n0,s0=band(series[b],None)
    print(f'{a:40s} {n1:16.3f} {n0:14.3f} {n1/n0:7.2f} | {s1:14.3f} {s0:6.3f} {s1/s0:7.2f}')
