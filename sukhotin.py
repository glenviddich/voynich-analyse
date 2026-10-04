import re, random, collections as C, unicodedata
exec(open('qtest.py').read().split("isq=lambda")[0])
def cuva(w):
    for a,b in [('cth','T'),('ckh','K'),('cph','P'),('cfh','F'),('ch','C'),('sh','S'),('iin','M'),('in','N')]: w=w.replace(a,b)
    return w
def sukhotin(words):
    chars=sorted(set(''.join(words))); idx={c:i for i,c in enumerate(chars)}; n=len(chars)
    M=[[0]*n for _ in range(n)]
    for w in words:
        for a,b in zip(w,w[1:]):
            if a!=b: M[idx[a]][idx[b]]+=1; M[idx[b]][idx[a]]+=1
    rows=[sum(M[i]) for i in range(n)]; vow=[]; cons=set(range(n))
    while True:
        best=max(cons,key=lambda i:rows[i]); 
        if rows[best]<=0: break
        vow.append(best); cons.remove(best)
        for i in cons: rows[i]-=2*M[i][best]
    V=set(vow)
    # Alternation strength: share of bigrams that are V-C or C-V
    tot=alt=0
    for w in words:
        for a,b in zip(w,w[1:]): tot+=1; alt+=(idx[a] in V)!=(idx[b] in V)
    return ''.join(chars[i] for i in vow), alt/tot*100
def clean(fn):
    t=open(fn,encoding='utf-8',errors='ignore').read(); t=t[len(t)//10:len(t)*9//10].lower().replace('ß','ss')
    t=unicodedata.normalize('NFKD',t); t=''.join(c for c in t if not unicodedata.combining(c)); return re.findall(r'[a-z]+',t)
r=random.Random(0)
V=[cuva(w) for l in L for w in l[5]]
tests=[('Voynich (ch,sh,… als 1 Zeichen)',V),('Voynich EVA roh',[w for l in L for w in l[5]]),('Latein',clean('la.txt')[:34000]),('Deutsch',clean('de.txt')[:34000]),('Finnisch',clean('fi.txt')[:34000])]
# Kontrolle: Latein mit zufällig permutiertem Alphabet (Ersetzung) – Vokale sollten trotzdem gefunden werden
la=clean('la.txt')[:34000]; al='abcdefghijklmnopqrstuvwxyz'; p=list(al); r.shuffle(p); tab=dict(zip(al,p))
tests.append(('Latein, Buchstaben vertauscht',[''.join(tab[c] for c in w) for w in la]))
# Kontrolle: zufällige Zeichenfolgen mit Voynich-Häufigkeiten
freq=C.Counter(''.join(V)); chars=list(freq); wts=[freq[c] for c in chars]
tests.append(('Zufall, Voynich-Häufigkeiten',[''.join(r.choices(chars,wts,k=len(w))) for w in V[:34000]]))
for name,ws in tests:
    v,a=sukhotin(ws); print(f'{name:34s} „Vokale“: {v:14s} Wechselanteil V↔K: {a:.0f}%')
