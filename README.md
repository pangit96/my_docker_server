# **my_docker_server**
Web application to manage docker services and its containers.

## PURPOSE:
- Managing docker-engine services
- Managing docker containers
- Launch new containers

## SET UP THIS ENVIRONMENT:
#### 1. Configure yum repolist in your linux system
        yum repolist
#### 2. Configure http service
        yum install httpd
        systemctl start httpd OR /usr/sbin/httpd
        systemctl enable httpd   
#### 3. Disable firewall and selinux security:
        setenforce 0
        systemctl disable firewalld or iptables -F
#### 4. Give apache user permissions of sudo:
        In file /etc/sudoers add this line:
        apache ALL=(ALL) NOPASSWD:ALL
#### 5. Restart httpd service
        systemctl restart httpd OR /usr/sbin/httpd
        
## LOCAL REPOSITORY:
##### Copy all the files to this apache web-server directory:
        /var/www/cgi-bin
##### Make all the files executable:
        chmod +x /var/www/cgi-bin/*.py
