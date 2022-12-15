import unittest
from main import *

class TestGUI(unittest.TestCase):
    def test_tru(self):
        i = GUI(self)
        self.assertEqual(i.Tru, True)

    def start_GUI(self):

if __name__ =='__main__':
    unittest.main()
