
PATH = "E:\gitpri\BDToolset\AvsPmod\avs\plugins\"
LoadPlugin(PATH + "mvtools2.dll")
LoadPlugin(PATH + "mt_masktools-26.dll")
LoadPlugin(PATH + "ffms2.dll")
Import(PATH + "SMDegrain v.2.2d.avsi")

ffvideosource("G:\REMUX\0001\Planet.Earth.EP05.2006.Ric.mkv")
Spline64Resize(1280, 720)
#smdegrain()
#smdegrain()
