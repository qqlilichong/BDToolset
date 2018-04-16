#################################################
###                                           ###
###                  logoNR                   ###
###                                           ###
###      by 06_taro - astrataro@gmail.com     ###
###                                           ###
###            v0.1 - 22 March 2012           ###
###                                           ###
#################################################
###
### Post-denoise filter of EraseLogo.
### Only process logo areas in logo frames, even if l/t/r/b are not set. Non-logo areas are left untouched.
###
###
### +---------+
### |  USAGE  |
### +---------+
###
### src = AviSource("input.avi")
### dlg = src.EraseLOGO("logo.lgd")
### logoNR(dlg, src, chroma=true, GPU=true, l=1280, t=40, r=-40, b=-960)
###
### dlg [clip]
### ------------------
###    Clip after delogo.
###
### src [clip]
### ------------------
###    Clip before delogo.
###
### chroma [bool, default: True]
### ------------------
###    Process chroma plane or not.
###
### GPU [bool, default: True]
### ------------------
###    Use FFT3DGPU instead of FFT3DFilter, will be ignored when "nr" is set.
###
### l/t/r/b [int, default: 0]
### ------------------
###    left/top/right/bottom pixels to be cropped for logo area.
###    Have the same restriction as Crop, e.g., no odd value for YV12.
###    logoNR only filters the logo areas in logo frames, no matter l/t/r/b are set or not.
###    So if you have other heavy filters running in a pipeline and don't care much about the speed of logoNR,
###    it is safe to left these values unset.
###    Setting these values only makes logoNR run faster, with rarely noticeable difference in result,
###    unless you set wrong values and the logo is not covered in your cropped target area.
###
### nr [string]
### ------------------
###    Set your custom nr filter to process logo areas, e.g., nr="RemoveGrain(4, 4)".
###
### +----------------+
### |  REQUIREMENTS  |
### +----------------+
###
### -> FFT3DFilter or FFT3DGPU, or your custom nr filter's requirements
### -> MaskTools2
### -> RemoveGrain
###
### +-----------+
### | CHANGELOG |
### +-----------+
###
### v0.1 - 22 Mar 2012
###      - First release
###

Function logoNR(clip dlg, clip src, bool "chroma", bool "GPU", int "l", int "t", int "r", int "b", string "nr"){

  chroma = Default(chroma, True)
  GPU    = Default(GPU,    True)
  l      = Default(l,         0)
  t      = Default(t,         0)
  r      = Default(r,         0)
  b      = Default(b,         0)

  b_crop = l==0 && t==0 && r==0 && b==0 ? false : true
  src    = b_crop ? src.Crop(l, t, r, b) : src
  last   = b_crop ? dlg.Crop(l, t, r, b) : dlg

  clp_nr = Defined(nr) ? Eval(nr)
  \                    : GPU ? FFT3DGPU(sigma=4, plane=chroma?4:0)
  \                          : FFT3DFilter(sigma=4, plane=chroma?4:0)

  logoM  = mt_lutxy(src, "x y - Abs 4 <<", U=chroma?3:1, V=chroma?3:1)
  \        .mt_expand(mode=mt_diamond(3), U=chroma?3:1, V=chroma?3:1)
  \        .RemoveGrain(19, chroma?19:-1)
  \        .mt_deflate(U=chroma?3:1, V=chroma?3:1)
  clp_nr = mt_merge(clp_nr, logoM, U=chroma?3:2, V=chroma?3:2)

  return b_crop ? Overlay(dlg, clp_nr, x=l, y=t) : clp_nr
}
