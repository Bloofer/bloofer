# Bloofer Blog  
this repository sets up [Bloofer Blog](http://jmyang.kr)  
  
</hr>
  
<h2>To set config files for apache2 using flask framework</h2>  
  
<h4>/home/username/www/routes/routes.wsgi</h4>  
  
<code>import sys</code>  
<code>sys.path.insert(0, '/home/username/www/routes')</code>  
<code>from routes import app as application</code>  

<h4>/etc/hosts</h4>  
  
<code>127.0.0.1       localhost</code>
<code>27.102.123.456  yourdomain.com       servername</code>
<code>::1     localhost ip6-localhost ip6-loopback</code>
<code>ff02::1 ip6-allnodes</code>
<code>ff02::2 ip6-allrouters</code>  
  
*server domain must be set properly*  
  
<h4>/etc/apache2/sites-enabled/my.route.conf</h4>  
  
<code>＜VirtualHost *:80＞  </code>  
<code> WSGIDaemonProcess routes user=username threads=5  </code>  
<code> WSGIScriptAlias / /home/username/www/routes/routes.wsgi  </code>  
<code> ＜Directory /home/username/www/routes＞  </code>  
<code>   WSGIProcessGroup routes  </code>  
<code>   WSGIApplicationGroup %{GLOBAL}  </code>  
<code>   Require all granted  </code>  
<code> ＜/Directory＞  </code>  
<code>       ErrorLog ${APACHE_LOG_DIR}/error.log  </code>  
<code>       CustomLog ${APACHE_LOG_DIR}/access.log combined  </code>  
<code>＜VirtualHost＞</code>  
  
*after setting, restart apache2 by 'service apache2 restart'*  
  
</hr>  
  
<h2>To resolve flask basic authentication problem(deployed in Apache2 WSGI)</h2>  
  
![auth_conf](https://jmyang.kr/static/img/auth_conf.jpg)
  
<code>WSGIPassAuthorization On</code> line must be inserted in the apache2.conf file. As the picture above, <code>WSGIPassAuthorization On</code> must be put among the directory tag which the application is deployed.
