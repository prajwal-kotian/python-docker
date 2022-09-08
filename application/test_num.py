import unittest
import main

class TestConn(unittest.TestCase):
    def test_conn(self):
        result = main.conn()
        self.assertIs(str(result), "PONG")

if __name__=='__main__':
    unittest.main()
