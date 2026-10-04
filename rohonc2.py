exec(open('rohonc_cmp.py').read().split("def stats")[0])
exec(open('bpe.py').read().split("def ustats")[0].split("exec(open('leet.py')")[1].split('\n',1)[1])
exec(open('qtest.py').read().split('isq=lambda')[0].replace('print(','(lambda *a,**k:0)('))
def inv90(ws):
    c=C.Counter(ch for w in ws for ch in w); tot=sum(c.values()); k=cov=0
    for _,v in c.most_common():
        cov+=v;k+=1
        if cov/tot>=.9: return k
def diffpos(ws,K=10):
    c=C.Counter(); r=random.Random(0)
    for i in range(K,len(ws)):
        w=ws[i]
        if len(w)<2: continue
        for p in ws[i-K:i]:
            if len(p)>=2 and Lv.distance(w,p)==1:
                o=Lv.editops(w,p)[0]; j=o.src_pos; n=len(w)
                c['Anfang' if j==0 else ('Ende' if j>=n-1 else 'Mitte')]+=1; break
    t=sum(c.values()); return {k:round(v/t*100) for k,v in c.items()}
def twins(ws,K=10):
    a=n=0
    for i in range(K,len(ws)):
        if len(ws[i])<2: continue
        n+=1; a+=any(len(p)>=2 and Lv.distance(ws[i],p)==1 for p in ws[i-K:i])
    return a/n*100
r=random.Random(0)
# Voynich auf Baustein-Ebene: Wörter als Folge von BPE-Blöcken, jeder Block ein Zeichen
seqs=bpe(V,30); bl=sorted({b for s in seqs for b in s}); bm={b:chr(0x4e00+i) for i,b in enumerate(bl)}
VB=[''.join(bm[b] for b in s) for s in seqs]
VBl=[]; i=0
for l in L:
    n=len(l[5]); VBl.append(VB[i:i+n]); i+=n
rows=[('Voynich Glyphen',[cuva(w) for w in V],[[cuva(w) for w in l[5]] for l in L]),('Voynich Bausteine (BPE30)',VB,VBl),('Rohonc Zeichen',R,[[''.join(gmap[c] for c in w) for w in l] for l in lines])]
print(f"{'':28s}{'Inventar 90%':>13}{'Zeichen/Wort':>13}{'Typen':>8}{'Doppelw':>9}{'Zwilling-Übersch.':>19}{'Kopplung':>10}   Änderungsposition")
for name,ws,ln in rows:
    s=ws[:]; r.shuffle(s)
    print(f"{name:28s}{inv90(ws):13d}{sum(map(len,ws))/len(ws):13.2f}{len(set(ws))/len(ws)*100:7.1f}%{sum(a==b for a,b in zip(ws,ws[1:]))/len(ws)*1000:8.1f}‰{twins(ws)-twins(s):+19.1f}{coupling(ln):10.3f}   {diffpos(ws)}")
