# CHANGELOG

## Unreleased

### Added
1. `set-door-passcodes` function to set supervisor passcodes for a door.

### Updated
1. Reworked `get-status` response decoding to set event fields to `None` if the response
   does not contain an event.
2. Fixed bug decoding IPv4 address in `get-controller` response.
3. Fixed typo decoding MAC address in `get-controller` response.


## [0.8.6](https://github.com/uhppoted/uhppoted-python/releases/tag/v0.8.6) - 2023-08-30

### Added
1. Initial release