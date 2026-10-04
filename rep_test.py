import re,random,collections as C,statistics as S
exec(open('imgcorr.py').read().split('fam={')[0])   # liefert norm(), pagew
feats={}
for ln in open('feats_rep.txt'):
    if ln.startswith('#') or not ln.strip(): continue
    p,a,b,c=ln.split(); feats[p]=(int(a),int(b),int(c))
pages=[p for p in feats if p in pagew]; print('Seiten im Test:',len(pages), [p for p in feats if p not in pagew])
rate={p:sum(norm(w)=='chol' for w in pagew[p])/len(pagew[p])*100 for p in pages}
nw={p:len(pagew[p]) for p in pages}
for k,name in enumerate(['Wurzel_betont','Blaetter_gross','Bluete_auffaellig']):
    lab=[feats[p][k] for p in pages]
    a=[rate[p] for p,y in zip(pages,lab) if y]; b=[rate[p] for p,y in zip(pages,lab) if not y]
    if not a or not b: print(name,'nur eine Klasse'); continue
    obs=S.mean(a)-S.mean(b)
    r=random.Random(0); null=[]
    for _ in range(10000):
        pl=lab[:]; r.shuffle(pl); aa=[rate[p] for p,y in zip(pages,pl) if y]; bb=[rate[p] for p,y in zip(pages,pl) if not y]; null.append(S.mean(aa)-S.mean(bb))
    p1=sum(x<=obs for x in null)/len(null); p2=sum(abs(x)>=abs(obs) for x in null)/len(null)
    print(f'{name}: ja n={len(a)} Rate {S.mean(a):.2f} | nein n={len(b)} Rate {S.mean(b):.2f} | Differenz {obs:+.2f} je 100 Wörter | p einseitig (niedriger) {p1:.3f}, zweiseitig {p2:.3f}')
print('\nSeite  Wurzel  chol-Rate  Wörter')
for p in pages: print(f'{p:6s} {feats[p][0]:5d} {rate[p]:8.2f} {nw[p]:6d}')
# Gewichtet nach Wörtern (gepoolte Rate)
lab=[feats[p][0] for p in pages]
A=sum(sum(norm(w)=='chol' for w in pagew[p]) for p,y in zip(pages,lab) if y)/sum(nw[p] for p,y in zip(pages,lab) if y)*100
B=sum(sum(norm(w)=='chol' for w in pagew[p]) for p,y in zip(pages,lab) if not y)/sum(nw[p] for p,y in zip(pages,lab) if not y)*100
print(f'\ngepoolt: Wurzel ja {A:.2f} / nein {B:.2f} je 100 Wörter')
