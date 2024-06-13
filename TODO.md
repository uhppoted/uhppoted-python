# TODO

- [x] TCP/IP protocol (cf. https://github.com/uhppoted/uhppote-core/issues/17)
      - [x] TCP implementation
      - [x] Update all functions:
      - [x] Integration tests
      - [x] commonalise utility functions
      - [x] Update UDP tests to use setUpClass and tearDownClass
      - [x] Documentation
      - [x] CHANGELOG
      - [x] README
      - [ ] Rework with disambiguated controller arg:
            - [x] get_controller
            - [x] set_ip
            - [ ] get_time
            - [ ] set_time
            - [ ] get_listener
            - [ ] set_listener
            - [ ] get_door_control
            - [ ] set_door_control
            - [ ] get_status
            - [ ] open_door
            - [ ] get_cards
            - [ ] get_card
            - [ ] get_card_by_index
            - [ ] put_card
            - [ ] delete_card
            - [ ] delete_all_cards
            - [ ] get_event
            - [ ] get_event_index
            - [ ] set_event_index
            - [ ] record_special_events
            - [ ] get_time_profile
            - [ ] set_time_profile
            - [ ] clear_time_profiles
            - [ ] add_task
            - [ ] refresh_tasklist
            - [ ] clear_tasklist
            - [ ] set_pc_control
            - [ ] set_interlock
            - [ ] activate_keypads
            - [ ] set_door_passcodes
            - [ ] restore_default_parameters
            - [ ] listen

def onEvent(event):
    if event != None:
        pprint.pprint(event.__dict__, indent=2, width=1)


- [ ] Use site-specific configuration to run examples locally
      - https://docs.python.org/3/library/site.html

- [x] Fix examples so that they run locally
- [x] Added `listen` to README and event-listenener examples (cf. https://github.com/uhppoted/uhppoted-python/issues/6)
- [x] UDP send (cf. https://github.com/uhppoted/uhppoted-app-home-assistant/issues/3)
- [x] Configurable call timeouts (cf. https://github.com/uhppoted/uhppoted-python/issues/5)

## TODO

1. `argparse` args for examples
   - https://docs.python.org/3/library/argparse.html#parents

2. (?) Automatically set-listener address
   - https://stackoverflow.com/questions/5281409/get-destination-address-of-a-received-udp-packet
   - https://stackoverflow.com/questions/39059418/python-sockets-how-can-i-get-the-ip-address-of-a-socket-after-i-bind-it-to-an

3. Unit/integration tests
      - https://hypothesis.readthedocs.io/en/latest/index.html
      - https://docs.python.org/3/library/doctest.html#module-doctest

4. Publish from github

