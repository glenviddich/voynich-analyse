# Nomenklator (Codebuch mit Voynich-artigen Codewörtern) + Funktionswort-Verschmelzung + Abschrift-mit-Variation
exec(open('hybrid2.py').read().split('train=V[:NW]')[0])
exec(open('combo.py').read().split('res=[]')[0].split("exec(open('common.py').read())")[1])
train=V[:NW]; T=ev(train); print('ZIEL   ',sh(T))
cnt=model(train,20,3)
# Codewort-Generator: reiner Bausteinstrom (ohne Kopie) liefert Typen in Zipf-Reihenfolge
gen=gen_h(cnt,3,60000,0.0,20,1,seed=7); gtypes=[w for w,_ in C.Counter(gen).most_common()]
def nomenklator(ws):
    rk=[w for w,_ in C.Counter(ws).most_common()]
    mp=dict(zip(rk,gtypes)); return [mp[w] for w in ws if w in mp]
def copystage(ws,c,K,nmut,seed=1):
    r=random.Random(seed); out=[]
    for w in ws:
        if out and r.random()<c:
            v=r.choice(out[-K:])
            for _ in range(r.choice(range(1,nmut+1))):
                v2=mutate(v,r)
                if len(v2)<=10: v=v2
            out.append(v)
        else: out.append(w)
    return out
for lang in ['Latein-Rezepte','Italienisch','Latein']:
    pt=PT[lang]
    for fuse in (0,1):
        base=[w for w in pt if not (fuse and w in STOP[lang])]
        code=nomenklator(base)
        for c in (0,0.1,0.15,0.2):
            ws=copystage(code,c,20,2)[:NW]; m=ev(ws); print(f'{lang:15s} fuse={fuse} copy={c:.2f}: loss {loss2(m):6.1f} | {sh(m)}')
