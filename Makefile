UIFILE = Qacam_UI
PYFILE = Qacam

all:
	pyuic4 $(UIFILE).ui -x -o $(UIFILE).py

test:
	python $(PYFILE).py
