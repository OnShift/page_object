.PHONY: specs features test release

specs:
	py.test -rwx -s specs/

features:
	cd features/ && \
	behave

test: specs features

release:
	pip install -r requirements.pip && \
	python setup.py sdist bdist_wheel egg_info && \
  twine upload dist/*
