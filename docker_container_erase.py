#!/usr/bin/python2

import commands as sp

print("content-type: text/html")

status = sp.getstatusoutput("sudo docker rm -f $(sudo docker ps -a -q )")

if status[0]==0:
	print("location: docker.py")
	print("")
else:
	print("")
	print("ERROR in erasing containers")
