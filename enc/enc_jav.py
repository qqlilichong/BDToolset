
#################################################################################


import os
import sys
import subprocess


#################################################################################


tool = {
    'BDTOOL': 'E:/gitpri/BDToolset',
    'X265': 'x265/x265.exe',
    'VS': 'C:/Softwares/VapourSynth/core64/vspipe.exe',
}

x265 = [
    '--preset', 'veryslow',
    '--tune', 'littlepox++',
    '--no-open-gop',
    '--no-sao',
    '--no-strong-intra-smoothing',
    '--no-rect',
    '--no-amp',
    '--y4m',
    '--input -',
]


#################################################################################


# vpy file.
tool['SOURCE'] = input('vpy file : ')

# crf.
crf = 23

# output file.
output = os.path.join(os.path.dirname(tool['SOURCE']), '%s.mkv' % crf)

# x265 params.
x265.insert(0, '--crf %s' % crf)
x265.append('-o "%s"' % output)


#################################################################################


# fix path.
for x, y in tool.items():
    if os.path.exists(y):
        continue
    y = os.path.join(tool['BDTOOL'], y)
    if not os.path.exists(y):
        print('missing : %s' % y)
        sys.exit(0)
    tool[x] = y

for x, y in tool.items():
    tool[x] = '"' + y + '"'


#################################################################################


# make command.
command = [
    tool['VS'],
    '--y4m',
    tool['SOURCE'],
    '-',
    '|',
    tool['X265'],
]

command += x265
command = ' '.join(line for line in command)


#################################################################################


# setup encoding.
print('')
print(command)
print('')

# clear old file.
if os.path.exists(output):
    os.remove(output)

# encoding...
subprocess.call(command, shell=True)

# end.
os.system('pause')


#################################################################################
