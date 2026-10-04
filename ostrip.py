exec(open("labels.py").read().split("hits=[]")[0].replace("print(","(lambda *a,**k:0)("))
txt=C.Counter(w for p in pagew.values() for w in p)
ol=[w for _,w in lf if w.startswith('o') and len(w)>=4]
non=[w for _,w in lf if not w.startswith('o') and len(w)>=4]
f=lambda ws: sum(txt[w]>0 for w in ws)/len(ws)*100
print(f'o-Beschriftungen ({len(ol)}): stehen im Text {f(ol):.0f}% | ohne o- im Text {f([w[1:] for w in ol]):.0f}% | mit q davor (qo...) {f(["q"+w for w in ol]):.0f}%')
# Kontrolle: anderer Anfangsbuchstabe weg
for c in 'scd':
    xs=[w for _,w in lf if w.startswith(c) and len(w)>=4]
    if len(xs)>=10: print(f'{c}-Beschriftungen ({len(xs)}): im Text {f(xs):.0f}% | ohne {c}- {f([w[1:] for w in xs]):.0f}%')
# Kontrolle aus dem Fließtext: seltene o-Wörter
r=random.Random(0); rare_o=[w for w in txt if w.startswith('o') and len(w)>=4 and txt[w]<=2]
s=r.sample(rare_o,min(300,len(rare_o)))
print(f'Kontrolle seltene o-Wörter aus dem Text ({len(s)}): ohne o- im Text {sum(txt[w[1:]]>0 for w in s)/len(s)*100:.0f}%')
print('Beispiele:',', '.join(f'{w}->{w[1:]}({txt[w[1:]]})' for w in ol[:12]))
