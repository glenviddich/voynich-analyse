import re,random,collections as C,statistics as S
exec(open('alch98.py').read().split("print('Kräuter")[0])
# UVM
ents=[];cur=None
for ln in open('uvm_entries.txt'):
    if ln.startswith('#') and not ln.startswith('##'): continue
    if ln.startswith('## '): cur=[];ents.append(cur);continue
    if cur is not None and ln.strip():
        for l in ln.strip().split('/'):
            ws=re.findall(r'[a-z]+',l.lower().replace('[','').replace(']',''))
            if ws: cur.append(ws)
# Voynich Herbal A: pages as entries, lines
vpg=C.defaultdict(list)
for l in L:
    if l[0] in seen: vpg[l[0]].append(l[5])
V=[vpg[p] for p in pgs]
def stats(name,E):
    wpe=[sum(len(l) for l in e) for e in E]; lpe=[len(e) for e in E]
    allw=[w for e in E for l in e for w in l]
    first=C.Counter(e[0][0] for e in E); lf=C.Counter(l[0] for e in E for l in e)
    top=C.Counter(allw)
    tt=[len(set(w for l in e for w in l))/sum(len(l) for l in e) for e in E]
    print(f'{name}: Einträge {len(E)}, Wörter/Eintrag median {S.median(wpe):.0f}, Zeilen/Eintrag median {S.median(lpe):.0f}, Wörter/Zeile {S.mean(wpe)/S.mean(lpe):.1f}, Typ/Token pro Eintrag {S.median(tt):.2f}')
    n=len(E); print(f'   Eintragsanfang Top-3: {[(w,c) for w,c in first.most_common(3)]} = {sum(c for _,c in first.most_common(5))/n*100:.0f}% (Top-5)')
    nl=sum(lpe); print(f'   Zeilenanfang Top-5: {lf.most_common(5)} = {sum(c for _,c in lf.most_common(5))/nl*100:.0f}%')
    print(f'   häufigstes Wort: {top.most_common(5)} ; Top-10 Anteil {sum(c for _,c in top.most_common(10))/len(allw)*100:.0f}%')
    # Wort, das in den meisten Einträgen vorkommt
    df=C.Counter(w for e in E for w in set(x for l in e for x in l))
    print(f'   in meisten Einträgen: {[(w,round(c/n*100)) for w,c in df.most_common(6)]}')
    return allw
u=stats('UVM MS 2',ents)
# Voynich gleich groß: zufällige 13 Seiten, 20 Wiederholungen
r=random.Random(3); acc=C.defaultdict(list)
stats('Voynich Kräuter A (alle 95 Seiten)',V)
sub=r.sample(V,13); stats('Voynich Kräuter A (13 zufällige Seiten)',sub)
