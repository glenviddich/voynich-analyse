exec(open('stream.py').read().split("train=V[:NW]")[0])
def analyse(name, ws, merges):
    seqs=bpe(ws,merges); seqs=[s for s in seqs if len(s)>=2]
    rep=sum(len(set(s))<len(s) for s in seqs)/len(seqs)*100
    # Reihenfolge-Strenge: für Blockpaare (A,B) beide Richtungen zählen
    fwd=C.Counter()
    for s in seqs:
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i]!=s[j]: fwd[(s[i],s[j])]+=1
    pairs={tuple(sorted(k)) for k in fwd}; strict=tot=0
    for a,b in pairs:
        x,y=fwd[(a,b)],fwd[(b,a)]
        if x+y>=20: tot+=1; strict+= max(x,y)/(x+y)>=0.95
    # Kontrolle: Blöcke innerhalb der Wörter mischen
    r=random.Random(0); sh=[]
    for s in seqs: t=s[:]; r.shuffle(t); sh.append(t)
    rep_sh=sum(len(set(s))<len(s) for s in sh)/len(sh)*100
    print(f'{name:22s} Blöcke/Wort {sum(map(len,seqs))/len(seqs):.2f} | Wörter mit doppeltem Block {rep:4.1f}% (gemischt {rep_sh:4.1f}%) | Blockpaare mit fester Reihenfolge (≥95%): {strict}/{tot} = {strict/max(tot,1)*100:.0f}%')
analyse('Voynich (20 Merges)',V,20)
analyse('Voynich (40 Merges)',V,40)
for L in ['Latein','Finnisch','Deutsch']:
    PT.setdefault(L,None)
import unicodedata
def clean2(fn):
    t=open(fn,encoding='utf-8',errors='ignore').read(); t=t[len(t)//10:len(t)*9//10].lower()
    t=unicodedata.normalize('NFKD',t); t=''.join(c for c in t if not unicodedata.combining(c)); return re.findall(r'[a-z]+',t)
analyse('Latein (BPE 100)',PT['Latein'][:len(V)],100)
analyse('Finnisch (BPE 100)',clean2('fi.txt')[:len(V)],100)
analyse('Deutsch (BPE 100)',PT['Deutsch'][:len(V)],100)
