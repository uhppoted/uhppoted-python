import ipaddress

from uhppoted import uhppote
from pprint import pprint

def main():
    controller = 405419896                             # controller serial number
    host_addr = ipaddress.IPv4Address('192.168.1.100') # IPv4 address of host machine
    host_port = 60001                                  # port on which to listen for events
    
    bind_addr = '0.0.0.0'                              # either INADDR_ANY (0.0.0.0) or the host IPv4 address
    broadcast_addr = '255.255.255.255:60000'           # either the broadcast address for INADDR_ANY or the host IP broadcast address
    listen_addr = f'0.0.0.0:{host_port}'               # either INADDR_ANY (0.0.0.0) or the host IP IPv4 address
    debug = True

    try:
        # base configuration for UHPPOTE driver
        u = uhppote.Uhppote(bind_addr, broadcast_addr, listen_addr, debug)

        # set the IPv4 address and UDP port to which the controller should send events
        set_listener(u,controller, host_addr, host_port)

        # enable door open/close/unlock events
        record_special_events(u,controller)

        # listen for incoming controller events
        listen(u)

    except Exception as x:
        print()
        print(f'*** ERROR  {x}')
        print()

def set_listener(u, controller, address, port):
    print('-- set-listener')
    
    response = u.set_listener(controller, address, port)
    
    print('  ', response)
    print()

def record_special_events(u, controller):
    print('-- record-special-events')
    
    response = u.record_special_events(controller, True)
    
    print('  ', response)
    print()

def listen(u):
    print('-- listening for events')
    u.listen(onEvent)

def onEvent(event):
    if event != None:
        pprint(event.__dict__, indent=2, width=1)

if __name__ == '__main__':
    main()