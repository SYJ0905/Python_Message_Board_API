# Flask Message Board Restful API

## Development

install requirements

```
pip install -r requirements.txt
```

set database url and app

```
### Windows
$env:DATABASE_URL="mysql+pymysql://root:MySQL0905@localhost:3306/message_board"
$env:FLASK_APP="src:create_app()"

### Mac
export DATABASE_URL=mysql+pymysql://root:MySQL0905@localhost:3306/message_board
export FLASK_APP="src:create_app()"
```

inital database tables

```
flask db init
flask db migrate
flask db upgrade
```

run the application

```
$ flask run
 * Tip: There are .env files present. Do "pip install python-dotenv" to use them.
 * Serving Flask app "src:create_app()"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

## Testing

```
pip install -r requirements.txt
python -m unittest discover
```

## Production

install requirements

```
pip install -r requirements.txt
```

set database url and app

```
### Windows

$env:DATABASE_URL="mysql+pymysql://root:MySQL0905@localhost:3306/message_board"
$env:FLASK_APP="src:create_app()"

### Mac

export DATABASE_URL=mysql+pymysql://root:MySQL0905@localhost:3306/message_board
export FLASK_APP="src:create_app()"
```

inital database tables

```
flask db init
flask db migrate
flask db upgrade
```

run the application

```
pip install gunicorn
gunicorn -w 4 --bind=0.0.0.0:8000 restdemo.wsgi:application
```
