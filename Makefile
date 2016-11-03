.PHONY: specs
.PHONY: features

specs:
	py.test -rwx -s specs/

features:
	cd features/ && \
	behave
