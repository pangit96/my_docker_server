#!/usr/bin/python2
import commands as sp
import cgi
print("content-type: text/html")

form  = cgi.FieldStorage()
d_name = form.getvalue("d_name")
c_name = form.getvalue("c_name")
gui = form.getvalue("gui")

if gui=="gui_yes":
	cmd="sudo docker run -dit --name {} -e DISPLAY=:0 -v  /tmp/.X11-unix:/tmp/.X11-unix  --ipc=host {}".format(c_name, d_name)	
else:
	cmd="sudo docker run -dit --name {} {}".format(c_name, d_name)	


output = sp.getstatusoutput(cmd)
if output[0] == 0:
	print("location: docker.py")
	print("")
else:
	print("")
	print("Error while launching container")
