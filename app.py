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


@app.route('/api/v1/entries', methods=['GET'])
def api_one():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for entry in entries:
        if entry['id'] == id:
            results.append(entry)
    return jsonify(results)


@app.route('/api/v1/entries/all', methods=['POST'])  # Post a new entry in the dictionary
def api_addone():
    entry = {'id':request.form['id'], 'title':request.form['title'], 'date':request.form['date'], 'body':request.form['body']}
    entries.append(entry)  # adds an entry to our diary
    return jsonify(entries)


@app.route('/api/v1/entries/<entryid>',methods=['PUT'])  # Update an entry in the dictionary
def api_update(entryid):
    en = [entry for entry in entries if (entry['id'] == entryid)]
    if 'date' in request.json:
        en[0]['date'] = request.json['date']
    if 'title' in request.json:
        en[0]['title'] = request.json['title']
    if 'body' in request.json:
        en[0]['body'] = request.json['body']
    return jsonify({'entry':en[0]})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
