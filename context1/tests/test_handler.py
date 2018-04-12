# coding:utf-8

import sys
import os
import unittest
sys.path.append(os.pardir)
import handler

class TestHandler(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hello_1(self):
      response = handler.hello('test', None)
      assert response['statusCode'] == 200

    def test_hello_2(self):
      response = handler.hello('test', None)
      assert response['body'] == '{"input": "test", "message": "Go Serverless v1.0! Your function executed successfully!"}'
