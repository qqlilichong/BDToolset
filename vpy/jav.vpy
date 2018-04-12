
##################################################################################


import os
import mvsfunc as mvf
from vapoursynth import core


##################################################################################


f_resize = {
	'use'		: 1,
	'w'			: 1280,
	'h'			: 720,
	'k'			: 'spline64'
}


##################################################################################

source = os.path.splitext(os.path.basename(__file__))[0]
video = core.ffms2.Source(source, timecodes = source + '.txt')

video = core.fmtc.resample(video, w = f_resize['w'], h = f_resize['h'], kernel = f_resize['k'])
video = core.fmtc.bitdepth(video, bits = 8)

video.set_output()

##################################################################################
