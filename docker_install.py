#!/usr/bin/python2
import commands as sp

print("content-type: text/html")

status=sp.getstatusoutput("sudo yum install docker-ce -y")

if status[0]==0:
	print("location: docker.py")
	print("")
else:
	print("Error while installing")
	print("")
