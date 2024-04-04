'''
UDP unit tests.

Tests the internal conversion functions.
'''

import unittest
from uhppoted.udp import timeout_to_seconds

class TestUDP(unittest.TestCase):

    def test_timeout_to_seconds(self):
        '''
        Tests a the conversion of valid and invalid timeout values.
        '''
        tests = [
           (1,1),
           (0.05,0.05),
           (30,30),
           (0, 2.5),
           (60, 2.5),
           ('12.5',12.5),
           (None, 2.5),
           ('qwerty', 2.5),
           ('5s',2.5),
        ]

        for test in tests:
            self.assertEqual(timeout_to_seconds(test[0]), test[1])

if __name__ == '__main__':
    unittest.main()
