# TODO

- [x] Fix examples so that they run locally
- [x] Added `listen` to README and event-listenener examples (cf. https://github.com/uhppoted/uhppoted-python/issues/6)
- [x] UDP send (cf. https://github.com/uhppoted/uhppoted-app-home-assistant/issues/3)
- [ ] Configurable call timeouts (cf. https://github.com/uhppoted/uhppoted-python/issues/5)
      - [x] udp.send timeout
      - [x] Handle timeout=None
      - [x] CHANGELOG
      - [x] Add to all functions
      - [x] Add to all example CLI commands
      - [ ] integration tests
            - https://stackoverflow.com/questions/34743448/how-to-specify-test-timeout-for-python-unittest
            - [ ] get_all_controllers
            - [x] get_controller
            - [ ] set_ip
            - [ ] get_time
            - [ ] set_time
            - [ ] get_status
            - [ ] get_listener
            - [ ] set_listener
            - [ ] get_door_control
            - [ ] set_door_control
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
            - [ ] set_time_profiole
            - [ ] delete_all_time_profiles
            - [ ] add_task
            - [ ] refresh_tasklist
            - [ ] clear_tasklist
            - [ ] set_pc_control
            - [ ] set_interlock
            - [ ] activate_keypads
            - [ ] set_door_passcodes
            - [ ] restore_default_parameters

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

