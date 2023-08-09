DIST ?= development
CMD   = cd examples/cli && python3 main.py 

.DEFAULT_GOAL := build

all: test      \
     benchmark \
     coverage

clean:

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

publish: release

debug: build
	$(CMD) --debug --bind 192.168.1.100 --broadcast 192.168.1.255:60000 --listen 192.168.1.100:60001 get-controller

usage: build
	$(CMD)

get-all-controllers: build
	$(CMD) --debug --bind 192.168.1.100 --broadcast 192.168.1.255 --listen 192.168.1.100:60001 get-all-controllers

get-controller: build
	$(CMD) --debug --bind 192.168.1.100 --broadcast 192.168.1.255 --listen 192.168.1.100:60001 get-controller

listen: python
	$(CMD) --debug --bind 192.168.1.100 --broadcast 192.168.1.255:60000 --listen 192.168.1.100:60001 listen
