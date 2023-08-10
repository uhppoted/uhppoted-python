![build](https://github.com/uhppoted/uhppoted-python/workflows/build/badge.svg)

**(IN PROGRESS)**

# uhppoted-python

Python API for the UHPPOTE TCP/IP access controllers, generated from the models in [uhppoted-codegen](https://github.com/uhppoted/uhppoted-codegen). A demo CLI illustrating the use of the API can be found in the [examples/cli](https://github.com/uhppoted/uhppoted-python/tree/main/examples/cli) folder.

## Installation

```
pip install uhppoted
```

## API

Invoking an API function requires an instance of the `Uhppote` class initialised with the information required
to access a controller:

```
class Uhppote:
    def __init__(self, uhppote=None):

where uhppote is an instance of 

class UHPPOTE:
    bind: str
    broadcast: str
    listen: str
    debug: bool

bind        IPv4 address:port to which to bind the UDP socket. Defaults to 0.0.0.0:0
broadcast   IPv4 address:port for broadcast UDP packets. Defaults to 255.255.255.255:60000
listen      IPv4 address:port for events from controller (unused). Defaults to 0.0.0.0:60001
debug       Displays the DLL and controller requests/responses if true.
```

e.g.:
```
from uhppoted import uhppote

    ...
    bind = '0.0.0.0:0'
    broadcast = '255.255.255.255:60000'
    listen = '0.0.0.0:60001'
    debug = True

    u = uhppote.Uhppote(bind, broadcast, listen, debug)
    record = u.get_controller(405419896)

    print(record)
    ...
```

All API functions raise an `Exception` if the call fails for any reason whatsoever.

### `get_controllers`
```
get_controllers()

Returns an array of `get_controller` responses if the call succeeded.

Raises an Exception if the call failed.
```

### `get_controller`
```
get_controller(ID)

ID  uint32  controller serial number 

Returns a `get_controller` dataclass instance populated with the controller device information
if the call succeeded.

Raises an Exception if the call failed.
```

### `set_address`
```
set_address(self, ID, address, subnet, gateway)

ID       uint32  controller serial number 
address  string  controller IPv4 address
subnet   string  controller IPv4 subnet mask
gateway  string  controller gateway IPv4 address

Raises an Exception if the call failed.
```

### `get_status`
```
get_status(ID)

ID  uint32  controller serial number 

Returns a Status dataclass instance populated with the controller status information if the call succeeded.

Raises an Exception if the call failed.
```

### `get_time`
```
get_time(ID)

ID  uint32  controller serial number 

Returns a date/time string (YYYY-MM-dd HH:mm:ss) with the controller current date/time if the call succeeded.

Raises an Exception if the call failed.
```

### `set_time`
```
set_time(ID, datetime)

ID        uint32    controller serial number 
datetime  datetime  date/time

Raises an Exception if the call failed.
```

### `get_listener`
```
get_listener(ID)

ID  uint32  controller serial number 

Returns the controller event listener IPv4 address:port as a string if the call succeeded.

Raises an Exception if the call failed.
```

### `set_listener`
```
set_listener(ID, listener)

ID        uint32  controller serial number 
listener  string  listener IPv4 address:port string

Raises an Exception if the call failed.
```

### `get_door_control`
```
get_door_control(ID, door)

ID    uint32  controller serial number 
door  uint8   door ID [1..4]

Returns a DoorControl dataclass instance populated with the controller door configuration if the call succeeded.

Raises an Exception if the call failed.
```

### `set_door_control`
```
set_door_control(ID, door, mode, delay)

ID    uint32  controller serial number 
door  uint8   door ID [1..4]
mode  uint8   normally open (1), normally closed (2) or controlled (3)
delay uintt8  door open delay in seconds

Raises an Exception if the call failed.
```

### `open_door`
```
open_door(ID, door)

ID    uint32  controller serial number 
door  uint8   door ID [1..4]

Raises an Exception if the call failed.
```

### `get_cards`
```
get_cards(ID)

ID  uint32  controller serial number 

Returns the number of cards stored on the controller if the call succeeded.

Raises an Exception if the call failed.
```

### `get_card`
```
get_card(ID, cardNumber)

ID          uint32  controller serial number 
cardNumber  uint32  card number

Returns a Card dataclass instance with the controller card information if the call succeeded.

Raises an Exception if the call failed.
```

### `get_card_by_index`
```
get_card_by_index(ID, index)

ID     uint32  controller serial number 
index  uint32  index of card to retrieve

Returns a Card dataclass instance with the controller card information if the call succeeded.

Raises an Exception if the call failed.
```

### `put_card`
```
put_card(ID, cardNumber, start, end, door1, door2, door3, door4)

ID           uint32     controller serial number 
card_number  uint32     card number
from         datetime   card valid from date, inclusive (YYYY-MM-dd)
to           datetime   card valid until, inclusive (YYYY-MM-dd)
door1        uint8      Door 1 access (0: none, 1: all, 2-254: time profile)
door2        uint8      Door 2 access (0: none, 1: all, 2-254: time profile)
door3        uint8      Door 3 access (0: none, 1: all, 2-254: time profile)
door4        uint8      Door 4 access (0: none, 1: all, 2-254: time profile)

Raises an Exception if the call failed.
```

### `delete_card`
```
delete_card(ID, cardNumber)

ID          uint32  controller serial number 
cardNumber  uint32  card number

Raises an Exception if the call failed.
```

### `delete_cards`
```
delete_cards(ID)

ID  uint32  controller serial number 

Raises an Exception if the call failed.
```

### `get_event_index`
```
get_event_index(ID)

ID  uint32  controller serial number 

Returns the controller event index if the call succeeded.

Raises an Exception if the call failed.
```

### `set_event_index`
```
set_event_index(ID, index)

ID     uint32  controller serial number 
index  uint32  controller event index

Raises an Exception if the call failed.
```

### `get_event`
```
get_event(ID, index)

ID     uint32  controller serial number 
index  uint32  index of event to retrieve

Returns an event dataclass instance with the controller event stored at the index.

Raises an Exception if the call failed.
```

### `record_special_events`
```
record_special_events(ID, enabled)

ID       uint32  controller serial number 
enabled  bool    Enables/disables recording of door, etc events

Raises an Exception if the call failed.
```

### `get_time_profile`
```
get_time_profile(ID, profileID)

ID          uint32  controller serial number 
profile_ID  uint8   ID [2..254] of time profile to retrieve

Returns a TimeProfile dataclass instance with the time profile stored at the profile ID on the controller.

Raises an Exception if the call failed.
```

### `set_time_profile`
```
set_time_profile(ID, profile)

ID       uint32  controller serial number 
profile  uint8   TimeProfile dataclass instance initialised with the time profile to store on the controller.

Raises an Exception if the call failed.
```

### `clear_time_profiles`
```
clear_time_profiles(ID)

ID  uint32  controller serial number 

Raises an Exception if the call failed.
```

### `add_task`
```
add_task(ID, task)

ID    uint32  controller serial number 
task  uint8   Task dataclass instance initialised with the task to store on the controller.

Raises an Exception if the call failed.
```

### `refresh_tasklist`
```
refresh_tasklist(ID)

ID  uint32  controller serial number 

Raises an Exception if the call failed.
```

### `clear_tasklist`
```
clear_tasklist(ID)

ID  uint32  controller serial number 

Raises an Exception if the call failed.
```

### `set_pc_control`
```
set_pc_control(ID, enabled)

ID       uint32  controller serial number 
enabled  bool    enables/disables host control

Raises an Exception if the call failed.
```

### `set_interlock`
```
set_interlock(ID, interlock)

ID        uint32  controller serial number 
interlock uint8   controller door interlock mode
                  0: no interlock
                  1: doors 1&2
                  2: doors 3&4
                  3: doors 1&2,3&4
                  4: doors 1&2&3
                  8: doors 1&2&3&4


Raises an Exception if the call failed.
```

### `activate_keypads`
```
activate_keypads(ID, reader1, reader2, reader3, reader4)

ID      uint32  controller serial number 
reader1 bool    activates/deactivates reader 1 access keypad
reader2 bool    activates/deactivates reader 2 access keypad
reader3 bool    activates/deactivates reader 3 access keypad
reader4 bool    activates/deactivates reader 4 access keypad


Raises an Exception if the call failed.
```

## Types

### `Controller`
Container class for use with the `uhppoted` _conclassor_.
```
@dataclass
class Controller:
    id: int
    address: str
```

### `Device`
Container class for the controller information retrieved by `get_device`
```
@dataclass
class Device:
    ID: int
    address: str
    subnet: str
    gateway: str
    MAC: str
    version: str
    date: str
```

### `Event`
Container class for the event information retrieved by `get_event`.
```
@dataclass
class Event:
    timestamp: str
    index: int
    eventType: int
    granted: bool
    door: int
    direction: int
    card: int
    reason: int
```

### `Status`
Container class for the controller status information retrieved by `get_status`
```
@dataclass
class Status:
    ID: int
    sysdatetime: str
    doors: list[bool]
    buttons: list[bool]
    relays: int
    inputs: int
    syserror: int
    seqno: int
    info: int
    evt: Event

```

### `DoorControl`
Container class for door configuration for `get_door_control` and `set_door_control`.
```
@dataclass
class DoorControl:
    mode: int
    delay: int
```

### `Card`
Container class for card information retrieved by `get_card` and `get_card_by_index`.
```
@dataclass
class Card:
    cardNumber: int
    start: str
    end: str
    doors: list[int]
```

### `TimeProfile`
Container class for time profile information retrieved/set by `get_time_profile` and 
`set_time_profile`.
```
@dataclass
class TimeProfile:
    ID: int
    linked: int
    start: str
    end: str
    monday: bool
    tuesday: bool
    wednesday: bool
    thursday: bool
    friday: bool
    saturday: bool
    sunday: bool
    segment1start: str
    segment1end: str
    segment2start: str
    segment2end: str
    segment3start: str
    segment3end: str
```

### task
Container class for the task information required for `add_task`.
```
@dataclass
class Task:
    task: int
    door: int
    start: str
    end: str
    monday: bool
    tuesday: bool
    wednesday: bool
    thursday: bool
    friday: bool
    saturday: bool
    sunday: bool
    at: str
    cards: int
```
