import re, math, random, collections as C, unicodedata, sys, json
exec(open('tests.py').read().split('vw=[cuva')[0])
V=[w for _,w in W]
def clean(fn):
    t=open(fn,encoding='utf-8',errors='ignore').read(); t=t[len(t)//10:len(t)*9//10].lower()
    t=t.replace('ß','ss'); t=unicodedata.normalize('NFKD',t); t=''.join(c for c in t if not unicodedata.combining(c))
    return re.findall(r'[a-z]+',t)
PT={'Latein':clean('la.txt'),'Italienisch':clean('it.txt'),'Deutsch':clean('de.txt'),'Tschechisch':clean('cs.txt'),'Latein-Rezepte':clean('ap.txt')}
NW=12000
def metrics(ws):
    w2=[cuva(w) for w in ws]; s='_'.join(w2)
    c1=C.Counter(s); c2=C.Counter(zip(s,s[1:])); n=len(s)
    H1=-sum(v/n*math.log2(v/n) for v in c1.values()); H2=-sum(v/(n-1)*math.log2(v/(n-1)) for v in c2.values())-H1
    wl=sum(map(len,w2))/len(w2)
    N=len(ws); rep=sum(a==b for a,b in zip(ws,ws[1:]))/N*1000; typ=len(set(ws))/N*100
    pos=C.defaultdict(lambda:[0,0,0])
    for w in w2:
        for i,ch in enumerate(w): pos[ch][0 if i==0 else (2 if i==len(w)-1 else 1)]+=1
    pur=sum(max(p)/sum(p) for p in sorted(pos.values(),key=sum,reverse=True)[:10])*10
    pr=[(w[:2],w[-2:]) for w in ws if len(w)>=4]; M=len(pr)
    a=C.Counter(x for x,_ in pr); b=C.Counter(y for _,y in pr); ab=C.Counter(pr)
    mi=sum(v/M*math.log2(v*M/(a[x]*b[y])) for (x,y),v in ab.items())
    ld=C.Counter(min(len(w),10) for w in w2); ld=[ld[i]/N for i in range(1,11)]
    return dict(h2=H2,wl=wl,typ=typ,rep=rep,pur=pur,mi=mi,ld=ld)
T=metrics(V[:NW]); T_full=metrics(V)
SC=dict(h2=.1,wl=.3,typ=3,rep=1.5,pur=3,mi=.1)
def loss(m): return sum(((m[k]-T[k])/SC[k])**2 for k in SC)+ (sum(abs(x-y) for x,y in zip(m['ld'],T['ld']))/.05)**2
vc=C.Counter(V); pool=list(vc); wts=[vc[w] for w in pool]
def gen(p,pt,seed=0):
    r=random.Random(seed)
    letters=sorted(set(''.join(pt)))
    def frag(w,part):
        k=max(1,min(len(w)-1,round(len(w)*p['f']))); return w[:k] if part=='p' else w[k:]
    tab={}
    for c in letters:
        tab[c]=dict(u=r.choices(pool,wts,k=p['hu']),
                    p=[frag(w,'p') for w in r.choices(pool,wts,k=p['hp'])],
                    s=[frag(w,'s') for w in r.choices(pool,wts,k=p['hs'])])
    def pick(lst): 
        ww=[(i+1)**-p['sk'] for i in range(len(lst))]; return r.choices(lst,ww)[0]
    out=[]
    for word in pt:
        i=0
        while i<len(word) and len(out)<NW:
            last=(i==len(word)-1) if p['wb'] else False
            if r.random()<p['pu'] or last: out.append(pick(tab[word[i]]['u'])); i+=1
            else:
                nx=word[i+1] if i+1<len(word) else None
                if nx is None: out.append(pick(tab[word[i]]['u'])); i+=1
                else: out.append(pick(tab[word[i]]['p'])+pick(tab[nx]['s'])); i+=2
        if len(out)>=NW: break
    return out
def rand_p(r): return dict(hu=r.randint(1,12),hp=r.randint(1,12),hs=r.randint(1,12),pu=r.uniform(.05,.9),sk=r.uniform(0,2.5),f=r.uniform(.25,.75),wb=r.random()<.5)
def mutate(p,r):
    q=dict(p); k=r.choice(list(q))
    if k in('hu','hp','hs'): q[k]=max(1,min(30,q[k]+r.choice([-2,-1,1,2])))
    elif k=='wb': q[k]=not q[k]
    elif k=='pu': q[k]=min(.98,max(.02,q[k]+r.gauss(0,.08)))
    elif k=='sk': q[k]=max(0,q[k]+r.gauss(0,.3))
    else: q[k]=min(.85,max(.15,q[k]+r.gauss(0,.06)))
    return q
lang=sys.argv[1]; pt=PT[lang]; r=random.Random(42)
best=None
for _ in range(40):
    p=rand_p(r); l=loss(metrics(gen(p,pt))); 
    if best is None or l<best[0]: best=(l,p)
for it in range(260):
    q=mutate(best[1],r); l=loss(metrics(gen(q,pt)))
    if l<best[0]: best=(l,q)
# robust: neu bewerten mit 3 anderen Tabellen-Seeds
ls=[loss(metrics(gen(best[1],pt,seed=s))) for s in (11,22,33)]
m=metrics(gen(best[1],pt,seed=11))
json.dump(dict(lang=lang,loss=best[0],val=ls,p=best[1],m={k:v for k,v in m.items() if k!='ld'},T={k:v for k,v in T.items() if k!='ld'},ex=gen(best[1],pt,seed=11)[:14]),open(f'res_{lang}.json','w'))
print(lang,'fertig',round(best[0],2),[round(x,1) for x in ls])
