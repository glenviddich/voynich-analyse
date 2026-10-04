# Sternenteil (f103-f116) gegen Rezeptgattungen: Antidotarium Nicolai 1471 (archive.org McGillLibrary-osl_antidotarium_WZ230N6397a1471-19972)
# und Tesoro de' poveri 1494 (archive.org ita-bnc-in1-00000270-001). OCR-Texte per fetch_data.sh laden (ant1471.txt, tesoro.txt).
import re,collections as C,statistics as S,json
exec(open('para.py').read())
paras=[];cur=None
for l in L2:
    if l[1]!='S' or l[0].startswith('f58'): continue
    if l[4] or cur is None: cur=[l[0],[]]; paras.append(cur)
    cur[1]+=l[6]
def stats(name,ents,firsts=None):
    L=[len(e) for e in ents]; allw=C.Counter(w for e in ents for w in e); n=sum(allw.values())
    first=C.Counter(e[0] for e in ents)
    print(f'{name:28s} n={len(ents):5d} Wörter/Eintrag median {S.median(L):5.0f} ({sorted(L)[len(L)//4]}-{sorted(L)[3*len(L)//4]}) | Erstwort-Top-3 {sum(c for _,c in first.most_common(3))/len(ents)*100:4.0f}% | verschieden {len(first)} | Top-10 {sum(c for _,c in allw.most_common(10))/n*100:4.1f}%')
stats('Voynich Sterne',[p[1] for p in paras])
try:
    t=open('tesoro.txt',encoding='utf-8',errors='ignore').read(); lines=[re.sub(r'\s+',' ',l).strip() for l in t.split('\n') if l.strip()]
    st=[i for i,l in enumerate(lines) if re.match(r'^(Item|Itē|Anco|Ancora|Anchora|Ite)\b',l)]
    ents=[[w.lower() for w in re.findall(r'[A-Za-zàèéìòù]{2,}',' '.join(lines[a:b]).replace('ſ','s'))] for a,b in zip(st,st[1:]+[len(lines)])]
    stats('Tesoro de poveri 1494',[e for e in ents if 5<=len(e)<=200])
except FileNotFoundError: print('tesoro.txt fehlt')
try:
    t=open('ant1471.txt',encoding='utf-8',errors='ignore').read(); lines=[l.strip() for l in t.split('\n')]
    heads=[i for i,l in enumerate(lines) if 3<=len(l.rstrip(' .'))<=40 and re.fullmatch(r'[A-Z][A-Za-z]+( [A-Za-z]+){0,3}',l.rstrip(' .')) and len(' '.join(lines[i+1:i+4]))>80]
    ents=[[w.lower() for w in re.findall(r'[A-Za-z]{2,}',' '.join(lines[a+1:b]))] for a,b in zip(heads,heads[1:]+[len(lines)])]
    stats('Antidotarium 1471 (grob)',[e for e in ents if 30<=len(e)<=600])
except FileNotFoundError: print('ant1471.txt fehlt')
