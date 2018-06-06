
##################################################################################


import os
import mvsfunc as mvf
import havsfunc as haf
import vapoursynth as vs


##################################################################################

core = vs.core
core.max_cache_size = 16 * 1024

source = os.path.splitext(os.path.basename(__file__))[0]
video = core.ffms2.Source(source, timecodes = source + '.txt')
video = haf.SMDegrain(video)
video = haf.SMDegrain(video, tr = 50, thSAD = 1200)
video = haf.SMDegrain(video)
video.set_output()

##################################################################################
