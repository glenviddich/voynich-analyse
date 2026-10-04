import collections as C,math,re,random
exec(open('qtest.py').read().split("isq=lambda")[0])
def H_order_given_multiset(words):
    # H(Wortform | Glyphen-Multimenge): 0 = Reihenfolge durch Inventar festgelegt (Slot-Grammatik)
    ms=C.defaultdict(C.Counter)
    for w in words: ms[''.join(sorted(w))][w]+=1
    n=len(words); h=0
    for k,c in ms.items():
        t=sum(c.values())
        for v in c.values(): h-= v/n*math.log2(v/t)
    anag=sum(1 for k,c in ms.items() if len(c)>1)
    return h,anag,len(ms)
def load(f,n=34000):
    t=open(f,encoding='utf-8',errors='ignore').read().lower()
    ws=re.findall(r'[a-zäöüßáéíóúàèìòùčšřžěůýňťď]+',t)[:n]; return ws
vw=[w for l in L for w in l[5] if len(w)>=3]
corp={'Voynich (ZL)':vw}
for n,f in [('Latein (Augustinus)','la.txt'),('Italienisch (Dante)','it.txt'),('Deutsch (Faust)','de.txt'),('Tschechisch','cs.txt'),('Finnisch','fi.txt')]:
    try: corp[n]=[w for w in load(f) if len(w)>=3]
    except Exception as e: print(n,e)
# Römische Zahlen 1..3999 als Kontrolle einer Slot-Grammatik
def roman(n):
    out='';
    for v,s in [(1000,'m'),(900,'cm'),(500,'d'),(400,'cd'),(100,'c'),(90,'xc'),(50,'l'),(40,'xl'),(10,'x'),(9,'ix'),(5,'v'),(4,'iv'),(1,'i')]:
        while n>=v: out+=s; n-=v
    return out
r=random.Random(0); corp['Römische Zahlen (Zipf-gezogen)']=[roman(min(3999,int(1/(r.random()**1.0*0.001+0.0003)))) for _ in range(30000)]
print(f'{"Korpus":32s} {"Wörter":>7s} {"H(Form|Inventar)":>18s} {"Multimengen mit >1 Form":>24s}')
for n,ws in corp.items():
    ws=ws[:34000]; h,a,m=H_order_given_multiset(ws); print(f'{n:32s} {len(ws):7d} {h:18.3f} {a:10d} von {m}')
