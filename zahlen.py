exec(open('residual.py').read().split("VA=V")[0])
exec(open('grille.py').read().split("cp=C.Counter()")[0].split("import json")[1])  # split3, PRE, SUF
# 1) Slot-Entropien im Voynich: Präfix / Mitte / Suffix
sp=[split3(w) for w in V]
def H(c): n=sum(c.values()); return -sum(v/n*math.log2(v/n) for v in c.values())
print('Voynich Slot-Entropie: Präfix %.2f | Mitte %.2f | Suffix %.2f bit'%tuple(H(C.Counter(x[i] for x in sp)) for i in range(3)))
# 2) Wo unterscheiden sich Fast-Zwillinge? (Position der Änderung, Nachbarn vs. Zufallspaare)
cw=[cuva(w) for w in V]; r=random.Random(0)
def diffpos(pairs):
    c=C.Counter()
    for a,b in pairs:
        if len(a)<3 or len(b)<3 or Lv.distance(a,b)!=1: continue
        o=Lv.editops(a,b)[0]; i=o.src_pos; n=len(a)
        c['Anfang' if i==0 else ('Ende' if i>=n-1 else 'Mitte')]+=1
    t=sum(c.values()); return {k:round(v/t*100) for k,v in c.items()}, t
near=[(cw[i],cw[i-d]) for i in range(10,len(cw)) for d in range(1,6)]
rnd=[(cw[r.randrange(len(cw))],cw[r.randrange(len(cw))]) for _ in range(len(cw)*5)]
print('Änderungsposition Fast-Zwillinge: Nachbarn',diffpos(near),' Zufallspaare',diffpos(rnd))
# 3) Synthetische Zahlenlisten: Mengenangaben in Rezepten, Stellenwertsystem Basis b, Voynich-Bausteine als Ziffern
blocks=[w for w,_ in C.Counter(cw).most_common(40)]
def numtext(base,nw,walk):
    rr=random.Random(1); out=[]; x=rr.randint(1,base**3)
    for _ in range(nw):
        if rr.random()<walk: x=max(1,x+rr.choice([-base,-1,1,base]))
        else: x=int(base**rr.uniform(0.3,3.3))
        s=[]; y=x
        while y: s.append(blocks[y%base]); y//=base
        out.append(''.join(reversed(s)))
    return out
for base,walk in [(12,0.0),(24,0.0),(24,0.5),(36,0.5)]:
    row(f'Zahlenliste Basis {base}, {int(walk*100)}% Nachbarzahlen',numtext(base,len(V),walk))
