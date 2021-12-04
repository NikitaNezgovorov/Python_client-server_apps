# -*- coding: utf8 -*-
from ..server import Server
from сommon.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE, ADDRESS, PORT

import sys
import os
import unittest

sys.path.append(os.path.join(os.getcwd(), '../../Messenger'))


class TestServer(unittest.TestCase):
    error_msg = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

    ok_msg = {ADDRESS: 'localhost', PORT: '7777', RESPONSE: 200}

    listen_address = 'localhost'
    listen_port = '7777'

    def test_ok_check(self):
        self.assertEqual(Server.process_client_message(self,
                                                       {ACTION: PRESENCE,
                                                        TIME: 1.1,
                                                        USER: {ACCOUNT_NAME: 'Guest'},
                                                        ADDRESS: 'localhost',
                                                        PORT: '7777'}
                                                       ), self.ok_msg)

    def test_no_action(self):
        self.assertEqual(Server.process_client_message(self,
                                                       {TIME: 1.1,
                                                        USER: {ACCOUNT_NAME: 'Guest'},
                                                        ADDRESS: 'localhost',
                                                        PORT: '7777'}
                                                       ), self.error_msg)

    def test_wrong_action(self):
        self.assertEqual(Server.process_client_message(self,
                                                       {ACTION: None,
                                                        TIME: 1.1,
                                                        USER: {ACCOUNT_NAME: 'Guest'},
                                                        ADDRESS: 'localhost',
                                                        PORT: '7777'}
                                                       ), self.error_msg)

    def test_no_time(self):
        self.assertEqual(Server.process_client_message(self,
                                                       {ACTION: PRESENCE,
                                                        USER: {ACCOUNT_NAME: 'Guest'},
                                                        ADDRESS: 'localhost',
                                                        PORT: '7777'}
                                                       ), self.error_msg)

    def test_no_user(self):
        self.assertEqual(Server.process_client_message(self,
                                                       {ACTION: PRESENCE,
                                                        TIME: 1.1,
                                                        ADDRESS: 'localhost',
                                                        PORT: '7777'}
                                                       ), self.error_msg)

    def test_unknown_user(self):
        self.assertEqual(Server.process_client_message(self,
                                                       {ACTION: PRESENCE,
                                                        TIME: 1.1,
                                                        USER: {ACCOUNT_NAME: 'Nick'},
                                                        ADDRESS: 'localhost',
                                                        PORT: '7777'}
                                                       ), self.error_msg)

    def test_unknown_address(self):
        self.assertEqual(Server.process_client_message(self,
                                                       {ACTION: PRESENCE,
                                                        TIME: 1.1,
                                                        USER: {ACCOUNT_NAME: 'Nick'},
                                                        ADDRESS: None,
                                                        PORT: '7777'}
                                                       ), self.error_msg)


if __name__ == '__main__':
    unittest.main()
