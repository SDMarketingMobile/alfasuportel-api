import bottle
from bottle import get, error, static_file
from controller.business import external

app = application = bottle.default_app()

from bottle import hook, route, response

_allowed_origin  = '*'
_allowed_methods = 'PUT, GET, POST, DELETE, OPTIONS'
_allowed_headers = 'Authorization, Origin, Accept, Content-Type, X-Requested-With'

@hook('after_request')
def enable_cors():
	'''Add headers to enable CORS'''
	response.headers['Access-Control-Allow-Origin']  = _allowed_origin
	response.headers['Access-Control-Allow-Methods'] = _allowed_methods
	response.headers['Access-Control-Allow-Headers'] = _allowed_headers

@route('/', method = 'OPTIONS')
@route('/<path:path>', method = 'OPTIONS')
def options_handler(path = None):
    return

@error(405)
def not_allowed_handler(error):
	return 'Metod not allowed!'

if __name__ == '__main__':
	bottle.debug(True)
	bottle.run(reloader=True, host="0.0.0.0")