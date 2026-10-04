import re,collections as C
exec(open('tests.py').read().split('vw=[cuva')[0])
L2=[]
for ln in open('ZL.txt',encoding='latin-1'):
    m=re.match(r'<(f\w+)\.(\d+),(.)(P\w*)>\s+(.*)',ln)
    if not m: continue
    raw=m.group(5); ps='<%>' in raw; pe='<$>' in raw
    t=re.sub(r'<[^>]*>','',raw); t=re.sub(r'\[([^:\]]*):[^\]]*\]',r'\1',t)
    t=re.sub(r'@\d+;','?',t).replace('{','').replace('}','').replace("'",'')
    ws=[w for w in re.split(r'[.,\s]+',t) if w and re.fullmatch(r'[a-z]+',w)]
    if ws:
        pg=pages.get(m.group(1),{}); L2.append((m.group(1),pg.get('I','?'),pg.get('L','?'),pg.get('H','?'),ps,pe,ws))
