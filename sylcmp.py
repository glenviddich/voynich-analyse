exec(open('residual.py').read().split("VA=V")[0])
VW='aeiouy'
def syllabify(w):
    parts=re.findall(r'[^aeiouy]*[aeiouy]+(?:[^aeiouy]*$)?',w)
    if not parts: return [w]
    # Konsonantengruppe zwischen Vokalen: letzter Konsonant zur nächsten Silbe
    out=[]
    for p in parts:
        m=re.match(r'([^aeiouy]*)([aeiouy]+)(.*)',p)
        out.append(p)
    res=[];carry=''
    for i,p in enumerate(out):
        p=carry+p; carry=''
        if i<len(out)-1:
            m=re.match(r'(.*?[aeiouy]+)([^aeiouy]*)$',p)
            if m and len(m.group(2))>1: p,carry=m.group(1)+m.group(2)[:-1],m.group(2)[-1]
            elif m and len(m.group(2))==1: p,carry=m.group(1),m.group(2)
        res.append(p)
    return res
def unit_stats(seqs):
    toks=[]; [toks.extend(s+['_']) for s in seqs]
    c=C.Counter(t for t in toks if t!='_'); tot=sum(c.values())
    cov=0;k=0
    for _,v in c.most_common():
        cov+=v;k+=1
        if cov/tot>=.9: break
    H1=-sum(v/len(toks)*math.log2(v/len(toks)) for v in C.Counter(toks).values())
    c2=C.Counter(zip(toks,toks[1:])); H2=-sum(v/(len(toks)-1)*math.log2(v/(len(toks)-1)) for v in c2.values())-H1
    upw=sum(map(len,seqs))/len(seqs)
    pr=[(s[0],s[-1]) for s in seqs if len(s)>=2]; N=len(pr)
    a=C.Counter(x for x,_ in pr); b=C.Counter(y for _,y in pr); ab=C.Counter(pr)
    mi=sum(v/N*math.log2(v*N/(a[x]*b[y])) for (x,y),v in ab.items())
    # Normierte MI (durch min Entropie), damit Inventargröße weniger verzerrt
    Ha=-sum(v/N*math.log2(v/N) for v in a.values()); Hb=-sum(v/N*math.log2(v/N) for v in b.values())
    return f'Einheiten/Wort {upw:.2f} | Inventar für 90% {k:4d} | h1 {H1:.2f} | h2 {H2:.2f} | erste↔letzte Einheit {mi/min(Ha,Hb):.2f} (normiert)'
N=30000
print('Silben echter Sprachen:')
for L in ['Latein','Italienisch','Tschechisch','Latein-Rezepte']:
    print(f'  {L:16s}',unit_stats([syllabify(w) for w in PT[L][:N]]))
print('\nVoynich-Blöcke (BPE) bei verschiedener Feinheit, Kopien entfernt (Varianten, letzte 3):')
res,_=remove_copies(V,3,1,True)
for m in (10,20,40,60,100):
    print(f'  {m:3d} Verschmelzungen  ',unit_stats(bpe(res[:N],m)))
print('\nGegenprobe: BPE auf Latein-Buchstaben (statt Silben):')
for m in (40,100,200):
    print(f'  {m:3d} Verschmelzungen  ',unit_stats(bpe(PT['Latein'][:N],m)))
