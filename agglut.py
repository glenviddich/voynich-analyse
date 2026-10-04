exec(open('residual.py').read().split("VA=V")[0])
def clean2(fn):
    t=open(fn,encoding='utf-8',errors='ignore').read(); t=t[len(t)//10:len(t)*9//10].lower()
    t=unicodedata.normalize('NFKD',t); t=''.join(c for c in t if not unicodedata.combining(c)); return re.findall(r'[a-z]+',t)
PT['Finnisch']=clean2('fi.txt'); PT['Finnisch-Prosa']=clean2('g11940.txt'); PT['Ungarisch']=clean2('hu.txt')
# Agglutination: Stamm + Endungen -> Anf<->End-MI auf Buchstabenebene vs. Voynich
row('Voynich',V)
for L in ['Finnisch','Finnisch-Prosa','Ungarisch','Latein','Deutsch']: row(L,PT[L][:len(V)])
# Zusatz: normierte MI Stamm(erste 3) <-> Endung(letzte 2) 
def mi_norm(ws,a=3,b=2):
    pr=[(w[:a],w[-b:]) for w in ws if len(w)>=a+b]; N=len(pr)
    A=C.Counter(x for x,_ in pr); B=C.Counter(y for _,y in pr); AB=C.Counter(pr)
    mi=sum(v/N*math.log2(v*N/(A[x]*B[y])) for (x,y),v in AB.items())
    H=lambda c: -sum(v/N*math.log2(v/N) for v in c.values())
    return mi/min(H(A),H(B))
print('\nStamm(3) <-> Endung(2), normierte MI:')
for L,ws in [('Voynich',[cuva(w) for w in V])]+[(L,PT[L][:len(V)]) for L in ['Finnisch','Ungarisch','Latein','Deutsch','Italienisch']]:
    print(f'   {L:14s} {mi_norm(ws):.2f}')
