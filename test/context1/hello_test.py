import os
import sys

path = os.path.join(os.path.dirname(__file__), '../../src/context1')
sys.path.append(path)

import unittest
import json
from handler import hello


class TestHandler(unittest.TestCase):
    """ Tests handler methods """

    def test_statusCode(self):
        res = hello(None, None)
        self.assertEquals(200, res['statusCode'])

    def test_body(self):
        res = hello(None, None)
        self.assertTrue(len(res['body']) > 0)
        post = json.loads(res['body'])
        self.assertEquals(None, post['input'])
        self.assertEquals(
            'Go Serverless v1.0! Your function executed successfully!',
            post['message']
        )

if __name__ == '__main__':
    unittest.main()
