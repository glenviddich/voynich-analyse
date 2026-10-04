exec(open('combo3.py').read().split("for lang in ['Latein-Rezepte'")[0])
# Autokey-Regel an der Wortgrenze: nach -dy wird die q-Variante des Codeworts gewählt
def autokey(ws,p_after_dy=0.5,p_else=0.03,seed=3):
    r=random.Random(seed); out=[]
    for w in ws:
        base=w[1:] if w.startswith('q') else w
        prev=out[-1] if out else ''
        p=p_after_dy if prev.endswith('dy') else p_else
        if base.startswith('o') and r.random()<p: out.append('q'+base)
        else: out.append(base)
    return out
print('Voynich-Ziel koppl', round(T['koppl'],3))
for lang in ['Latein-Rezepte','Italienisch']:
    pt=PT[lang]; base=[w for w in pt if w not in STOP[lang]]; code=nomenklator(base)
    for pdy in (0.0,0.5,0.8):
        for c in (0.15,0.2,0.25):
            ws=copystage(autokey(code,pdy),c,20,2)[:NW]; m=ev(ws); print(f'{lang:15s} q-nach-dy={pdy:.1f} copy={c:.2f}: loss {loss2(m):6.1f} | {sh(m)}')
