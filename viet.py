exec(open('residual.py').read().split("VA=V")[0])
import unicodedata
TONE={'́':'A','̀':'B','̉':'C','̃':'D','̣':'E'}   # sắc huyền hỏi ngã nặng
QUAL={'̆':'w','̂':'j','̛':'z'}                              # breve circumflex horn
def tr(word):
    out=[];tone=''
    for ch in unicodedata.normalize('NFD',word.lower()):
        if ch in TONE: tone=TONE[ch]
        elif ch in QUAL: out.append(QUAL[ch])
        elif ch=='đ': out.append('f')
        elif 'a'<=ch<='z': out.append(ch)
        else: return None
    return ''.join(out)+tone if out else None
toks=[]
for tok in re.findall(r'\S+',open('vi_raw.txt',encoding='utf-8').read()):
    t=tr(re.sub(r'[^\w]','',tok))
    if t: toks.append(t)
print(f'Vietnamesisch: {len(toks)} Silben, Beispiel:',' '.join(toks[500:512]))
row('Voynich',V)
row('Vietnamesisch, Silben+Ton',toks[:len(V)])
row('Vietnamesisch, ohne Ton',[re.sub(r'[A-E]$','',t) for t in toks][:len(V)])
# Anlaut<->Rest MI normiert
INIT=sorted(['ngh','ng','nh','ch','gh','gi','kh','ph','qu','th','tr','b','c','d','f','g','h','k','l','m','n','p','r','s','t','v','x'],key=len,reverse=True)
def split(s):
    for i in INIT:
        if s.startswith(i) and len(s)>len(i): return i,s[len(i):]
    return '',s
pr=[split(re.sub(r'[A-E]$','',t)) for t in toks]; N=len(pr)
A=C.Counter(x for x,_ in pr); B=C.Counter(y for _,y in pr); AB=C.Counter(pr)
mi=sum(v/N*math.log2(v*N/(A[x]*B[y])) for (x,y),v in AB.items()); H=lambda c:-sum(v/N*math.log2(v/N) for v in c.values())
print(f'Anlaut<->Rest normierte MI: {mi/min(H(A),H(B)):.2f} | verschiedene Silben mit Ton: {len(set(toks))}')
