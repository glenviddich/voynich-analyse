exec(open('combo.py').read().split('res=[]')[0])
def copystage(ws,c,seed=1):
    r=random.Random(seed); out=[]
    for w in ws:
        if out and r.random()<c:
            src=r.choice(out[-10:]); 
            # Variante: ein Zeichen am Rand ändern/anfügen/löschen
            op=r.random()
            if op<.4 and len(src)>2: v=src[:-1]+r.choice('ydlrmn')
            elif op<.7: v=src+r.choice('ydl')
            else: v=r.choice('oqd')+src
            out.append(v)
        else: out.append(w)
    return out
print('Ziel Voynich:',show(TT))
for lang,cfg in [('Italienisch',(0,1.0,3,'pos',0.3)),('Italienisch',(1,1.0,3,'pos',0.15)),('Latein-Rezepte',(0,1.0,3,'pos',0.3)),('Latein-Rezepte',(1,1.0,3,'pos',0.15))]:
    base=pipeline(PT[lang],lang,*cfg)
    for c in [0,0.1,0.15,0.25,0.35]:
        ws=copystage(base,c)[:NW]; m=full(ws); print(f'{lang:15s} fuse={cfg[0]} copy={c:.2f}: loss {loss2(m):6.1f} | {show(m)}')
