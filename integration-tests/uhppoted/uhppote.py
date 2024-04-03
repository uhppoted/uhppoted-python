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

def messages():
    return [
        { # get-controller
          'request': [
              0x17, 0x94, 0x00, 0x00, 0x78, 0x37, 0x2a, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          ],
          'response': [
              0x17, 0x94, 0x00, 0x00, 0x78, 0x37, 0x2a, 0x18, 0xc0, 0xa8, 0x01, 0x64, 0xff, 0xff, 0xff, 0x00,
              0xc0, 0xa8, 0x01, 0x01, 0x00, 0x12, 0x23, 0x34, 0x45, 0x56, 0x08, 0x92, 0x20, 0x18, 0x11, 0x05,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          ],
        },
        { # get-time
          'request': [
              0x17, 0x32, 0x00, 0x00, 0x78, 0x37, 0x2a, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
          ],
          'response': [
              0x17, 0x32, 0x00, 0x00, 0x78, 0x37, 0x2a, 0x18, 0x20, 0x21, 0x05, 0x28, 0x13, 0x51, 0x30, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
              0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
          ],
        },
    ]

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
        Tests the get-controller function with valid dest_addr.
        '''
        expected = structs.GetControllerResponse(
            controller=405419896, 
            ip_address=IPv4Address('192.168.1.100'), 
            subnet_mask=IPv4Address('255.255.255.0'), 
            gateway=IPv4Address('192.168.1.1'), 
            mac_address='00:12:23:34:45:56', 
            version='v8.92', 
            date=datetime.date(2018, 11, 5))

        controller = CONTROLLER
        dest = '127.0.0.1:54321'
        response = self.u.get_controller(controller, dest_addr=dest)

        self.assertEqual(response, expected)

    def test_set_ip(self):
        '''
        Tests the set-ip function with valid dest_addr.
        '''
        expected = True

        controller = CONTROLLER
        address = IPv4Address('192.168.1.100')
        netmask = IPv4Address('255.255.255.0')
        gateway = IPv4Address('192.168.1.1')
        dest = '127.0.0.1:54321'

        response = self.u.set_ip(controller, address, netmask, gateway, dest_addr=dest)

        self.assertEqual(response, expected)

    def test_get_time(self):
        '''
        Tests the get-time function with valid dest_addr.
        '''
        expected = structs.GetTimeResponse(
            controller=405419896, 
            datetime=datetime.datetime(2021, 5, 28, 13, 51, 30))
        
        controller = CONTROLLER
        dest = '127.0.0.1:54321'

        response = self.u.get_time(controller, dest_addr=dest)

        self.assertEqual(response, expected)

if __name__ == '__main__':
    unittest.main()
