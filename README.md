<h1 align="center">Hoodka workshop</h1>
<h3 align="center">A Single page with Django Template and Sqlite </h3>
<p align="center">

</p>


# Demo
<p align="center">
<img src="./docs/db-diagram.png" width="100%">
</p>


# How to use
You must have [Python](http://python.org/) installed.

create virtualenv and activate

Then run ```pip install -r requirements.txt``` to install dependencies.

cp `.env-sample` to `.env`

```bash
py manage.py makemigrations
py manage.py migrate

py manage.py createsuperuser
py manage.py runserver
```




