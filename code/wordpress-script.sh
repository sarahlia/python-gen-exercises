#!/bin/bash
yum install httpd php php-mysql -y
amazon-linux-extras install -y php7.2
cd /var/www/html
wget https://wordpress.org/wordpress-5.4.1.tar.gz
tar -xzf wordpress-5.4.1.tar.gz
cp -r wordpress/* /var/www/html/
rm -rf wordpress
rm -rf wordpress-5.4.1.tar.gz
chmod -R 755 wp-content
chown -R apache:apache wp-content
yum remove 'php*'
amazon-linux-extras install php7.2
service httpd start
chkconfig httpd on