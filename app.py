import flask
from flask import request, jsonify  # Import objects from the Flask model

app = flask.Flask(__name__)  # Define app using Flask
app.config["DEBUG"] = True


# Create some test data for our diary Entries.
entries = [
    {'id': 0,
     'date': '07-07-2018',
     'title': 'Go to National Library',
     'body': 'The coldsleep itself was dreamless.'},
    {'id': 1,
     'date': '08-07-2018',
     'title': 'Call mum',
     'body': 'to wish her happy mothers day!.'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>An online Diary to open emotions, feelings and events</h1>
<p>A prototype APIs for GETTING all entries and one entry in an online Diary.</p>'''


@app.route('/api/v1/entries/all', methods=['GET'])
def api_all(self):
    response = jsonify(entries)
    response.status_code = 200
    return jsonify(entries)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
