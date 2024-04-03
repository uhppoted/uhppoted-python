# CHANGELOG

## Unreleased

### Added
1. Added support for destination IPv4 addresses.
2. Added support for per-call operation timeouts.


## [0.8.8](https://github.com/uhppoted/uhppoted-python/releases/tag/v0.8.8) - 2024-03-26

### Added
1. `restore-default-parameters` function to reset a controller to the manufacturer default configuration.


## [0.8.7.1](https://github.com/uhppoted/uhppoted-python/releases/tag/v0.8.7.1) - 2024-02-22

### Updated
1. Fixed listen event decoding (cf. https://github.com/uhppoted/uhppoted-python/issues/3)


## [0.8.7](https://github.com/uhppoted/uhppoted-python/releases/tag/v0.8.7) - 2023-12-01

### Added
1. `set-door-passcodes` function to set supervisor passcodes for a door.

### Updated
1. Reworked `get-status` response decoding to set event fields to `None` if the response
   does not contain an event.
2. Fixed bug decoding IPv4 address in `get-controller` response.
3. Fixed typo decoding MAC address in `get-controller` response.
4. Reworked date/time decoding to unpack invalid date/times as `None`.


## [0.8.6](https://github.com/uhppoted/uhppoted-python/releases/tag/v0.8.6) - 2023-08-30

### Added
1. Initial release
