import re, math, collections as C
pages={}; 
for ln in open('ZL.txt',encoding='latin-1'):
    m=re.match(r'<(f\w+)>\s+<!(.*)>',ln)
    if m: pages[m.group(1)]=dict(re.findall(r'\$(\w)=(\w+)',m.group(2)))
W=[]  # (page, word)
for ln in open('ZL.txt',encoding='latin-1'):
    m=re.match(r'<(f\w+)\.\d+,.(P\w*)>\s+(.*)',ln)
    if not m: continue
    t=re.sub(r'<[^>]*>','',m.group(3)); t=re.sub(r'\[([^:\]]*):[^\]]*\]',r'\1',t)
    t=re.sub(r'@\d+;','?',t).replace('{','').replace('}','').replace("'",'')
    for w in re.split(r'[.,\s]+',t):
        if w and re.fullmatch(r'[a-z]+',w): W.append((m.group(1),w))
def cuva(w):
    for a,b in [('cth','T'),('ckh','K'),('cph','P'),('cfh','F'),('ch','C'),('sh','S'),('iin','M'),('in','N')]: w=w.replace(a,b)
    return w
def words(fn):
    t=open(fn,encoding='utf-8',errors='ignore').read(); t=t[len(t)//20:len(t)*19//20].lower()
    t=t.replace('ä','ae').replace('ö','oe').replace('ü','ue').replace('ß','ss'); return re.findall(r'[a-z]+',t)
def h2(ws):
    s='_'.join(ws); c1=C.Counter(s); c2=C.Counter(zip(s,s[1:])); n=len(s); n2=n-1
    H1=-sum(v/n*math.log2(v/n) for v in c1.values()); H12=-sum(v/n2*math.log2(v/n2) for v in c2.values())
    return H1,H12-H1
vw=[cuva(w) for _,w in W]
print("1) Einfache Ersetzung (jedes Zeichen = ein Buchstabe)?")
for n,ws in [('Voynich',vw),('Deutsch',words('de.txt')[:len(vw)]),('Latein',words('la.txt')[:len(vw)])]:
    a,b=h2(ws); print(f"   {n:8s} h1={a:.2f}  h2={b:.2f} bit")
print("\n2) Positionszwang: Anteil eines Zeichens am Wortanfang / -ende")
pos=C.defaultdict(lambda:[0,0,0])
for w in vw:
    for i,c in enumerate(w): pos[c][0 if i==0 else (2 if i==len(w)-1 else 1)]+=1
for c,(s,m,e) in sorted(pos.items(),key=lambda x:-sum(x[1]))[:14]:
    t=s+m+e; print(f"   {c}: Anfang {s/t*100:5.1f}%  Mitte {m/t*100:5.1f}%  Ende {e/t*100:5.1f}%  (n={t})")
for n,ws in [('Deutsch',words('de.txt')[:len(vw)])]:
    p=C.defaultdict(lambda:[0,0,0])
    for w in ws:
        for i,c in enumerate(w): p[c][0 if i==0 else (2 if i==len(w)-1 else 1)]+=1
    ex=max(p.items(),key=lambda x:max(x[1][0],x[1][2])/sum(x[1]) if sum(x[1])>2000 else 0)
    print(f"   Zum Vergleich extremstes häufiges Zeichen im Deutschen: {ex[0]} {[round(v/sum(ex[1])*100,1) for v in ex[1]]}")
print("\n3) Wiederholungen: gleiches Wort direkt hintereinander")
for n,ws in [('Voynich',[w for _,w in W]),('Deutsch',words('de.txt')[:len(vw)]),('Latein',words('la.txt')[:len(vw)])]:
    r=sum(a==b for a,b in zip(ws,ws[1:])); print(f"   {n:8s} {r} mal ({r/len(ws)*1000:.1f} pro 1000 Wörter)")
print("\n4) Themen-Signal: typische Wörter je Abschnitt (log-odds vs. Rest)")
sec=C.defaultdict(C.Counter); tot=C.Counter()
names={'H':'Kräuter','B':'Badende Frauen ("biologisch")','S':'Sterne/Rezepte','P':'Pharma','A':'Astronomie','Z':'Tierkreis','C':'Kosmologie'}
for p,w in W:
    s=pages.get(p,{}).get('I','?'); sec[s][w]+=1; tot[w]+=1
N=sum(tot.values())
for s in ['H','B','S']:
    c=sec[s]; n=sum(c.values())
    sc=sorted([(math.log((c[w]+.5)/(n+.5))-math.log((tot[w]-c[w]+.5)/(N-n+.5)),w) for w in c if c[w]>=25],reverse=True)[:6]
    print(f"   {names[s]} ({n} Wörter): "+", ".join(f"{w}(x{math.exp(v):.0f})" for v,w in sc))
print("\n5) Currier-Sprachen A/B (zwei 'Dialekte'): Top-Wörter")
lang=C.defaultdict(C.Counter)
for p,w in W: lang[pages.get(p,{}).get('L','?')][w]+=1
for l in 'AB': print(f"   {l}: "+", ".join(w for w,_ in lang[l].most_common(8)))
