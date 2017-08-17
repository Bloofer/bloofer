# Bloofer Blog  
this repository sets up [Bloofer Blog](http://jmyang.kr)  
  
###To set config files for apache2 using flask framework  
  
#####/home/username/www/routes/routes.wsgi  
  
>import sys  
sys.path.insert(0, '/home/username/www/routes')  
from routes import app as application  
  
#####/etc/hosts  
  
>127.0.0.1       localhost  
27.102.123.456  yourdomain.com       servername  
::1     localhost ip6-localhost ip6-loopback  
ff02::1 ip6-allnodes  
ff02::2 ip6-allrouters  
  
*server domain must be set properly*  
  
#####/etc/apache2/sites-enabled/my.route.conf
  
><VirtualHost *:80>  
  
  WSGIDaemonProcess routes user=username threads=5  
  WSGIScriptAlias / /home/username/www/routes/routes.wsgi  
  
  <Directory /home/username/www/routes>  
    WSGIProcessGroup routes  
    WSGIApplicationGroup %{GLOBAL}  
    Require all granted  
  
  </Directory>  
  
        ErrorLog ${APACHE_LOG_DIR}/error.log  
        CustomLog ${APACHE_LOG_DIR}/access.log combined  
  
</VirtualHost>  
  
*after setting, restart apache2 by 'service apache2 restart'*
