import os
import hashlib

def file_md5(file):
	md5 = hashlib.md5()
	with open(file, 'rb') as f:
		data = f.read(64 * 1024)
		while data:
			md5.update(data)
			data = f.read(64 * 1024)
		return str(md5.hexdigest())
	return None

file_hash_map = {}
for dirpath, dirnames, filenames in os.walk(os.path.dirname(__file__)):
	for filename in filenames:
		file = os.path.join(dirpath, filename)
		if not os.path.exists(file):
			continue

		md5 = file_md5(file)
		if not md5:
			continue

		if not file_hash_map.get(md5):
			file_hash_map[md5] = []

		file_hash_map[md5].append(file)

for key, val in file_hash_map.items():
	if len(val) > 1:
		print(val)

os.system('pause')
