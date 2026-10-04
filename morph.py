exec(open('common.py').read())
# Voynich-Wörter in Stamm + Endung zerlegen
VEND=sorted(['aiiin','aiin','ain','iin','in','eedy','edy','dy','eey','ey','y','ol','or','al','ar','am','an','al','r','l','s','d','o','e','m'],key=len,reverse=True)
def vsplit(w):
    for e in VEND:
        if w.endswith(e) and len(w)>len(e): return w[:-len(e)],e
    return w,''
vs=C.Counter(); ve=C.Counter()
for w in V: s,e=vsplit(w); vs[s]+=1; ve[e]+=1
VS=[s for s,_ in vs.most_common()]; VE=[e for e,_ in ve.most_common()]
END={'Latein':'ibus orum arum ntur tur ius ium ere are ire unt ant ent es is us um am em ae os as it at et ur re ri a o i e m s'.split(),
 'Deutsch':'ungen ung en er es em ern est et te st e n s t'.split(),
 'Tschechisch':'ami ach ovi ou em ho mu ch li la lo ly te me a e i o u y'.split(),
 'Italienisch':'zione mente ando ato ata are ere ire ano ono i e a o'.split(),
 'Latein-Rezepte':'ibus orum arum ntur tur ius ium ere are ire unt ant ent es is us um am em ae os as it at et ur re ri a o i e m s'.split()}
stop=set(open('codebook.py').read().split('stop=set("')[1].split('".split()')[0].split())
def psplit(w,ends):
    for e in sorted(ends,key=len,reverse=True):
        if w.endswith(e) and len(w)-len(e)>=2: return w[:-len(e)],e
    return w,''
def encode(ws,ends):
    sp=[psplit(w,ends) for w in ws]
    sc=[s for s,_ in C.Counter(s for s,_ in sp).most_common()]; ec=[e for e,_ in C.Counter(e for _,e in sp).most_common()]
    r=random.Random(1)
    while len(VS)<len(sc): VS.append(r.choice(VS[:300])+r.choice('ktpfdlrs')+r.choice(['ch','sh','e','o','']))
    ms=dict(zip(sc,VS)); me=dict(zip(ec,VE+['y']*99))
    return [ms[s]+me[e] for s,e in sp]
def plainword(ws):
    vt=[w for w,_ in C.Counter(V).most_common()]; rk=[w for w,_ in C.Counter(ws).most_common()]
    r=random.Random(1); ext=[r.choice(vt[:300])[:3]+r.choice(vt)[3:] for _ in range(max(0,len(rk)-len(vt)))]
    mp=dict(zip(rk,vt+ext)); return [mp[w] for w in ws]
print('ZIEL                                ',show(TT))
for L in ['Latein','Latein-Rezepte','Deutsch','Tschechisch','Italienisch']:
    for mode in ['Text','Notizen']:
        ws=PT[L] if mode=='Text' else [w for w in PT[L] if w not in stop]
        ws=ws[:NW]
        for kind,f in [('Ganzwort-Code',plainword),('Stamm+Endung-Code',lambda x:encode(x,END[L]))]:
            m=full(f(ws)); print(f'{L[:11]:11s} {mode:7s} {kind:18s}',show(m),'| loss',round(loss2(m),1))
