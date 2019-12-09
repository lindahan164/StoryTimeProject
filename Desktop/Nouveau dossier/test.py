import unittest
import registerlogin



# This is a generalized example, not specific to a test framework
class Test_TestAccountValidator(unittest.TestCase):
    def test_login1(self):
        self.assertEqual(len(registerlogin.main.loginInfo('ora','ok')),1)
    def test_login2(self):
        self.assertEqual(len(registerlogin.main.loginInfo('ora','oklkdjok')),0)
    def test_new_user3(self):
        self.assertTrue(registerlogin.main.insertuser())
    def test_getdata(self):
        self.assertEqual(len(registerlogin.main.getdata('Ora','Noam','Child','10')),1)
    def test_getdata(self):
        self.assertEqual(len(registerlogin.main.getdata('Ora','Noam','child','10')),0)
if __name__ == '__main__':
    unittest.main()
    # 
    # ... tests for all other casess