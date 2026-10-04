import re,collections as C
exec(open('qtest.py').read().split("isq=lambda")[0])
labs=[]
for ln in open('ZL.txt',encoding='latin-1'):
    m=re.match(r'<(f\w+)\.(\d+),(.)(\w+)>\s+(.*)',ln)
    if not m: continue
    pg=m.group(1); sec=pages.get(pg,{}).get('I','?')
    if sec not in 'ZAC': continue
    t=re.sub(r'<[^>]*>','',m.group(5)); t=re.sub(r'\[([^:\]]*):[^\]]*\]',r'\1',t).replace('{','').replace('}','').replace("'",'')
    ws=[w for w in re.split(r'[.,\s]+',t) if w and re.fullmatch(r'[a-z]+',w)]
    labs.append((pg,sec,m.group(4),ws))
Z=[(p,l,ws) for p,s,l,ws in labs if s=='Z' and l.startswith('L')]
per=C.defaultdict(list)
for p,l,ws in Z: per[p]+=ws
allt=[w for l in L for w in l[5]]; freq=C.Counter(allt)
