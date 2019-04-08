RUNFILE := Qacam.py
UIFILE := $(wildcard *.ui)
PYFILE := $(UIFILE:.ui=.py)
SUBDIRS := $(wildcard Q*/.)
MAKE = make
PYTHON = python
PYUIC = pyuic5

.PHONY: all test $(SUBDIRS)

all: $(PYFILE) $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@

test: $(PYFILE)
	$(PYTHON) $(RUNFILE)

clean:
	-rm $(PYFILE)
	for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir clean; \
	done


%.py: %.ui
	$(PYUIC) $< -x -o $@
