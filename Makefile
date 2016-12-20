.PHONY: specs features test

specs:
	py.test -rwx -s specs/

features:
	cd features/ && \
	behave

test: specs features
