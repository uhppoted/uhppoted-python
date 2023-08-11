'''
Implements a Python wrapper around the UHPPOTE TCP/IP access controller API.
'''

from . import encode
from . import decode
from . import udp


class Uhppote:

    def __init__(self, bind='0.0.0.0', broadcast='255.255.255.255:60000', listen="0.0.0.0:60001", debug=False):
        '''
        Initialises a Uhppote object with the bind address, broadcast address and listen address.

            Parameters:
               bind      (string)  The IPv4 address to which to bind when sending a request.
               broadcast (string)  The IPv4 address:port to which to send broadcast UDP messages.
               listen    (string)  The IPv4 address:port on which to listen for events from the
                                   access controllers.
               debug     (bool)    Enables verbose debugging information.

            Returns:
               Initialised Uhppote object.

            Raises:
               ValueError  If any of the supplied IPv4 values cannot be translated to a valid IPv4 
                           address:port combination.
        '''
        self._udp = udp.UDP(bind, broadcast, listen, debug)

    def get_all_controllers(self):
        '''
        Retrieves a list of all controllers accessible on the local LAN segment.

            Returns:
               []get_controller_response  List of get_controller_responses from access controllers 
                                          on the local LAN segment.

            Raises:
               Exception  If any of the responses from the access controllers cannot be decoded.
        '''
        request = encode.get_controller_request(0)
        replies = self._udp.broadcast(request)

        list = []
        for reply in replies:
            list.append(decode.get_controller_response(reply))

        return list

    def get_controller(self, controller):
        '''
        Retrieves the controller information for an access controller.

            Parameters:
               controller (uint32)  Controller serial number (expected to be greater than 0).

            Returns:
               get_controller_response  Response from access controller to the get-controller request.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.get_controller_request(controller)
        reply = self._udp.send(request)

        if reply != None:
            return decode.get_controller_response(reply)

        return None

    def set_ip(self, controller, address, netmask, gateway):
        '''
        Sets the controller IPv4 address, netmask and gateway address.

            Parameters:
               controller (uint32)       Controller serial number (expected to be greater than 0).
               address    (IPv4Address)  Controller IPv4 address.
               netmask    (IPv4Address)  Controller IPv4 subnet mask.
               gateway    (IPv4Address)  Controller IPv4 gateway address.

            Returns:
               True  For (probably) internal reasons the access controller does not respond to this command.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.set_ip_request(controller, address, netmask, gateway)
        self._udp.send(request)

        return True

    def get_time(self, controller):
        '''
        Retrieves the access controller current date/time.

            Parameters:
               controller (uint32)  Controller serial number (expected to be greater than 0).

            Returns:
               get_time_response  Controller current date/time.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.get_time_request(controller)
        reply = self._udp.send(request)

        if reply != None:
            return decode.get_time_response(reply)

        return None

    def set_time(self, controller, datetime):
        '''
        Sets the access controller current date/time.

            Parameters:
               controller (uint32)   Controller serial number (expected to be greater than 0).
               datetime   (dateime)  Date/time to set.

            Returns:
               set_time_response  Controller current date/time.

            Raises:
               Exception  If the datetime format cannot be encoded or the response from the 
                          access controller cannot be decoded.
        '''
        request = encode.set_time_request(controller, datetime)
        reply = self._udp.send(request)

        if reply != None:
            return decode.set_time_response(reply)

        return None

    def get_status(self, controller):
        '''
        Retrieves the current status of an access controller.

            Parameters:
               controller (uint32)  Controller serial number (expected to be greater than 0).

            Returns:
               get_status_response  Current controller status.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.get_status_request(controller)
        reply = self._udp.send(request)

        if reply != None:
            return decode.get_status_response(reply)

        return None

    def get_listener(self, controller):
        '''
        Retrieves the configured event listener address:port from an access controller.

            Parameters:
               controller (uint32)  Controller serial number (expected to be greater than 0).

            Returns:
               get_listener_response  Current controller event listener UDP address and port.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.get_listener_request(controller)
        reply = self._udp.send(request)

        if reply != None:
            return decode.get_listener_response(reply)

        return None

    def set_listener(self, controller, address, port):
        '''
        Sets an access controller event listener IPv4 address and port.

            Parameters:
               controller (uint32)       Controller serial number (expected to be greater than 0).
               address    (IPv4Address)  IPv4 address of event listener.
               port       (uint16)       UDP port of event listener.

            Returns:
               set_listener_response  Success/fail response from controller.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.set_listener_request(controller, address, port)
        reply = self._udp.send(request)

        if reply != None:
            return decode.set_listener_response(reply)

        return None

    def get_door_control(self, controller, door):
        '''
        Gets the door delay and control mode for an access controller door.

            Parameters:
               controller (uint32)  Controller serial number (expected to be greater than 0).
               door       (uint8)   Door [1..4]

            Returns:
               get_door_control_response  Door delay and control mode.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.get_door_control_request(controller, door)
        reply = self._udp.send(request)

        if reply != None:
            return decode.get_door_control_response(reply)

        return None

    def set_door_control(self, controller, door, mode, delay):
        '''
        Sets the door delay and control mode for an access controller door.

            Parameters:
               controller (uint32)  Controller serial number (expected to be greater than 0).
               door       (uint8)   Door [1..4]
               mode       (uint8)   Control mode (1: normally open, 2: normally closed, 3: controlled)
               delay      (uint8)   Door unlock duration (seconds)

            Returns:
               set_door_control_response  Door delay and control mode.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.set_door_control_request(controller, door, mode, delay)
        reply = self._udp.send(request)

        if reply != None:
            return decode.set_door_control_response(reply)

        return None

    def open_door(self, controller, door):
        '''
        Remotely opens a door controlled by an access controller.

            Parameters:
               controller (uint32)  Controller serial number (expected to be greater than 0).
               door       (uint8)   Door [1..4]

            Returns:
               open_door_response  Door open success/fail response.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.open_door_request(controller, door)
        reply = self._udp.send(request)

        if reply != None:
            return decode.open_door_response(reply)

        return None

    def get_cards(self, controller):
        '''
        Retrieves the number of cards stored in the access controller.

            Parameters:
               controller (uint32)  Controller serial number (expected to be greater than 0).

            Returns:
               get_cards_response  Number of cards stored locally in controller.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.get_cards_request(controller)
        reply = self._udp.send(request)

        if reply != None:
            return decode.get_cards_response(reply)

        return None

    def get_card(self, controller, card_number):
        '''
        Retrieves the card access record for a card number from the access controller.
            Parameters:
               controller  (uint32)  Controller serial number (expected to be greater than 0).
               card_number (uint32)  Access card number.

            Returns:
               get_card_response  Card information associated with the card number.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.get_card_request(controller, card_number)
        reply = self._udp.send(request)

        if reply != None:
            return decode.get_card_response(reply)

        return None

    def get_card_by_index(self, controller, card_index):
        '''
        Retrieves the card access record for a card record from the access controller.
            Parameters:
               controller  (uint32)  Controller serial number (expected to be greater than 0).
               index       (uint32)  Controller card list record number.

            Returns:
               get_card_by_index_response  Card information associated with the card number.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.get_card_by_index_request(controller, card_index)
        reply = self._udp.send(request)

        if reply != None:
            return decode.get_card_by_index_response(reply)

        return None

    def put_card(self, controller, card_number, start_date, end_date, door_1, door_2, door_3, door_4, pin):
        '''
        Adds (or updates) a card record stored on the access controller.
            Parameters:
               controller  (uint32)  Controller serial number (expected to be greater than 0).
               card_number (uint32)  Access card number.
               start_date  (date)    Card 'valid from' date (YYYYMMDD).
               end_date    (date)    Card 'valid until' date (YYYYMMDD).
               door_1      (uint8)   Card access permissions for door 1 (0: none, 1: all, 2-254: time profile ID)
               door_2      (uint8)   Card access permissions for door 2 (0: none, 1: all, 2-254: time profile ID)
               door_3      (uint8)   Card access permissions for door 3 (0: none, 1: all, 2-254: time profile ID)
               door_4      (uint8)   Card access permissions for door 4 (0: none, 1: all, 2-254: time profile ID)
               pin         (uint24)  Card access keypad PIN code (0 for none)

            Returns:
               put_card_response  Card record add/update success/fail.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.put_card_request(controller, card_number, start_date, end_date, door_1, door_2, door_3, door_4,
                                          pin)
        reply = self._udp.send(request)

        if reply != None:
            return decode.put_card_response(reply)

        return None

    def delete_card(self, controller, card_number):
        '''
        Deletes the card record from the access controller.
            Parameters:
               controller  (uint32)  Controller serial number (expected to be greater than 0).
               card_number (uint32)  Access card number to delete.

            Returns:
               delete_card_response  Card record delete success/fail.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.delete_card_request(controller, card_number)
        reply = self._udp.send(request)

        if reply != None:
            return decode.delete_card_response(reply)

        return None

    def delete_all_cards(self, controller):
        '''
        Deletes all card records stored on the access controller.
            Parameters:
               controller  (uint32)  Controller serial number (expected to be greater than 0).

            Returns:
               delete_all_cards_response  Clear card records success/fail.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.delete_cards_request(controller)
        reply = self._udp.send(request)

        if reply != None:
            return decode.delete_all_cards_response(reply)

        return None

    def get_event(self, controller, event_index):
        '''
        Retrieves a stored event from the access controller.
            Parameters:
               controller  (uint32)  Controller serial number (expected to be greater than 0).
               event_index (uint32)  Index of event in controller list.

            Returns:
               get_event_response  Event information.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.get_event_request(controller, event_index)
        reply = self._udp.send(request)

        if reply != None:
            return decode.get_event_response(reply)

        return None

    def get_event_index(self, controller):
        '''
        Retrieves the 'last downloaded event' index from the controller. The downloaded event index
        is a single utility register on the controller that is managed by an application (not by the
        controller).

            Parameters:
               controller  (uint32)  Controller serial number (expected to be greater than 0).

            Returns:
               get_event_index_response  Current value of downloaded event index.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.get_event_index_request(controller)
        reply = self._udp.send(request)

        if reply != None:
            return decode.get_event_index_response(reply)

        return None

    def set_event_index(self, controller, event_index):
        '''
        Sets the 'last downloaded event' index on the controller. The downloaded event index is a 
        single utility register on the controller that is managed by an application (not by the
        controller).

            Parameters:
               controller  (uint32)  Controller serial number (expected to be greater than 0).
               event_index (uitn32)  Event index to which to set the 'downloaded event' index.

            Returns:
               set_event_index_response  Set event index success/fail response.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.set_event_index_request(controller, event_index)
        reply = self._udp.send(request)

        if reply != None:
            return decode.set_event_index_response(reply)

        return None

    def record_special_events(self, controller, enable):
        '''
        Enables or disables door open and close and pushbutton press events.

            Parameters:
               controller  (uint32)  Controller serial number (expected to be greater than 0).
               enable      (bool)    Includes door open and close and pushbutton events in the
                                     events stored and broadcast by the controller.

            Returns:
               record_special_events_response  Record special events success/fail response.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.record_special_events_request(controller, enable)
        reply = self._udp.send(request)

        if reply != None:
            return decode.record_special_events_response(reply)

        return None

    def get_time_profile(self, controller, profile_id):
        '''
        Retrieves a time profile from an access conntroller.

            Parameters:
               controller  (uint32)  Controller serial number (expected to be greater than 0).
               profile_id  (uint8)   Time profile ID [2..254] to retrieve.

            Returns:
               get_time_profile_response  Time profile information for the profile ID.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.get_time_profile_request(controller, profile_id)
        reply = self._udp.send(request)

        if reply != None:
            return decode.get_time_profile_response(reply)

        return None

    def set_time_profile(self, controller, profile_id, start_date, end_date, monday, tuesday, wednesday, thursday,
                         friday, saturday, sunday, segment_1_start, segment_1_end, segment_2_start, segment_2_end,
                         segment_3_start, segment_3_end, linked_profile_id):
        '''
        Creates (or updates) a time profile on an access conntroller.

            Parameters:
               controller        (uint32)  Controller serial number (expected to be greater than 0).
               profile_id        (uint8)   Time profile ID [2..254] to retrieve.
               start_date        (date)    Time profile 'valid from' date.
               end_date          (date)    Time profile 'valid until' date.
               monday            (bool)    Time profile enabled on Monday.
               tuesday           (bool)    Time profile enabled on Tuesday.
               wednesday         (bool)    Time profile enabled on Wednesday.
               thursday          (bool)    Time profile enabled on Thursday.
               friday            (bool)    Time profile enabled on Friday.
               saturday          (bool)    Time profile enabled on Saturday.
               sunday            (bool)    Time profile enabled on Sunday.
               segment_1_start   (time)    Time profile segment 1 start time (HHmm).
               segment_1_end     (time)    Time profile segment 1 end time (HHmm).
               segment_2_start   (time)    Time profile segment 2 start time (HHmm).
               segment_2_end     (time)    Time profile segment 2 end time (HHmm).
               segment_3_start   (time)    Time profile segment 3 start time (HHmm).
               segment_3_end     (time)    Time profile segment 3 end time (HHmm).
               linked_profile_id (uint8)   Next profile ID in chain (0 if none).
 
            Returns:
               set_time_profile_response  Set time profile success/fail response.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.set_time_profile_request(controller, profile_id, start_date, end_date, monday, tuesday,
                                                  wednesday, thursday, friday, saturday, sunday, segment_1_start,
                                                  segment_1_end, segment_2_start, segment_2_end, segment_3_start,
                                                  segment_3_end, linked_profile_id)
        reply = self._udp.send(request)

        if reply != None:
            return decode.set_time_profile_response(reply)

        return None

    def delete_all_time_profiles(self, controller):
        '''
        Clears all time profiles from an access conntroller.

            Parameters:
               controller (uint32)  Controller serial number (expected to be greater than 0).

            Returns:
               delete_all_time_profiles_response  Clear time profiles success/fail response.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.delete_all_time_profiles_request(controller)
        reply = self._udp.send(request)

        if reply != None:
            return decode.delete_all_time_profiles_response(reply)

        return None

    def add_task(self, controller, start_date, end_date, monday, tuesday, wednesday, thursday, friday, saturday, sunday,
                 start_time, door, task_type, more_cards):
        '''
        Creates a scheduled task on an access conntroller.

            Parameters:
               controller  (uint32)    Controller serial number (expected to be greater than 0).
               start_date  (datetime)  Task 'valid from' date.
               end_date    (datetime)  Task 'valid until' date.
               monday      (bool)      Task enabled on Monday.
               tuesday     (bool)      Task enabled on Tuesday.
               wednesday   (bool)      Task enabled on Wednesday.
               thursday    (bool)      Task enabled on Thursday.
               friday      (bool)      Task enabled on Friday.
               saturday    (bool)      Task enabled on Saturday.
               sunday      (bool)      Task enabled on Sunday.
               start_time  (time)      Task 'run at' time (HHmm).
               door        (uint8)     Door [1..4] to which task is assigned.
               task_type   (uint8)     Task type
                                       0:  door controlled
                                       1:  door unlocked
                                       2:  door locked
                                       3:  disable time profile
                                       4:  enable time profile
                                       5:  card, no password
                                       6:  card, IN password
                                       7:  card, password
                                       8:  enable 'more cards'
                                       9:  disable 'more cards'
                                       10: trigger once
                                       11: disable pushbutton
                                       12: enable pushbutton
               more_cards  (uint8)     Number of cards for the 'more cards' task.

            Returns:
               add_task_response  Add task success/fail response.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.add_task_request(controller, start_date, end_date, monday, tuesday, wednesday, thursday,
                                          friday, saturday, sunday, start_time, door, task_type, more_cards)
        reply = self._udp.send(request)

        if reply != None:
            return decode.add_task_response(reply)

        return None

    def refresh_tasklist(self, controller):
        '''
        Updates the active tasklist to include tasks added by add_task.

            Parameters:
               controller  (uint32)  Controller serial number (expected to be greater than 0).

            Returns:
               refresh_tasklist_response  Refresh tasklist success/fail response.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.refresh_tasklist_request(controller)
        reply = self._udp.send(request)

        if reply != None:
            return decode.refresh_tasklist_response(reply)

        return None

    def clear_tasklist(self, controller):
        '''
        Clears all active and pending tasks.

            Parameters:
               controller  (uint32)  Controller serial number (expected to be greater than 0).

            Returns:
               clear_tasklist_response  Clear tasklist success/fail response.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.clear_tasklist_request(controller)
        reply = self._udp.send(request)

        if reply != None:
            return decode.clear_tasklist_response(reply)

        return None

    def set_pc_control(self, controller, enable):
        '''
        Defers access control decisions to a remote host. The remote host is expected to 
        interact with the controller at least once every 30 seconds (typically by enabling
        set_pc_control), failing which the access controller will fallback to the internal
        access control list.

            Parameters:
               controller  (uint32)  Controller serial number (expected to be greater than 0).
               enable      (bool)    Enables remote control of access.

            Returns:
               set_pc_control_response  Enable PC control success/fail response.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.set_pc_control_request(controller, enable)
        reply = self._udp.send(request)

        if reply != None:
            return decode.set_pc_control_response(reply)

        return None

    def set_interlock(self, controller, interlock):
        '''
        Sets the door interlock mode for an access controller.

            Parameters:
               controller  (uint32)  Controller serial number (expected to be greater than 0).
               interlock   (uint8)   Door interlock mode:
                                     0:  none
                                     1:  doors 1 and 2 interlocked
                                     2:  doors 2 and 3 interlocked
                                     3:  doors 1 and 2 interlocked, doors 3 and 4 interlocked
                                     4:  doors 1 and 2 and 3 interlocked
                                     8:  doors 1 and 2 and 3 and 4 interlocked

            Returns:
               set_interlock_response  Set interlock success/fail response.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.set_interlock_request(controller, interlock)
        reply = self._udp.send(request)

        if reply != None:
            return decode.set_interlock_response(reply)

        return None

    def activate_keypads(self, controller, reader_1, reader_2, reader_3, reader_4):
        '''
        Enables (or disables) the keypad associated with an access reader.

            Parameters:
               controller (uint32)  Controller serial number (expected to be greater than 0).
               reader_1   (bool)    Enables/disable reader 1 access keypad
               reader_2   (bool)    Enables/disable reader 2 access keypad
               reader_3   (bool)    Enables/disable reader 3 access keypad
               reader_4   (bool)    Enables/disable reader 4 access keypad

            Returns:
               activate_keypads_response  Activate keypads success/fail response.

            Raises:
               Exception  If the response from the access controller cannot be decoded.
        '''
        request = encode.activate_keypads_request(controller, reader_1, reader_2, reader_3, reader_4)
        reply = self._udp.send(request)

        if reply != None:
            return decode.activate_keypads_response(reply)

        return None

    def listen(self, onEvent):
        '''
        Establishes a listener for events from the access controllers by binding to the UDP listen 
        address from the constructor.

            Parameters:
               onEvent  (function)  Handler function for received events, with a function signature 
                                    f(event).

            Returns:
               None
        '''

        def handler(packet):
            try:
                onEvent(decode.event(packet))
            except BaseException as err:
                print('   *** ERROR {}'.format(err))

        self._udp.listen(lambda packet: handler(packet))

        return None
