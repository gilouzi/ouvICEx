# Importamos nosso app
from init_flask import app

# Importamos a biblioteca de testes
import unittest
import json

class TestHomeView(unittest.TestCase):

    def setUp(self):
        app_test = app.test_client()
        self.response = app_test.get('/home')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)
        self.assertIn('text/html', self.response.content_type)

class TestFormsPage(unittest.TestCase):

    def setUp(self):
        app_test = app.test_client()
        self.response = app_test.get('/form')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)
        self.assertIn('text/html', self.response.content_type)

class TestHistoryPage(unittest.TestCase):

    def setUp(self):
        app_test = app.test_client()
        self.response = app_test.post('/history')

    def test_get(self):
        self.assertEqual(400, self.response.status_code)
        self.assertIn('text/html', self.response.content_type)


if __name__ == '__main__':
    unittest.main()