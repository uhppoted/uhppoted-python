DIST ?= development
CMD   = cd examples/cli && python3 main.py --debug --bind 192.168.1.100 --broadcast 192.168.1.255 --listen 192.168.1.100:60001

.DEFAULT_GOAL := build
.PHONY: update
.PHONY: update-release

clean:

update:

update-release:

format: 
	yapf -ri src
#	yapf -ri test
	yapf -ri examples

build: format

test: build

vet: 

lint: 

build-all: test vet lint

release: build-all 
	rm -rf dist/*
	python3 -m build
	python3 -m twine check dist/* 

publish: release
	echo "Releasing version $(VERSION)"
	gh release create "$(VERSION)" dist/*.tar.gz --draft --prerelease --title "$(VERSION)-beta" --notes-file release-notes.md
	python3 -m twine upload --repository testpypi -u __token__ --skip-existing dist/*
#	python3 -m twine upload --repository pypi     -u __token__ --skip-existing dist/*

debug: build
	$(CMD) --debug --bind 192.168.1.100 --broadcast 192.168.1.255:60000 --listen 192.168.1.100:60001 get-controller

usage: build
	$(CMD)

get-all-controllers: build
	$(CMD) get-all-controllers

get-controller: build
	$(CMD) get-controller

set-address: build
	$(CMD) set-address

get-status: build
	$(CMD) get-status

get-time: build
	$(CMD) get-time

set-time: build
	$(CMD) set-time

get-listener: build
	$(CMD) get-listener

set-listener: build
	$(CMD) set-listener

get-door-control: build
	$(CMD) get-door-control

set-door-control: build
	$(CMD) set-door-control

open-door: build
	$(CMD) open-door

get-cards: build
	$(CMD) get-cards

get-card: build
	$(CMD) get-card

get-card-by-index: build
	$(CMD) get-card-by-index

put-card: build
	$(CMD) put-card

delete-card: build
	$(CMD) delete-card

delete-cards: build
	$(CMD) delete-cards

get-event-index: build
	$(CMD) get-event-index

set-event-index: build
	$(CMD) set-event-index

get-event: build
	$(CMD) get-event

record-special-events: build
	$(CMD) record-special-events

get-time-profile: build
	$(CMD) get-time-profile

set-time-profile: build
	$(CMD) set-time-profile

clear-time-profiles: build
	$(CMD) clear-time-profiles

add-task: build
	$(CMD) add-task

refresh-tasklist: build
	$(CMD) refresh-tasklist

clear-tasklist: build
	$(CMD) clear-tasklist

set-pc-control: build
	$(CMD) set-pc-control

set-interlock: build
	$(CMD) set-interlock

activate-keypads: build
	$(CMD) activate-keypads

all: build
	$(CMD) all

listen: build
	$(CMD) listen
