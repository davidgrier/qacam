RUNFILE := Qacam.py
UIFILE := $(wildcard *.ui)
PYFILE := $(UIFILE:.ui=.py)
SUBDIRS := $(wildcard Q*/.)
MAKE = gmake
PYTHON = python
PYUIC = pyuic5

.PHONY: all test $(SUBDIRS)

all: $(PYFILE) $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@

test: $(PYFILE)
	$(PYTHON) $(RUNFILE)

%.py: %.ui
	$(PYUIC) $< -x -o $@
