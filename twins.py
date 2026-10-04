exec(open('common.py').read())
def twins(ws, K=10):
    ws=[cuva(w) for w in ws]; a=b=n=0
    for i in range(K,len(ws)):
        w=ws[i]
        if len(w)<3: continue
        n+=1; prev=ws[i-K:i]
        a+=any(len(p)>=3 and Lv.distance(w,p)==1 for p in prev)
        b+=w in prev
    return a/n*100, b/n*100
def shuf(ws):
    s=ws[:]; random.Random(0).shuffle(s); return s
print(f"{'':16s}{'Fast-Zwilling in letzten 10':>30}{'(gemischt)':>12}{'identisch in letzten 10':>26}{'(gemischt)':>12}")
for name,ws in [('Voynich',V[:NW]),('Voynich alles',V),('Latein',PT['Latein'][:NW]),('Latein-Rezepte',PT['Latein-Rezepte'][:NW]),('Deutsch',PT['Deutsch'][:NW]),('Tschechisch',PT['Tschechisch'][:NW]),('Italienisch',PT['Italienisch'][:NW])]:
    a,b=twins(ws); c,d=twins(shuf(ws)); print(f'{name:16s}{a:29.1f}%{c:11.1f}%{b:25.1f}%{d:11.1f}%')
