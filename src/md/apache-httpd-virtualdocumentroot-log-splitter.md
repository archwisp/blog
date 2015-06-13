# Apache HTTPD VirtualDocumentRoot Log Splitter
The VirtualDocumentRoot configuration option in the Apache HTTPD server is
incredibly handy. The one major complaint I've heard related to it is the fact
that there is no way write separate log files based on the host name.

    ErrorLog /var/log/apache2/error.log  
    VirtualDocumentRoot /var/www/virtual-hosts/%0/www  
    LogFormat "%V:%p %h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\""
    vhost_combined  
    CustomLog /var/log/apache2/access.log vhost_combined
