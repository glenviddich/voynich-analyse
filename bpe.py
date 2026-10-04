import re, math, random, collections as C, unicodedata
exec(open('leet.py').read().split("print('VOYNICH")[0])
def bpe(words, merges):
    seqs=[list(w) for w in words]
    for _ in range(merges):
        pc=C.Counter()
        for s in seqs:
            for a,b in zip(s,s[1:]): pc[(a,b)]+=1
        if not pc: break
        (a,b),_=pc.most_common(1)[0]; ab=a+b
        for i,s in enumerate(seqs):
            j=0; out=[]
            while j<len(s):
                if j<len(s)-1 and s[j]==a and s[j+1]==b: out.append(ab); j+=2
                else: out.append(s[j]); j+=1
            seqs[i]=out
    return seqs
def ustats(seqs):
    toks=[]
    for s in seqs: toks+=s+['_']
    c1=C.Counter(toks); n=len(toks)
    H1=-sum(v/n*math.log2(v/n) for v in c1.values())
    c2=C.Counter(zip(toks,toks[1:])); H2=-sum(v/(n-1)*math.log2(v/(n-1)) for v in c2.values())-H1
    used=sum(1 for k,v in c1.items() if v/n>0.001 and k!='_')
    pos=C.defaultdict(lambda:[0,0,0])
    for s in seqs:
        for i,u in enumerate(s):
            if len(s)>1: pos[u][0 if i==0 else (2 if i==len(s)-1 else 1)]+=1
    pur=sum(max(p)/sum(p) for p in sorted(pos.values(),key=sum,reverse=True)[:10])*10
    wl=sum(map(len,seqs))/len(seqs)
    return dict(units=used,h1=H1,h2=H2,gap=H1-H2,wl=wl,pur=pur), c1
def fmt(d): return f"Einheiten {d['units']:3d} | h1 {d['h1']:.2f} | h2 {d['h2']:.2f} | Differenz {d['gap']:.2f} | Wortl. {d['wl']:.1f} | Positionstreue {d['pur']:.0f}%"
# Kalibrierung: Latein -> feste Mehrzeichen-Leet aus Voynich-ähnlichem 20er-Alphabet
G='oaeydklrshtcinpfqm'
r=random.Random(5); tab={}
used=set()
for c in 'abcdefghijklmnopqrstuvwxyz':
    while True:
        x=''.join(r.choice(G) for _ in range(r.choice([2,2,3])))
        if x not in used: used.add(x); tab[c]=x; break
leetla=[''.join(tab[c] for c in w) for w in la]
ref,_=ustats([list(w) for w in la])
print('Referenz Latein (Buchstaben):    ',fmt(ref))
print('\nKALIBRIERUNG: Latein als Mehrzeichen-Leet, dann Blöcke per BPE zurückgewinnen')
for m in (0,20,40,60,80,120):
    d,_=ustats(bpe(leetla,m)); print(f'  {m:3d} Verschmelzungen          ',fmt(d))
print('\nVOYNICH (EVA)')
res={}
for m in (0,10,20,30,40,60,80,120):
    seqs=bpe(VE,m); d,c1=ustats(seqs); res[m]=(seqs,c1); print(f'  {m:3d} Verschmelzungen          ',fmt(d))
import pickle; pickle.dump({m:(r_[1]) for m,r_ in res.items()},open('bpe_units.pkl','wb'))
for m in (30,60):
    print(f'\n  Häufigste Einheiten nach {m}:',', '.join(f'{u}' for u,_ in res[m][1].most_common(32) if u!='_'))
    print('  Beispiel:',' | '.join('.'.join(s) for s in res[m][0][400:410]))
