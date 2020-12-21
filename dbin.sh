sudo /etc/init.d/mysql start
mysql -uroot -e "create database dbweb;"
mysql -uroot -e "grant all privileges on dbweb.* to 'box'@'localhost' with grant option;"
~/web/ask/manage.py makemigrations
~/web/ask/manage.py migrate
