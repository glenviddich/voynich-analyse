import re, random, collections as C, unicodedata
from rapidfuzz.distance import Levenshtein as Lv
exec(open('tests.py').read().split('vw=[cuva')[0])
# Voynich mit Seite, Zeile, Abschnitt
toks=[]  # (page, lineid, section, lang, word)
for ln in open('ZL.txt',encoding='latin-1'):
    m=re.match(r'<(f\w+)\.(\d+),.(P\w*)>\s+(.*)',ln)
    if not m: continue
    t=re.sub(r'<[^>]*>','',m.group(4)); t=re.sub(r'\[([^:\]]*):[^\]]*\]',r'\1',t)
    t=re.sub(r'@\d+;','?',t).replace('{','').replace('}','').replace("'",'')
    pg=pages.get(m.group(1),{})
    for w in re.split(r'[.,\s]+',t):
        if w and re.fullmatch(r'[a-z]+',w): toks.append((m.group(1),m.group(1)+'.'+m.group(2),pg.get('I','?'),pg.get('L','?'),cuva(w)))
def clean(fn):
    t=open(fn,encoding='utf-8',errors='ignore').read(); t=t[len(t)//10:len(t)*9//10].lower().replace('ß','ss')
    t=unicodedata.normalize('NFKD',t); t=''.join(c for c in t if not unicodedata.combining(c)); return re.findall(r'[a-z]+',t)
r=random.Random(0)
D=[1,2,3,5,8,15,30,60,120,250,500,1000,3000]
def curve(ws, n=40000):
    N=len(ws); res=[]
    for d in D+['zufällig']:
        near=same=0; k=0
        for _ in range(n):
            i=r.randrange(N); j=i-d if d!='zufällig' else r.randrange(N)
            if j<0 or j==i: continue
            a,b=ws[i],ws[j]; k+=1
            if len(a)<3 or len(b)<3: continue
            e=Lv.distance(a,b); near+=(e==1); same+=(e==0)
        res.append((near/k*100,same/k*100))
    return res
V=[t[4] for t in toks]
def shuffle_within(key):
    g=C.defaultdict(list)
    for t in toks: g[key(t)].append(t[4])
    for v in g.values(): r.shuffle(v)
    it={k:iter(v) for k,v in g.items()}; return [next(it[key(t)]) for t in toks]
series={'Voynich echt':V,
 'Voynich gemischt in Abschnitt+Dialekt':shuffle_within(lambda t:(t[2],t[3])),
 'Voynich gemischt innerhalb Seite':shuffle_within(lambda t:t[0])}
la=clean('la.txt')[:len(V)]; de=clean('de.txt')[:len(V)]; cs=clean('cs.txt')[:len(V)]
for n,ws in [('Latein',la),('Deutsch',de),('Tschechisch',cs)]:
    series[n+' echt']=ws; s=ws[:]; r.shuffle(s); series[n+' gemischt']=s
out={k:curve(v) for k,v in series.items()}
print('Fast-gleiche Wortpaare (1 Zeichen Unterschied) in % je Abstand in Wörtern')
print(f"{'':40s}"+''.join(f'{d:>7}' for d in D)+'   zufällig  | Verhältnis nah(1-8)/fern(1000-3000)')
for k,v in out.items():
    near=sum(x for x,_ in v[0:5])/5; far=sum(x for x,_ in v[11:13])/2
    print(f'{k:40s}'+''.join(f'{x:7.2f}' for x,_ in v)+f'   | {near/far:5.2f}')
# Zeile-darüber-Effekt
lines=C.OrderedDict()
for t in toks: lines.setdefault(t[1],[]).append(t[4])
L=list(lines.items()); pos=rnd=k=0
for (id1,a),(id2,b) in zip(L,L[1:]):
    if id1.split('.')[0]!=id2.split('.')[0]: continue
    for j,w in enumerate(b):
        if j<len(a) and len(w)>=3 and len(a[j])>=3:
            k+=1; pos+=Lv.distance(w,a[j])<=1; rnd+=Lv.distance(w,r.choice(a))<=1
print(f'\nZeile darüber, gleiche Position: {pos/k*100:.1f}% fast gleich/identisch  vs. beliebige Position derselben Zeile: {rnd/k*100:.1f}%  (n={k})')
