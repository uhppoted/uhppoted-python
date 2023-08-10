'''
UHPPOTE UDP communications wrapper.

Implements the functionality to send and receive 64 byte UDP packets to/from a UHPPOTE 
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


class UDP:

    def __init__(self, bind='0.0.0.0', broadcast='255.255.255.255:60000', listen="0.0.0.0:60001", debug=False):
        '''
        Initialises a Uhppote object with the bind address, broadcast address and listen address.

            Parameters:
               bind      (string)  The IPv4 address:port to which to bind when sending a request.
               broadcast (string)  The IPv4 address:port to which to send broadcast UDP messages.
               listen    (string)  The IPv4 address:port on which to listen for events from the
                                   access controllers.
               debug     (bool)    Dumps the sent and received packets to the console if enabled.

            Returns:
               Initialised UDP object.

            Raises:
               Exception  If any of the supplied IPv4 values cannot be translated to a valid IPv4 
                          address:port combination.
        '''
        self._bind = (bind, 0)
        self._broadcast = resolve(broadcast)
        self._listen = resolve(listen)
        self._debug = debug

    def broadcast(self, request):
        '''
        Binds to the bind address from the constructor and then broadcasts a UDP request to the broadcast
        address from the constructor and then waits 5 seconds for the replies from any reponding access 
        controllers.

            Parameters:
               request  (bytearray)  64 byte request packet.

            Returns:
               List of received response packets (may be empty).

            Raises:
               Error  For any socket related errors.
        '''
        self.dump(request)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

        try:
            sock.bind(self._bind)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDTIMEO, WRITE_TIMEOUT)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, READ_TIMEOUT)

            sock.sendto(request, self._broadcast)

            return read_all(sock, self._debug)
        finally:
            sock.close()

    def send(self, request):
        '''
        Binds to the bind address from the constructor and then broadcasts a UDP request to the broadcast,
        and then waits 5 seconds for a reply from the destination access controllers.

            Parameters:
               request  (bytearray)  64 byte request packet.

            Returns:
               Received response packet (if any) or None (for set-ip request).

            Raises:
               Error  For any socket related errors.
        '''
        self.dump(request)

        # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM | socket.SOCK_NONBLOCK)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

        try:
            sock.bind(self._bind)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDTIMEO, WRITE_TIMEOUT)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, READ_TIMEOUT)

            sock.sendto(request, self._broadcast)

            if request[1] == 0x96:
                return None

            return read(sock, self._debug)
        finally:
            sock.close()

    def listen(self, onEvent):
        '''
        Binds to the listen address from the constructor and invokes the events handler for
        any received 64 byte UDP packets. Invalid'ish packets are silently discarded.

            Parameters:
               onEvent  (function)  Handler function for received events, with a function signature 
                                    f(packet).

            Returns:
               None.

            Raises:
               Error  For any socket related errors.
        '''
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

        try:
            sock.bind(self._listen)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, NO_TIMEOUT)

            while True:
                message = sock.recv(1024)
                if len(message) == 64:
                    if self._debug:
                        dump(message)
                    onEvent(message)
        finally:
            sock.close()

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


# TODO convert to asyncio
def read(sock, debug):
    '''
    Waits 2.5 seconds for a single 64 byte packet to be received on the socket. Prints the packet to the console
    if debug is True.

        Parameters:
            sock  (socket)  Initialised and open UDP socket.
            debug (bool)    Enables dumping the received packet to the console.

        Returns:
            Received 64 byte UDP packet (or None).
    '''
    sock.settimeout(2.5)

    while True:
        reply = sock.recv(1024)
        if len(reply) == 64:
            if debug:
                dump(reply)
            return reply

    return None


# TODO convert to asyncio
def read_all(sock, debug):
    '''
    Accumulates received 64 byte UDP packets, waiting up to 2.5 seconds for an incoming packet. Prints the 
    packet to the console if debug is True.

        Parameters:
            sock  (socket)  Initialised and open UDP socket.
            debug (bool)    Enables dumping the received packet to the console.

        Returns:
            List of received 64 byte UDP packets (may be empty).
    '''
    sock.settimeout(2.5)

    replies = []
    while True:
        try:
            reply = sock.recv(1024)
            if len(reply) == 64:
                replies.append(reply)
                if debug:
                    dump(reply)
        except socket.timeout:
            break

    return replies


def resolve(addr):
    '''
    Resolves an address:port string into the equivalent ( address, port ) tuple. An addr value
    without a :port suffix defaults to port 60000.

        Parameters:
            addr  (string)  address:port string

        Returns:
            (address, port) as a (string, uint16) tuple
    '''
    match = re.match(r'(.*?):([0-9]+)', addr)
    if match:
        return (match.group(1), int(match.group(2)))
    else:
        address = ipaddress.IPv4Address(addr)
        return (str(address), 60000)


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
