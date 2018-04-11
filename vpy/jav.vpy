
##################################################################################


import os
import mvsfunc as mvf
from vapoursynth import core


##################################################################################


f_depth = {
	'use'		: 1,
	'end'		: 8,
}

f_resize = {
	'use'		: 1,
	'w'			: 1280,
	'h'			: 720,
	'k'			: 'spline64'
}


##################################################################################

video = core.ffms2.Source(os.path.splitext(os.path.basename(__file__))[0], fpsnum = 24000, fpsden = 1001)

video = core.fmtc.resample(video, w = f_resize['w'], h = f_resize['h'], kernel = f_resize['k'])
video = mvf.Depth(video, depth = f_depth['end'])

video.set_output()

##################################################################################
