exec(open('rohonc2.py').read().split("rows=[('Voynich Glyphen'")[0])
import numpy as np
def analyse(name, seqs, lines_seq, top_show=12):
    # seqs: list of list-of-units per word; lines_seq: list of lines, each list of seqs
    units=C.Counter(u for s in seqs for u in s); N=sum(units.values())
    pos=C.defaultdict(lambda:C.Counter())
    for s in seqs:
        if len(s)==1: pos[s[0]]['solo']+=1
        else:
            pos[s[0]]['init']+=1; pos[s[-1]]['final']+=1
            for u in s[1:-1]: pos[u]['mid']+=1
    freq=[u for u,_ in units.most_common() if units[u]>=30]
    cls={}
    for u in freq:
        c=pos[u]; t=sum(c.values()); p={k:c[k]/t for k in ('init','mid','final','solo')}
        if p['init']>=.8: cls[u]='Präfix'
        elif p['final']>=.8: cls[u]='Suffix'
        elif p['solo']+p['mid']>=.6: cls[u]='Kern'
        else: cls[u]='gemischt'
    cc=C.Counter(cls.values()); cov={k:sum(units[u] for u in cls if cls[u]==k)/N*100 for k in cc}
    print(f'\n== {name}: {len(freq)} Einheiten mit ≥30 Vorkommen')
    print('   Klassen (Anzahl / Anteil am Text): '+', '.join(f'{k} {cc[k]} / {cov[k]:.0f}%' for k in ('Präfix','Suffix','Kern','gemischt') if k in cc))
    # Stamm = Wort ohne Präfix-/Suffix-Einheiten
    def stem(s): 
        t=[u for u in s if cls.get(u) not in ('Präfix','Suffix')]; return tuple(t)
    def affixes(s): return tuple(u for u in s if cls.get(u) in ('Präfix','Suffix'))
    stems=C.Counter(stem(s) for s in seqs); 
    para=C.defaultdict(set)
    for s in seqs: para[stem(s)].add(affixes(s))
    multi=[k for k in para if stems[k]>=20]
    ps=[len(para[k]) for k in multi]
    print(f'   Stämme gesamt {len(stems)} | mit ≥20 Vorkommen {len(multi)} | Ø verschiedene Affix-Kombinationen je Stamm {np.mean(ps):.1f} (Median {np.median(ps):.0f}) | Wörter ohne Kern {sum(1 for s in seqs if not stem(s))/len(seqs)*100:.0f}%')
    # Zipf-Steigung der Stämme
    c=sorted(stems.values(),reverse=True)[:500]; x=np.log(np.arange(1,len(c)+1)); y=np.log(c)
    print(f'   Zipf-Steigung Stämme {np.polyfit(x[1:200],y[1:200],1)[0]:.2f}')
    # Kopplung: welche Paare tragen sie? letztes Affix -> erstes Affix / Kern->Kern
    def mi(p):
        if not p: return 0
        N_=len(p); a=C.Counter(x for x,_ in p); b=C.Counter(y for _,y in p); ab=C.Counter(p)
        return sum(v/N_*math.log2(v*N_/(a[x]*b[y])) for (x,y),v in ab.items())
    rr=random.Random(0)
    def coup(f):
        real=[(f(a),f(b)) for l in lines_seq for a,b in zip(l,l[1:])]; real=[(x,y) for x,y in real if x and y]
        sh=[]
        for l in lines_seq:
            l=l[:]; rr.shuffle(l); sh+=[(f(a),f(b)) for a,b in zip(l,l[1:])]
        sh=[(x,y) for x,y in sh if x and y]
        return mi(real)-mi(sh)
    print(f'   Kopplung Wortende→Wortanfang: ganze Einheit {coup(lambda s:s[-1]):.3f} ... als (letzte Einheit→erste Einheit)')
    print(f'   nur Stamm(n)→Stamm(n+1) {coup(lambda s:stem(s)[-1] if stem(s) else None):.3f} | Suffix(n)→Präfix(n+1) {coup(lambda s: s[-1] if cls.get(s[-1])=="Suffix" else None):.3f}')
    print('   Beispiele Präfix:',', '.join(u for u in freq if cls[u]=='Präfix')[:80])
    print('   Beispiele Suffix:',', '.join(u for u in freq if cls[u]=='Suffix')[:80])
    print('   Beispiele Kern:',', '.join(u for u in freq if cls[u]=='Kern')[:80])
    return cls
# Voynich-Bausteine
seqs=bpe(V,30); i=0; VL_=[]
for l in L:
    n=len(l[5]); VL_.append(seqs[i:i+n]); i+=n
analyse('Voynich Bausteine (BPE30)', seqs, VL_)
# Rohonc: Zeichen = Einheit; Namen zu kurzen Codes
Rseq=[[f'{ord(c)-0x4e00:04d}' for c in w] for w in R]; i=0; RL_=[]
for l in lines:
    n=len(l); RL_.append(Rseq[i:i+n]); i+=n
analyse('Rohonc Zeichen', Rseq, RL_)
# Kontrolle: Latein-Silben
exec(open('sylcmp.py').read().split("def unit_stats")[0].split("exec(open('residual.py')")[1].split('\n',1)[1])
la=PT['Latein'][:34000]; Ls=[syllabify(w) for w in la]; LL=[Ls[i:i+10] for i in range(0,len(Ls),10)]
analyse('Latein Silben', Ls, LL)
