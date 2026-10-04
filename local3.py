import json, random
exec(open('local2.py').read().split("print(f\"{'':40s}")[0])
ns={}; exec(open('opt.py').read().split("lang=sys.argv[1]")[0].replace("import re, math","import sys, re, math"),ns)
NW_old=ns['NW']; ns['NW']=34000
d=json.load(open('res_Latein-Rezepte.json')); ciph=[cuva(w) for w in ns['gen'](d['p'],ns['PT']['Latein'],seed=11)]
sc={}; src=open('selfcite2.py').read().split("r=random.Random(3)")[0].replace("import sys; sys.argv=['x','Latein']","import sys; sys.argv=['x','Latein']"); exec(src,sc); sc['NW']=34000
p=dict(a=0.0,b=0.0,K=8,m0=0.19,m2=0.32,Lmax=7); selfc=[cuva(w) for w in sc['gen'](p,5)]
for name,ws in [('Voynich echt',V),('Würfel-Chiffre (Latein)',ciph),('Selbstzitat-Modell',selfc)]:
    s=ws[:]; r.shuffle(s)
    n1,s1=band(ws,[1,2,3,4,5,6,7,8],200000); n0,s0=band(s,None,200000)
    print(f'{name:28s} fast gleich nah {n1:5.2f}% vs gemischt {n0:5.2f}% -> Faktor {n1/n0:4.2f} | identisch Faktor {s1/max(s0,1e-9):4.2f}')
