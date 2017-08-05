from flask import Flask, request, jsonify
from flaskmimerender import mimerender
from hermesmodel import Element, Function
import jsonpickle


render_xml = lambda message: '<hermesModel>%s</hermesModel>' % message
render_json = lambda **args: jsonpickle.encode(args)
render_html = lambda message: '<html><body>%s</body></html>' % message
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

    if request.method == 'GET':
        return { "elements": e, "functions": f }

if __name__ == "__main__":
    app.run(debug=True)
