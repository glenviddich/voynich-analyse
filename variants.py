exec(open('stream.py').read().split("train=V[:NW]")[0])
exec(open('selfcite2.py').read().split("def gen(p,seed=0):")[0].split("exec(open('opt.py')")[1].split('\n',1)[1])  # R, mutate
vt=[w for w,_ in C.Counter(V[:NW]).most_common()]
def codebook(ws):
    rk=[w for w,_ in C.Counter(ws).most_common()]; r=random.Random(1)
    ext=[r.choice(vt[:300])[:3]+r.choice(vt)[3:] for _ in range(max(0,len(rk)-len(vt)))]
    return dict(zip(rk,vt+ext))
def run(ws, p, nvar, seed=0, rule=False):
    r=random.Random(seed); cb=codebook(ws)
    var={}  # jedes Klartextwort hat eine feste kleine Menge Schreibvarianten
    out=[]
    for w in ws:
        base=cb[w]
        if w not in var:
            vs=[base]
            for _ in range(nvar):
                x=base
                for _ in range(r.choice([1,1,2])): x=mutate(x,r)
                vs.append(x)
            var[w]=vs
        x=r.choice(var[w][1:]) if r.random()<p else base
        if rule and out:   # Anschlussregel: nach -dy/-ey bevorzugt q-, nach -in/-r ohne q
            prev=out[-1]
            if prev.endswith(('dy','ey')) and x.startswith('o') and r.random()<.5: x='q'+x
            if prev.endswith(('in','r','l')) and x.startswith('qo') and r.random()<.5: x=x[1:]
        out.append(x)
    return out
T=ev(V[:NW]); print('ZIEL Voynich                 ',sh(T))
for L in ['Latein','Deutsch','Tschechisch','Latein-Rezepte']:
    ws=PT[L][:NW]
    m=ev(run(ws,0,0)); print(f'{L[:9]:9s} Codebuch ohne Varianten   ',sh(m),'| loss',round(loss2(m),1))
    best=None
    for p in (.3,.5,.7):
        for nv in (1,2,4):
            m=ev(run(ws,p,nv)); l=loss2(m)
            if best is None or l<best[0]: best=(l,p,nv,m)
    print(f'{L[:9]:9s} + Varianten p={best[1]} n={best[2]}    ',sh(best[3]),'| loss',round(best[0],1))
    m=ev(run(ws,best[1],best[2],rule=True)); print(f'{L[:9]:9s} + Varianten + Anschlussregel',sh(m),'| loss',round(loss2(m),1))
