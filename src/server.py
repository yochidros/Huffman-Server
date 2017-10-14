from bottle import route, run, request,response,HTTPResponse
import json
from huffman import generate_image

@route('/')
def hello():
    return "<html><body><h1>Hello!!</h1></body></html>"

@route('/huffman', method='POST')
def huffman():
    data = json.load(request.body)
    print(data)
    generate_image(data['data'])
    body = {"status":"OK", "message":"Received datas!! Thank you!!"}
    r = HTTPResponse(status=200, body=body)
    r.set_header("Content-Type","application/json")
    return r



run(host='localhost', port=8000, debug=True)
