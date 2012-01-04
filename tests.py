import os
import myapp
import unittest
import tempfile

class MyappTestCase(unittest.TestCase):

    def setUp(self):
        myapp.app.config['DEBUG'] = tempfile.mkstemp()
        self.app = myapp.app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        rv = self.app.get('/')
        assert '<h2>Posts</h2>' in rv.data

if __name__ == '__main__':
    unittest.main()