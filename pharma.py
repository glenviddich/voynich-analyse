import re, random, math, collections as C
exec(open('qtest.py').read().split("isq=lambda")[0])
def norm(w):
    w=re.sub(r'^q','',w); return w.replace('sh','ch').replace('cth','ckh').replace('t','k').replace('ee','e').replace('r','l')
R='f88r f99r f99v f102v1 f102v2'.split(); Lf='f100r f100v f101r f101v f102r1 f102r2'.split()
para=C.defaultdict(list)
for l in L:
    if l[0] in R+Lf: para[l[0]]+=l[5]
labs=C.defaultdict(list)
for ln in open('ZL.txt',encoding='latin-1'):
    m=re.match(r'<(f\w+)\.\d+,.L[a-z0-9]>\s+(.*)',ln)
    if m and m.group(1) in R+Lf:
        t=re.sub(r'<[^>]*>','',m.group(2)); t=re.sub(r'\[([^:\]]*):[^\]]*\]',r'\1',t).replace('{','').replace('}','').replace("'",'')
        labs[m.group(1)]+=[w for w in re.split(r'[.,\s]+',t) if w and re.fullmatch(r'[a-z]+',w)]
def rate(pages,src,fam): 
    ws=[w for p in pages for w in src[p]]; return sum(norm(w)==fam for w in ws)/len(ws)*100, len(ws)
print('Absatztext:  Wurzelseiten %d Wörter, Blattseiten %d Wörter'%(rate(R,para,'chol')[1],rate(Lf,para,'chol')[1]))
print('Beschriftg.: Wurzelseiten %d Wörter, Blattseiten %d Wörter'%(rate(R,labs,'chol')[1],rate(Lf,labs,'chol')[1]))
allw=[w for p in R+Lf for w in para[p]]
fams=[f for f,c in C.Counter(norm(w) for w in allw).items() if c>=12]
r=random.Random(0); pages=R+Lf; lab=[1]*len(R)+[0]*len(Lf)
def diff(f,lab_):
    a=[sum(norm(w)==f for w in para[p])/len(para[p])*100 for p,y in zip(pages,lab_) if y]
    b=[sum(norm(w)==f for w in para[p])/len(para[p])*100 for p,y in zip(pages,lab_) if not y]
    return sum(a)/len(a)-sum(b)/len(b)
print(f'\nAbsatztext, {len(fams)} Familien, Rate pro 100 Wörter (Wurzel minus Blatt), p aus Seiten-Permutation:')
obs={f:diff(f,lab) for f in fams}
null=[]
for _ in range(2000):
    pl=lab[:]; r.shuffle(pl); null.append({f:diff(f,pl) for f in fams})
mx=sorted(max(abs(v) for v in n.values()) for n in null)
for f,v in sorted(obs.items(),key=lambda x:-abs(x[1]))[:8]:
    p1=sum(abs(n[f])>=abs(v) for n in null)/2000; pc=sum(m>=abs(v) for m in mx)/2000
    print(f'   {f:8s} {v:+6.2f}   Einzel-p {p1:.3f}   korrigiert p {pc:.2f}')
v=obs.get('chol',0); print(f'\nchol-Familie: Wurzelseiten {rate(R,para,"chol")[0]:.2f} vs Blattseiten {rate(Lf,para,"chol")[0]:.2f} pro 100 Wörter | Einzel-p {sum(abs(n["chol"])>=abs(v) for n in null)/2000:.3f}')
print(f'chol in Beschriftungen: Wurzel {rate(R,labs,"chol")[0]:.1f}% vs Blatt {rate(Lf,labs,"chol")[0]:.1f}%')
# Vorhersage aus dem Kräuterteil: chol-Rate dort 4,2 (Wurzel) vs 6,8 (andere)
