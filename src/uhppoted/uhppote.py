from . import encode
from . import decode
from . import udp


class Uhppote:

    def __init__(self,
                 bind='0.0.0.0',
                 broadcast='255.255.255.255:60000',
                 listen="0.0.0.0:60001",
                 debug=False):
        self._udp = udp.UDP(bind, broadcast, listen, debug)

    def get_all_controllers(self):
        request = encode.get_controller_request(0)
        replies = self._udp.broadcast(request)

        list = []
        for reply in replies:
            list.append(decode.get_controller_response(reply))

        return list

    def listen(self, onEvent):
        self._udp.listen(lambda packet: events(packet, onEvent))
        return None

    def events(packet, onEvent):
        onEvent(decode.event(packet))

    def get_controller(self, device_id):
        request = encode.get_controller_request(device_id)
        reply = self._udp.send(request)

        if reply != None:
            return decode.get_controller_response(reply)

        return None

    def set_ip(self, device_id, address, netmask, gateway):

        request = encode.set_ip_request(device_id, address, netmask, gateway)
        self._udp.send(request)

        return True

    def get_time(self, device_id):
        request = encode.get_time_request(device_id)
        reply = self._udp.send(request)

        if reply != None:
            return decode.get_time_response(reply)

        return None

    def set_time(self, device_id, time):
        request = encode.set_time_request(device_id, time)
        reply = self._udp.send(request)

        if reply != None:
            return decode.set_time_response(reply)

        return None

    def get_status(self, device_id):
        request = encode.get_status_request(device_id)
        reply = self._udp.send(request)

        if reply != None:
            return decode.get_status_response(reply)

        return None

    def get_listener(self, device_id):
        request = encode.get_listener_request(device_id)
        reply = self._udp.send(request)

        if reply != None:
            return decode.get_listener_response(reply)

        return None

    def set_listener(self, device_id, address, port):
        request = encode.set_listener_request(device_id, address, port)
        reply = self._udp.send(request)

        if reply != None:
            return decode.set_listener_response(reply)

        return None

    def get_door_control(self, device_id, door):
        request = encode.get_door_control_request(device_id, door)
        reply = self._udp.send(request)

        if reply != None:
            return decode.get_door_control_response(reply)

        return None

    def set_door_control(self, device_id, door, mode, delay):
        request = encode.set_door_control_request(device_id, door, mode, delay)
        reply = self._udp.send(request)

        if reply != None:
            return decode.set_door_control_response(reply)

        return None

    def open_door(self, device_id, door):
        request = encode.open_door_request(device_id, door)
        reply = self._udp.send(request)

        if reply != None:
            return decode.open_door_response(reply)

        return None

    def get_cards(self, device_id):
        request = encode.get_cards_request(device_id)
        reply = self._udp.send(request)

        if reply != None:
            return decode.get_cards_response(reply)

        return None

    def get_card(self, device_id, card_number):
        request = encode.get_card_request(device_id, card_number)
        reply = self._udp.send(request)

        if reply != None:
            return decode.get_card_response(reply)

        return None

    def get_card_by_index(self, device_id, card_index):
        request = encode.get_card_by_index_request(device_id, card_index)
        reply = self._udp.send(request)

        if reply != None:
            return decode.get_card_by_index_response(reply)

        return None

    def put_card(self, device_id, card_number, start_date, end_date, door_1, door_2, door_3, door_4,
                 pin):
        request = encode.put_card_request(device_id, card_number, start_date, end_date, door_1,
                                          door_2, door_3, door_4, pin)
        reply = self._udp.send(request)

        if reply != None:
            return decode.put_card_response(reply)

        return None

    def delete_card(self, device_id, card_number):
        request = encode.delete_card_request(device_id, card_number)
        reply = self._udp.send(request)

        if reply != None:
            return decode.delete_card_response(reply)

        return None

    def delete_all_cards(self, device_id):
        request = encode.delete_cards_request(device_id)
        reply = self._udp.send(request)

        if reply != None:
            return decode.delete_all_cards_response(reply)

        return None

    def get_event(self, device_id, event_index):
        request = encode.get_event_request(device_id, event_index)
        reply = self._udp.send(request)

        if reply != None:
            return decode.get_event_response(reply)

        return None

    def get_event_index(self, device_id):
        request = encode.get_event_index_request(device_id)
        reply = self._udp.send(request)

        if reply != None:
            return decode.get_event_index_response(reply)

        return None

    def set_event_index(self, device_id, event_index):
        request = encode.set_event_index_request(device_id, event_index)
        reply = self._udp.send(request)

        if reply != None:
            return decode.set_event_index_response(reply)

        return None

    def record_special_events(self, device_id, enable):
        request = encode.record_special_events_request(device_id, enable)
        reply = self._udp.send(request)

        if reply != None:
            return decode.record_special_events_response(reply)

        return None

    def get_time_profile(self, device_id, profile_id):
        request = encode.get_time_profile_request(device_id, profile_id)
        reply = self._udp.send(request)

        if reply != None:
            return decode.get_time_profile_response(reply)

        return None

    def set_time_profile(self, device_id, profile_id, start_date, end_date, monday, tuesday,
                         wednesday, thursday, friday, saturday, sunday, segment_1_start,
                         segment_1_end, segment_2_start, segment_2_end, segment_3_start,
                         segment_3_end, linked_profile_id):
        request = encode.set_time_profile_request(device_id, profile_id, start_date, end_date,
                                                  monday, tuesday, wednesday, thursday, friday,
                                                  saturday, sunday, segment_1_start, segment_1_end,
                                                  segment_2_start, segment_2_end, segment_3_start,
                                                  segment_3_end, linked_profile_id)
        reply = self._udp.send(request)

        if reply != None:
            return decode.set_time_profile_response(reply)

        return None

    def delete_all_time_profiles(self, device_id):
        request = encode.delete_all_time_profiles_request(device_id)
        reply = self._udp.send(request)

        if reply != None:
            return decode.delete_all_time_profiles_response(reply)

        return None

    def add_task(self, device_id, start_date, end_date, monday, tuesday, wednesday, thursday,
                 friday, saturday, sunday, start_time, door, task_type, more_cards):
        request = encode.add_task_request(device_id, start_date, end_date, monday, tuesday,
                                          wednesday, thursday, friday, saturday, sunday, start_time,
                                          door, task_type, more_cards)
        reply = self._udp.send(request)

        if reply != None:
            return decode.add_task_response(reply)

        return None

    def refresh_tasklist(self, device_id):
        request = encode.refresh_tasklist_request(device_id)
        reply = self._udp.send(request)

        if reply != None:
            return decode.refresh_tasklist_response(reply)

        return None

    def clear_tasklist(self, device_id):
        request = encode.clear_tasklist_request(device_id)
        reply = self._udp.send(request)

        if reply != None:
            return decode.clear_tasklist_response(reply)

        return None

    def set_pc_control(self, device_id, enable):
        request = encode.set_pc_control_request(device_id, enable)
        reply = self._udp.send(request)

        if reply != None:
            return decode.set_pc_control_response(reply)

        return None

    def set_interlock(self, device_id, interlock):
        request = encode.set_interlock_request(device_id, interlock)
        reply = self._udp.send(request)

        if reply != None:
            return decode.set_interlock_response(reply)

        return None

    def activate_keypads(self, device_id, reader_1, reader_2, reader_3, reader_4):
        request = encode.activate_keypads_request(device_id, reader_1, reader_2, reader_3, reader_4)
        reply = self._udp.send(request)

        if reply != None:
            return decode.activate_keypads_response(reply)

        return None
