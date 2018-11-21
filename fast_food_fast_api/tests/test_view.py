from django.test import TestCase, Client
import json

class TestView(TestCase):

    def setUp(self):
        """initialize the test client"""
        self.client = Client()

    def test_successfully_signup(self):
        """test user successfully signup"""
        details = {
            'username':'anything9',
            'email': 'anything@gmail.com',
            'password': 'pass'
        }
        res = self.client.post('/signup/', data=json.dumps(details), content_type='application/json')
        data = res.data
        self.assertTrue(data['username']=='anything9')
        self.assertEqual(res.status_code, 201)

    def test_invalid_signup_email(self):
        """test using a invalid email"""
        details = {
            'username':'anything9',
            'email': 'anything@gm',
            'password': 'pass'
        }
        res = self.client.post('/signup/', data=json.dumps(details), content_type='application/json')
        self.assertEqual(res.status_code, 400)
