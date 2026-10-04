import re, math, random, collections as C, unicodedata
exec(open('qtest.py').read().split("isq=lambda")[0])
def clean(fn):
    t=open(fn,encoding='utf-8',errors='ignore').read(); t=t[len(t)//10:len(t)*9//10].lower().replace('ß','ss')
    t=re.sub(r"[’'`]",'',t); t=unicodedata.normalize('NFKD',t); t=''.join(c for c in t if not unicodedata.combining(c))
    return [re.findall(r'[a-z]+',ln) for ln in t.split('\n') if len(re.findall(r'[a-z]+',ln))>1]
VL=[[cuva(w) for w in l[5]] for l in L]
def take(lines,n):
    out=[];c=0
    for l in lines:
        if c>=n: break
        out.append(l); c+=sum(map(len,l))
    return out
def run(lines, n):
    seqs=[]; bounds=[]
    for ws in lines:
        s=''.join(ws); b=set(); p=0
        for w in ws[:-1]: p+=len(w); b.add(p)
        seqs.append(s); bounds.append(b)
    def ent_model(seqs):
        cnt=C.defaultdict(C.Counter)
        for s in seqs:
            s='^'*n+s+'$'
            for i in range(n,len(s)): cnt[s[i-n:i]][s[i]]+=1
        H={}
        for k,c in cnt.items():
            t=sum(c.values()); H[k]=-sum(v/t*math.log2(v/t) for v in c.values())
        return H
    Hf=ent_model(seqs); Hb=ent_model([s[::-1] for s in seqs])
    scores=[]; truth=[]
    for s,b in zip(seqs,bounds):
        sf='^'*n+s; sb=('^'*n+s[::-1])
        L_=len(s)
        for i in range(1,L_):
            f=Hf.get(sf[i:i+n],0)                  # Entropie nach Kontext s[i-n:i]
            bk=Hb.get(sb[L_-i:L_-i+n],0)           # rückwärts: Kontext s[i:i+n] umgedreht
            scores.append(f+bk); truth.append(i in b)
    k=sum(truth); order=sorted(range(len(scores)),key=lambda i:-scores[i]); pred=set(order[:k])
    hit=sum(truth[i] for i in pred); F=hit/k
    return F, k/len(truth), scores, truth, seqs
N=150000
corp={'Voynich':take(VL,N),'Latein':take(clean('la.txt'),N),'Deutsch':take(clean('de.txt'),N),'Tschechisch':take(clean('cs.txt'),N),'Italienisch':take(clean('it.txt'),N)}
print('Trefferquote der automatisch gefundenen Wortgrenzen vs. echte Leerzeichen')
print(f"{'':12s}"+''.join(f'{"n="+str(n):>8}' for n in (1,2,3,4))+f"{'Zufall':>9}")
best={}
for name,lines in corp.items():
    row=[]
    for n in (1,2,3,4):
        F,dens,*_=run(lines,n); row.append(F)
    best[name]=max(range(4),key=lambda i:row[i])+1
    print(f'{name:12s}'+''.join(f'{x*100:7.1f}%' for x in row)+f'{dens*100:8.1f}%')
import pickle; pickle.dump(best,open('segbest.pkl','wb'))
