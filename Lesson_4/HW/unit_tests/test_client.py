# -*- coding: utf8 -*-
import sys
import os
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))

from сommon.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, ADDRESS, PORT
from ..client import Client


class TestClient(unittest.TestCase):
    """
    Класс тестов функций Клиента
    """
    server_address = 'localhost'
    server_port = '7777'
    test_time = 1.1
    correct_msg = {ACTION: PRESENCE,
                   TIME: 1.1,
                   USER: {ACCOUNT_NAME: 'Guest'},
                   ADDRESS: 'localhost',
                   PORT: '7777'}

    def test_def_presence(self):
        test = Client.create_presence(self)
        test[TIME] = self.test_time

        self.assertEqual(test, self.correct_msg)

    def test_def_presence_not_equal(self):
        test = Client.create_presence(self)
        test[TIME] = self.test_time

        self.assertNotEqual(test, {ACTION: PRESENCE,
                                   TIME: 1.1,
                                   USER: {ACCOUNT_NAME: None},
                                   ADDRESS: None,
                                   PORT: None})

    def test_def_presence_TypeError(self):
        self.assertRaises(TypeError, Client.create_presence(self),{None})


    def test_200_ans(self):
        test = Client.server_answer({RESPONSE: 200, ADDRESS: self.correct_msg[ADDRESS], PORT: self.correct_msg[PORT]})

        self.assertEqual(test, '200 : OK\nADDRESS : localhost\nPORT : 7777')

    def test_400_ans(self):
        test = Client.server_answer({RESPONSE: 400, ERROR: 'error'})

        self.assertEqual(test, '400 : error')

    def test_no_responce(self):
        self.assertRaises(ValueError, Client.server_answer, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
