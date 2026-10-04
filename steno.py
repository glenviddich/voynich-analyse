import sys; sys.argv=['x','Latein']
exec(open('opt.py').read().split("lang=sys.argv[1]")[0])
import re
def abbr(w,heavy=False):
    w=re.sub(r'^(con|com)','C',w); w=re.sub(r'^per','P',w); w=re.sub(r'^pro','R',w); w=re.sub(r'^pr(ae|e)','E',w)
    for a,b in [('orum$','4'),('arum$','3'),('bus$','B'),('que$','Z'),('tur$','t2'),('us$','9'),('ur$','2'),('um$','u~'),('em$','e~'),('am$','a~')]:
        w=re.sub(a,b,w)
    w=re.sub(r'([aeiou])[mn](?=[bcdfgpqstv])',r'\1~',w)
    if heavy and len(w)>4: w=w[0]+re.sub(r'[aeiou]','',w[1:-1])+w[-1]
    return w
def skel(w): return w[0]+re.sub(r'[aeiou]','',w[1:]) if len(w)>1 else w
la=PT["Latein"][:NW]; ap=PT["Latein-Rezepte"][:NW]; it=PT['Italienisch'][:NW]; de=PT['Deutsch'][:NW]
print('Ziel Voynich     ',{k:round(v,2) for k,v in T.items() if k!='ld'})
for name,ws in [('Latein',la),('Latein, Schreiber-Abk.',[abbr(w) for w in la]),('Latein, starke Kontraktion',[abbr(w,True) for w in la]),
                ('Latein, nur Konsonanten',[skel(w) for w in la]),('Deutsch, nur Konsonanten',[skel(w) for w in de]),('Italienisch, starke Kontr.',[abbr(w,True) for w in it])]:
    m=metrics(ws); print(f'{name:27s}',{k:round(v,2) for k,v in m.items() if k!='ld'},'loss',round(loss(m),1))
print('Beispiel:',' '.join(abbr(w,True) for w in la[300:314]))
