
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
    '--tune', 'vcb-s++',
    '--deblock', '-1:-1',
    '--ctu', '32',
    '--pbratio', '1.2',
    '--cbqpoffs', '-2',
    '--crqpoffs', '-2',
    '--me', '3',
    '--subme', '3',
    '--merange', '44',
    '--rdoq-level', '2',
    '--rc-lookahead', '80',
    '--scenecut', '40',
    '--qcomp', '0.65',
    '--ref', '4',
    '--keyint', '360',
    '--min-keyint', '1',
    '--bframes', '6',
    '--aq-mode', '2',
    '--aq-strength', '0.9',
    '--rd', '4',
    '--psy-rd', '2.0',
    '--psy-rdoq', '3.0',
    '--no-open-gop',
    '--no-sao',
    '--no-strong-intra-smoothing',
    '--no-rect',
    '--no-amp',
    '--b-intra',
    '--weightb',
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
