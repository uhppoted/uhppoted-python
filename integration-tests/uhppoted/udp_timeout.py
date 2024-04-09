'''
UHPPOTE function tests.

End-to-end tests for the uhppote functions.
'''

import unittest
import socket
import struct
import threading
import time
import datetime

from ipaddress import IPv4Address

from uhppoted import uhppote
from uhppoted import structs
from uhppoted.udp import dump

from .stub import messages
from .expected import *

CONTROLLER = 405419896
CARD = 8165538
CARD_INDEX = 2
EVENT_INDEX = 29
TIME_PROFILE = 29
NO_TIMEOUT = struct.pack('ll', 0, 0)  # (infinite)

def handle(sock, bind, debug):
    '''
    Replies to received UDP packets with the matching response.
    '''
    never = struct.pack('ll', 0, 0)  # (infinite)

    try:
        sock.bind(bind)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, never)

        while True:
            (message,addr) = sock.recvfrom(1024)
            if len(message) == 64:
                if debug:
                    dump(message)
                for m in messages():
                    if bytes(m['request']) == message:
                        time.sleep(0.5)
                        sock.sendto(bytes(m['response']), addr)
                        break
    except Exception as x:
        pass
    finally:
        sock.close()

class TestUhppoteWithTimeout(unittest.TestCase):
    def setUp(self):
        bind = '0.0.0.0'
        broadcast = '255.255.255.255:60000'
        listen = '0.0.0.0:60001'
        debug = False

        self.u = uhppote.Uhppote(bind, broadcast, listen, debug)
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        self._thread = threading.Thread(target = handle, args = (self._sock,('127.0.0.1', 54321), False))

        self._thread.start()
        time.sleep(1)


    def tearDown(self):
        self._sock.close()
        pass

    def test_get_controller(self):
        '''
        Tests the get-controller function with a timeout.
        '''
        controller = CONTROLLER
        dest = '127.0.0.1:54321'
        timeout = 0.25

        self.u.get_controller(controller, dest_addr=dest)
        self.assertRaises(socket.timeout, self.u.get_controller,controller, dest_addr=dest, timeout=timeout)
