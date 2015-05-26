#uwsgi --http :8000 --wsgi-file app.py --single-interpreter --enable-threads
import newrelic.agent
newrelic.agent.initialize('newrelic.ini')

@newrelic.agent.wsgi_application()
def application(environ, start_response):
	status = '200 OK'
	response_headers = [('Content-type','text/plain')]
	start_response(status, response_headers)
	return ['Hello world']
