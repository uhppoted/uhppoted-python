'''
Shared dataclass definitions.
'''

import datetime
import struct

from ipaddress import IPv4Address
from dataclasses import dataclass
from typing import NewType

PIN = NewType('PIN', int)


@dataclass
class GetControllerResponse:
    '''
    Container class for the decoded response from a get-controller request.

       Fields:
          controller   (uint32)       Serial number.
          ip_address   (IPv4Address)  IP address.
          subnet_mask  (IPv4Address)  Subnet mask.
          gateway      (IPv4Address)  Gateway IP address.
          mac_address  (string)       MAC address (XX:XX:XX:XX:XX:XX).
          version      (string)       Firmware version (vN.NN).
          date         (date)         Release date (YYYY-MM-DD).
    '''
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
