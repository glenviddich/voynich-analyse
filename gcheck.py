import sys; sys.argv=['x','2']
src=open('grille.py').read().split("r=random.Random(SEED)")[0].replace("SEED=int(sys.argv[1])","SEED=2")
exec(src); import json
q=json.load(open('grille_2.json'))['q']
NW=34000; g=gen(q,5)
def coupling(ws):
    lines=[ws[i:i+10] for i in range(0,len(ws),10)]
    def mi(p):
        N=len(p); a=C.Counter(x for x,_ in p); b=C.Counter(y for _,y in p); ab=C.Counter(p)
        return sum(v/N*math.log2(v*N/(a[x]*b[y])) for (x,y),v in ab.items())
    real=[(a[-1],b[0]) for l in lines for a,b in zip(l,l[1:])]
    rr=random.Random(0); sh=[]
    for l in lines:
        l=l[:]; rr.shuffle(l); sh+=[(a[-1],b[0]) for a,b in zip(l,l[1:])]
    return mi(real)-mi(sh)
def qafter(ws):
    a=b=c=d=0
    for x,y in zip(ws,ws[1:]):
        if x.endswith('dy'): a+=y.startswith('q'); b+=1
        if x.endswith('in'): c+=y.startswith('q'); d+=1
    return a/b*100,c/max(d,1)*100
print('Voynich:   Kopplung %.3f | q nach -dy %.1f%%, q nach -in %.1f%%'%((coupling(V),)+qafter(V)))
print('Schablone: Kopplung %.3f | q nach -dy %.1f%%, q nach -in %.1f%%'%((coupling(g),)+qafter(g)))
