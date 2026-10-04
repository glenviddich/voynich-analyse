exec(open('seg.py').read().split("N=150000")[0])
N=150000
corp={'Voynich':take(VL,N),'Latein':take(clean('la.txt'),N),'Deutsch':take(clean('de.txt'),N),'Tschechisch':take(clean('cs.txt'),N),'Italienisch':take(clean('it.txt'),N)}
def pairrule(lines, ctx=1):
    allj=C.Counter(); spj=C.Counter()
    for ws in lines:
        s=''.join(ws); b=set(); p=0
        for w in ws[:-1]: p+=len(w); b.add(p)
        for i in range(1,len(s)):
            j=(s[max(0,i-ctx):i],s[i:i+ctx]); allj[j]+=1; spj[j]+=i in b
    T=sum(allj.values()); S=sum(spj.values())
    acc=sum(max(spj[j],allj[j]-spj[j]) for j in allj)/T
    # Anteil der Leerzeichen-Information, die der Kontext erklärt
    def h(p): return 0 if p in(0,1) else -(p*math.log2(p)+(1-p)*math.log2(1-p))
    H0=h(S/T); Hc=sum(allj[j]/T*h(spj[j]/allj[j]) for j in allj)
    # F1 der Regel für Leerzeichen
    tp=sum(spj[j] for j in allj if spj[j]>allj[j]-spj[j]); pp=sum(allj[j] for j in allj if spj[j]>allj[j]-spj[j])
    prec=tp/pp if pp else 0; rec=tp/S; F=2*prec*rec/(prec+rec) if tp else 0
    return acc, 1-Hc/H0, F
print('Wie gut erklärt das Nachbar-Zeichenpaar die Leerzeichen?')
print(f"{'':12s}{'1+1 Zeichen: erklärt':>22}{'F1':>7}   {'2+2 Zeichen: erklärt':>22}{'F1':>7}")
for name,lines in corp.items():
    a1,i1,f1=pairrule(lines,1); a2,i2,f2=pairrule(lines,2)
    print(f'{name:12s}{i1*100:21.1f}%{f1*100:6.1f}%   {i2*100:21.1f}%{f2*100:6.1f}%')
