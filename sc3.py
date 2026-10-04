import sys; SEED=sys.argv[1]
exec(open('common.py').read())
import json
exec(open('selfcite2.py').read().split("def gen(p,seed=0):")[0].split("exec(open('opt.py')")[1].split('\n',1)[1])  # R, mutate
def gen(p,seed=0):
    r=random.Random(seed); out=[]; page=[]
    while len(out)<NW:
        if len(page)>=p['plen'] or not page: page=[[r.choice(V) for _ in range(p['seed'])]]
        prev=page[-1]; Lw=[]
        for j in range(r.randint(7,11)):
            u=r.random()
            if u<p['a'] and j<len(prev): src=prev[min(max(0,j+r.choice([-1,0,0,1])),len(prev)-1)]
            elif u<p['a']+p['fresh']: src=r.choice(V)   # gelegentlich frisches Wort (neues Thema / Startwort)
            else:
                lines=page[-p['K']:]+[Lw] if Lw else page[-p['K']:]
                # Rezenz-Gewichtung
                wts=[]; pool_=[]
                for d,l in enumerate(reversed(lines)):
                    for w in l: pool_.append(w); wts.append(p['dec']**d)
                src=r.choices(pool_,wts)[0]
            w=src
            for _ in range(r.choices(range(5),[p['m0'],1,p['m2'],p['m2']**2,p['m2']**3])[0]):
                w2=mutate(w,r)
                if len(cuva(w2))<=p['Lmax'] and 'eeee' not in w2 and 'iiii' not in w2 and 'cc' not in w2 and 'hh' not in w2 and w2.count('ch')+w2.count('sh')<=2: w=w2
            Lw.append(w)
        page.append(Lw); out+=Lw
    return out[:NW]
def rnd(r): return dict(a=r.uniform(0,.4),fresh=r.uniform(0,.3),K=r.randint(1,30),dec=r.uniform(.5,1),m0=r.uniform(0,1.5),m2=r.uniform(.1,1),Lmax=r.randint(5,8),plen=r.randint(10,40),seed=r.randint(3,15))
def mut(p,r):
    q=dict(p); k=r.choice(list(q))
    if k in('K','Lmax','plen','seed'): q[k]=max(1,q[k]+r.choice([-3,-1,1,3]))
    else: q[k]=min(1.5 if k=='m0' else 1,max(0,q[k]+r.gauss(0,.08)))
    return q
r=random.Random(int(SEED)); best=None
import time; t0=time.time()
for it in range(500):
    p=rnd(r) if it<80 or best is None else mut(best[1],r)
    m=full(gen(p)); l=loss2(m)
    if best is None or l<best[0]: best=(l,p,m)
    if time.time()-t0>1500: break
val=[round(loss2(full(gen(best[1],s))),1) for s in (5,6,7)]
json.dump(dict(loss=best[0],val=val,p=best[1],m={k:v for k,v in best[2].items() if k!='ld'},ex=gen(best[1],5)[300:320]),open(f'sc3_{SEED}.json','w'))
print("SC3",SEED,round(best[0],1),val,best[1]); print('  ',show(best[2]))
