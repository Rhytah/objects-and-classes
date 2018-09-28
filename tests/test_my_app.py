from project.my_app import User
import unittest

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user=User()
        
        self.sample_user= dict (
            name="Rita",
            username="Rhyath",
            age=12,
            email="saxs@mail.com",
            password="pAsw_o1d",
            gender="female"

        )
        self.second_user= dict(

            name="peter",
            username="peter",
            age=23,
            email="paxsmailom",
            password="password",
            gender=""

        )
        self.third_user=dict(
            name="olga",
            username="freshgal",
            age="old",
            email="jokes",
            password="pass",
            gender="female"

        )
        self.accounts=[{"username":"olga","password":"pass"}]
        
    def test_register_user(self):
        # self.assertEqual(len(self.accounts),1)
        self.user.signup(**self.sample_user)
        self.assertEqual(len(self.accounts),1)
    
    def test_register_similar_username_to_name(self):
        with self.assertRaises(ValueError)as context:
            self.user.signup(**self.second_user)
            self.assertTrue("Username should be different form name and not less than 4 characters" in context.exception)
   
    def test_register_user_with_invalid_email_format(self):
        with self.assertRaises(ValueError)as context:
            self.user.signup(**self.second_user)
            self.assertTrue("Please use valid email format, john@mail.com" in context.exception)
    
    def test_password_format(self):
        with self.assertRaises(ValueError)as context:
            self.user.signup(**self.third_user)
            self.assertTrue("Password should be at least 4 characters, contain a capital letter, a small letter,a digit and a special character" in context.exception)

    def test_valid_age(self):
        with self.assertRaises(ValueError)as context:
            self.user.signup(**self.third_user)
            self.assertTrue("Age should be a number higher than 0"in context.exception)

    def test_gender_input(self):
        with self.assertRaises(ValueError)as context:
            self.user.signup(**self.second_user)
            self.assertTrue("Gender should be male or female" in context.exception)

    def test_login(self):
        self.user.signup( **self.sample_user)
        response= self.user.login("peter", "password")
        self.assertEqual(response, "{} you have logged in.".format('username'))