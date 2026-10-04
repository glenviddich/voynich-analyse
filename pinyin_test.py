exec(open('residual.py').read().split("VA=V")[0])
from pypinyin import pinyin, Style
t=open('zh.txt',encoding='utf-8').read(); t=t[len(t)//10:len(t)*9//10]
chars=[c for c in t if '一'<=c<='鿿'][:60000]
syl=[s[0] for s in pinyin(chars,style=Style.TONE3,neutral_tone_with_five=True)]
syl=[re.sub(r'[^a-z0-9]','',s) for s in syl]; syl=[s for s in syl if s]
# Variante: Ton als Buchstabe (a-e) damit nur a-z, wie Voynich-Alphabet
tonemap={'1':'a','2':'b','3':'c','4':'d','5':'e'}
syl2=[s[:-1]+tonemap[s[-1]] if s[-1] in tonemap else s for s in syl]
print('Beispiel:',' '.join(syl2[1000:1012]))
row('Voynich',V)
row('Chinesisch, Silben+Ton',syl2[:len(V)])
row('Chinesisch, Silben ohne Ton',[re.sub(r'\d','',s) for s in syl][:len(V)])
# Silben-Inventar und Teil-Unabhängigkeit (Anlaut vs Auslaut)
INIT=['zh','ch','sh','b','p','m','f','d','t','n','l','g','k','h','j','q','x','r','z','c','s','y','w']
def split(s):
    for i in INIT:
        if s.startswith(i): return i,s[len(i):]
    return '',s
pr=[split(re.sub(r'\d','',s)) for s in syl]; N=len(pr)
A=C.Counter(x for x,_ in pr); B=C.Counter(y for _,y in pr); AB=C.Counter(pr)
mi=sum(v/N*math.log2(v*N/(A[x]*B[y])) for (x,y),v in AB.items()); H=lambda c:-sum(v/N*math.log2(v/N) for v in c.values())
print(f'Chinesisch: Anlaut<->Auslaut normierte MI {mi/min(H(A),H(B)):.2f} (Voynich Blöcke 0,09-0,13; europ. Silben 0,5-0,67) | verschiedene Silben ohne Ton: {len(set(re.sub(r"\d","",s) for s in syl))}')
