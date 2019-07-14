from flask import request
import flask
import json
import sys
sys.path.insert(0, '../')
import SwapMain


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        if request.form['numbers']:
            input_list = request.form['numbers']
            SwapMain.start_theo(list(map(int, input_list.split(','))))
            return json_operation()
        else:
            return 'The credentials ain\'t right'


def json_operation():
    return json.dumps(SwapMain.operation_array)


app.run()
