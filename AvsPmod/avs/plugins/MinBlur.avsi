function MinBlur(clip clp, int r, int "uv")
{
uv   = default(uv,3)
uv2  = (uv==2) ? 1 : uv
rg4  = (uv==3) ? 4 : -1
rg11 = (uv==3) ? 11 : -1
rg20 = (uv==3) ? 20 : -1
medf = (uv==3) ? 1 : -200

RG11D = (r==1) ? mt_makediff(clp,clp.removegrain(11,rg11),U=uv2,V=uv2)
 \    : (r==2) ? mt_makediff(clp,clp.removegrain(11,rg11).removegrain(20,rg20),U=uv2,V=uv2)
 \    :          mt_makediff(clp,clp.removegrain(11,rg11).removegrain(20,rg20).removegrain(20,rg20),U=uv2,V=uv2)
RG4D  = (r==1) ? mt_makediff(clp,clp.removegrain(4,rg4),U=uv2,V=uv2)
 \    : (r==2) ? mt_makediff(clp,clp.medianblur(2,2*medf,2*medf),U=uv2,V=uv2)
 \    :          mt_makediff(clp,clp.medianblur(3,3*medf,3*medf),U=uv2,V=uv2)
DD    = mt_lutxy(RG11D,RG4D,"x 128 - y 128 - * 0 < 128 x 128 - abs y 128 - abs < x y ? ?",U=uv2,V=uv2)
clp.mt_makediff(DD,U=uv,V=uv)
return(last)
}