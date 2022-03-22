test:  ## Run tests
	python -m pytest -ra

deps:  ## Install dependencies
	pip install --upgrade pip
	pip install -r requirements.txt

testdeps:
	pip install pytest

build:
	make deps
	make testdeps
	make test