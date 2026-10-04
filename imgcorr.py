import re, math, random, collections as C
exec(open('qtest.py').read().split("isq=lambda")[0])
def norm(w):
    w=re.sub(r'^q','',w); return w.replace('sh','ch').replace('cth','ckh').replace('t','k').replace('ee','e').replace('r','l')
F={l.split()[0]:list(map(int,l.split()[1:])) for l in open('feats.txt')}
pagew=C.defaultdict(list)
for l in L: pagew[l[0]]+=l[5]
pages=[p for p in F if p in pagew]
print(f'{len(pages)} Seiten | Wurzel betont {sum(F[p][0] for p in pages)} | Blätter groß {sum(F[p][1] for p in pages)} | Blüte auffällig {sum(F[p][2] for p in pages)}')
fam={p:C.Counter(norm(w) for w in pagew[p]) for p in pages}
nw={p:len(pagew[p]) for p in pages}
cnt=C.Counter(f for p in pages for f in fam[p])
cands=[f for f in cnt if 15<=sum(1 for p in pages if fam[p][f])<=len(pages)-10]
print('getestete Wortfamilien:',len(cands))
def score(f,k,lab):
    # Differenz der Rate (pro 100 Wörter) zwischen Seiten mit/ohne Merkmal
    a=[fam[p][f]/nw[p]*100 for p,y in zip(pages,lab) if y]; b=[fam[p][f]/nw[p]*100 for p,y in zip(pages,lab) if not y]
    return sum(a)/len(a)-sum(b)/len(b)
names=['Wurzel betont','Blätter groß','Blüte auffällig']
r=random.Random(0)
for k in range(3):
    lab=[F[p][k] for p in pages]
    obs={f:score(f,k,lab) for f in cands}
    # Permutation: Maximum |Effekt| über alle Familien unter Zufall (familienweise Fehlerkontrolle)
    mx=[]
    for _ in range(300):
        pl=lab[:]; r.shuffle(pl); mx.append(max(abs(score(f,k,pl)) for f in cands))
    mx.sort(); thr=mx[int(.95*len(mx))]
    top=sorted(obs.items(),key=lambda x:-abs(x[1]))[:6]
    print(f'\n{names[k]}: 95%-Schwelle unter Zufall (max. über alle Familien) = {thr:.2f} pro 100 Wörter')
    for f,v in top:
        p_=sum(m>=abs(v) for m in mx)/len(mx)
        print(f'   {f:10s} {v:+.2f} pro 100 Wörter   korrigiertes p≈{p_:.2f}')
    v=obs.get('chol'); print(f'   chol-Familie: {v:+.2f} (unkorr. Einzeltest folgt)')
    # Einzeltest chol
    if 'chol' in cands:
        null=[]
        for _ in range(2000):
            pl=lab[:]; r.shuffle(pl); null.append(score('chol',k,pl))
        print(f'   chol Einzeltest p≈{sum(abs(x)>=abs(v) for x in null)/2000:.3f}')
