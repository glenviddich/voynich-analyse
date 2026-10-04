import random,collections as C,math
exec(open('qtest.py').read().split("isq=lambda")[0])
def lev(a,b):
    if abs(len(a)-len(b))>2: return 3
    d=list(range(len(b)+1))
    for i,ca in enumerate(a,1):
        p=d[:];d[0]=i
        for j,cb in enumerate(b,1): d[j]=min(p[j]+1,d[j-1]+1,p[j-1]+(ca!=cb))
    return d[-1]
# Wortstrom je Seite (Fließtext, Absatzreihenfolge)
pages=C.defaultdict(list)
for l in L: pages[l[0]]+=l[5]
streams=[v for v in pages.values() if len(v)>=60]
def profile(streams,maxd=30):
    hit=C.Counter();tot=C.Counter()
    for ws in streams:
        for i in range(len(ws)):
            for d in range(1,maxd+1):
                if i+d<len(ws):
                    tot[d]+=1; hit[d]+=lev(ws[i],ws[i+d])<=1
    return [hit[d]/tot[d]*100 for d in range(1,maxd+1)]
obs=profile(streams)
r=random.Random(0); sh=[]
for s in streams: t=s[:]; r.shuffle(t); sh.append(t)
base=profile(sh)
print('Abstand d: Anteil Paare mit Levenshtein<=1 (%), beobachtet / gemischt / Überschuss')
for d in range(30): print(f'{d+1:3d}  {obs[d]:5.2f}  {base[d]:5.2f}  {obs[d]-base[d]:+5.2f}')
