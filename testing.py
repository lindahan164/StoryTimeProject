import unittest
import newstory as project
from tkinter import *

totest = project.main(Tk(),test=False)

class TestStringMethods(unittest.TestCase):
    # def test_upper(self):
    #     a=totest.getData('linoyS')
    #     self.assertIsNotNone(a)

    def testMainGetUser(self):
        totest.username = 'ora'
        totest.password = 'kloug'
        vUser = totest.login()
        self.assertTrue(vUser == None)
        totest.username = 'ora'
        totest.password = 'ora'
        vUser = totest.login()
        self.assertTrue(vUser != None && upper(vUser[3]) == 'TEACHER')
        totest.username = 'noamp'
        totest.password = 'noamp'
        vUser = totest.login()
        self.assertTrue(vUser != None && upper(vUser[3]) == 'STUDENT')
        totest.username = 'ora'
        totest.password = 'ora'
        vUser = totest.login()
        self.assertTrue(vUser != None && upper(vUser[3]) == 'PARENT')
    def testDb2(self):
        returnStatement=totest.getUser()  
        self.assertTrue(len(returnStatement)>1)
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()