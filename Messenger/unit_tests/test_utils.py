# -*- coding: utf8 -*-
import json

from ..сommon.utils import get_message, send_message
from ..сommon.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, ADDRESS, PORT, ENCODING

import sys
import os
import unittest

sys.path.append(os.path.join(os.getcwd(), '../../Messenger'))


class TestSocket:
    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoded_message = None
        self.received_message = None

    def send(self, message_to_send):
        json_test_message = json.dumps(self.test_dict)
        self.encoded_message = json_test_message.encode(ENCODING)
        self.received_message = message_to_send

    def recv(self, MAX_PACKAGE_LENGTH):
        json_test_message = json.dumps(self.test_dict)
        return json_test_message.encode(ENCODING)


class TestUtils(unittest.TestCase):
    test_dict_send = {
        ACTION: PRESENCE,
        TIME: 1.1,
        USER: {ACCOUNT_NAME: 'Guest'},
        ADDRESS: 'localhost',
        PORT: '7777'
    }

    test_dict_received_ok = {ADDRESS: 'localhost', PORT: '7777', RESPONSE: 200}
    test_dict_received_error = {RESPONSE: 400, ERROR: 'Bad Request'}

    def test_send_message_equal(self):
        test_socket = TestSocket(self.test_dict_send)
        send_message(test_socket, self.test_dict_send)
        self.assertEqual(test_socket.encoded_message, test_socket.received_message)

    def test_send_message_type_error(self):
        test_socket = TestSocket(self.test_dict_send)
        send_message(test_socket, self.test_dict_send)
        self.assertRaises(TypeError, send_message, test_socket, 'Wrong_msg')

    def test_get_message(self):
        test_socket_ok = TestSocket(self.test_dict_received_ok)
        self.assertEqual(get_message(test_socket_ok), self.test_dict_received_ok)

    def test_get_message_error(self):
        test_socket_error = TestSocket(self.test_dict_received_error)
        self.assertEqual(get_message(test_socket_error), self.test_dict_received_error)


if __name__ == '__main__':
    unittest.main()
