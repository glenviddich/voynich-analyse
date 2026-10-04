import sys
exec(open('common.py').read())
exec(open('bpe.py').read().split("def ustats")[0].split("exec(open('leet.py')")[1].split('\n',1)[1])  # bpe()
import json
def coupling(ws):
    lines=[ws[i:i+10] for i in range(0,len(ws),10)]
    def mi(p):
        N=len(p); a=C.Counter(x for x,_ in p); b=C.Counter(y for _,y in p); ab=C.Counter(p)
        return sum(v/N*math.log2(v*N/(a[x]*b[y])) for (x,y),v in ab.items())
    real=[(a[-1],b[0]) for l in lines for a,b in zip(l,l[1:])]
    rr=random.Random(0); sh=[]
    for l in lines:
        l=l[:]; rr.shuffle(l); sh+=[(a[-1],b[0]) for a,b in zip(l,l[1:])]
    return mi(real)-mi(sh)
def model(train_words, merges, order):
    seqs=bpe(train_words,merges); toks=[]
    for s in seqs: toks+=s+['_']
    cnt={k:C.defaultdict(C.Counter) for k in range(order+1)}
    for i in range(len(toks)):
        for k in range(order+1):
            if i-k>=0: cnt[k][tuple(toks[i-k:i])][toks[i]]+=1
    return cnt
def generate(cnt, order, nw, lam=0.0, page=150, seed=0, cache_order=1):
    r=random.Random(seed); out=[]; hist=['_']*order; cur=[]
    cache=C.defaultdict(C.Counter)
    while len(out)<nw:
        if len(out)%page==0 and not cur: cache=C.defaultdict(C.Counter)
        dist=None
        for k in range(order,-1,-1):
            ctx=tuple(hist[-k:]) if k else ()
            if ctx in cnt[k] and sum(cnt[k][ctx].values())>=3: dist=cnt[k][ctx]; break
        cctx=tuple(hist[-cache_order:])
        if lam>0 and cache[cctx] and r.random()<lam: dist=cache[cctx]
        t=r.choices(list(dist),list(dist.values()))[0]
        cache[cctx][t]+=1
        hist.append(t)
        if t=='_':
            if cur: out.append(''.join(cur)); cur=[]
        else: cur.append(t)
    return out
def ev(ws):
    m=full(ws); m['koppl']=coupling(ws); return m
def sh(m): return show(m)+f" | koppl {m['koppl']:.3f}"
train=V[:NW]
T=ev(train); print('ZIEL Voynich        ',sh(T),'| loss 0')
la=PT['Latein'][:NW]
TL=ev(la)
res=[]
for order in (1,2,3):
    cnt=model(train,20,order)
    g=generate(cnt,order,NW,seed=1); m=ev(g); print(f'Strom Ordnung {order}      ',sh(m),'| loss',round(loss2(m),1))
cnt=model(train,20,2)
for lam in (0.1,0.2,0.3,0.45,0.6):
    g=generate(cnt,2,NW,lam=lam,seed=1); m=ev(g); res.append((loss2(m),lam,m,g))
    print(f'Ordnung 2 + Seitengedächtnis {lam:.2f}',sh(m),'| loss',round(loss2(m),1))
best=min(res,key=lambda x:x[0]); print('\nBeispiel (bestes Gedächtnis %.2f):'%best[1],' '.join(best[3][300:316]))
print('Echt Voynich:',' '.join(train[300:316]))
print('\n--- Gegenprobe Latein (Buchstabenstrom statt Blöcke) ---')
print('Latein echt          ',sh(TL))
cl=model(la,0,3); g=generate(cl,3,NW,seed=1); m=ev(g); print('Latein Strom Ord.3   ',sh(m))
g=generate(cl,3,NW,lam=0.3,seed=1); m=ev(g); print('Latein Strom+Gedächt.',sh(m))
