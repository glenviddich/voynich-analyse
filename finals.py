exec(open('seg.py').read().split("N=150000")[0])
import math
W=[w for l in VL for w in l]
def ctx_vec(cond):
    v=C.defaultdict(C.Counter)
    for w in W:
        for i,c in enumerate(w):
            if cond(i,len(w)): v[c][w[i-1] if i>0 else '#']+=1
    return v
fin=ctx_vec(lambda i,n:i==n-1 and i>0)      # Zeichen am Wortende: was steht davor?
med=ctx_vec(lambda i,n:0<i<n-1)             # Zeichen in der Wortmitte: was steht davor?
def cos(a,b):
    ks=set(a)|set(b); return sum(a[k]*b[k] for k in ks)/math.sqrt(sum(x*x for x in a.values())*sum(x*x for x in b.values()))
tot=C.Counter(c for w in W for c in w)
def share(c,pos):
    n=sum(1 for w in W for i,x in enumerate(w) if x==c and ((i==len(w)-1) if pos=='f' else (0<i<len(w)-1)))
    return n/tot[c]
finals=[c for c in tot if tot[c]>800 and share(c,'f')>.5]
medials=[c for c in tot if tot[c]>800 and share(c,'m')>.5]
print('Endzeichen (>50% am Wortende):',{c:round(share(c,'f'),2) for c in finals})
print('Mittelzeichen (>50% in der Mitte):',{c:round(share(c,'m'),2) for c in medials})
print('\nWelches Mittelzeichen hat den ähnlichsten Vorgänger-Kontext wie das Endzeichen?')
for f in finals:
    sims=sorted(((cos(fin[f],med[m]),m) for m in medials if m!=f),reverse=True)
    print(f'   Ende {f}: '+', '.join(f'{m} {s:.2f}' for s,m in sims[:4]))
# Kontrolle: dieselbe Analyse bei Latein/Deutsch mit bekannten Fällen
for name,fn in [('Latein','la.txt'),('Deutsch','de.txt')]:
    LW=[w for l in clean(fn)[:20000] for w in l]
    def cv(cond):
        v=C.defaultdict(C.Counter)
        for w in LW:
            for i,c in enumerate(w):
                if cond(i,len(w)): v[c][w[i-1] if i>0 else '#']+=1
        return v
    F=cv(lambda i,n:i==n-1 and i>0); M=cv(lambda i,n:0<i<n-1)
    print(f'\nKontrolle {name}: Ende s/m/t/e vs Mitte (Top-Treffer) –',
          '; '.join(f'{f}: '+', '.join(f'{m} {s:.2f}' for s,m in sorted(((cos(F[f],M[m]),m) for m in M if sum(M[m].values())>500),reverse=True)[:3]) for f in 'smte'))
