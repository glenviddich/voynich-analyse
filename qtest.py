import re, random, collections as C, math
exec(open('tests.py').read().split('vw=[cuva')[0])
# Zeilen mit Metadaten
L=[]  # list of (page, section, lang, hand, parastart, words)
for ln in open('ZL.txt',encoding='latin-1'):
    m=re.match(r'<(f\w+)\.(\d+),(.)(P\w*)>\s+(.*)',ln)
    if not m: continue
    t=re.sub(r'<[^>]*>','',m.group(5)); t=re.sub(r'\[([^:\]]*):[^\]]*\]',r'\1',t)
    t=re.sub(r'@\d+;','?',t).replace('{','').replace('}','').replace("'",'')
    ws=[w for w in re.split(r'[.,\s]+',t) if w and re.fullmatch(r'[a-z]+',w)]
    if ws:
        pg=pages.get(m.group(1),{}); L.append((m.group(1),pg.get('I','?'),pg.get('L','?'),pg.get('H','?'),m.group(3) in '*@',ws))
isq=lambda w:w.startswith('q')
allw=[w for l in L for w in l[5]]; base=sum(map(isq,allw))/len(allw)
print(f'q-Wörter gesamt: {sum(map(isq,allw))} = {base*100:.1f}%\n')
print('1) Nach Abschnitt / Dialekt / Schreiber')
for key,idx,names in [('Abschnitt',1,{'H':'Kräuter','B':'Badefrauen','S':'Sterne/Rezepte','P':'Pharma','A':'Astro','Z':'Tierkreis','C':'Kosmo','T':'Text'}),('Dialekt',2,{}),('Schreiber',3,{})]:
    c=C.defaultdict(lambda:[0,0])
    for l in L:
        for w in l[5]: c[l[idx]][0]+=isq(w); c[l[idx]][1]+=1
    print('   '+key+': '+', '.join(f"{names.get(k,k)} {a/b*100:.1f}%" for k,(a,b) in sorted(c.items(),key=lambda x:-x[1][1]) if b>500))
print('\n2) Position in der Zeile')
pos=C.defaultdict(lambda:[0,0])
for l in L:
    ws=l[5]; n=len(ws)
    for i,w in enumerate(ws):
        k='1. Wort' if i==0 else ('letztes' if i==n-1 else ('2. Wort' if i==1 else 'Mitte'))
        pos[k][0]+=isq(w); pos[k][1]+=1
    if l[4]: pos['1. Wort Absatz'][0]+=isq(ws[0]); pos['1. Wort Absatz'][1]+=1
for k in ['1. Wort Absatz','1. Wort','2. Wort','Mitte','letztes']: a,b=pos[k]; print(f'   {k:15s} {a/b*100:5.1f}%  (n={b})')
print('\n3) Abhängigkeit vom Ende des Vorgängerworts (innerhalb der Zeile)')
prev=C.defaultdict(lambda:[0,0])
for l in L:
    ws=l[5]
    for a,b in zip(ws,ws[1:]):
        e=a[-2:] if a.endswith(('dy','in','ol','or','al','ar','ey')) else a[-1]
        prev[e][0]+=isq(b); prev[e][1]+=1
for e,(a,b) in sorted(prev.items(),key=lambda x:-x[1][1])[:12]: print(f'   Vorgänger endet auf -{e:3s}: q danach {a/b*100:5.1f}%  (n={b})')
# Kontrolle: gleiche Analyse bei gemischter Wortfolge innerhalb Zeile
r=random.Random(0); pv=C.defaultdict(lambda:[0,0])
for l in L:
    ws=l[5][:]; r.shuffle(ws)
    for a,b in zip(ws,ws[1:]):
        e=a[-2:] if a.endswith(('dy','in','ol','or','al','ar','ey')) else a[-1]; pv[e][0]+=isq(b); pv[e][1]+=1
print('   Kontrolle (Zeile gemischt): '+', '.join(f"-{e} {pv[e][0]/pv[e][1]*100:.1f}%" for e in ['y','dy','in','ol','r','l']))
print('\n4) Paare X / qX: teilen sie sich dieselben Seiten?')
pw=C.defaultdict(C.Counter)
for l in L:
    for w in l[5]: pw[w][l[0]]+=1
freq=C.Counter(allw)
def cos(a,b):
    ks=set(pw[a])|set(pw[b]); num=sum(pw[a][k]*pw[b][k] for k in ks)
    return num/math.sqrt(sum(v*v for v in pw[a].values())*sum(v*v for v in pw[b].values()))
pairs=[(w[1:],w) for w in freq if isq(w) and w[1:] in freq and freq[w]>=15 and freq[w[1:]]>=15]
ctrl=[]; fl=[w for w in freq if freq[w]>=15]
for x,qx in pairs:
    cands=[w for w in fl if w not in(x,qx) and abs(math.log(freq[w]/freq[qx]))<.3]; ctrl.append(cos(x,r.choice(cands)))
pc=[cos(x,qx) for x,qx in pairs]
# Vergleich: X / chX und X / oX
def prefpairs(p): return [(w[len(p):],w) for w in freq if w.startswith(p) and w[len(p):] in freq and freq[w]>=15 and freq[w[len(p):]]>=15]
print(f'   X/qX  Paare: {len(pairs)}, Seiten-Ähnlichkeit {sum(pc)/len(pc):.3f}  vs. zufälliges gleich häufiges Wort {sum(ctrl)/len(ctrl):.3f}')
for p in ['o','ch','sh','d','y','l']:
    pp=prefpairs(p)
    if pp: v=[cos(a,b) for a,b in pp]; print(f'   X/{p}X Paare: {len(pp)}, Seiten-Ähnlichkeit {sum(v)/len(v):.3f}')
print('   Top-Paare:',', '.join(f'{x}/{qx}({freq[x]}/{freq[qx]})' for x,qx in sorted(pairs,key=lambda p:-freq[p[1]])[:8]))
print('\n5) Folgen q-Wörter aufeinander? (q nach q)')
a=b=0
for l in L:
    for x,y in zip(l[5],l[5][1:]):
        if isq(x): a+=isq(y); b+=1
print(f'   nach q-Wort: {a/b*100:.1f}% q   (Grundrate {base*100:.1f}%)')
