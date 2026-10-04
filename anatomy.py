import re, math, random, collections as C
exec(open('qtest.py').read().split("isq=lambda")[0])
def norm(w):
    w=re.sub(r'^q','',w); return w.replace('sh','ch').replace('cth','ckh').replace('t','k').replace('ee','e').replace('r','l')
M={}
for ln in open('ZL.txt',encoding='latin-1'):
    m=re.match(r'<(f\w+)>\s+<!(.*)>',ln)
    if m: M[m.group(1)]=dict(re.findall(r'\$(\w)=(\w+)',m.group(2)))
pagew=C.defaultdict(list)
for l in L: pagew[l[0]]+=l[5]
names={'H':'Kräuter','B':'Badefrauen','S':'Sterne/Rezepte','P':'Pharma','Z':'Tierkreis','A':'Astro','C':'Kosmo','T':'Text'}
def vec(ws): 
    c=C.Counter(norm(w) for w in ws); n=sum(c.values()); return {k:v/n for k,v in c.items()}
def cos(a,b):
    ks=set(a)|set(b); return sum(a.get(k,0)*b.get(k,0) for k in ks)/math.sqrt(sum(v*v for v in a.values())*sum(v*v for v in b.values()))
# Innerhalb Dialekt B: Kräuter-B-Seiten gegen Badefrauen (B) und Sterne (B)
for dia in ['B','A']:
    secw=C.defaultdict(list)
    for p,ws in pagew.items():
        if M[p].get('L')==dia: secw[M[p].get('I')]+=ws
    herbs=[p for p in pagew if M[p].get('I')=='H' and M[p].get('L')==dia and len(pagew[p])>=40]
    others=[s for s in secw if s!='H' and len(secw[s])>=1500]
    print(f'\nDialekt {dia}: {len(herbs)} Kräuterseiten; Vergleichsabschnitte: '+', '.join(f'{names[s]} ({len(secw[s])} W.)' for s in others))
    res={s:[] for s in others}
    for p in herbs:
        v=vec(pagew[p])
        for s in others:
            # Referenz ohne diese Seite (Kräuter sind eh nicht drin)
            res[s].append(cos(v,vec(secw[s])))
    for s in others: print(f'   Ähnlichkeit Kräuterseite -> {names[s]:16s} {sum(res[s])/len(res[s]):.3f}')
    # Kontrolle: Kräuterseite -> andere Kräuterseiten
    hv=[cos(vec(pagew[p]),vec([w for q in herbs if q!=p for w in pagew[q]])) for p in herbs]
    print(f'   Kontrolle Kräuterseite -> übrige Kräuterseiten {sum(hv)/len(hv):.3f}')
# Wurzel-betonte Seiten (Merkmale aus feats.txt): näher an Badefrauen?
F={l.split()[0]:list(map(int,l.split()[1:])) for l in open('feats.txt')}
bio=vec([w for p,ws in pagew.items() if M[p].get('I')=='B' for w in ws]); star=vec([w for p,ws in pagew.items() if M[p].get('I')=='S' for w in ws])
a=[cos(vec(pagew[p]),bio)-cos(vec(pagew[p]),star) for p in F if F[p][0] and p in pagew]
b=[cos(vec(pagew[p]),bio)-cos(vec(pagew[p]),star) for p in F if not F[p][0] and p in pagew]
print(f'\nWurzel-betonte Kräuterseiten: Ähnlichkeit(Badefrauen) − Ähnlichkeit(Sterne) = {sum(a)/len(a):+.3f} (n={len(a)}); andere Kräuterseiten {sum(b)/len(b):+.3f} (n={len(b)})')
