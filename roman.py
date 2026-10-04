exec(open('bpe.py').read().split("# Kalibrierung")[0])
def roman(n):
    out=''
    for v,s in [(1000,'m'),(900,'cm'),(500,'d'),(400,'cd'),(100,'c'),(90,'xc'),(50,'l'),(40,'xl'),(10,'x'),(9,'ix'),(5,'v'),(4,'iv'),(1,'i')]:
        while n>=v: out+=s; n-=v
    return out
def roman_med(n):  # mittelalterlich: iiii statt iv, oft j am Ende
    out=''
    for v,s in [(1000,'m'),(500,'d'),(100,'c'),(50,'l'),(10,'x'),(5,'v'),(1,'i')]:
        while n>=v: out+=s; n-=v
    return out[:-1]+'j' if out.endswith('i') else out
r=random.Random(1)
nums=[int(10**r.uniform(0,3)) for _ in range(len(VE))]   # Zahlen 1..1000, log-verteilt
mix=[]
for w in la:  # Rezepttext-artig: Wörter mit eingestreuten Zahlen
    mix.append(w)
    if r.random()<.25: mix.append(roman_med(int(10**r.uniform(0,2))))
mix=mix[:len(VE)]
for name,ws in [('VOYNICH',VE),('Latein',la),('Römische Zahlen (modern)',[roman(n) for n in nums]),('Römische Zahlen (mittelalterl.)',[roman_med(n) for n in nums]),('Latein + 25% Zahlen',mix)]:
    d,c1=ustats([list(w) for w in ws]); N=len(ws)
    rep=sum(a==b for a,b in zip(ws,ws[1:]))/N*1000; typ=len(set(ws))/N*100
    print(f'{name:32s}',fmt(d),f'| Typen {typ:.0f}% | Doppelw. {rep:.1f}‰')
print('Beispiel mittelalterl.:',' '.join(roman_med(n) for n in nums[:12]))
