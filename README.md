# LaravelENV

Environment Laravel used to store a configuration on the website.

Example file .env : 
```
APP_ENV=local
APP_KEY=base64:B6Oc3R8cYDv3tJXn26LlMKIhmZlItr84LDgdixSbKxQ=
APP_DEBUG=true
APP_LOG_LEVEL=debug
APP_URL=http://localhost

DB_CONNECTION=mysql
DB_HOST=localhost
DB_PORT=3306
DB_DATABASE=database
DB_USERNAME=udatabase
DB_PASSWORD=pdatabase

MAIL_DRIVER=smtp
MAIL_HOST=boxxxx.bluehost.com
MAIL_PORT=465
MAIL_USERNAME=noreply@xxxxx.xxxx
MAIL_PASSWORD=xxxxxx
MAIL_ENCRYPTION=ssl
```
This configuration can be used to retrieve SMTP / Database.

## How to use?
$ python -V

Python 2.7.12

$ git clone https://github.com/zerobyte-id/LaravelENV.git

$ cd LaravelENV/

$ python eNv.py

<img src="Screenshot/Laravel-Screenshot.png">

## How to secure .env file in laravel using file permission?

Add this code in .htaccess file
```
<Files .env>
  Order allow,deny
    Deny from all
</Files>
```
Reference : https://stackoverflow.com/questions/47352541/how-to-secure-env-file-in-laravel-using-file-permission

