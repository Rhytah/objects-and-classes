from project.my_app import User
import unittest

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user=User()
        self.accounts=self.user.accounts
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
            age=-4,
            email="paxs@mail.com",
            password="password",
            gender=""

        )
    def test_register_user(self):
        self.assertEqual(len(self.accounts),0)
        self.user.signup(**self.sample_user)
        self.assertEqual(len(self.accounts),1)
    
    def test_register_similar_username_to_name(self):
        with self.assertRaises(ValueError)as context:
            self.user.signup(**self.second_user)
            self.assertTrue("Username should be different form name and not less than 4 characters" in context.exception)