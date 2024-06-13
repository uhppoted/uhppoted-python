import os
import ipaddress
import datetime
import pprint
import sys
import pathlib

if os.environ['UHPPOTED_ENV'] == 'DEV':
    root = pathlib.Path(__file__).resolve().parents[2]
    sys.path.append(os.path.join(root, 'src'))

from uhppoted import uhppote

CONTROLLER = 405419896
DOOR = 3
MODE = 2
DELAY = 10
CARD = 8165538
CARD_INDEX = 3
EVENT_INDEX = 37
TIME_PROFILE_ID = 29

ADDRESS = ipaddress.IPv4Address('192.168.1.100')
NETMASK = ipaddress.IPv4Address('255.255.255.0')
GATEWAY = ipaddress.IPv4Address('192.168.1.1')
LISTENER = (ipaddress.IPv4Address('192.168.1.100'), 60001)


def commands():
    return {
        'get-all-controllers': get_all_controllers,
        'get-controller': get_controller,
        'set-ip': set_ip,
        'get-time': get_time,
        'set-time': set_time,
        'get-listener': get_listener,
        'set-listener': set_listener,
        'get-door-control': get_door_control,
        'set-door-control': set_door_control,
        'get-status': get_status,
        'open-door': open_door,
        'get-cards': get_cards,
        'get-card': get_card,
        'get-card-by-index': get_card_by_index,
        'put-card': put_card,
        'delete-card': delete_card,
        'delete-all-cards': delete_all_cards,
        'get-event': get_event,
        'get-event-index': get_event_index,
        'set-event-index': set_event_index,
        'record-special-events': record_special_events,
        'get-time-profile': get_time_profile,
        'set-time-profile': set_time_profile,
        'clear-time-profiles': clear_time_profiles,
        'add-task': add_task,
        'refresh-tasklist': refresh_tasklist,
        'clear-tasklist': clear_tasklist,
        'set-pc-control': set_pc_control,
        'set-interlock': set_interlock,
        'activate-keypads': activate_keypads,
        'set-door-passcodes': set_door_passcodes,
        'restore-default-parameters': restore_default_parameters,
        'listen': listen,
    }


def exec(f, args):
    bind = args.bind
    broadcast = args.broadcast
    listen = args.listen
    debug = args.debug

    dest = args.destination
    timeout = args.timeout
    protocol = 'udp'

    if args.udp:
        protocol = 'udp'
    elif args.tcp:
        protocol = 'tcp'

    u = uhppote.Uhppote(bind, broadcast, listen, debug)
    response = f(u, dest, timeout, args,protocol=protocol)

    if response != None:
        if type(response).__name__ == 'list':
            for v in response:
                pprint.pprint(v.__dict__, indent=2, width=1, sort_dicts=False)
        elif type(response).__name__ == 'bool':
            pprint.pprint(response, indent=2, width=1, sort_dicts=False)
        else:
            pprint.pprint(response.__dict__, indent=2, width=1, sort_dicts=False)


def get_all_controllers(u, dest, timeout, args, protocol='udp'):
    return u.get_all_controllers(timeout=timeout)


def get_controller(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER

    return u.get_controller((controller, dest, protocol), timeout=timeout)


def set_ip(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER
    address = ADDRESS
    netmask = NETMASK
    gateway = GATEWAY

    return u.set_ip((controller, dest, protocol), address, netmask, gateway, timeout=timeout)


def get_time(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER

    return u.get_time(controller, dest_addr=dest, timeout=timeout, protocol=protocol)


def set_time(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER
    now = datetime.datetime.now()

    return u.set_time(controller, now, dest_addr=dest, timeout=timeout, protocol=protocol)


def get_listener(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER

    return u.get_listener(controller, dest_addr=dest, timeout=timeout, protocol=protocol)


def set_listener(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER
    (address, port) = LISTENER

    return u.set_listener(controller, address, port, dest_addr=dest, timeout=timeout, protocol=protocol)


def get_door_control(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER
    door = DOOR

    return u.get_door_control(controller, door, dest_addr=dest, timeout=timeout, protocol=protocol)


def set_door_control(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER
    door = DOOR
    mode = MODE
    delay = DELAY

    return u.set_door_control(controller, door, mode, delay, dest_addr=dest, timeout=timeout, protocol=protocol)


def get_status(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER

    return u.get_status(controller, dest_addr=dest, timeout=timeout, protocol=protocol)


def open_door(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER
    door = DOOR

    return u.open_door(controller, door, dest_addr=dest, timeout=timeout, protocol=protocol)


def get_cards(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER

    return u.get_cards(controller, dest_addr=dest, timeout=timeout, protocol=protocol)


def get_card(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER
    card = CARD

    response = u.get_card(controller, card, dest_addr=dest, timeout=timeout, protocol=protocol)
    if response.card_number == 0:
        raise ValueError(f'card {card} not found')

    return response


def get_card_by_index(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER
    index = CARD_INDEX

    response = u.get_card_by_index(controller, index, dest_addr=dest, timeout=timeout, protocol=protocol)
    if response.card_number == 0:
        raise ValueError(f'card @ index {index} not found')
    elif response.card_number == 0xffffffff:
        raise ValueError(f'card @ index {index} deleted')

    return response


def put_card(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER
    card = CARD
    start = datetime.datetime.strptime("2024-01-01", '%Y-%m-%d').date()
    end = datetime.datetime.strptime("2024-12-31", '%Y-%m-%d').date()
    door1 = 0    # no access
    door2 = 1    # 24/7 access
    door3 = 29   # time_profile
    door4 = 0    # no access
    PIN = 7531

    return u.put_card(controller, card, start, end, door1, door2, door3, door4, PIN, dest_addr=dest, timeout=timeout, protocol=protocol)


def delete_card(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER
    card = CARD

    return u.delete_card(controller, card, dest_addr=dest, timeout=timeout, protocol=protocol)


def delete_all_cards(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER

    return u.delete_all_cards(controller, dest_addr=dest, timeout=timeout, protocol=protocol)


def get_event(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER
    index = EVENT_INDEX

    response = u.get_event(controller, index, dest_addr=dest, timeout=timeout, protocol=protocol)
    if response.event_type == 0xff:
        raise ValueError(f'event @ index {index} overwritten')
    elif response.index == 0:
        raise ValueError(f'event @ index {index} not found')

    return response


def get_event_index(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER

    return u.get_event_index(controller, dest_addr=dest, timeout=timeout, protocol=protocol)


def set_event_index(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER
    index = EVENT_INDEX

    return u.set_event_index(controller, index, dest_addr=dest, timeout=timeout, protocol=protocol)


def record_special_events(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER
    enabled = True

    return u.record_special_events(controller, enabled, dest_addr=dest, timeout=timeout, protocol=protocol)


def get_time_profile(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER
    profile_id = TIME_PROFILE_ID

    response = u.get_time_profile(controller, profile_id, dest_addr=dest, timeout=timeout, protocol=protocol)
    if response.profile_id == 0:
        raise ValueError(f'time profile {profile_id} not defined')

    return response


def set_time_profile(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER
    profile_id = TIME_PROFILE_ID
    start = datetime.datetime.strptime("2022-01-01", '%Y-%m-%d').date()
    end = datetime.datetime.strptime("2022-12-31", '%Y-%m-%d').date()
    monday = True
    tuesday = False
    wednesday = True
    thursday = True
    friday = False
    saturday = False
    sunday = True
    segment1start = datetime.datetime.strptime("08:15", '%H:%M').time()
    segment1end = datetime.datetime.strptime("11:45", '%H:%M').time()
    segment2start = datetime.datetime.strptime("12:45", '%H:%M').time()
    segment2end = datetime.datetime.strptime("17:15", '%H:%M').time()
    segment3start = datetime.datetime.strptime("19:30", '%H:%M').time()
    segment3end = datetime.datetime.strptime("22:00", '%H:%M').time()
    linked_profile_ID = 23

    # yapf: disable
    return u.set_time_profile(controller, 
                              profile_id, 
                              start, end, 
                              monday, tuesday, wednesday, thursday, friday, saturday, sunday, 
                              segment1start, segment1end, 
                              segment2start, segment2end, 
                              segment3start, segment3end, 
                              linked_profile_ID, 
                              dest_addr=dest, timeout=timeout, protocol=protocol)
    # yapf: enable

def clear_time_profiles(u, dest, timeout, args, protocol='udp'):
    return u.delete_all_time_profiles(CONTROLLER, dest_addr=dest, timeout=timeout, protocol=protocol)


def add_task(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER
    start_date = datetime.datetime.strptime("2022-01-01", '%Y-%m-%d').date()
    end_date = datetime.datetime.strptime("2022-12-31", '%Y-%m-%d').date()
    monday = True
    tuesday = False
    wednesday = True
    thursday = True
    friday = False
    saturday = False
    sunday = True
    start_time = datetime.datetime.strptime("08:15", '%H:%M').time()
    door = DOOR
    task_type = 2
    more_cards = 0

    # yapf: disable
    return u.add_task(controller, 
                      start_date, end_date, 
                      monday, tuesday, wednesday, thursday, friday, saturday, sunday,
                      start_time, 
                      door, 
                      task_type, 
                      more_cards,
                      dest_addr=dest, timeout=timeout, protocol=protocol)
    # yapf: enable


def refresh_tasklist(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER

    return u.refresh_tasklist(controller, dest_addr=dest, timeout=timeout, protocol=protocol)


def clear_tasklist(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER

    return u.clear_tasklist(controller, dest_addr=dest, timeout=timeout, protocol=protocol)


def set_pc_control(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER
    enabled = True

    return u.set_pc_control(controller, enabled, dest_addr=dest, timeout=timeout, protocol=protocol)


def set_interlock(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER
    interlock = 3

    return u.set_interlock(controller, interlock, dest_addr=dest, timeout=timeout, protocol=protocol)


def activate_keypads(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER
    reader1 = True
    reader2 = True
    reader3 = False
    reader4 = True

    return u.activate_keypads(controller, reader1, reader2, reader3, reader4, dest_addr=dest, timeout=timeout, protocol=protocol)


def set_door_passcodes(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER
    door = DOOR
    passcode1 = 12345
    passcode2 = 0
    passcode3 = 999999
    passcode4 = 54321

    return u.set_door_passcodes(controller, door, passcode1, passcode2, passcode3, passcode4, dest_addr=dest, timeout=timeout, protocol=protocol)


def restore_default_parameters(u, dest, timeout, args, protocol='udp'):
    controller = CONTROLLER

    return u.restore_default_parameters(controller, dest_addr=dest, timeout=timeout, protocol=protocol)


def listen(u, dest, timeout, args, protocol='udp'):
    return u.listen(onEvent)


def onEvent(event):
    if event != None:
        pprint.pprint(event.__dict__, indent=2, width=1)
