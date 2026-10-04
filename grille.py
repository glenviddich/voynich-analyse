import sys; SEED=int(sys.argv[1])
exec(open('common.py').read())
import json
# Bausteine aus Voynich: Präfix | Mitte | Suffix (grobe Zerlegung)
SUF=sorted(['aiiin','aiin','ain','iin','in','eedy','edy','dy','eey','ey','y','ol','or','al','ar','am','an','r','l','s','m','o'],key=len,reverse=True)
PRE=sorted(['qok','qot','qop','qof','ok','ot','op','of','qo','o','ch','sh','d','s','y','l','q','k','t','p','f','cth','ckh','cph','cfh','a'],key=len,reverse=True)
def split3(w):
    p=next((x for x in PRE if w.startswith(x) and len(w)>len(x)),'')
    rest=w[len(p):]; s=next((x for x in SUF if rest.endswith(x)),'')
    m=rest[:len(rest)-len(s)] if s else rest
    return p,m,s
cp=C.Counter();cm=C.Counter();cs=C.Counter()
for w in V: p,m,s=split3(w); cp[p]+=1; cm[m]+=1; cs[s]+=1
def gen(q,seed=0):
    r=random.Random(seed)
    R=q['R']; T=[(r.choices(list(cp),list(cp.values()))[0],r.choices(list(cm),list(cm.values()))[0],r.choices(list(cs),list(cs.values()))[0]) for _ in range(R)]
    out=[]; pos=r.randrange(R); off=[0,r.randint(1,q['spread']),r.randint(1,q['spread'])]
    while len(out)<NW:
        if r.random()<q['jump']: pos=r.randrange(R); off=[0,r.randint(1,q['spread']),r.randint(1,q['spread'])]
        else: pos=(pos+r.choice(range(-q['step'],q['step']+1)))%R
        w=''.join(T[(pos+off[k])%R][k] for k in range(3))
        if r.random()<q['skip']: w=T[pos][0]+T[(pos+off[2])%R][2]   # Mitte leer lassen
        out.append(w if w else 'o')
    return out
def rnd(r): return dict(R=r.randint(20,400),spread=r.randint(1,40),step=r.randint(1,6),jump=r.uniform(0,.3),skip=r.uniform(0,.6))
def mut(q,r):
    q=dict(q); k=r.choice(list(q))
    if k in('R','spread','step'): q[k]=max(1,q[k]+r.choice([-int(q[k]*.2)-1,int(q[k]*.2)+1]))
    else: q[k]=min(.9,max(0,q[k]+r.gauss(0,.05)))
    return q
r=random.Random(SEED); best=None; import time; t0=time.time()
for it in range(400):
    q=rnd(r) if it<80 or best is None else mut(best[1],r)
    m=full(gen(q)); l=loss2(m)
    if best is None or l<best[0]: best=(l,q,m)
    if time.time()-t0>1300: break
val=[round(loss2(full(gen(best[1],s))),1) for s in (5,6,7)]
json.dump(dict(loss=best[0],val=val,q=best[1],m={k:v for k,v in best[2].items() if k!='ld'},ex=gen(best[1],5)[200:216]),open(f'grille_{SEED}.json','w'))
print('GRILLE',SEED,round(best[0],1),val,best[1]); print('  ',show(best[2])); print('   ',' '.join(gen(best[1],5)[200:216]))
