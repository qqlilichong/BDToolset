
import os
import subprocess

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
	for filename in filenames:
		file = os.path.join(dirpath, filename)
		if not os.path.exists(file):
			continue
		if filename != '0000.py':
			continue

		subprocess.call(['python', file])
