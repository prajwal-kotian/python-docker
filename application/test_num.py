import unittest
import application

class TestConn(unittest.TestCase):
    def test_conn(self):
        result = application.conn()
        self.assertIs(str(result), "PONG")

if __name__=='__main__':
    unittest.main()
