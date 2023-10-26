'''
UHPPOTE request packet decoder unit tests.

Tests the packet decoding functions.
'''

import unittest
import datetime

from uhppoted import decode


class TestDecode(unittest.TestCase):

    def test_get_status_response(self):
        '''
        Tests a valid get-status response.
        '''
        # yapf: disable
        packet = bytearray([
            0x17, 0x20, 0x00, 0x00, 0x78, 0x37, 0x2a, 0x18, 0x4e, 0x00, 0x00, 0x00, 0x02, 0x01, 0x03, 0x01,
            0xa1, 0x98, 0x7c, 0x00, 0x20, 0x22, 0x08, 0x23, 0x09, 0x47, 0x06, 0x2c, 0x00, 0x01, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x01, 0x03, 0x09, 0x49, 0x39, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x27, 0x07, 0x09, 0x22, 0x08, 0x23, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        ])
        # yapf: enable

        response = decode.get_status_response(packet)

        self.assertEqual(response.controller, 405419896)
        self.assertEqual(response.system_date, datetime.date(2022, 8, 23))
        self.assertEqual(response.system_time, datetime.time(9, 49, 39))
        self.assertEqual(response.door_1_open, False)
        self.assertEqual(response.door_2_open, True)
        self.assertEqual(response.door_3_open, False)
        self.assertEqual(response.door_4_open, False)
        self.assertEqual(response.door_1_button, False)
        self.assertEqual(response.door_2_button, False)
        self.assertEqual(response.door_3_button, False)
        self.assertEqual(response.door_4_button, True)
        self.assertEqual(response.relays, 7)
        self.assertEqual(response.inputs, 9)
        self.assertEqual(response.system_error, 3)
        self.assertEqual(response.special_info, 39)
        self.assertEqual(response.event_index, 78)
        self.assertEqual(response.event_type, 2)
        self.assertEqual(response.event_access_granted, True)
        self.assertEqual(response.event_door, 3)
        self.assertEqual(response.event_direction, 1)
        self.assertEqual(response.event_card, 8165537)
        self.assertEqual(response.event_timestamp, datetime.datetime(2022, 8, 23, 9, 47, 6))
        self.assertEqual(response.event_reason, 44)
        self.assertEqual(response.sequence_no, 0)

    def test_get_status_response_with_no_event(self):
        '''
        Tests a valid get-status response with no event information in the response.
        '''
        # yapf: disable
        packet = bytearray([
                  0x17, 0x20, 0x00, 0x00, 0x78, 0x37, 0x2a, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00,
                  0x00, 0x00, 0x00, 0x01, 0x03, 0x09, 0x49, 0x39, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x27, 0x07, 0x09, 0x22, 0x08, 0x23, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        ])
        # yapf: enable

        response = decode.get_status_response(packet)

        self.assertEqual(response.controller, 405419896)
        self.assertEqual(response.system_date, datetime.date(2022, 8, 23))
        self.assertEqual(response.system_time, datetime.time(9, 49, 39))
        self.assertEqual(response.door_1_open, False)
        self.assertEqual(response.door_2_open, True)
        self.assertEqual(response.door_3_open, False)
        self.assertEqual(response.door_4_open, False)
        self.assertEqual(response.door_1_button, False)
        self.assertEqual(response.door_2_button, False)
        self.assertEqual(response.door_3_button, False)
        self.assertEqual(response.door_4_button, True)
        self.assertEqual(response.relays, 7)
        self.assertEqual(response.inputs, 9)
        self.assertEqual(response.system_error, 3)
        self.assertEqual(response.special_info, 39)
        self.assertEqual(response.event_index, 0)
        self.assertEqual(response.event_type, None)
        self.assertEqual(response.event_access_granted, None)
        self.assertEqual(response.event_door, None)
        self.assertEqual(response.event_direction, None)
        self.assertEqual(response.event_card, None)
        self.assertEqual(response.event_timestamp, None)
        self.assertEqual(response.event_reason, None)
        self.assertEqual(response.sequence_no, 0)


if __name__ == '__main__':
    unittest.main()
