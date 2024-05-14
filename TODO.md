# TODO

- [ ] TCP/IP protocol (cf. https://github.com/uhppoted/uhppote-core/issues/17)
      - [x] TCP implementation
      - [x] Update all functions:
           - [x] get_controller
           - [x] set_ip
           - [x] get_time
           - [x] set_time
           - [x] get_status
           - [x] get_listener
           - [x] set_listener
           - [x] get_door_control
           - [x] set_door_control
           - [x] open_door
           - [x] get_cards
           - [x] get_card
           - [x] get_card_by_index
           - [x] put_card
           - [x] delete_card
           - [x] delete_all_cards
           - [x] get_event
           - [x] get_event_index
           - [x] set_event_index
           - [x] record_special_events
           - [x] get_time_profile
           - [x] set_time_profile
           - [x] delete_all_time_profiles
           - [x] add_task
           - [x] refresh_tasklist
           - [x] clear_tasklist
           - [x] set_pc_control
           - [x] set_interlock
           - [x] activate_keypads
           - [x] set_door_passcodes
           - [x] restore_default_parameters
      
      - [ ] Integration tests
      - [ ] commonalise utility functions
            - [ ] resolve
            - [ ] dump
            - [ ] timeout_to_seconds
            - [ ] constants

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

