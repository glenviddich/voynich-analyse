import re, random, math, collections as C, unicodedata
exec(open('qtest.py').read().split("isq=lambda")[0])
def clean(fn):
    t=open(fn,encoding='utf-8',errors='ignore').read(); t=t[len(t)//10:len(t)*9//10].lower().replace('ß','ss')
    t=unicodedata.normalize('NFKD',t); t=''.join(c for c in t if not unicodedata.combining(c))
    return [re.findall(r'[a-z]+',ln) for ln in t.split('\n') if ln.strip()]
def mi(pairs):
    N=len(pairs); a=C.Counter(x for x,_ in pairs); b=C.Counter(y for _,y in pairs); ab=C.Counter(pairs)
    return sum(v/N*math.log2(v*N/(a[x]*b[y])) for (x,y),v in ab.items())
def xb(lines, unit=1):
    real=[(a[-unit:],b[:unit]) for ws in lines for a,b in zip(ws,ws[1:])]
    r=random.Random(0); sh=[]
    for ws in lines:
        w=ws[:]; r.shuffle(w); sh+=[(a[-unit:],b[:unit]) for a,b in zip(w,w[1:])]
    return mi(real), mi(sh), len(real)
def inner(lines,unit=1):  # Vergleich: innerhalb eines Wortes, Mitte geteilt
    p=[(w[:len(w)//2][-unit:],w[len(w)//2:][:unit]) for ws in lines for w in ws if len(w)>=4]
    return mi(p)
VL=[[cuva(w) for w in l[5]] for l in L]
print('Kopplung Wortende -> nächster Wortanfang (Mutual Information, Bit; letztes/erstes Zeichen)')
print(f"{'':14s}{'echt':>7}{'gemischt':>10}{'Überschuss':>11}{'  zum Vgl. Wortmitte':>22}")
for name,lines in [('Voynich',VL),('Latein',clean('la.txt')),('Deutsch',clean('de.txt')),('Tschechisch',clean('cs.txt')),('Italienisch',clean('it.txt'))]:
    n=sum(len(l)-1 for l in VL); acc=[];c=0
    for l in lines:
        if c>n: break
        if len(l)>1: acc.append(l); c+=len(l)-1
    a,b,k=xb(acc); print(f'{name:14s}{a:7.3f}{b:10.3f}{a-b:11.3f}{inner(acc):22.3f}')
