import re
exec(open('common.py').read())
def words(fn):
    t=open(fn,encoding='utf-8',errors='ignore').read().lower()
    t=t.replace('ä','ae').replace('ö','oe').replace('ü','ue').replace('ß','ss').replace('æ','ae').replace('œ','oe')
    t=re.sub(r'[âêîôûáéíóú]',lambda m:'aeiouaeiou'['âêîôûáéíóú'.index(m.group())],t)
    ws=re.findall(r'[a-z]+',t); return [w for w in ws if len(w)<=12]
corp={'Voynich (ZL)':V,'Mittelhochdeutsch, Nibelungenlied Hs. B (~1200)':words('mhd_nibelungen.txt'),
      'Frühneuhochdeutsch, Wittenwiler „Der Ring“ (Konstanz ~1410)':words('fnhd_wittenwiler.txt'),
      'Frühneuhochdeutsch, Ackermann aus Böhmen (Saaz 1401)':words('fnhd_ackermann.txt'),
      'Neuhochdeutsch, Faust':PT['Deutsch'],'Latein, Augustinus':PT['Latein'],'Italienisch, Dante':PT['Italienisch']}
print(f'{"Korpus":60s} {"n":>6s} {"h2":>5s} {"wl":>5s} {"typ":>5s} {"pur":>5s} {"mi":>5s} {"top10%":>6s} {"loss":>7s}')
for n,ws in corp.items():
    k=min(NW,len(ws)); m=full(ws[:k]); c=C.Counter(ws[:k]); top=sum(v for _,v in c.most_common(10))/k*100
    print(f'{n:60s} {k:6d} {m["h2"]:5.2f} {m["wl"]:5.2f} {m["typ"]:5.1f} {m["pur"]:5.1f} {m["mi"]:5.2f} {top:6.1f} {loss2(m):7.1f}')
