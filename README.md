# Emoticon voting simulator 2014

idk

    00:12 <+dx> Wally: i want to feel young again, make shitty webapps in 30 minutes and give zero fucks about scalability or good practices
    00:18 <@Wally> HELL YES LETS DO IT

depends on gspread, jinja2. includes bundled bottle.py and clouderdb (AKA fuckitdb)

database configuration goes in a file called `dual_ec_drbg` with `username:password`

## screenshot

![](http://dump.dequis.org/soSxV.png)

## database schema

![](http://dump.dequis.org/8QHRf.png)

## deploying to production

now with fastcgi because i was kinda tired of the thing dying all the time

start tmux, python2 main.py, chmod 777 fcgi.sock

nginx config:

    server {
        server_name idk.dequis.org;
        root /what;
        location / {
            include fastcgi_params;
            fastcgi_param SCRIPT_NAME "";
            fastcgi_pass unix:/home/dx/web/idk/fcgi.sock;
        }
    }


[link to production server (do not hack pls)](http://idk.dequis.org)
