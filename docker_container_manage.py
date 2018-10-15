#!/usr/bin/python2
import commands as sp

print("content-type: text/html")
print("")
print("""<h1 align='centre'>Docker Container Management Server<h1> </br>""")


cmd=sp.getoutput("sudo docker ps -a")
output=cmd.split("\n")

print("<table border='5' align='center' width=60%>")
print("""
<tr>
	<th>Image Name</th>
	<th>Container ID</th>
	<th>Container Name</th>
	<th>Status</th>
	<th>Start</th>
	<th>Stop</th>
</tr>
""")

for i in output[1:]:
	image=i.split()[1]
	container_id=i.split()[0]
	container_name=i.split()[-1]
	
	if "Exited" in i :
		status="Stopped"
	elif "Up" in i :
		status="Running"
	else:
		status="Not known"

	print("""
<tr>
<td>{0}</td>
<td>{1}</td>
<td>{2}</td>
<td>{3}</td>
<td><a href=docker_container_start.py?x={2}>Start</a></td>
<td><a href=docker_container_stop.py?x={2}>Stop</a></td>
</tr>
""".format(image,container_id,container_name,status))
print("</table> </br></br></br>")


print("""<a href="docker.py"><font size=3">Return to Docker Server</font> </a>""")

