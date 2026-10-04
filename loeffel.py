import re, math, random, collections as C
random.seed(1)
# --- Voynich (ZL, nur Fließtext-Absätze) ---
vw=[]
for ln in open('ZL.txt',encoding='latin-1'):
    m=re.match(r'<f\w+\.\d+,.(P\w*)>\s+(.*)',ln)
    if not m: continue
    t=re.sub(r'<[^>]*>','',m.group(2))
    t=re.sub(r'\[([^:\]]*):[^\]]*\]',r'\1',t)
    t=re.sub(r'@\d+;','?',t); t=t.replace('{','').replace('}','').replace("'",'')
    for w in re.split(r'[.,\s]+',t):
        if w and re.fullmatch(r'[a-z]+',w): vw.append(w)
def cuva(w):
    for a,b in [('cth','T'),('ckh','K'),('cph','P'),('cfh','F'),('ch','C'),('sh','S'),('iin','M'),('in','N')]: w=w.replace(a,b)
    return w
def words(fn,a,b):
    t=open(fn,encoding='utf-8',errors='ignore').read()
    t=t[len(t)*a//100:len(t)*b//100].lower()
    t=t.replace('ä','ae').replace('ö','oe').replace('ü','ue').replace('ß','ss')
    return re.findall(r'[a-z]+',t)
V='aeiou'
def loeffel(w):  # Löffelsprache: nach jedem Vokal(-cluster) "lew"+Vokal
    return re.sub(r'([aeiou]+)',lambda m:m.group(1)+'lew'+m.group(1),w)
de=words('de.txt',5,95); la=words('la.txt',5,95)
N=len(vw)
corp={'Voynich EVA':vw,'Voynich (ch,sh.. als 1 Zeichen)':[cuva(w) for w in vw],
 'Deutsch':de[:N],'Deutsch Löffelsprache':[loeffel(w) for w in de[:N]],
 'Latein':la[:N],'Latein Löffelsprache':[loeffel(w) for w in la[:N]]}
def ent(ws):
    s='_'.join(ws); c1=C.Counter(s); n=len(s)
    h1=-sum(v/n*math.log2(v/n) for v in c1.values())
    c2=C.Counter(zip(s,s[1:])); n2=sum(c2.values())
    h12=-sum(v/n2*math.log2(v/n2) for v in c2.values())
    return h1,h12-h1
def echo(ws):
    best=[]
    for L in (1,2,3):
        ctx=C.defaultdict(list)
        for w in ws:
            for i in range(len(w)-L-1): ctx[w[i+1:i+1+L]].append((w[i],w[i+L+1]))
        for k,pr in ctx.items():
            if len(pr)<300: continue
            same=sum(x==y for x,y in pr)/len(pr)
            l=C.Counter(x for x,_ in pr); r=C.Counter(y for _,y in pr); n=len(pr)
            exp=sum(l[c]*r[c] for c in l)/n/n
            best.append(((same-exp)*n,k,same,exp,n))
    best.sort(reverse=True); return best[:3]
print(f"Voynich-Wörter: {N}\n")
for name,ws in corp.items():
    h1,h2=ent(ws); ml=sum(map(len,ws))/len(ws)
    e=echo(ws)
    print(f"== {name}: Wortlänge {ml:.2f}, h1 {h1:.2f} bit, h2 {h2:.2f} bit")
    for f,k,s,x,n in e: print(f"   Echo-Muster X·'{k}'·X: {s*100:.1f}% gleich (Zufall {x*100:.1f}%) -> {f:.0f} überzählige Echos, n={n}")
