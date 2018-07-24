import flask_testing
from unittest import TestCase
from flask import jsonify
import app


class testApp(TestCase):

    def test_api_all(self):
        result = app.api_all()
        response = jsonify(result)
        response.status_code = 200
        self.assertequal(response.status_code, 200)


    def test_api_one(self):
        assert (type(id) == int)
        assert (len(id) == 0), "Abort 404"
        results = []
        response = jsonify(results)
        self.assertequal(response.status_code, "Error: id should be an integer provided.")



    def test_api_addone(id):
        assert (type(id) == int)
        results = []
        response = jsonify(results)
        id.assertequal(response.status_code, "Error: id should be an integer provided.")


    def test_api_update(id):
        assert (type(id) == int)
        results = []
        response = jsonify(results)
        id.assertequal(response.status_code, "Error: id should be an integer provided.")

