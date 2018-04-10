#################################################################################


import os
import subprocess
import win32clipboard as w
import win32con


#################################################################################


def getClipboard():
	w.OpenClipboard()
	d = w.GetClipboardData(win32con.CF_TEXT)
	w.CloseClipboard()
	return d.decode('gbk')


#################################################################################


aria2 = 'G:/BDTool/aria2/aria2c.exe -x12 -s12 --file-allocation=none'
url = input('url : ')
if not url:
	url = getClipboard()

aria2 = '%s "%s"' % (aria2, url)

# downloading...
subprocess.call(aria2, shell=True)

# end.
os.system('pause')


#################################################################################
