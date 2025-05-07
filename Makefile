# Makefile

install:
	pip install .

test:
	pytest

lint:
	black a2a_gateway_cli.py

agent:
	python demo_agent.py

build:
	python -m build

publish:
	twine upload dist/*
