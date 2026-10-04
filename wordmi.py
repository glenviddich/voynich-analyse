exec(open('rohonc2.py').read().split("rows=[('Voynich Glyphen'")[0])
def mi(p):
    N=len(p); a=C.Counter(x for x,_ in p); b=C.Counter(y for _,y in p); ab=C.Counter(p)
    return sum(v/N*math.log2(v*N/(a[x]*b[y])) for (x,y),v in ab.items())
def wordcoup(lines_, nw, seed=0):
    # nur häufige Wörter (Top nw), Rest -> '_' damit Sparsity nicht dominiert
    allw=[w for l in lines_ for w in l]; top=set(w for w,_ in C.Counter(allw).most_common(nw))
    f=lambda w: w if w in top else '_'
    real=[(f(a),f(b)) for l in lines_ for a,b in zip(l,l[1:])]
    rr=random.Random(seed); sh=[]
    for l in lines_:
        l=l[:]; rr.shuffle(l); sh+=[(f(a),f(b)) for a,b in zip(l,l[1:])]
    # auch: Nachbarzeilen-Mischung (Wörter über die ganze Seite mischen) als zweite Baseline
    return mi(real), mi(sh)
exec(open('sylcmp.py').read().split("def unit_stats")[0].split("exec(open('residual.py')")[1].split('\n',1)[1])
la=PT['Latein'][:34000]; LL=[la[i:i+10] for i in range(0,len(la),10)]
de=PT['Deutsch'][:34000]; DL=[de[i:i+10] for i in range(0,len(de),10)]
VLn=[[cuva(w) for w in l[5]] for l in L]
RLn=[[''.join(gmap[c] for c in w) for w in l] for l in lines]
print('Wort(n) → Wort(n+1): Information in Bit, nur die 300 häufigsten Wörter unterschieden; echt / Zeile gemischt / Überschuss')
for name,ln in [('Voynich',VLn),('Rohonc',RLn),('Latein',LL),('Deutsch',DL)]:
    a,b=wordcoup(ln,300); print(f'   {name:10s} {a:.3f} / {b:.3f} / {a-b:+.3f}')
# Zusatz: Glyphen-Kopplung dy->q bleibt; prüfen ob sie "innerhalb" der Wortpaare steckt, die auch als Wörter koppeln
