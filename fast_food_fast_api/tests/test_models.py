from django.test import TestCase, Client
from foods.models import SignUp, LogIn, Food
from datetime import date

class TestModels(TestCase):

    def setUp(self):
        self.client = Client()
        SignUp.objects.create(username='myname', email='kasule@gmail.com', password='pass')
        # Food.objects.create(
        #     user = SignUp.username, dish='matooke', desc='all kinds', price=8000, date_created= '2018-11-01')
    
    def test_signup_model(self):
        user = SignUp.objects.get(username='myname')
        self.assertEqual(user.email, 'kasule@gmail.com')

    def test_can_create_an_order_model(self):
        user = SignUp.objects.get(username='myname')
        Food.objects.create(user = user, dish='matooke', desc='all kinds', price=8000, date_created= '2018-11-01')
    

        
        

    
