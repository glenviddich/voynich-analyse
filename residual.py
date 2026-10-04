exec(open('stream.py').read().split("train=V[:NW]")[0])
import numpy as np
def remove_copies(ws, K, maxd, only_variants=False):
    keep=[]; cw=[cuva(w) for w in ws]; removed=0
    for i,w in enumerate(cw):
        prev=cw[max(0,i-K):i]
        hit=any((Lv.distance(w,p)<=maxd and (p!=w or not only_variants)) for p in prev if len(p)>=2) if len(w)>=2 else False
        if hit: removed+=1
        else: keep.append(ws[i])
    return keep, removed/len(ws)*100
def twins(ws, K=10):
    ws=[cuva(w) for w in ws]; a=n=0
    for i in range(K,len(ws)):
        w=ws[i]
        if len(w)<3: continue
        n+=1; a+=any(len(p)>=3 and Lv.distance(w,p)==1 for p in ws[i-K:i])
    return a/n*100
def zipf(ws):
    c=sorted(C.Counter(ws).values(),reverse=True)[:1000]
    x=np.log(np.arange(1,len(c)+1)); y=np.log(c); return np.polyfit(x[1:200],y[1:200],1)[0]
def syl(ws):  # Silben-/Blockebene
    return ws
def row(name,ws):
    m=ev(ws[:NW]); s=ws[:]; random.Random(0).shuffle(s)
    tw=twins(ws[:NW]); tws=twins(s[:NW])
    print(f'{name:34s} h2 {m["h2"]:.2f} | Wortl {m["wl"]:.1f} | Typen {m["typ"]:4.1f}% | Doppelw {m["rep"]:4.1f}‰ | Pos {m["pur"]:.0f}% | Anf↔End {m["mi"]:.2f} | Zwilling-Überschuss {tw-tws:+.1f} | Zipf {zipf(ws):.2f} | Koppl {m["koppl"]:.3f}')
VA=V  # ganzer Text
print('Anteil entfernt in Klammern\n')
row('Voynich original',VA)
for K,d,ov,lab in [(3,1,True,'nur Varianten, letzte 3'),(10,1,True,'nur Varianten, letzte 10'),(10,1,False,'Varianten+identisch, letzte 10')]:
    r_,p=remove_copies(VA,K,d,ov); row(f'ohne Kopien: {lab} ({p:.0f}%)',r_)
print()
for L in ['Latein','Latein-Rezepte','Deutsch','Tschechisch','Italienisch']:
    row(L,PT[L][:len(VA)])
r_,p=remove_copies(PT['Latein'][:len(VA)],10,1,True); row(f'Latein, gleiche Entfernung ({p:.0f}%)',r_)
