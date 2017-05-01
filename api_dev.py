from bottle import route, run

"""@route('/hello')
def hello():
    return "Hello World!"

run(host='localhost', port=8080, debug=True)

from bottle import error
@error(404)
def error404(error):
    return 'Nothing here, sorry'
"""
from bottle import static_file
@route('/all_api/<filename>')
def server_static(filename):
    return static_file(filename, root='C:/Users/sk972/Crawler/all_api')
run(host='localhost', port=8080, debug=True)    
