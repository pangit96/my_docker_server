#!/usr/bin/python2
import commands as sp

print("content-type: text/html")

status=sp.getstatusoutput("sudo systemctl start docker")

if status[0]==0:
	print("location: docker.py")
	print("")
else:
	print("Error while starting docker")
	print("")



