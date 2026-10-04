import sys; sys.argv=['x','Latein']
exec(open('opt.py').read().split("lang=sys.argv[1]")[0])
stop=set("der die das und ist in zu den von mit sich des auf fur nicht ein eine einer einem einen als auch es an er so dass sie nach wie im bei ich du wir ihr man dem was wird sind war hat haben kann nur noch wenn um aus am mir mich dir dich mein dein sein ihm ihn uns euch doch ja nun da wo hier dort schon mehr sehr zum zur oder aber denn wer soll will muss et est non ad cum ut quod qui quae sed de ex a ab per si se sunt esse enim autem vel aut nec ne iam tamen hoc haec id eius eo ea etiam atque ac quam quia ita nam a se je na v ve to ze s z i k o by jako tak ale co si jsem byl bylo by jen uz jeho ktery ktera ktere e di che il la per non un una le si con mi lo ma come piu io".split())
vtypes=[w for w,_ in C.Counter(V[:NW]).most_common()]
def code(ws):
    rk=[w for w,_ in C.Counter(ws).most_common()]
    extra=[]; r=random.Random(1)
    while len(vtypes)+len(extra)<len(rk): extra.append(r.choice(vtypes[:500])[:2]+r.choice(vtypes)[2:])
    mp=dict(zip(rk,vtypes+extra)); return [mp[w] for w in ws]
print('Ziel Voynich:',{k:round(v,2) for k,v in T.items() if k!='ld'})
for L in ['Latein','Deutsch','Tschechisch','Italienisch']:
    for mode in ['normal','Notizen']:
        ws=PT[L] if mode=='normal' else [w for w in PT[L] if w not in stop]
        m=metrics(code(ws[:NW])); print(f'{L:11s} {mode:8s}',{k:round(v,2) for k,v in m.items() if k not in('ld','h2','wl','pur','mi')},'loss',round(loss(m),1))
