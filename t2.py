import re, math, random, collections as C
random.seed(7)
exec(open('tests.py').read().split('vw=[cuva')[0])  # lädt W, pages, cuva, words, h2
V=[w for _,w in W]; n=len(V)
de=words('de.txt'); la=words('la.txt')
def stats(ws, cu=True):
    ws2=[cuva(w) for w in ws] if cu else ws
    _,H2=h2(ws2); wl=sum(map(len,ws2))/len(ws2)
    rep=sum(a==b for a,b in zip(ws,ws[1:]))/len(ws)*1000
    c=C.Counter(ws); N=len(ws)
    Hw=-sum(v/N*math.log2(v/N) for v in c.values())
    ttr=len(c)/N*100
    # Positionszwang: mittlere "Positionsreinheit" der 10 häufigsten Zeichen
    pos=C.defaultdict(lambda:[0,0,0])
    for w in ws2:
        for i,ch in enumerate(w): pos[ch][0 if i==0 else (2 if i==len(w)-1 else 1)]+=1
    top=sorted(pos.values(),key=sum,reverse=True)[:10]
    pur=sum(max(p)/sum(p) for p in top)/10*100
    return f"h2 {H2:.2f} | Wortlänge {wl:.1f} | Wortentropie {Hw:.1f} bit | Typen {ttr:.0f}% | Doppelwörter {rep:.1f}‰ | Positionstreue {pur:.0f}%"
print("VOYNICH                 ", stats(V))
print("Deutsch                 ", stats(de[:n],False))
print("Latein                  ", stats(la[:n],False))
# ---- B) Notizen ohne Verben/Füllwörter
stop_de=set("der die das und ist in zu den von mit sich des auf für nicht ein eine einer einem einen als auch es an er so dass sie nach wie im bei ich du wir ihr man dem was wird sind war hat haben kann nur noch wenn um aus am mir mich dir dich mein dein sein ihm ihn uns euch doch ja nun da wo hier dort schon mehr sehr zum zur oder aber denn wer soll will muss mag ward wohl hab bin bist seid".split())
stop_la=set("et in est non ad cum ut quod qui quae sed de ex a ab per si se sunt esse enim autem vel aut nec ne iam tamen hoc haec id eius eo ea etiam atque ac sicut quam quia ita nam inter erat fuit sub pro post ante".split())
nd=[w for w in de if w not in stop_de and not (w.endswith(('en','et','te','st')) and len(w)>4)][:n]
nl=[w for w in la if w not in stop_la and not w.endswith(('t','nt','re','ri'))][:n]
print("\nB) Notizstil (Funktionswörter & typische Verbformen raus)")
print("Deutsch-Notizen         ", stats(nd,False))
print("Latein-Notizen          ", stats(nl,False))
# ---- A) Würfel-/Tabellen-Chiffre à la Naibbe (vereinfacht, eigene Tabellen)
PRE=['qo','o','ch','sh','d','qok','ok','ot','qot','y','l','s','','','']
MID=['k','t','ke','te','kee','ckh','cth','ee','e','','','l','r']
SUF=['y','dy','edy','eedy','aiin','ain','ol','or','ar','al','am','iin','eey','chy','shy']
alpha='abcdefghilmnopqrstuxyz'
def tab(): return {c:[random.choice(PRE)+random.choice(MID) for _ in range(3)] for c in alpha}
pre_t=tab(); suf_t={c:[random.choice(MID[:6]+[''])+random.choice(SUF) for _ in range(3)] for c in alpha}
uni_t={c:[random.choice(PRE)+random.choice(MID)+random.choice(SUF) for _ in range(3)] for c in alpha}
def naibbe(ws):
    s=''.join(c for c in ''.join(ws) if c in alpha).replace('j','i').replace('v','u'); out=[];i=0
    while i<len(s):
        d=random.randint(1,6)  # Würfel entscheidet Uni- oder Bigramm + Tabelle
        if d<=2 or i==len(s)-1: out.append(random.choice(uni_t[s[i]])); i+=1
        else: out.append(random.choice(pre_t[s[i]])+random.choice(suf_t[s[i+1]])); i+=2
    return [w for w in out if w]
nb=naibbe(la[:n])[:n]
print("\nA) Würfel-Tabellen-Chiffre (Latein rein)")
print("Latein -> Würfel-Chiffre", stats(nb))
print("   Beispiel:", ' '.join(nb[:12]))
# ---- C) Komprimiert/binär
print("\nC) Kompression: Bits pro Zeichen (zlib/lzma) – komprimierte Daten wären ~8")
import lzma
for name,ws in [('Voynich',V),('Latein',la[:n]),('Latein lzma-komprimiert, Base32 als Text',None)]:
    if ws is None:
        import base64; b=base64.b32encode(lzma.compress(' '.join(la[:n]).encode())).decode().lower()
        s=b
    else: s=' '.join(ws)
    c=len(lzma.compress(s.encode()))*8/len(s); print(f"   {name:42s} {c:.2f} Bit/Zeichen")
# Gesamtinformation: wie viel Klartext passt rein?
tot_v=len(lzma.compress(' '.join(V).encode())); tot_l=len(lzma.compress(' '.join(la[:n]).encode()))
print(f"   Info-Gehalt Voynich ≈ {tot_v/1024:.0f} KB, gleich viele lat. Wörter ≈ {tot_l/1024:.0f} KB")
# Slot-Unabhängigkeit: Anfang vs Ende eines Wortes (Mutual Information)
def mi(ws):
    pr=[(w[:2],w[-2:]) for w in ws if len(w)>=4]; N=len(pr)
    a=C.Counter(x for x,_ in pr); b=C.Counter(y for _,y in pr); ab=C.Counter(pr)
    return sum(v/N*math.log2(v*N/(a[x]*b[y])) for (x,y),v in ab.items())
print("\nC2) Hängen Wortanfang und Wortende zusammen? (Mutual Information, Bit)")
for name,ws in [('Voynich',V),('Deutsch',de[:n]),('Latein',la[:n]),('Würfel-Chiffre',nb)]:
    sh=[ws[i][:2]+ws[(i*7919)%len(ws)][-2:] for i in range(len(ws))]
    print(f"   {name:15s} MI={mi(ws):.2f}  (Zufallspaarung: {mi(sh):.2f})")
