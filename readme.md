Welcome to WordCount website

<h1>For mysql-connect create database </h1>
<p> by using following command: </p>
<code>create database wordcount;</code>

<h1>For mysql database connection make changes on DEFAULT DATABASE in setting.py </h1>
<code>
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wordcount',
        'USER': 'root',
        'PASSWORD': '*********',
        'HOST': 'localhost',
        'PORT': '3306',
    }
</code>

<p>According to your local setup</p>