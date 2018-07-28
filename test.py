import unittest

from app import app

class testApp(unittest.TestCase):
    def set_up(self):
        self.app = app.test_client()


    def test_api_one(self):
        self.app = app.test_client()
        response = self.app.get('/api/v1/entries')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)
        

if __name__ == '__main__':
    unittest.main()
