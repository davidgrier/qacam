UIFILE = Qacam_UI
PYFILE = Qacam

all:
	pyuic5 $(UIFILE).ui -x -o $(UIFILE).py

test:
	python $(PYFILE).py
