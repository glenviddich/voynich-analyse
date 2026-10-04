exec(open('imgcorr.py').read().split("names=['Wurzel")[0].replace("print(","(lambda *a,**k:0)("))
meta={p:pg_ for p,pg_ in pages_meta.items()} if False else None
import re
M={}
for ln in open('ZL.txt',encoding='latin-1'):
    m=re.match(r'<(f\w+)>\s+<!(.*)>',ln)
    if m: M[m.group(1)]=dict(re.findall(r'\$(\w)=(\w+)',m.group(2)))
rate={p:fam[p]['chol']/nw[p]*100 for p in pages}
lab=[F[p][0] for p in pages]
def diff(lab_): 
    a=[rate[p] for p,y in zip(pages,lab_) if y]; b=[rate[p] for p,y in zip(pages,lab_) if not y]; return sum(a)/len(a)-sum(b)/len(b)
obs=diff(lab); print(f'chol-Rate: Wurzelseiten {sum(rate[p] for p,y in zip(pages,lab) if y)/sum(lab):.2f} vs andere {sum(rate[p] for p,y in zip(pages,lab) if not y)/(len(lab)-sum(lab)):.2f} pro 100 Wörter')
print('Dialekte:',C.Counter(M[p].get('L') for p in pages),' Schreiber:',C.Counter(M[p].get('H') for p in pages))
# Permutation innerhalb Quire
groups=C.defaultdict(list)
for i,p in enumerate(pages): groups[M[p].get('Q')].append(i)
r=random.Random(1); null=[]
for _ in range(5000):
    pl=lab[:]
    for g in groups.values():
        v=[lab[i] for i in g]; r.shuffle(v)
        for i,x in zip(g,v): pl[i]=x
    null.append(diff(pl))
print(f'Permutation innerhalb der Lagen (Quires): p≈{sum(abs(x)>=abs(obs) for x in null)/len(null):.4f}')
# Nur Dialekt A / Schreiber 1
for key,val in [('L','A'),('H','1')]:
    sub=[i for i,p in enumerate(pages) if M[p].get(key)==val]
    a=[rate[pages[i]] for i in sub if lab[i]]; b=[rate[pages[i]] for i in sub if not lab[i]]
    o=sum(a)/len(a)-sum(b)/len(b); nl=[]
    for _ in range(5000):
        v=[lab[i] for i in sub]; r.shuffle(v); aa=[rate[pages[i]] for i,x in zip(sub,v) if x]; bb=[rate[pages[i]] for i,x in zip(sub,v) if not x]
        nl.append(sum(aa)/len(aa)-sum(bb)/len(bb))
    print(f'Nur {key}={val} ({len(sub)} Seiten): Differenz {o:+.2f}, p≈{sum(abs(x)>=abs(o) for x in nl)/len(nl):.4f}')
# Welche Varianten tragen den Effekt?
for v in ['chol','chor','shol','shor']:
    a=[pagew[p].count(v)/nw[p]*100 for p,y in zip(pages,lab) if y]; b=[pagew[p].count(v)/nw[p]*100 for p,y in zip(pages,lab) if not y]
    print(f'   {v}: Wurzelseiten {sum(a)/len(a):.2f} vs andere {sum(b)/len(b):.2f}')
# Seitenlänge
print(f'Wörter pro Seite: Wurzelseiten {sum(nw[p] for p,y in zip(pages,lab) if y)/sum(lab):.0f} vs andere {sum(nw[p] for p,y in zip(pages,lab) if not y)/(len(lab)-sum(lab)):.0f}')
