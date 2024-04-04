'''
Expected responses for UHPPOTE integration tests.
'''

import datetime
import ipaddress

from uhppoted import structs

GetControllerResponse = structs.GetControllerResponse(
    controller=405419896, 
    ip_address=ipaddress.IPv4Address('192.168.1.100'), 
    subnet_mask=ipaddress.IPv4Address('255.255.255.0'), 
    gateway=ipaddress.IPv4Address('192.168.1.1'), 
    mac_address='00:12:23:34:45:56', 
    version='v8.92', 
    date=datetime.date(2018, 11, 5))

SetIPResponse = True

GetTimeResponse = structs.GetTimeResponse(
    controller=405419896, 
    datetime=datetime.datetime(2021, 5, 28, 13, 51, 30))
        
SetTimeResponse = structs.SetTimeResponse(
    controller=405419896, 
    datetime=datetime.datetime(2021, 5, 28, 14, 56, 14))

GetStatusResponse = structs.GetStatusResponse(
    controller=405419896, 
    system_date=datetime.date(2021, 5, 28), 
    system_time=datetime.time(15, 14, 46), 
    door_1_open=False, 
    door_2_open=False, 
    door_3_open=False, 
    door_4_open=False, 
    door_1_button=False, 
    door_2_button=False, 
    door_3_button=False, 
    door_4_button=False, 
    relays=0, 
    inputs=0, 
    system_error=0, 
    special_info=0, 
    event_index=69, 
    event_type=2, 
    event_access_granted=True, 
    event_door=1, 
    event_direction=1, 
    event_card=0, 
    event_timestamp=datetime.datetime(2019, 8, 10, 10, 28, 32), 
    event_reason=44, 
    sequence_no=0)

GetListenerResponse = structs.GetListenerResponse(
    controller=405419896, 
    address=ipaddress.IPv4Address('192.168.1.100'), 
    port=60001)

SetListenerResponse = structs.SetListenerResponse(
    controller=405419896, 
    ok=True)

GetDoorControlResponse = structs.GetDoorControlResponse(
    controller=405419896, 
    door=3, 
    mode=3, 
    delay=7)

SetDoorControlResponse = structs.SetDoorControlResponse(
    controller=405419896, 
    door=3, 
    mode=2, 
    delay=4)

OpenDoorResponse = structs.OpenDoorResponse(
    controller=405419896, 
    opened=True)
