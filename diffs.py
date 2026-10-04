exec(open('common.py').read())
from rapidfuzz.distance import Levenshtein as Lv
W2=[cuva(w) for w in V]; r=random.Random(0)
def ops(a,b):
    o=Lv.editops(a,b)[0]
    if o.tag=='replace': return f'{a[o.src_pos]}->{b[o.dest_pos]}' if a[o.src_pos]<b[o.dest_pos] else f'{b[o.dest_pos]}->{a[o.src_pos]}'
    ch=b[o.dest_pos] if o.tag=='insert' else a[o.src_pos]
    pos='Anfang' if (o.src_pos==0) else ('Ende' if o.src_pos>=len(a)-(o.tag=='delete') else 'Mitte')
    return f'±{ch} ({pos})'
near=C.Counter(); far=C.Counter(); N=len(W2)
for _ in range(400000):
    i=r.randrange(8,N); j=i-r.randint(1,8); k=r.randrange(N)
    for (x,y),acc in (((W2[i],W2[j]),near),((W2[i],W2[k]),far)):
        if len(x)>=3 and len(y)>=3 and Lv.distance(x,y)==1: acc[ops(x,y)]+=1
tn=sum(near.values()); tf=sum(far.values())
print('Unterschied            nah%   fern%   Anreicherung')
for o,c in near.most_common(18): print(f'{o:20s} {c/tn*100:6.1f} {far[o]/tf*100:6.1f}  {c/tn/(far[o]/tf+1e-9):5.2f}')
# Beispiele
ex=[]; 
for i in range(1,N):
    if len(W2[i])>=4 and Lv.distance(V[i],V[i-1])==1: ex.append(V[i-1]+' '+V[i])
print('\nBeispiele direkt benachbart:', ' | '.join(ex[100:112]))
