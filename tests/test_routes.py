import unittest
from flask import Flask
from app.routes import app

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_analyze_message_route(self):
        response = self.client.post('/analyze_message', json={'message': 'Hello, World!'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['word_count'], 2)
            
if __name__ == '__main__':
    unittest.main()