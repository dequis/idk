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

start tmux, python2 main.py

nginx config:

    server {
        server_name idk.dequis.org;
        root /what;
        location / {
            proxy_pass http://localhost:8000/;
        }
    }

[link to production server (do not hack pls)](http://idk.dequis.org)
