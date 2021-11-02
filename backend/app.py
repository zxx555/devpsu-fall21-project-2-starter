from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import json

# Use this file as the flask app source if selected
app = Flask(__name__)

# enable CORS
CORS(app)

TO_DO_LIST = [
    {
        'name': 'DevPSU Project 1',
        'deadline': '10-19-2021',
        'completed': True,
    },
    {
        'name': 'DevPSU Project 2',
        'deadline': '11-9-2021',
        'completed': False,
    },
    {
        'name': 'CMPSC Final',
        'deadline': '12-15-2021',
        'completed': False,
    }
]

SHOPPING = [
	{
		'item': 'Tomato',
		'number': '2',
		'completed': True,
	},
	{
		'item': 'Potato',
		'number': '5',
		'completed': False,
	}
]


# Handle Routing for the app
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_name(name=None):
    return render_template('hello.html', name=name)

@app.route('/parks')
def read_users():

    # Read the parks.json file and store it as parks
    with open('parks.json', 'r') as f:
        parks = json.load(f)

    return render_template('parks.html', parks=parks)

@app.route('/todolist', methods=['GET', 'POST'])
def index():

    response_dict = {
        'status': 'success',
        'message': '',
        'to_do_list': TO_DO_LIST
    }

    if request.method == 'POST':
        # update the to do list
        TO_DO_LIST.clear()
        TO_DO_LIST.extend(request.get_json())
        response_dict['message'] = 'List updated'
    else:
        # return default list
        response_dict['message'] = 'List acquired'

    return jsonify(response_dict)

@app.route('/shoppinglist', methods=['GET', 'POST'])
def index():

    response_dict = {
        'status': 'success',
        'message': '',
        'shopping': SHOPPING
    }

    if request.method == 'POST':
        # update the to do list
        SHOPPING.clear()
        SHOPPING.extend(request.get_json())
        response_dict['message'] = 'List updated'
    else:
        # return default list
        response_dict['message'] = 'List acquired'

    return jsonify(response_dict)
# If this file is executed, run the app
if __name__ == "__main__":
    app.run()
