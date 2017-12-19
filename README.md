# Bloofer Blog  
this repository sets up [Bloofer Blog](http://jmyang.kr)  

## Blog Outline  
<img class="img-responsive" src="https://raw.githubusercontent.com/Bloofer/bloofer_www/master/static/img/main.jpg">  
<i>Blog main page</i>  
  
</br></br>  
  
<img class="img-responsive" src="https://raw.githubusercontent.com/Bloofer/bloofer_www/master/static/img/rev.jpg">  
<img class="img-responsive" src="https://raw.githubusercontent.com/Bloofer/bloofer_www/master/static/img/std.jpg">      
<img class="img-responsive" src="https://raw.githubusercontent.com/Bloofer/bloofer_www/master/static/img/blog.jpg">  
<i>Blog posts as markdown pages (Jekyll style)</i>  
  
</br></br>  
  
<img class="img-responsive" src="https://raw.githubusercontent.com/Bloofer/bloofer_www/master/static/img/photo.jpg">  
<i>Blog photos using outside Flickr image server</i>  
  
</br></br></hr>
 
## Troubleshooting

<h3>To set config files for apache2 using flask framework</h3>  
  
<h4>/home/username/www/routes/routes.wsgi</h4>  
  
```
import sys  
sys.path.insert(0, '/home/username/www/routes')  
from routes import app as application  
```
  
<h4>/etc/hosts</h4>  
  
```
127.0.0.1       localhost  
27.102.123.456  yourdomain.com       servername  
::1     localhost ip6-localhost ip6-loopback  
ff02::1 ip6-allnodes  
ff02::2 ip6-allrouters  
```  

*server domain must be set properly*  
  
<h4>/etc/apache2/sites-enabled/my.route.conf</h4>  
  
```
＜VirtualHost *:80＞  
WSGIDaemonProcess routes user=username threads=5  
WSGIScriptAlias / /home/username/www/routes/routes.wsgi  
＜Directory /home/username/www/routes＞  
WSGIProcessGroup routes  
WSGIApplicationGroup %{GLOBAL}  
Require all granted  
＜/Directory＞  
ErrorLog ${APACHE_LOG_DIR}/error.log  
CustomLog ${APACHE_LOG_DIR}/access.log combined  
＜VirtualHost＞   
```  
  
*after setting, restart apache2 by 'service apache2 restart'*  
  
</hr>  
  
<h3>To resolve flask basic authentication problem(deployed in Apache2 WSGI)</h3>  
  
![auth_conf](https://raw.githubusercontent.com/Bloofer/bloofer_www/master/static/img/auth_conf.jpg)
  
<code>WSGIPassAuthorization On</code> line must be inserted in the apache2.conf file. As the picture above, <code>WSGIPassAuthorization On</code> must be put among the directory tag which the application is deployed.
