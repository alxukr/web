
sudo rm -rf /etc/nginx/sites-enabled/default

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test

sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/djask.py /etc/gunicorn.d/djask.py

sudo /etc/init.d/nginx restart
#sudo nginx
sudo /etc/init.d/gunicorn stop
sudo gunicorn -D -c /etc/gunicorn.d/hello.py hello:app
sudo gunicorn -D -c /etc/gunicorn.d/djask.py ask.wsgi:application
#sudo /etc/init.d/gunicorn strat
