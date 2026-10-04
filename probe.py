import sys; sys.argv=['x','Italienisch']
src=open('opt.py').read().split("lang=sys.argv[1]")[0]; exec(src)
pt=PT['Italienisch']
for hu,hp,hs,pu,sk in [(11,13,9,.34,0),(30,30,30,.34,0),(60,60,60,.34,0),(30,30,30,.34,1.5)]:
    p=dict(hu=hu,hp=hp,hs=hs,pu=pu,sk=sk,f=.62,wb=True); m=metrics(gen(p,pt))
    print((hu,hp,hs,sk),{k:round(v,2) for k,v in m.items() if k!='ld'},'loss',round(loss(m),1))
