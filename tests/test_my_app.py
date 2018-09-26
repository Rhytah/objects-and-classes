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
    def test_register_user(self):
        self.assertEqual(len(self.accounts),0)
        self.user.signup(**self.sample_user)
        self.assertEqual(len(self.accounts),1)