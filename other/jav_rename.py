import os
import re

for p in os.listdir():
	m = re.match( r'(^.+-\w+)(.*)(\.\w+$)', p )
	if m:
		os.rename( m.group( 0 ), m.group( 1 ) + m.group( 3 ) )
