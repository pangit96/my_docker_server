#!/usr/bin/python2

import commands as sp

print("content-type: text/html")
print("")

print("""<h1>Docker Server<h1> """)
print("<form action='container_launch.py'>")

cmd1="sudo rpm -q docker-ce"
output1=sp.getstatusoutput(cmd1)
if output1[0]==0:
	docker_status="Installed"
else:
	docker_status="Not installed"

cmd2="sudo systemctl status docker"
output2=sp.getstatusoutput(cmd2)
if output2[0]==0:
	docker_service="Active"
else:
	docker_service="Dead"


print("<table border='5' align='center' width=60%>")
print("""
<caption>Docker Service</caption>

<tr>
	<td>Docker Software Status</td>
	<th>{}</th>
</tr>
	<td>Install Docker</td>
	<th><a href="docker_install.py">Click Here</a></th>
	
</tr>
<tr>
	<td>Docker Service Status</td>
	<th>{}</th>
</tr>
<tr>
	<td>Start Docker</td>
	<th><a href="docker_start.py">Click Here</a></th>
</tr>

<tr>
	<td>Active Docker Containers</td>
	<th>
		<select name="docker_container">
		<option selected>container id | name</option>	
""".format(docker_status,docker_service))


cmd4="sudo docker ps"
output4=sp.getoutput(cmd4)
container_list=output4.split("\n")
for i in container_list[1:]:
	print("<option>"+i.split()[0]+" | "+i.split()[9]+"</option>")
print("""
	</select></th>
</tr>


<tr>
	<td>Erase All Containers</td>
	<th><a href="docker_container_erase.py">Click Here</a></th>
</tr>

<tr>
	<td>Manage Containers</td>
	<th><a href="docker_container_manage.py">Click Here</a></th>
</tr>

</table>
</br>
""")

print("""
<table border='5' align='center' width=60%>
<caption>Launch New Container<caption>

<tr>
	<td>Docker Images</td>
	<th>
		<select name="d_name">
	<option selected>docker_images</option>
	
""".format(docker_status,docker_service))

cmd3="sudo docker images"
output3=sp.getoutput(cmd3)
image_list=output3.split("\n")
for i in image_list[1:]:
	print("<option>"+i.split()[0]+":"+i.split()[1]+"</option>")


print("""
	</select></th>
</tr>
<tr>

<tr>
	<td>Container Name</td>
	<td><input type="text" name="c_name" placeholder="Type container name here "><br></td>
</tr>

<tr>
	<td>Does you container require GUI</td> 
	<td>Yes <input type='radio' name='gui' value='gui_yes' />
	     No <input type='radio' name='gui' value='gui_no' /></td>
</tr>

</table>
""")

print("""
<table border='0' align='center' width=60%>
<tr>
	<td><input type='submit' /><input type="reset" /></td>
<tr>
</table>
""")
print("</form>")
