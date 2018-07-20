from flask import Flask, jsonify, request #Import objects from the Flask model
app = Flask(__name__) #Define app using Flask

languages = [{'name' : 'Javascript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'It works!'})

@app.route('/lang', methods=['GET'])
def returnAll():
    return jsonify({'languages' : languages})

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    langs = [language for language in languages if language['name'] ==name]
    return jsonify({'language' : langs[0]})


@app.route('/lang', methods=['POST'])
def addOne():
    language = {}
    language['name'] = request.form['name']
    languages.append(language)

    return_val = {}
    return_val['languages'] = languages

    return jsonify(return_val)


@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):
    langs = [language for language in languages if language['name'] == name]
    langs[0]['name'] = request.json['name']
    return jsonify({'language': langs[0]})


if (__name__ == "__main__"):
    app.run(debug=True, port=8080)