import struct


def get_controller_request(device_id):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0x94

    pack_uint32(device_id, packet, 4)

    return packet


def set_ip_request(device_id, address, netmask, gateway):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0x96

    pack_uint32(device_id, packet, 4)
    pack_IPv4(address, packet, 8)
    pack_IPv4(netmask, packet, 12)
    pack_IPv4(gateway, packet, 16)
    pack_uint32(0x55aaaa55, packet, 20)

    return packet


def get_time_request(device_id):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0x32

    pack_uint32(device_id, packet, 4)

    return packet


def set_time_request(device_id, datetime):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0x30

    pack_uint32(device_id, packet, 4)
    pack_datetime(datetime, packet, 8)

    return packet


def get_status_request(device_id):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0x20

    pack_uint32(device_id, packet, 4)

    return packet


def get_listener_request(device_id):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0x92

    pack_uint32(device_id, packet, 4)

    return packet


def set_listener_request(device_id, address, port):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0x90

    pack_uint32(device_id, packet, 4)
    pack_IPv4(address, packet, 8)
    pack_uint16(port, packet, 12)

    return packet


def get_door_control_request(device_id, door):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0x82

    pack_uint32(device_id, packet, 4)
    pack_uint8(door, packet, 8)

    return packet


def set_door_control_request(device_id, door, mode, delay):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0x80

    pack_uint32(device_id, packet, 4)
    pack_uint8(door, packet, 8)
    pack_uint8(mode, packet, 9)
    pack_uint8(delay, packet, 10)

    return packet


def open_door_request(device_id, door):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0x40

    pack_uint32(device_id, packet, 4)
    pack_uint8(door, packet, 8)

    return packet


def get_cards_request(device_id):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0x58

    pack_uint32(device_id, packet, 4)

    return packet


def get_card_request(device_id, card_number):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0x5a

    pack_uint32(device_id, packet, 4)
    pack_uint32(card_number, packet, 8)

    return packet


def get_card_by_index_request(device_id, card_index):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0x5c

    pack_uint32(device_id, packet, 4)
    pack_uint32(card_index, packet, 8)

    return packet


def put_card_request(device_id, card_number, start_date, end_date, door_1, door_2, door_3, door_4,
                     pin):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0x50

    pack_uint32(device_id, packet, 4)
    pack_uint32(card_number, packet, 8)
    pack_date(start_date, packet, 12)
    pack_date(end_date, packet, 16)
    pack_uint8(door_1, packet, 20)
    pack_uint8(door_2, packet, 21)
    pack_uint8(door_3, packet, 22)
    pack_uint8(door_4, packet, 23)
    pack_pin(pin, packet, 24)

    return packet


def delete_card_request(device_id, card_number):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0x52

    pack_uint32(device_id, packet, 4)
    pack_uint32(card_number, packet, 8)

    return packet


def delete_cards_request(device_id):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0x54

    pack_uint32(device_id, packet, 4)
    pack_uint32(0x55aaaa55, packet, 8)

    return packet


def get_event_request(device_id, event_index):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0xb0

    pack_uint32(device_id, packet, 4)
    pack_uint32(event_index, packet, 8)

    return packet


def get_event_index_request(device_id):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0xb4

    pack_uint32(device_id, packet, 4)

    return packet


def set_event_index_request(device_id, event_index):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0xb2

    pack_uint32(device_id, packet, 4)
    pack_uint32(event_index, packet, 8)
    pack_uint32(0x55aaaa55, packet, 12)

    return packet


def record_special_events_request(device_id, enable):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0x8e

    pack_uint32(device_id, packet, 4)
    pack_bool(enable, packet, 8)

    return packet


def get_time_profile_request(device_id, profile_id):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0x98

    pack_uint32(device_id, packet, 4)
    pack_uint8(profile_id, packet, 8)

    return packet


def set_time_profile_request(device_id, profile_id, start_date, end_date, monday, tuesday,
                             wednesday, thursday, friday, saturday, sunday, segment_1_start,
                             segment_1_end, segment_2_start, segment_2_end, segment_3_start,
                             segment_3_end, linked_profile_id):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0x88

    pack_uint32(device_id, packet, 4)
    pack_uint8(profile_id, packet, 8)
    pack_date(start_date, packet, 9)
    pack_date(end_date, packet, 13)
    pack_bool(monday, packet, 17)
    pack_bool(tuesday, packet, 18)
    pack_bool(wednesday, packet, 19)
    pack_bool(thursday, packet, 20)
    pack_bool(friday, packet, 21)
    pack_bool(saturday, packet, 22)
    pack_bool(sunday, packet, 23)
    pack_HHmm(segment_1_start, packet, 24)
    pack_HHmm(segment_1_end, packet, 26)
    pack_HHmm(segment_2_start, packet, 28)
    pack_HHmm(segment_2_end, packet, 30)
    pack_HHmm(segment_3_start, packet, 32)
    pack_HHmm(segment_3_end, packet, 34)
    pack_uint8(linked_profile_id, packet, 36)

    return packet


def delete_all_time_profiles_request(device_id):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0x8a

    pack_uint32(device_id, packet, 4)
    pack_uint32(0x55aaaa55, packet, 8)

    return packet


def add_task_request(device_id, start_date, end_date, monday, tuesday, wednesday, thursday, friday,
                     saturday, sunday, start_time, door, task_type, more_cards):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0xa8

    pack_uint32(device_id, packet, 4)
    pack_date(start_date, packet, 8)
    pack_date(end_date, packet, 12)
    pack_bool(monday, packet, 16)
    pack_bool(tuesday, packet, 17)
    pack_bool(wednesday, packet, 18)
    pack_bool(thursday, packet, 19)
    pack_bool(friday, packet, 20)
    pack_bool(saturday, packet, 21)
    pack_bool(sunday, packet, 22)
    pack_HHmm(start_time, packet, 23)
    pack_uint8(door, packet, 25)
    pack_uint8(task_type, packet, 26)
    pack_uint8(more_cards, packet, 27)

    return packet


def refresh_tasklist_request(device_id):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0xac

    pack_uint32(device_id, packet, 4)
    pack_uint32(0x55aaaa55, packet, 8)

    return packet


def clear_tasklist_request(device_id):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0xa6

    pack_uint32(device_id, packet, 4)
    pack_uint32(0x55aaaa55, packet, 8)

    return packet


def set_pc_control_request(device_id, enable):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0xa0

    pack_uint32(device_id, packet, 4)
    pack_uint32(0x55aaaa55, packet, 8)
    pack_bool(enable, packet, 12)

    return packet


def set_interlock_request(device_id, interlock):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0xa2

    pack_uint32(device_id, packet, 4)
    pack_uint8(interlock, packet, 8)

    return packet


def activate_keypads_request(device_id, reader_1, reader_2, reader_3, reader_4):
    packet = bytearray(64)

    packet[0] = 0x17
    packet[1] = 0xa4

    pack_uint32(device_id, packet, 4)
    pack_bool(reader_1, packet, 8)
    pack_bool(reader_2, packet, 9)
    pack_bool(reader_3, packet, 10)
    pack_bool(reader_4, packet, 11)

    return packet


def pack_uint8(v, packet, offset):
    packet[offset] = v


def pack_uint16(v, packet, offset):
    struct.pack_into('<H', packet, offset, v)


def pack_uint32(v, packet, offset):
    struct.pack_into('<L', packet, offset, v)


def pack_IPv4(v, packet, offset):
    packet[offset:offset + 4] = v.packed


def pack_date(v, packet, offset):
    bcd = f'{v:%Y%m%d}'
    packet[offset:offset + 4] = bytes.fromhex(bcd)


def pack_datetime(v, packet, offset):
    bcd = f'{v:%Y%m%d%H%M%S}'
    packet[offset:offset + 7] = bytes.fromhex(bcd)


def pack_HHmm(v, packet, offset):
    bcd = f'{v:%H%M}'
    packet[offset:offset + 2] = bytes.fromhex(bcd)


def pack_bool(v, packet, offset):
    packet[offset] = 0x00 if not v else 0x01


def pack_pin(v, packet, offset):
    packet[offset] = (v >> 0) & 0x00ff
    packet[offset + 1] = (v >> 8) & 0x0ff
    packet[offset + 2] = (v >> 16) & 0x0ff
