import re, math, collections as C
exec(open('qtest.py').read().split("isq=lambda")[0])
# --- Kalibrierung: Culpeper, Einträge ab "_Descript._", je erste 90 Wörter
t=open('culp.txt',encoding='utf-8').read()
parts=t.split('_Descript._]')[1:]
ent=[re.findall(r"[a-z]+",p.lower())[:90] for p in parts]
ent=[e for e in ent if len(e)>=60]
other=re.findall(r"[a-z]+",open('en_epiktet.txt',encoding='utf-8').read().lower())
def finder(pages, other_words, mindf=.25, minspec=2.0, top=15):
    df=C.Counter(); tf=C.Counter()
    for p in pages:
        for w in set(p): df[w]+=1
        tf.update(p)
    on=C.Counter(other_words); N1=sum(tf.values()); N2=sum(on.values())
    rows=[]
    for w,d in df.items():
        cov=d/len(pages)
        spec=((tf[w]+.5)/N1)/((on[w]+.5)/N2)
        # mittlere relative Position des ersten Auftretens auf der Seite
        pos=[p.index(w)/len(p) for p in pages if w in p]
        if cov>=mindf and spec>=minspec: rows.append((cov,spec,sum(pos)/len(pos),w,tf[w]))
    rows.sort(reverse=True); return rows[:top]
print(f'KALIBRIERUNG Culpeper ({len(ent)} Pflanzeneinträge): Wörter auf ≥25% der Einträge UND ≥2x häufiger als in Normaltext')
for cov,spec,pos,w,n in finder(ent,other): print(f'   {w:12s} auf {cov*100:4.0f}% der Einträge | {spec:5.1f}x | steht im Schnitt bei {pos*100:3.0f}% der Seite')
# --- Voynich: Kräuterseiten vs. Rest
pagew=C.defaultdict(list); sec={}
for l in L:
    pagew[l[0]]+=l[5]; sec[l[0]]=l[1]
herb=[w for p,w in pagew.items() if sec[p]=='H' and len(w)>=40]
rest=[x for p,w in pagew.items() if sec[p]!='H' for x in w]
print(f'\nVOYNICH ({len(herb)} Kräuterseiten, Ø {sum(map(len,herb))/len(herb):.0f} Wörter): gleiche Kriterien')
rows=finder(herb,rest)
for cov,spec,pos,w,n in rows: print(f'   {w:12s} auf {cov*100:4.0f}% der Seiten | {spec:5.1f}x | steht im Schnitt bei {pos*100:3.0f}% der Seite | n={n}')
print('\n   lockerer (≥15% der Seiten, ≥3x):')
for cov,spec,pos,w,n in finder(herb,rest,.15,3.0,20): print(f'   {w:12s} auf {cov*100:4.0f}% | {spec:5.1f}x | Pos {pos*100:3.0f}% | n={n}')
import pickle; pickle.dump((herb,rest,ent),open('pw.pkl','wb'))
