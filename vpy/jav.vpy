
##################################################################################


import os
import mvsfunc as mvf
import havsfunc as haf
import vapoursynth as vs


##################################################################################


f_depth = {
	'use'		: 0,
	'begin'		: 16,
	'end'		: 8,
}

f_crop = {
	'use'		: 0,
	'top'		: 0,
	'bottom'	: 0,
	'left'		: 0,
	'right'		: 0,
}

f_resize = {
	'use'		: 0,
	'w'			: 1280,
	'h'			: 720,
	'k'			: 'spline64'
}

f_waifu2x = {
	'use'		: 0,
	'noise'		: 2,
	'scale'		: 1,
}

f_smd = {
	'use'		: 1,
	'pre'		: 1,
	'tr'		: 50,
	'thSAD'		: 1200,
}


##################################################################################

core = vs.core
core.max_cache_size = 16 * 1024

source = os.path.splitext(os.path.basename(__file__))[0]
video = core.ffms2.Source(source, timecodes = source + '.txt')

if f_depth['use']:
	video = mvf.Depth(video, depth = f_depth['begin'])
	
if f_crop['use']:
	video = core.std.CropRel(video, left = f_crop['left'], right = f_crop['right'], top = f_crop['top'], bottom = f_crop['bottom'])

if f_resize['use']:
	video = core.fmtc.resample(video, w = f_resize['w'], h = f_resize['h'], kernel = f_resize['k'])

if f_waifu2x['use']:
	video = core.caffe.Waifu2x(video, noise = f_waifu2x['noise'], scale = f_waifu2x['scale'], model = 3)

if f_smd['pre']:
    video = haf.SMDegrain(video)
    video = haf.SMDegrain(video)

if f_smd['use']:
    video = haf.SMDegrain(video, tr = f_smd['tr'], thSAD = f_smd['thSAD'])
    
if f_depth['use']:
	video = mvf.Depth(video, depth = f_depth['end'])

video.set_output()


##################################################################################
