# Kombinierte Epochen-Chiffre: Funktionswort-Verschmelzung + Abkürzung + Vokal-Homophone + Nullen
import itertools,time
exec(open('common.py').read())
STOP={'Latein-Rezepte':set('et in cum ad ex de ut si aut vel ac atque per ne non est sed'.split()),
      'Italienisch':set('e ed di a da in con su per che il lo la i gli le un uno una non si ne se o od al del dal nel'.split()),
      'Latein':set('et in cum ad ex de ut si aut vel ac atque per ne non est sed enim autem quod qui quae'.split())}
SUFL={'Latein-Rezepte':['ibus','orum','arum','us','um','is','ae','as','os','es','em','am','ur'],'Latein':['ibus','orum','arum','us','um','is','ae','as','os','es','em','am','ur'],
      'Italienisch':['mente','zione','are','ere','ire','ato','ata','ati','ate','o','a','e','i']}
VOW='aeiou'
def pipeline(pt,lang,fuse,abbr,homk,homo_mode,nullp,seed=0):
    r=random.Random(seed); out=[]; stop=STOP[lang]; sufl=SUFL[lang]; pend=''
    stopsym={w:chr(0x30+i%10) for i,w in enumerate(sorted(stop))}  # Ziffern als Funktionswort-Glyphen
    for w in pt:
        if fuse and w in stop: pend+=stopsym[w]; continue
        x=w
        if abbr and r.random()<abbr:
            for s in sufl:
                if len(x)>len(s)+1 and x.endswith(s): x=x[:-len(s)]+'Q'; break
            x=re.sub(r'([aeiou])[nm](?=[^aeiou])',r'\1N',x)   # Tilde für n/m vor Konsonant
        if homk>1:
            y=[]
            for i,ch in enumerate(x):
                if ch in VOW:
                    if homo_mode=='pos': k=(0 if i==0 else (2 if i==len(x)-1 else 1))%homk
                    else: k=r.randrange(homk)
                    ch=ch if k==0 else (ch.upper() if k==1 else 'J'+ch if False else {'a':'4','e':'3','i':'1','o':'0','u':'7'}[ch])
                y.append(ch)
            x=''.join(y)
        if nullp and r.random()<nullp: x=('X'+x) if r.random()<.5 else (x+'X')
        out.append(pend+x); pend=''
    return out
res=[]
for lang in ['Latein-Rezepte','Italienisch']:
    pt=PT[lang]
    base=full(pt[:NW]); print(f'{lang} unverändert: loss {loss2(base):.1f} | {show(base)}')
    for fuse,abbr,homk,mode,nullp in itertools.product([0,1],[0,0.5,1.0],[1,2,3],['rnd','pos'],[0,0.15,0.3]):
        if homk==1 and mode=='pos': continue
        ws=pipeline(pt,lang,fuse,abbr,homk,mode,nullp)[:NW]
        m=full(ws); L=loss2(m); res.append((L,lang,fuse,abbr,homk,mode,nullp,m))
res.sort(key=lambda x:x[0])
print('\nZiel Voynich:',show(TT))
print('beste Kombinationen (loss, Sprache, fuse, abbr, homophone k, modus, nullen):')
for L,lang,fuse,abbr,homk,mode,nullp,m in res[:12]: print(f'{L:7.1f} {lang:15s} fuse={fuse} abbr={abbr} hom={homk}{mode} null={nullp} | {show(m)}')
print('\nzum Vergleich: Hybridmodell Bausteinstrom+15% Kopie: loss 2.6')
