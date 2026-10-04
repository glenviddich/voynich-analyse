import re, math, collections as C, unicodedata
exec(open('tests.py').read().split('vw=[cuva')[0])
VE=[w for _,w in W]  # EVA roh: i = Minimstrich
def clean(fn):
    t=open(fn,encoding='utf-8',errors='ignore').read(); t=t[len(t)//10:len(t)*9//10].lower().replace('ß','ss')
    t=unicodedata.normalize('NFKD',t); t=''.join(c for c in t if not unicodedata.combining(c)); return re.findall(r'[a-z]+',t)
la=clean('la.txt')[:len(VE)]; de=clean('de.txt')[:len(VE)]
def stats(ws):
    s='_'.join(ws); c1=C.Counter(s); c2=C.Counter(zip(s,s[1:])); n=len(s)
    H1=-sum(v/n*math.log2(v/n) for v in c1.values()); H2=-sum(v/(n-1)*math.log2(v/(n-1)) for v in c2.values())-H1
    pos=C.defaultdict(lambda:[0,0,0])
    for w in ws:
        for i,ch in enumerate(w): pos[ch][0 if i==0 else (2 if i==len(w)-1 else 1)]+=1
    pur=sum(max(p)/sum(p) for p in sorted(pos.values(),key=sum,reverse=True)[:10])*10
    N=len(ws); typ=len(set(ws))/N*100; rep=sum(a==b for a,b in zip(ws,ws[1:]))/N*1000
    ii=sum(len(m) for w in ws for m in re.findall(r'i{2,}',w))/n*100
    return f"Zeichen {len(c1):2d} | h1 {H1:.2f} | h2 {H2:.2f} | Wortl. {sum(map(len,ws))/N:.1f} | Positionstreue {pur:.0f}% | Typen {typ:.0f}% | Doppelw. {rep:.1f}‰ | i-Ketten {ii:.1f}%"
def gothic(w, level):
    w=w.replace('j','i').replace('v','u').replace('w','uu').replace('y','i')
    w=w.replace('m','iii').replace('n','ii').replace('u','ii')            # Minimen
    if level>=2:
        for a,b in [('e','c'),('t','c'),('f','l'),('s','l'),('b','l'),('h','l'),('k','l'),('r','2'),('x','2'),('z','2')]: w=w.replace(a,b)   # Formenverschmelzung
    if level>=3:
        w=re.sub(r'(us|con|com)$','9',w); w=re.sub(r'^(con|com|ciii|cii)','9',w); w=w.replace('o','a') if False else w  # Kürzel
    return w
print('VOYNICH (EVA, i = Strich)  ', stats(VE))
print('Latein                     ', stats(la))
print('Latein Minimen             ', stats([gothic(w,1) for w in la]))
print('Latein Minimen+Formen      ', stats([gothic(w,2) for w in la]))
print('Latein Minimen+Formen+Kürzel', stats([gothic(w,3) for w in la]))
print('Deutsch Minimen+Formen     ', stats([gothic(w,2) for w in de]))
print('\nBeispiel Latein „gotisch gesehen“:', ' '.join(gothic(w,2) for w in la[400:412]))
print('Original:                         ', ' '.join(la[400:412]))
print('Voynich:                          ', ' '.join(VE[400:412]))

import random
def gap(ws):
    s='_'.join(ws); c1=C.Counter(s); c2=C.Counter(zip(s,s[1:])); n=len(s)
    H1=-sum(v/n*math.log2(v/n) for v in c1.values()); H2=-sum(v/(n-1)*math.log2(v/(n-1)) for v in c2.values())-H1
    return H1,H2
print('\nh1 = Vielfalt der Zeichen, h2 = Unvorhersagbarkeit des nächsten Zeichens, Differenz = wie stark die Reihenfolge festgelegt ist')
G='abcdefghijklmnopqrstuvwxyz'
for name,ws in [('Voynich',VE),('Latein',la),('Latein Minimen+Formen',[gothic(w,2) for w in la])]:
    a,b=gap(ws); print(f'   {name:34s} h1 {a:.2f}  h2 {b:.2f}  Differenz {a-b:.2f}')
for k in (1,2,3):
    r=random.Random(k); tab={c:''.join(r.choice(G) for _ in range(r.choice([1,2,2,3]))) for c in G}
    lw=[''.join(tab[c] for c in w) for w in la]; a,b=gap(lw)
    print(f'   Latein Mehrzeichen-Leet (Variante {k})   h1 {a:.2f}  h2 {b:.2f}  Differenz {a-b:.2f}  Wortl. {sum(map(len,lw))/len(lw):.1f}')
