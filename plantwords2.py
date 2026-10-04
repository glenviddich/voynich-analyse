exec(open('plantwords.py').read().split("print(f'KALIBRIERUNG")[0])
def norm(w):
    w=re.sub(r'^q','',w); w=w.replace('sh','ch').replace('cth','ckh').replace('t','k').replace('ee','e').replace('r','l')
    return w
pagew=C.defaultdict(list); sec={}; lang={}
for l in L: pagew[l[0]]+=l[5]; sec[l[0]]=l[1]; lang[l[0]]=l[2]
herb=[w for p,w in pagew.items() if sec[p]=='H' and len(w)>=40]
herbA=[w for p,w in pagew.items() if sec[p]=='H' and lang[p]=='A' and len(w)>=40]
pharmaA=[x for p,w in pagew.items() if sec[p]=='P' for x in w]
restA=[x for p,w in pagew.items() if sec[p]!='H' and lang[p]=='A' for x in w]
rest=[x for p,w in pagew.items() if sec[p]!='H' for x in w]
print(f'Kräuterseiten Dialekt A: {len(herbA)}, Pharma-Wörter: {len(pharmaA)}, sonstige A-Wörter: {len(restA)}')
for title,pages,oth in [('Varianten zusammengefasst, gegen alle anderen Seiten',[[norm(w) for w in p] for p in herb],[norm(w) for w in rest]),
                        ('Varianten zusammengefasst, nur Dialekt A, gegen übrige A-Seiten',[[norm(w) for w in p] for p in herbA],[norm(w) for w in restA]),
                        ('Ohne Zusammenfassung, nur Dialekt A, gegen übrige A-Seiten',herbA,restA)]:
    print('\n'+title)
    for cov,spec,pos,w,n in finder(pages,oth,.2,2.0,12): print(f'   {w:10s} auf {cov*100:4.0f}% | {spec:5.1f}x | Pos {pos*100:3.0f}% | n={n}')
# Welche Originalformen stecken in der Familie 'chol'?
fam=C.Counter(w for p in herb for w in p if norm(w)=='chol')
print('\nFamilie „chol“ besteht aus:',', '.join(f'{w}({c})' for w,c in fam.most_common(10)))
