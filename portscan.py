# -*- coding: utf-8 -*-

import socket
import sys
import time

if( len(sys.argv) < 2 ):
	print '\n+ Example: python {} <host>\n'.format(sys.argv[0])
	sys.exit()

host = sys.argv[1]

print 'portscan VERSION: 1.0'
print '\nPORT    STATE   SERVICE'

for port in range(0, 10000):
	aux = ''
	aux += str(port)

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(1)
	code = s.connect_ex((str(host), int(aux)))
	time.sleep(1)

	if( code == 0 ):
		s.settimeout(0.5)
		try:
			if( len(aux) == 2 ):
				print '%d/tcp   open   %s' % (port, str(socket.getservbyport(port)))
			if( len(aux) == 3 ):
				print '%d/tcp  open   %s' % (port, str(socket.getservbyport(port)))
			if( len(aux) == 4 ):
				print '%d/tcp open   %s' % (port, str(socket.getservbyport(port)))
			else:
				pass
       
			del aux

		except socket.error:
			if( len(aux) == 3 ):
				print '%d/tcp  open   unknown' % (port)
			elif( len(aux) == 4 ):
				print '%d/tcp open   unknown' % (port)
			else:
				pass
			
			del aux
	else:
		pass
