'''
UHPPOTE TCP communications wrapper.

Implements the functionality to send and receive 64 byte TCP packets to/from a UHPPOTE 
access controller.
'''

import socket
import struct
import re
import time
import ipaddress

READ_TIMEOUT = struct.pack('ll', 5, 0)  # 5 seconds
WRITE_TIMEOUT = struct.pack('ll', 1, 0)  # 1 second
NO_TIMEOUT = struct.pack('ll', 0, 0)  # (infinite)


class TCP:

    def __init__(self, bind='0.0.0.0', debug=False):
        '''
        Initialises a TCP communications wrapper with the bind address.

            Parameters:
               bind      (string)  The IPv4 address:port to which to bind when sending a request.
               debug     (bool)    Dumps the sent and received packets to the console if enabled.

            Returns:
               Initialised TCP object.

            Raises:
               Exception  If any of the supplied IPv4 values cannot be translated to a valid IPv4 
                          address:port combination.
        '''
        self._bind = (bind, 0)
        self._debug = debug

    def send(self, request, dest_addr, timeout=2.5):
        '''
        Binds to the bind address from the constructor and connects to the access controller after which it sends
        the request and waits 'timeout' seconds for the reply (if any).

            Parameters:
               request   (bytearray)  64 byte request packet.
               dest_addr (string)     Optional IPv4 address:port of the controller. Defaults to port 60000
                                      if dest_addr does not include a port.
               timeout   (float)      Optional operation timeout (in seconds). Defaults to 2.5s.

            Returns:
               Received response packet (if any) or None (for set-ip request).

            Raises:
               Error  For any socket related errors.
        '''
        self.dump(request)

        raise NotImplementedError

        # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

        # try:
        #     sock.bind(self._bind)
        #     sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        #     sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDTIMEO, WRITE_TIMEOUT)
        #     sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, READ_TIMEOUT)

        #     if dest_addr == None:
        #         sock.sendto(request, self._broadcast)
        #     else:
        #         addr = resolve(f'{dest_addr}')
        #         sock.sendto(request, addr)

        #     if request[1] == 0x96:
        #         return None

        #     return _read(sock, timeout=timeout, debug=self._debug)
        # finally:
        #     sock.close()

    def dump(self, packet):
        '''
        Prints a packet to the console as a formatted hexadecimal string if debug was enabled in the
        constructor.

            Parameters:
               packet  (bytearray)  64 byte UDP packet.

            Returns:
               None.
        '''
        if self._debug:
            dump(packet)


def dump(packet):
    '''
    Prints a packet to the console as a formatted hexadecimal string.

        Parameters:
           packet  (bytearray)  64 byte UDP packet.

        Returns:
            None.
    '''
    for i in range(0, 4):
        offset = i * 16
        u = packet[offset:offset + 8]
        v = packet[offset + 8:offset + 16]

        p = f'{u[0]:02x} {u[1]:02x} {u[2]:02x} {u[3]:02x} {u[4]:02x} {u[5]:02x} {u[6]:02x} {u[7]:02x}'
        q = f'{v[0]:02x} {v[1]:02x} {v[2]:02x} {v[3]:02x} {v[4]:02x} {v[5]:02x} {v[6]:02x} {v[7]:02x}'

        print(f'   {offset:08x}  {p}  {q}')

    print()
