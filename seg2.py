exec(open('seg.py').read().split("N=150000")[0])
# Voynich mit Info über sichere(.) / unsichere(,) Leerzeichen und ohne Trennung (Wort zusammengeschrieben)
lines=[]; kinds=[]
for ln in open('ZL.txt',encoding='latin-1'):
    m=re.match(r'<(f\w+)\.(\d+),(.)(P\w*)>\s+(.*)',ln)
    if not m: continue
    t=re.sub(r'<[^>]*>','',m.group(5)); t=re.sub(r'\[([^:\]]*):[^\]]*\]',r'\1',t)
    t=re.sub(r'@\d+;','?',t).replace('{','').replace('}','').replace("'",'')
    toks=re.split(r'([.,])',t); ws=[];ks=[]
    for x in toks:
        if x in '.,' and x: ks.append(x)
        elif x: ws.append(x)
    if all(re.fullmatch(r'[a-z]+',w) for w in ws) and len(ws)>1 and len(ks)==len(ws)-1:
        lines.append([cuva(w) for w in ws]); kinds.append(ks)
for n in (1,2):
    F,dens,scores,truth,seqs=run(lines,n)
    k=sum(truth); thr=sorted(scores,reverse=True)[k-1]
    # Score je Grenzart
    idx=0; sure=[];unsure=[]; junc=C.Counter(); juncmiss=C.Counter(); fp=C.Counter()
    for ws,ks,s in zip(lines,kinds,seqs):
        b={}; p=0
        for w,kk in zip(ws[:-1],ks): p+=len(w); b[p]=kk
        for i in range(1,len(s)):
            sc=scores[idx]; idx+=1
            if i in b:
                (sure if b[i]=='.' else unsure).append(sc>=thr)
                j=s[i-1]+'|'+s[i]; junc[j]+=1
                if sc<thr: juncmiss[j]+=1
            elif sc>=thr: fp[s[i-1]+'|'+s[i]]+=1
    print(f'n={n}: Gesamt {F*100:.1f}% | sichere Leerzeichen erkannt {sum(sure)/len(sure)*100:.1f}% (n={len(sure)}) | unsichere {sum(unsure)/len(unsure)*100:.1f}% (n={len(unsure)})')
    if n==1:
        print('   Vom Schreiber gesetzt, vom Algorithmus NICHT erwartet (häufigste):')
        print('   ',', '.join(f'{j} {juncmiss[j]}/{junc[j]}' for j,_ in juncmiss.most_common(10)))
        print('   Vom Algorithmus erwartet, aber KEIN Leerzeichen (häufigste):')
        print('   ',', '.join(f'{j} {c}' for j,c in fp.most_common(10)))
        print('   Grenze y|q bzw. y|o etc. – Anteil, wo Schreiber Leerzeichen setzt:')
        allj=C.Counter(); spj=C.Counter()
        for ws in lines:
            s=''.join(ws); bset=set(); p=0
            for w in ws[:-1]: p+=len(w); bset.add(p)
            for i in range(1,len(s)): allj[s[i-1]+s[i]]+=1; spj[s[i-1]+s[i]]+=i in bset
        for j in ['yq','yo','yC','yS','yd','Mq','Mo','lq','lo','rq','ro','oq','eq','ok','aM','ed']:
            if allj[j]>50: print(f'      {j[0]}|{j[1]}: {spj[j]/allj[j]*100:5.1f}% Leerzeichen (n={allj[j]})')
