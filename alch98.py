import re,random,collections as C
exec(open('qtest.py').read().split("isq=lambda")[0])
names=[l.strip() for l in open('alch98.txt')]
# Kräuterseiten Sprache A in Folio-Reihenfolge (Reihenfolge wie in ZL.txt)
pgs=[];seen=set()
for l in L:
    if l[1]=='H' and l[2]=='A' and l[0] not in seen: seen.add(l[0]); pgs.append(l[0])
first={}
for l in L:
    if l[0] in seen and l[0] not in first: first[l[0]]=l[5][0]
nw=C.Counter(); 
for l in L:
    if l[0] in seen: nw[l[0]]+=len(l[5])
print('Kräuter-A-Seiten:',len(pgs),' Namen:',len(names))
fw=[first[p] for p in pgs]
print('erste Wörter:',' '.join(f'{p}:{w}' for p,w in zip(pgs,fw))[:1500])
# Test 1: Längenkorrelation Name (ohne Herba, ohne Leerzeichen) vs erstes Wort, Reihenfolge 1:1
import math
def corr(a,b):
    n=len(a);ma=sum(a)/n;mb=sum(b)/n
    sa=math.sqrt(sum((x-ma)**2 for x in a));sb=math.sqrt(sum((x-mb)**2 for x in b))
    return sum((x-ma)*(y-mb) for x,y in zip(a,b))/(sa*sb)
n=min(len(pgs),len(names))
nl=[len(x.replace(' ','')) for x in names[:n]]
for lab,v in [('1.Wort-Länge',[len(w) for w in fw[:n]]),('Wörter/Seite',[nw[p] for p in pgs[:n]])]:
    r=corr(nl,v); rs=[]
    rnd=random.Random(1)
    for _ in range(5000):
        s=v[:];rnd.shuffle(s);rs.append(corr(nl,s))
    p=sum(abs(x)>=abs(r) for x in rs)/len(rs)
    print(f'{lab}: r={r:+.3f}  p={p:.3f}')
# Test 2: wiederholte Namen -> gleiche Anfangswörter?
dup=C.defaultdict(list)
for i,x in enumerate(names): dup[x].append(i)
for x,ix in dup.items():
    if len(ix)>1 and max(ix)<len(pgs): print(x,ix,[fw[i] for i in ix])
# Baseline: wie oft teilen zwei zufällige Seiten das Anfangswort?
same=sum(fw[i]==fw[j] for i in range(len(fw)) for j in range(i+1,len(fw)));tot=len(fw)*(len(fw)-1)//2
print(f'Anfangswort-Gleichheit zufälliger Seitenpaare: {same}/{tot} = {same/tot*100:.1f}%')
