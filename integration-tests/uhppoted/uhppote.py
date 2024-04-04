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
                        sock.sendto(bytes(m['response']), addr)
                        break
    except Exception as x:
        pass
    finally:
        sock.close()

class TestUhppoteWithDestAddr(unittest.TestCase):
    def setUp(self):
        bind = '0.0.0.0'
        broadcast = '255.255.255.255:60000'
        listen = '0.0.0.0:60001'
        debug = False

        self.u = uhppote.Uhppote(bind, broadcast, listen, debug)
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        self._thread = threading.Thread(target = handle, args = (self._sock,('127.0.0.1', 54321), True))

        self._thread.start()
        time.sleep(1)


    def tearDown(self):
        self._sock.close()
        pass

    def test_get_controller(self):
        '''
        Tests the get-controller function with a valid dest_addr.
        '''
        controller = CONTROLLER
        dest = '127.0.0.1:54321'
        response = self.u.get_controller(controller, dest_addr=dest)

        self.assertEqual(response, GetControllerResponse)

    def test_set_ip(self):
        '''
        Tests the set-ip function with a valid dest_addr.
        '''
        controller = CONTROLLER
        address = IPv4Address('192.168.1.100')
        netmask = IPv4Address('255.255.255.0')
        gateway = IPv4Address('192.168.1.1')
        dest = '127.0.0.1:54321'

        response = self.u.set_ip(controller, address, netmask, gateway, dest_addr=dest)

        self.assertEqual(response, SetIPResponse)

    def test_get_time(self):
        '''
        Tests the get-time function with a valid dest_addr.
        '''
        controller = CONTROLLER
        dest = '127.0.0.1:54321'

        response = self.u.get_time(controller, dest_addr=dest)

        self.assertEqual(response, GetTimeResponse)

    def test_set_time(self):
        '''
        Tests the set-time function with a valid dest_addr.
        '''
        controller = CONTROLLER
        time = datetime.datetime(2021, 5, 28, 14, 56, 14)
        dest = '127.0.0.1:54321'

        response = self.u.set_time(controller, time, dest_addr=dest)

        self.assertEqual(response, SetTimeResponse)

    def test_get_status(self):
        '''
        Tests the get-status function with a valid dest_addr.
        '''
        controller = CONTROLLER
        dest = '127.0.0.1:54321'

        response = self.u.get_status(controller, dest_addr=dest)

        self.assertEqual(response, GetStatusResponse)

    def test_get_listener(self):
        '''
        Tests the get-listener function with a valid dest_addr.
        '''
        controller = CONTROLLER
        dest = '127.0.0.1:54321'

        response = self.u.get_listener(controller, dest_addr=dest)

        self.assertEqual(response, GetListenerResponse)

    def test_set_listener(self):
        '''
        Tests the set-listener function with a valid dest_addr.
        '''
        controller = CONTROLLER
        address = IPv4Address('192.168.1.100')
        port = 60001
        dest = '127.0.0.1:54321'

        response = self.u.set_listener(controller, address, port, dest_addr=dest)

        self.assertEqual(response, SetListenerResponse)

    def test_get_door_control(self):
        '''
        Tests the get-door-control function with a valid dest_addr.
        '''
        controller = CONTROLLER
        door = 3
        dest = '127.0.0.1:54321'

        response = self.u.get_door_control(controller, door, dest_addr=dest)

        self.assertEqual(response, GetDoorControlResponse)

    def test_set_door_control(self):
        '''
        Tests the set-door-control function with a valid dest_addr.
        '''
        controller = CONTROLLER
        door = 3
        delay = 4
        mode = 2
        dest = '127.0.0.1:54321'

        response = self.u.set_door_control(controller, door, mode, delay, dest_addr=dest)

        self.assertEqual(response, SetDoorControlResponse)

    def test_open_door(self):
        '''
        Tests the open-door function with a valid dest_addr.
        '''
        controller = CONTROLLER
        door = 3
        dest = '127.0.0.1:54321'

        response = self.u.open_door(controller, door, dest_addr=dest)

        print(response)

        self.assertEqual(response, OpenDoorResponse)

if __name__ == '__main__':
    unittest.main()
