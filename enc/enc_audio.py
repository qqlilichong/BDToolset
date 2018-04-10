
#################################################################################


import os
import sys
import subprocess


#################################################################################


tool = {
    'BDTOOL': 'G:/BDTool',
    'EAC3TO': 'eac3to/eac3to.exe',
    'QAAC': 'qaac/qaac.exe',
}

qaac = [
    '--quality', '2',
    '--ignorelength',
    '-',
]


#################################################################################


# media file.
tool['SOURCE'] = input('media file : ')

# tvbr.
tvbr = input('tvbr (default 127) : ')
if not tvbr:
    tvbr = '127'

# output file.
output = os.path.join(os.path.dirname(tool['SOURCE']), 'audio.m4a')

# QAAC params.
qaac.insert(0, '--tvbr %s' % tvbr)
qaac.append('-o "%s"' % output)


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


# list media info.
subprocess.call(tool['EAC3TO'] + ' ' + tool['SOURCE'], shell=True)


#################################################################################


# get audio track index.
print("")
track_audio = input("audio track (default 2) : ")
if not track_audio:
    track_audio = '2'
track_audio += ':'


#################################################################################


# make command.
command = [
    tool['EAC3TO'],
    tool['SOURCE'],
    track_audio,
    'stdout.wav',
    '|',
    tool['QAAC'],
]

command += qaac
command = ' '.join(line for line in command)


#################################################################################


# setup encoding.
print('')
print(command)
print('')
os.system('pause')

# clear old file.
if os.path.exists(output):
    os.remove(output)

# encoding...
subprocess.call(command, shell=True)

# end.
os.system('pause')


#################################################################################
