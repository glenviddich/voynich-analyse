exec(open('variants.py').read().split("vt=[w for w")[0])
def gen_h(cnt, order, nw, c, K, nmut, seed=0, page=150):
    r=random.Random(seed); out=[]; hist=['_']*order; cur=[]
    while len(out)<nw:
        if not cur and out and r.random()<c:
            pool=out[-K:] if len(out)%page>0 else out[-1:]
            w=r.choice(pool)
            for _ in range(r.choice(range(nmut+1))): 
                w2=mutate(w,r)
                if len(w2)<=10: w=w2
            out.append(w); hist=hist+list(bpe([w],20)[0]) if False else hist+[w[-2:] if w[-2:] in ('dy','ey','in','ol','ar','or','al') else w[-1:], '_']
            continue
        dist=None
        for k in range(order,-1,-1):
            ctx=tuple(hist[-k:]) if k else ()
            if ctx in cnt[k] and sum(cnt[k][ctx].values())>=3: dist=cnt[k][ctx]; break
        t=r.choices(list(dist),list(dist.values()))[0]; hist.append(t)
        if t=='_':
            if cur: out.append(''.join(cur)); cur=[]
        else: cur.append(t)
    return out[:nw]
train=V[:NW]; T=ev(train); print('ZIEL                          ',sh(T))
cnt=model(train,20,3)
res=[]
for c in (.05,.1,.15,.2,.3):
    for K in (5,20,80):
        for nm in (1,2):
            m=ev(gen_h(cnt,3,NW,c,K,nm,seed=1)); res.append((loss2(m),c,K,nm,m))
res.sort(key=lambda x:x[0])
for l,c,K,nm,m in res[:5]: print(f'c={c:.2f} K={K:3d} Änderungen≤{nm}  ',sh(m),'| loss',round(l,1))
l,c,K,nm,m=res[0]
val=[]
for s in (5,6,7):
    mm=ev(gen_h(cnt,3,NW,c,K,nm,seed=s)); val.append(round(loss2(mm),1))
print('Validierung andere Zufallsstarts:',val)
print('Beispiel:',' '.join(gen_h(cnt,3,NW,c,K,nm,seed=5)[500:518]))
