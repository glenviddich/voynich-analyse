import json, glob, re, math, random, collections as C
from rapidfuzz.distance import Levenshtein as Lv
exec(open('residual.py').read().split("VA=V")[0])
# Rohonc laden: Reihenfolge wie pagelist, nur Hauptblöcke, Wörter = durch Leerzeichen getrennte Zeichenfolgen
order=json.load(open('kt_pagelist.json')); words=[]; lines=[]
for p in order:
    try: blocks=json.load(open(f'kt/{p}.json',encoding='utf-8'))
    except Exception: continue
    for b in blocks:
        if b.get('blocktype')!='main': continue
        for r in b.get('rows',[]):
            ws=[w for w in r['text'].split() if w and all(''<=c<='' for c in w)]
            if ws: lines.append(ws); words+=ws
# PUA-Codepoints -> kompakte Zeichen (jede Glyphe 1 Zeichen), damit die Kennzahlen 1:1 vergleichbar sind
glyphs=sorted(set(''.join(words))); gmap={g:chr(0x4e00+i) for i,g in enumerate(glyphs)}
R=[''.join(gmap[c] for c in w) for w in words]
print(f'Rohonc: {len(R)} Wörter, {len(glyphs)} verschiedene Glyphen, {len(set(R))} verschiedene Wörter')
# Zeichen-Alphabet-Größe: Voynich (cuva) hat ~26; Rohonc ~ hundert+ -> h-Werte nicht direkt vergleichbar; zusätzlich normiert ausgeben
def stats(ws, label):
    s='_'.join(ws); c1=C.Counter(s); c2=C.Counter(zip(s,s[1:])); n=len(s)
    H1=-sum(v/n*math.log2(v/n) for v in c1.values()); H2=-sum(v/(n-1)*math.log2(v/(n-1)) for v in c2.values())-H1
    N=len(ws); typ=len(set(ws))/N*100; rep=sum(a==b for a,b in zip(ws,ws[1:]))/N*1000
    pos=C.defaultdict(lambda:[0,0,0])
    for w in ws:
        for i,ch in enumerate(w): pos[ch][0 if i==0 else (2 if i==len(w)-1 else 1)]+=1
    pur=sum(max(p)/sum(p) for p in sorted(pos.values(),key=sum,reverse=True)[:10])*10
    pr=[(w[:1],w[-1:]) for w in ws if len(w)>=2]; M=len(pr)
    a=C.Counter(x for x,_ in pr); b=C.Counter(y for _,y in pr); ab=C.Counter(pr)
    mi=sum(v/M*math.log2(v*M/(a[x]*b[y])) for (x,y),v in ab.items())
    Ha=-sum(v/M*math.log2(v/M) for v in a.values()); Hb=-sum(v/M*math.log2(v/M) for v in b.values())
    print(f'{label:12s} Zeichen {len(c1)-1:3d} | h1 {H1:.2f} | h2 {H2:.2f} | h2/h1 {H2/H1:.2f} | Wortl {sum(map(len,ws))/N:.1f} | Typen {typ:4.1f}% | Doppelw {rep:4.1f}‰ | Pos {pur:.0f}% | Anf↔End normiert {mi/min(Ha,Hb):.2f}')
stats([cuva(w) for w in V],'Voynich'); stats(R,'Rohonc'); stats(PT['Latein'][:len(V)],'Latein')
# Zwillinge, Kopplung
def twins(ws,K=10):
    a=n=0
    for i in range(K,len(ws)):
        if len(ws[i])<2: continue
        n+=1; a+=any(len(p)>=2 and Lv.distance(ws[i],p)==1 for p in ws[i-K:i])
    return a/n*100
def coupling(lines):
    def mi(p):
        N=len(p); a=C.Counter(x for x,_ in p); b=C.Counter(y for _,y in p); ab=C.Counter(p)
        return sum(v/N*math.log2(v*N/(a[x]*b[y])) for (x,y),v in ab.items())
    real=[(a[-1],b[0]) for l in lines for a,b in zip(l,l[1:])]
    rr=random.Random(0); sh=[]
    for l in lines:
        l=l[:]; rr.shuffle(l); sh+=[(a[-1],b[0]) for a,b in zip(l,l[1:])]
    return mi(real)-mi(sh)
exec(open('qtest.py').read().split('isq=lambda')[0].replace('print(','(lambda *a,**k:0)('))
r=random.Random(0)
for label,ws,ln in [('Voynich',[cuva(w) for w in V],[[cuva(w) for w in l[5]] for l in L]),('Rohonc',R,[[''.join(gmap[c] for c in w) for w in l] for l in lines])]:
    s=ws[:]; r.shuffle(s)
    print(f'{label:12s} Fast-Zwilling-Überschuss {twins(ws)-twins(s):+.1f} Punkte | Kopplung Wortende→Wortanfang {coupling(ln):.3f}')
# Sukhotin
exec(open('sukhotin.py').read().split("def clean")[0].split("return ''.join(chars[i] for i in vow), alt/tot*100")[0]+"return ''.join(chars[i] for i in vow), alt/tot*100")
v,a=sukhotin(R); print(f'Rohonc Sukhotin: {len(v)} „Vokale“, Wechselanteil {a:.0f}%  (Voynich 79%, Sprachen 71–82%, Zufall 50%)')
