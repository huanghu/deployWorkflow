'''
Created on 2013-1-9

@author: huanghu
'''
import unittest
from readProperties import saveProperties
from main import Main


class Test(unittest.TestCase):

    def setUp(self):
        self.prop = saveProperties();
    def testName(self):
        self.prop.readUnicode()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()