.PHONY: specs features test clean install build push release

specs:
	py.test -rwx -s specs/

features:
	cd features/ && \
	behave

clean:
	rm -rf dist/
	rm -rf build/

install:
	pip install -r requirements.pip

build:
	python setup.py sdist bdist_wheel egg_info

push:
	twine upload dist/*

release: clean install build push

test: specs features
