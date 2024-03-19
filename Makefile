SHELL := /bin/bash

build:
	docker build -t sprint-namer .

run: build
	docker run -d -p 5000:5000 sprint-namer
