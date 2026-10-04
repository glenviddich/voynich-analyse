exec(open('stream.py').read().split("train=V[:NW]")[0])
import json
ns={}; exec(open('opt.py').read().split("lang=sys.argv[1]")[0].replace("import re, math","import sys, re, math"),ns)
pool,wts=ns['pool'],ns['wts']
def gen_lazy(p, pt, lazy, K=12, seed=0):
    r=random.Random(seed); letters=sorted(set(''.join(pt)))
    def frag(w,part):
        k=max(1,min(len(w)-1,round(len(w)*p['f']))); return w[:k] if part=='p' else w[k:]
    tab={c:dict(u=r.choices(pool,wts,k=p['hu']),p=[frag(w,'p') for w in r.choices(pool,wts,k=p['hp'])],s=[frag(w,'s') for w in r.choices(pool,wts,k=p['hs'])]) for c in letters}
    last={}  # (letter,slot) -> (choice, word_index)
    out=[]; wi=0
    def pick(c,slot):
        key=(c,slot)
        if key in last and wi-last[key][1]<=K and r.random()<lazy: ch=last[key][0]
        else: ch=r.choice(tab[c][slot])
        last[key]=(ch,wi); return ch
    for word in pt:
        i=0
        while i<len(word) and len(out)<NW:
            nx=word[i+1] if i+1<len(word) else None
            if r.random()<p['pu'] or nx is None: out.append(pick(word[i],'u')); i+=1
            else: out.append(pick(word[i],'p')+pick(nx,'s')); i+=2
            wi+=1
        if len(out)>=NW: break
    return out
T=ev(V[:NW]); print('ZIEL                       ',sh(T))
p=json.load(open('res_Latein-Rezepte.json'))['p']
for L in ['Latein','Latein-Rezepte','Deutsch']:
    pt=ns['PT'][L]
    for lazy in (0.0,0.5,0.8,0.95):
        m=ev(gen_lazy(p,pt,lazy)); print(f'{L[:10]:10s} Bequemlichkeit {lazy:.2f}  ',sh(m),'| loss',round(loss2(m),1))
