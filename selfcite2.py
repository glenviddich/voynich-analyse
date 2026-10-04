import sys; sys.argv=['x','Latein']
exec(open('opt.py').read().split("lang=sys.argv[1]")[0])
R=[('ee','e'),('e','ee'),('k','t'),('t','k'),('ch','sh'),('sh','ch'),('o','a'),('a','o'),('aiin','ain'),('ain','aiin'),('aiin','aiiin'),('dy','y'),('y','dy'),('edy','eedy'),('ol','or'),('or','ol'),('ar','al'),('al','ar'),('d','l'),('l','r'),('r','l'),('k','ckh'),('t','cth'),('ckh','k'),('cth','t'),('ch','che'),('y','ey'),('ey','y'),('dy','ol'),('l','dy')]
def mutate(w,r):
    if r.random()<.35:  # Präfix-Operationen
        ops=[lambda w:'q'+w if w.startswith('o') else w, lambda w:w[1:] if w.startswith('q') and len(w)>2 else w,
             lambda w:'o'+w if not w.startswith(('o','q')) else w, lambda w:w[1:] if w.startswith('o') and len(w)>2 else w,
             lambda w:'ch'+w if len(w)<5 else w, lambda w:w[2:] if w.startswith(('ch','sh')) and len(w)>3 else w]
        return r.choice(ops)(w)
    a=[(x,y) for x,y in R if x in w]
    if not a: return w
    x,y=r.choice(a); idx=[i for i in range(len(w)) if w.startswith(x,i)]; i=r.choice(idx)
    return w[:i]+y+w[i+len(x):]
def gen(p,seed=0):
    r=random.Random(seed); out=[]; lines=[]
    while len(out)<NW:
        if len(lines)%25==0: lines=[[r.choice(V) for _ in range(9)]]  # neue Seite: kleine Startsaat
        prev=lines[-1]; L=[]
        for j in range(r.randint(7,11)):
            if r.random()<p['a'] and j<len(prev): src=prev[min(j+r.choice([-1,0,0,1]),len(prev)-1)]
            elif r.random()<p['b'] and L: src=L[-1]  # Wort direkt davor
            else:
                pool_=[w for l in lines[-p['K']:] for w in l]+L; src=r.choice(pool_)
            w=src
            for _ in range(r.choices(range(5),[p['m0'],1,p['m2'],p['m2']**2,p['m2']**3])[0]):
                w2=mutate(w,r)
                if len(cuva(w2))<=p['Lmax'] and 'eeee' not in w2 and 'iiii' not in w2 and 'cc' not in w2 and 'hh' not in w2 and w2.count('ch')+w2.count('sh')<=2: w=w2
            L.append(w)
        lines.append(L); out+=L
    return out[:NW]
r=random.Random(3); best=None
for it in range(220):
    p=dict(a=r.uniform(0,.8),b=r.uniform(0,.5),K=r.randint(1,6),m0=r.uniform(0,1.5),m2=r.uniform(.1,1),Lmax=r.randint(4,8)) if it<60 or best is None else {k:(max(1,min(8,v+r.choice([-1,1]))) if k in('K','Lmax') else max(0.0,v+r.gauss(0,.1))) for k,v in best[1].items()}
    l=loss(metrics(gen(p)))
    if best is None or l<best[0]: best=(l,p)
val=[round(loss(metrics(gen(best[1],s))),1) for s in (5,6,7)]
m=metrics(gen(best[1],5))
print('SELBSTZITAT loss',round(best[0],1),'val',val,{k:round(v,2) for k,v in best[1].items()})
print('  ',{k:round(v,2) for k,v in m.items() if k!='ld'})
print('   Ziel',{k:round(v,2) for k,v in T.items() if k!='ld'})
print('  ',' '.join(gen(best[1],5)[200:216]))
