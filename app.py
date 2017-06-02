import bottle
from bottle import route, run, template
from raven import Client
from raven.contrib.bottle import Sentry

app = bottle.app()
app.catchall = False

client = Client('https://345f7e5775b14e56a7d4e5b1b05652d2:43f75fb855c74195bcba9db8cb33907f@sentry.io/175151')
app = Sentry(app, client)

@route('/hello/<name>')
def index(name):
    x / 0
    return template('<b>Hello {{name}}</b>!', name=name)

run(app=app, host='localhost', port=8000)
