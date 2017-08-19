from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *
from flask import Flask, request, jsonify, g
from flaskmimerender import mimerender
from hermesmodel import Element, Function
import jsonpickle, pprint, json


e = [ Element('Hair Dryer'),
      Element('Air Heating System'),
      Element('Power and Control System'),
      Element('Blower System'),
      Element('(Wet) Hair'),
      Element('Mains'),
      Element('Air (Ambient)'),
      Element('Operator') ]

f = [ Function(e[0], e[1], "Heats Air"),
      Function(e[2], e[1]),
      Function(e[2], e[3], "Controls"),
      Function(e[3], e[0], "Blows Air"),
      Function(e[0], e[4], "Dries"),
      Function(e[5], e[0], "Powers"),
      Function(e[6], e[0], "Provides Heating Medium"),
      Function(e[7], e[0], "Controls") ]

render_xml = lambda **args: jsonpickle.encode(args)
render_json = lambda **args: jsonpickle.encode(args)
render_html = lambda **args: jsonpickle.encode(args)
render_txt = lambda message: message

app = Flask(__name__)

@app.route('/')
@mimerender(
    default = 'json',
    html = render_html,
    xml  = render_xml,
    json = render_json,
    txt  = render_txt
)
def index():
    if request.method == 'GET':
        return { "elements": e, "functions": f }

@app.before_request
def before():
    pprint.pprint( (request.method,
                    request.endpoint,
                    request.headers) )

def save_response(resp):
    resp_data = {}
    #resp_data['uuid'] = uuid
    resp_data['status_code'] = resp.status_code
    resp_data['status'] = resp.status
    resp_data['headers'] = dict(resp.headers)
    resp_data['data'] = resp.response
    return resp_data

@app.after_request
def after(resp):
    resp.headers.add('Access-Control-Allow-Origin', '*')
    resp.headers.add('Access-Control-Allow-Headers', 'Content-Type, X-Token')
    resp.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
    resp_data = save_response(resp)
    print('Response:: ', json.dumps(resp_data, indent=4))
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=True)
