
#################################################################################


import os
import sys
import subprocess


#################################################################################


tool = {
    'BDTOOL': 'E:/gitpri/BDToolset',
    'FFMPEG': 'ffmpeg/ffmpeg.exe',
}

ffmpeg = [
    '-c:v copy',
    '-c:a aac',
    '-q:a 1.0',
]


#################################################################################


# media file.
tool['SOURCE'] = input('media file : ')

output = os.path.join(os.path.dirname(tool['SOURCE']), 'ffaac_' + os.path.basename(tool['SOURCE']))

# QAAC params.
ffmpeg.append('"%s"' % output)


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
    tool['FFMPEG'],
    '-i',
    tool['SOURCE'],
]

command += ffmpeg
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
