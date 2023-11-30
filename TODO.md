# TODO

- [x] `set-door-passcodes` (cf. https://github.com/uhppoted/uhppoted/issues/40)
- [x] `GetStatus` response decode with no event (cf. https://github.com/uhppoted/uhppote-core/issues/18)
      - [x] `decode.get_status_response`
      - [x] unit test
      - [x] CHANGELOG
      - [x] README

- [ ] Fix unpack_datetime bug

```
Traceback (most recent call last):
  File "sensor.py", line 274, in async_update
    response = self.uhppote.get_time(controller)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "uhppote.py", line 111, in get_time
    return decode.get_time_response(reply)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "decode.py", line 107, in get_time_response
    unpack_datetime(packet, 8),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "decode.py", line 1159, in unpack_datetime
    return datetime.datetime.strptime(bcd, '%Y%m%d%H%M%S')
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "_strptime.py", line 568, in _strptime_datetime
    tt, fraction, gmtoff_fraction = _strptime(data_string, format)
                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "_strptime.py", line 349, in _strptime
    raise ValueError("time data %r does not match format %r" %
ValueError: time data '20000000000000' does not match format '%Y%m%d%H%M%S'
2023-11-29 11:37:29.754 ERROR (MainThread) [custom_components.uhppoted.sensor] error retrieving controller status


- [ ] Unit/integration tests
- [ ] Publish from github

