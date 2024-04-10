DIST ?= development
CMD   = cd examples/cli && python3 main.py --debug --bind 192.168.1.100 --broadcast 192.168.1.255 --listen 192.168.1.100:60001

.DEFAULT_GOAL := debug
.PHONY: update
.PHONY: update-release

clean:

update:

update-release:

format: 
	yapf -ri src
	# yapf -ri tests
	# yapf -ri examples

build: format
	python3 -m compileall .

test: build
	python3 -m unittest tests/uhppoted/*.py 

integration-tests: build
	python3 -m unittest integration-tests/uhppoted/*.py 

vet: 

lint: 

build-all: test vet lint

release: build-all integration-tests
	rm -rf dist/*
	python3 -m build
	python3 -m twine check dist/* 

publish: release
	echo "Releasing version $(VERSION)"
	gh release create "$(VERSION)" dist/*.tar.gz --draft --prerelease --title "$(VERSION)-beta" --notes-file release-notes.md
	python3 -m twine upload --repository testpypi -u __token__ --skip-existing --verbose dist/*
	python3 -m twine upload --repository pypi     -u __token__ --skip-existing --verbose dist/*

debug: build
	python3 -m unittest integration-tests/uhppoted/udp_timeout.py 

usage: build
	$(CMD)

get-all-controllers: build
	export UHPPOTED_ENV=DEV && $(CMD) get-all-controllers

get-controller: build
	export UHPPOTED_ENV=DEV && $(CMD) get-controller

set-address: build
	export UHPPOTED_ENV=DEV && $(CMD) set-address

get-status: build
	export UHPPOTED_ENV=DEV && $(CMD) get-status

get-time: build
	export UHPPOTED_ENV=DEV && $(CMD) get-time

set-time: build
	export UHPPOTED_ENV=DEV && $(CMD) set-time

get-listener: build
	export UHPPOTED_ENV=DEV && $(CMD) get-listener

set-listener: build
	export UHPPOTED_ENV=DEV && $(CMD) set-listener

get-door-control: build
	export UHPPOTED_ENV=DEV && $(CMD) get-door-control

set-door-control: build
	export UHPPOTED_ENV=DEV && $(CMD) set-door-control

open-door: build
	export UHPPOTED_ENV=DEV && $(CMD) open-door

get-cards: build
	export UHPPOTED_ENV=DEV && $(CMD) get-cards

get-card: build
	export UHPPOTED_ENV=DEV && $(CMD) get-card

get-card-by-index: build
	export UHPPOTED_ENV=DEV && $(CMD) get-card-by-index

put-card: build
	export UHPPOTED_ENV=DEV && $(CMD) put-card

delete-card: build
	export UHPPOTED_ENV=DEV && $(CMD) delete-card

delete-cards: build
	export UHPPOTED_ENV=DEV && $(CMD) delete-cards

get-event-index: build
	export UHPPOTED_ENV=DEV && $(CMD) get-event-index

set-event-index: build
	export UHPPOTED_ENV=DEV && $(CMD) set-event-index

get-event: build
	export UHPPOTED_ENV=DEV && $(CMD) get-event

record-special-events: build
	export UHPPOTED_ENV=DEV && $(CMD) record-special-events

get-time-profile: build
	export UHPPOTED_ENV=DEV && $(CMD) get-time-profile

set-time-profile: build
	export UHPPOTED_ENV=DEV && $(CMD) set-time-profile

clear-time-profiles: build
	export UHPPOTED_ENV=DEV && $(CMD) clear-time-profiles

add-task: build
	export UHPPOTED_ENV=DEV && $(CMD) add-task

refresh-tasklist: build
	export UHPPOTED_ENV=DEV && $(CMD) refresh-tasklist

clear-tasklist: build
	export UHPPOTED_ENV=DEV && $(CMD) clear-tasklist

set-pc-control: build
	export UHPPOTED_ENV=DEV && $(CMD) set-pc-control

set-interlock: build
	export UHPPOTED_ENV=DEV && $(CMD) set-interlock

activate-keypads: build
	export UHPPOTED_ENV=DEV && $(CMD) activate-keypads

set-door-passcodes: build
	export UHPPOTED_ENV=DEV && $(CMD) set-door-passcodes

restore-default-parameters: build
	export UHPPOTED_ENV=DEV && $(CMD) restore-default-parameters

listen: build
	export UHPPOTED_ENV=DEV && $(CMD) listen

all: build
	# export UHPPOTED_ENV=DEV && $(CMD) all
	export UHPPOTED_ENV=DEV && $(CMD) all --destination 192.168.1.100:60000 --timeout 0.5

event-listener: build
	export UHPPOTED_ENV=DEV    && \
	cd examples/event-listener && \
	python3 main.py --debug --bind 192.168.1.100 --broadcast 192.168.1.255 --listen 192.168.1.100:60001

	
