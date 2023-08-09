import datetime
import struct

from ipaddress import IPv4Address
from dataclasses import dataclass
from typing import NewType

PIN = NewType('PIN', int)


def get_controller_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0x94:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return GetControllerResponse(
        unpack_uint32(packet, 4),
        unpack_ipv4(packet, 8),
        unpack_ipv4(packet, 12),
        unpack_ipv4(packet, 16),
        unpack_mac(packet, 20),
        unpack_version(packet, 26),
        unpack_date(packet, 28),
    )


def get_time_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0x32:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return GetTimeResponse(
        unpack_uint32(packet, 4),
        unpack_datetime(packet, 8),
    )


def set_time_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0x30:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return SetTimeResponse(
        unpack_uint32(packet, 4),
        unpack_datetime(packet, 8),
    )


def get_status_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0x20:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return GetStatusResponse(
        unpack_uint32(packet, 4),
        unpack_shortdate(packet, 51),
        unpack_time(packet, 37),
        unpack_bool(packet, 28),
        unpack_bool(packet, 29),
        unpack_bool(packet, 30),
        unpack_bool(packet, 31),
        unpack_bool(packet, 32),
        unpack_bool(packet, 33),
        unpack_bool(packet, 34),
        unpack_bool(packet, 35),
        unpack_uint8(packet, 49),
        unpack_uint8(packet, 50),
        unpack_uint8(packet, 36),
        unpack_uint8(packet, 48),
        unpack_uint32(packet, 8),
        unpack_uint8(packet, 12),
        unpack_bool(packet, 13),
        unpack_uint8(packet, 14),
        unpack_uint8(packet, 15),
        unpack_uint32(packet, 16),
        unpack_optional_datetime(packet, 20),
        unpack_uint8(packet, 27),
        unpack_uint32(packet, 40),
    )


def get_listener_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0x92:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return GetListenerResponse(
        unpack_uint32(packet, 4),
        unpack_ipv4(packet, 8),
        unpack_uint16(packet, 12),
    )


def set_listener_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0x90:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return SetListenerResponse(
        unpack_uint32(packet, 4),
        unpack_bool(packet, 8),
    )


def get_door_control_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0x82:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return GetDoorControlResponse(
        unpack_uint32(packet, 4),
        unpack_uint8(packet, 8),
        unpack_uint8(packet, 9),
        unpack_uint8(packet, 10),
    )


def set_door_control_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0x80:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return SetDoorControlResponse(
        unpack_uint32(packet, 4),
        unpack_uint8(packet, 8),
        unpack_uint8(packet, 9),
        unpack_uint8(packet, 10),
    )


def open_door_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0x40:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return OpenDoorResponse(
        unpack_uint32(packet, 4),
        unpack_bool(packet, 8),
    )


def get_cards_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0x58:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return GetCardsResponse(
        unpack_uint32(packet, 4),
        unpack_uint32(packet, 8),
    )


def get_card_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0x5a:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return GetCardResponse(
        unpack_uint32(packet, 4),
        unpack_uint32(packet, 8),
        unpack_optional_date(packet, 12),
        unpack_optional_date(packet, 16),
        unpack_uint8(packet, 20),
        unpack_uint8(packet, 21),
        unpack_uint8(packet, 22),
        unpack_uint8(packet, 23),
        unpack_pin(packet, 24),
    )


def get_card_by_index_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0x5c:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return GetCardByIndexResponse(
        unpack_uint32(packet, 4),
        unpack_uint32(packet, 8),
        unpack_optional_date(packet, 12),
        unpack_optional_date(packet, 16),
        unpack_uint8(packet, 20),
        unpack_uint8(packet, 21),
        unpack_uint8(packet, 22),
        unpack_uint8(packet, 23),
        unpack_pin(packet, 24),
    )


def put_card_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0x50:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return PutCardResponse(
        unpack_uint32(packet, 4),
        unpack_bool(packet, 8),
    )


def delete_card_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0x52:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return DeleteCardResponse(
        unpack_uint32(packet, 4),
        unpack_bool(packet, 8),
    )


def delete_all_cards_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0x54:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return DeleteAllCardsResponse(
        unpack_uint32(packet, 4),
        unpack_bool(packet, 8),
    )


def get_event_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0xb0:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return GetEventResponse(
        unpack_uint32(packet, 4),
        unpack_uint32(packet, 8),
        unpack_uint8(packet, 12),
        unpack_bool(packet, 13),
        unpack_uint8(packet, 14),
        unpack_uint8(packet, 15),
        unpack_uint32(packet, 16),
        unpack_optional_datetime(packet, 20),
        unpack_uint8(packet, 27),
    )


def get_event_index_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0xb4:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return GetEventIndexResponse(
        unpack_uint32(packet, 4),
        unpack_uint32(packet, 8),
    )


def set_event_index_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0xb2:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return SetEventIndexResponse(
        unpack_uint32(packet, 4),
        unpack_bool(packet, 8),
    )


def record_special_events_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0x8e:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return RecordSpecialEventsResponse(
        unpack_uint32(packet, 4),
        unpack_bool(packet, 8),
    )


def get_time_profile_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0x98:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return GetTimeProfileResponse(
        unpack_uint32(packet, 4),
        unpack_uint8(packet, 8),
        unpack_optional_date(packet, 9),
        unpack_optional_date(packet, 13),
        unpack_bool(packet, 17),
        unpack_bool(packet, 18),
        unpack_bool(packet, 19),
        unpack_bool(packet, 20),
        unpack_bool(packet, 21),
        unpack_bool(packet, 22),
        unpack_bool(packet, 23),
        unpack_hhmm(packet, 24),
        unpack_hhmm(packet, 26),
        unpack_hhmm(packet, 28),
        unpack_hhmm(packet, 30),
        unpack_hhmm(packet, 32),
        unpack_hhmm(packet, 34),
        unpack_uint8(packet, 36),
    )


def set_time_profile_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0x88:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return SetTimeProfileResponse(
        unpack_uint32(packet, 4),
        unpack_bool(packet, 8),
    )


def delete_all_time_profiles_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0x8a:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return DeleteAllTimeProfilesResponse(
        unpack_uint32(packet, 4),
        unpack_bool(packet, 8),
    )


def add_task_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0xa8:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return AddTaskResponse(
        unpack_uint32(packet, 4),
        unpack_bool(packet, 8),
    )


def refresh_tasklist_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0xac:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return RefreshTasklistResponse(
        unpack_uint32(packet, 4),
        unpack_bool(packet, 8),
    )


def clear_tasklist_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0xa6:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return ClearTasklistResponse(
        unpack_uint32(packet, 4),
        unpack_bool(packet, 8),
    )


def set_pc_control_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0xa0:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return SetPcControlResponse(
        unpack_uint32(packet, 4),
        unpack_bool(packet, 8),
    )


def set_interlock_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0xa2:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return SetInterlockResponse(
        unpack_uint32(packet, 4),
        unpack_bool(packet, 8),
    )


def activate_keypads_response(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0xa4:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return ActivateKeypadsResponse(
        unpack_uint32(packet, 4),
        unpack_bool(packet, 8),
    )


def event(packet):
    if len(packet) != 64:
        raise ValueError(f'invalid reply packet length ({len(packet)})')

    # Ref. v6.62 firmware event
    if packet[0] != 0x17 and (packet[0] != 0x19 or packet[1] != 0x20):
        raise ValueError(
            f'invalid reply start of message byte ({packet[0]:02x})')

    if packet[1] != 0x20:
        raise ValueError(f'invalid reply function code ({packet[1]:02x})')

    return Event(
        unpack_uint32(packet, 4),
        unpack_uint32(packet, 8),
        unpack_uint8(packet, 12),
        unpack_bool(packet, 13),
        unpack_uint8(packet, 14),
        unpack_uint8(packet, 15),
        unpack_uint32(packet, 16),
        unpack_datetime(packet, 20),
        unpack_uint8(packet, 27),
        unpack_shortdate(packet, 51),
        unpack_time(packet, 37),
        unpack_uint8(packet, 36),
        unpack_bool(packet, 28),
        unpack_bool(packet, 29),
        unpack_bool(packet, 30),
        unpack_bool(packet, 31),
        unpack_bool(packet, 32),
        unpack_bool(packet, 33),
        unpack_bool(packet, 34),
        unpack_bool(packet, 35),
        unpack_uint8(packet, 49),
        unpack_uint8(packet, 50),
        unpack_uint8(packet, 48),
        unpack_uint32(packet, 40),
    )


@dataclass
class GetControllerResponse:
    controller: int
    ip_address: IPv4Address
    subnet_mask: IPv4Address
    gateway: IPv4Address
    mac_address: str
    version: str
    date: datetime.date


@dataclass
class GetTimeResponse:
    controller: int
    datetime: datetime.datetime


@dataclass
class SetTimeResponse:
    controller: int
    datetime: datetime.datetime


@dataclass
class GetStatusResponse:
    controller: int
    system_date: datetime.date
    system_time: datetime.time
    door_1_open: bool
    door_2_open: bool
    door_3_open: bool
    door_4_open: bool
    door_1_button: bool
    door_2_button: bool
    door_3_button: bool
    door_4_button: bool
    relays: int
    inputs: int
    system_error: int
    special_info: int
    event_index: int
    event_type: int
    event_access_granted: bool
    event_door: int
    event_direction: int
    event_card: int
    event_timestamp: datetime.datetime
    event_reason: int
    sequence_no: int


@dataclass
class GetListenerResponse:
    controller: int
    address: IPv4Address
    port: int


@dataclass
class SetListenerResponse:
    controller: int
    ok: bool


@dataclass
class GetDoorControlResponse:
    controller: int
    door: int
    mode: int
    delay: int


@dataclass
class SetDoorControlResponse:
    controller: int
    door: int
    mode: int
    delay: int


@dataclass
class OpenDoorResponse:
    controller: int
    opened: bool


@dataclass
class GetCardsResponse:
    controller: int
    cards: int


@dataclass
class GetCardResponse:
    controller: int
    card_number: int
    start_date: datetime.date
    end_date: datetime.date
    door_1: int
    door_2: int
    door_3: int
    door_4: int
    pin: PIN


@dataclass
class GetCardByIndexResponse:
    controller: int
    card_number: int
    start_date: datetime.date
    end_date: datetime.date
    door_1: int
    door_2: int
    door_3: int
    door_4: int
    pin: PIN


@dataclass
class PutCardResponse:
    controller: int
    stored: bool


@dataclass
class DeleteCardResponse:
    controller: int
    deleted: bool


@dataclass
class DeleteAllCardsResponse:
    controller: int
    deleted: bool


@dataclass
class GetEventResponse:
    controller: int
    index: int
    event_type: int
    access_granted: bool
    door: int
    direction: int
    card: int
    timestamp: datetime.datetime
    reason: int


@dataclass
class GetEventIndexResponse:
    controller: int
    event_index: int


@dataclass
class SetEventIndexResponse:
    controller: int
    updated: bool


@dataclass
class RecordSpecialEventsResponse:
    controller: int
    updated: bool


@dataclass
class GetTimeProfileResponse:
    controller: int
    profile_id: int
    start_date: datetime.date
    end_date: datetime.date
    monday: bool
    tuesday: bool
    wednesday: bool
    thursday: bool
    friday: bool
    saturday: bool
    sunday: bool
    segment_1_start: datetime.time
    segment_1_end: datetime.time
    segment_2_start: datetime.time
    segment_2_end: datetime.time
    segment_3_start: datetime.time
    segment_3_end: datetime.time
    linked_profile_id: int


@dataclass
class SetTimeProfileResponse:
    controller: int
    stored: bool


@dataclass
class DeleteAllTimeProfilesResponse:
    controller: int
    deleted: bool


@dataclass
class AddTaskResponse:
    controller: int
    added: bool


@dataclass
class RefreshTasklistResponse:
    controller: int
    refreshed: bool


@dataclass
class ClearTasklistResponse:
    controller: int
    cleared: bool


@dataclass
class SetPcControlResponse:
    controller: int
    ok: bool


@dataclass
class SetInterlockResponse:
    controller: int
    ok: bool


@dataclass
class ActivateKeypadsResponse:
    controller: int
    ok: bool


@dataclass
class Event:
    device_id: int
    event_index: int
    event_type: int
    event_access_granted: bool
    event_door: int
    event_direction: int
    event_card: int
    event_timestamp: datetime.datetime
    event_reason: int
    system_date: datetime.date
    system_time: datetime.time
    system_error: int
    door_1_open: bool
    door_2_open: bool
    door_3_open: bool
    door_4_open: bool
    door_1_button: bool
    door_2_button: bool
    door_3_button: bool
    door_4_button: bool
    relays: int
    inputs: int
    special_info: int
    sequence_no: int


def unpack_uint8(packet, offset):
    return packet[offset]


def unpack_uint16(packet, offset):
    return struct.unpack_from('<H', packet, offset)[0]


def unpack_uint32(packet, offset):
    return struct.unpack_from('<L', packet, offset)[0]


def unpack_ipv4(packet, offset):
    return IPv4Address(packet[offset:offset + 4])


def unpack_mac(packet, offset):
    return '{:02x}:{:02x}:{:02x}:{:02x}::{:02x}:{:02x}'.format(
        *packet[offset:offset + 7])


def unpack_version(packet, offset):
    return 'v{:x}.{:02x}'.format(*packet[offset:offset + 2])


def unpack_date(packet, offset):
    bcd = '{:02x}{:02x}{:02x}{:02x}'.format(*packet[offset:offset + 4])

    return datetime.datetime.strptime(bcd, '%Y%m%d').date()


def unpack_shortdate(packet, offset):
    bcd = '20{:02x}{:02x}{:02x}'.format(*packet[offset:offset + 3])

    return datetime.datetime.strptime(bcd, '%Y%m%d').date()


def unpack_optional_date(packet, offset):
    bcd = '{:02x}{:02x}{:02x}{:02x}'.format(*packet[offset:offset + 4])

    try:
        return datetime.datetime.strptime(bcd, '%Y%m%d').date()
    except ValueError as x:
        return None


def unpack_datetime(packet, offset):
    bcd = '{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}'.format(
        *packet[offset:offset + 7])

    return datetime.datetime.strptime(bcd, '%Y%m%d%H%M%S')


def unpack_optional_datetime(packet, offset):
    bcd = '{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}{:02x}'.format(
        *packet[offset:offset + 7])

    try:
        return datetime.datetime.strptime(bcd, '%Y%m%d%H%M%S')
    except ValueError as x:
        return None


def unpack_time(packet, offset):
    bcd = '{:02x}{:02x}{:02x}'.format(*packet[offset:offset + 3])

    return datetime.datetime.strptime(bcd, '%H%M%S').time()


def unpack_hhmm(packet, offset):
    bcd = '{:02x}{:02x}'.format(*packet[offset:offset + 2])

    return datetime.datetime.strptime(bcd, '%H%M').time()


def unpack_bool(packet, offset):
    return packet[offset] != 0x00


def unpack_pin(packet, offset):
    v = packet[offset + 2] & 0x0ff
    v <<= 8
    v |= packet[offset + 1] & 0x0ff
    v <<= 8
    v |= packet[offset] & 0x00ff

    return v
