exec(open('plantwords2.py').read().split("print(f'Kräuterseiten")[0])
labs=[]
for ln in open('ZL.txt',encoding='latin-1'):
    m=re.match(r'<(f\w+)\.(\d+),.(L[a-z0-9])>\s+(.*)',ln)
    if m:
        t=re.sub(r'<[^>]*>','',m.group(4)); t=re.sub(r'\[([^:\]]*):[^\]]*\]',r'\1',t).replace('{','').replace('}','').replace("'",'')
        for w in re.split(r'[.,\s]+',t):
            if w and re.fullmatch(r'[a-z]+',w): labs.append((m.group(1),m.group(3),w))
herbpages={p:set(w) for p,w in pagew.items() if sec[p]=='H'}
allpages={p:set(w) for p,w in pagew.items()}
freq=C.Counter(w for p in pagew.values() for w in p)
lf=[(p,w) for p,t,w in labs if t=='Lf']
print(f'Pharma-Beschriftungen (Lf): {len(lf)}, davon verschieden: {len(set(w for _,w in lf))}')
print('Anfangsbuchstaben der Beschriftungen:',C.Counter(w[0] for _,w in lf).most_common(5),' | Fließtext:',C.Counter(w[0] for p in pagew.values() for w in p).most_common(5))
fam_lab=sum(norm(w)=='chol' for _,w in lf); print(f'chol-Familie unter den Beschriftungen: {fam_lab}  (im Fließtext {sum(norm(w)=="chol" for p in pagew.values() for w in p)} mal)')
hits=[]
for p,w in lf:
    hp=[q for q,s in herbpages.items() if w in s]
    ap=[q for q,s in allpages.items() if w in s and q!=p]
    hits.append((p,w,hp,ap))
none=sum(1 for h in hits if not h[3]); rare=[h for h in hits if 1<=len(h[2])<=2 and len(h[3])<=3]
print(f'Beschriftungen, die NIRGENDS sonst im Fließtext stehen: {none} ({none/len(lf)*100:.0f}%)')
print(f'Beschriftungen, die auf genau 1–2 Kräuterseiten (und höchstens 3 Seiten insgesamt) stehen: {len(rare)}')
for p,w,hp,ap in rare[:25]: print(f'   {p:6s} „{w}“ -> Kräuterseite(n) {", ".join(hp)}   (insgesamt auf {len(ap)} Seiten, Häufigkeit {freq[w]})')
# Kontrolle: zufällige Wörter gleicher Häufigkeit
import random
r=random.Random(0); pool=[w for w in freq if 1<=freq[w]<=6]
ctrl=0
for _ in range(2000):
    w=r.choice(pool); hp=[q for q,s in herbpages.items() if w in s]; ap=[q for q,s in allpages.items() if w in s]
    ctrl+=1<=len(hp)<=2 and len(ap)<=3
print(f'Kontrolle: seltene Zufallswörter mit demselben Muster: {ctrl/2000*100:.0f}%')
