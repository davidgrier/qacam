# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qacam_UI.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Qacam(object):
    def setupUi(self, Qacam):
        Qacam.setObjectName(_fromUtf8("Qacam"))
        Qacam.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Qacam)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setMargin(4)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabScan = QtGui.QWidget()
        self.tabScan.setObjectName(_fromUtf8("tabScan"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tabScan)
        self.verticalLayout.setMargin(6)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scanner = QtGui.QWidget(self.tabScan)
        self.scanner.setMaximumSize(QtCore.QSize(16777215, 40))
        self.scanner.setObjectName(_fromUtf8("scanner"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.scanner)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.n1 = QtGui.QLCDNumber(self.scanner)
        self.n1.setMaximumSize(QtCore.QSize(16777215, 25))
        self.n1.setObjectName(_fromUtf8("n1"))
        self.horizontalLayout.addWidget(self.n1)
        spacerItem = QtGui.QSpacerItem(197, 19, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.scan = QtGui.QPushButton(self.scanner)
        self.scan.setObjectName(_fromUtf8("scan"))
        self.horizontalLayout.addWidget(self.scan)
        spacerItem1 = QtGui.QSpacerItem(196, 19, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.n2 = QtGui.QLCDNumber(self.scanner)
        self.n2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.n2.setObjectName(_fromUtf8("n2"))
        self.horizontalLayout.addWidget(self.n2)
        self.verticalLayout.addWidget(self.scanner)
        self.plot = PlotWidget(self.tabScan)
        self.plot.setObjectName(_fromUtf8("plot"))
        self.verticalLayout.addWidget(self.plot)
        self.tabWidget.addTab(self.tabScan, _fromUtf8(""))
        self.tabAmplitude = QtGui.QWidget()
        self.tabAmplitude.setObjectName(_fromUtf8("tabAmplitude"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabAmplitude)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.plotAmplitude = PlotWidget(self.tabAmplitude)
        self.plotAmplitude.setObjectName(_fromUtf8("plotAmplitude"))
        self.verticalLayout_2.addWidget(self.plotAmplitude)
        self.tabWidget.addTab(self.tabAmplitude, _fromUtf8(""))
        self.tabPhase = QtGui.QWidget()
        self.tabPhase.setObjectName(_fromUtf8("tabPhase"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabPhase)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.plotPhase = PlotWidget(self.tabPhase)
        self.plotPhase.setObjectName(_fromUtf8("plotPhase"))
        self.verticalLayout_3.addWidget(self.plotPhase)
        self.tabWidget.addTab(self.tabPhase, _fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.controlWidget = QtGui.QWidget(self.centralwidget)
        self.controlWidget.setMinimumSize(QtCore.QSize(250, 0))
        self.controlWidget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.controlWidget.setObjectName(_fromUtf8("controlWidget"))
        self.layoutControls = QtGui.QVBoxLayout(self.controlWidget)
        self.layoutControls.setMargin(4)
        self.layoutControls.setSpacing(2)
        self.layoutControls.setObjectName(_fromUtf8("layoutControls"))
        self.labelPolargraph = QtGui.QLabel(self.controlWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelPolargraph.setFont(font)
        self.labelPolargraph.setObjectName(_fromUtf8("labelPolargraph"))
        self.layoutControls.addWidget(self.labelPolargraph)
        self.polargraph = QPolargraphSettings(self.controlWidget)
        self.polargraph.setObjectName(_fromUtf8("polargraph"))
        self.layoutControls.addWidget(self.polargraph)
        self.labelLockin = QtGui.QLabel(self.controlWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelLockin.setFont(font)
        self.labelLockin.setObjectName(_fromUtf8("labelLockin"))
        self.layoutControls.addWidget(self.labelLockin)
        self.lockin = QSR830Settings(self.controlWidget)
        self.lockin.setMinimumSize(QtCore.QSize(100, 0))
        self.lockin.setObjectName(_fromUtf8("lockin"))
        self.layoutControls.addWidget(self.lockin)
        self.horizontalLayout_2.addWidget(self.controlWidget)
        Qacam.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Qacam)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        Qacam.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Qacam)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Qacam.setStatusBar(self.statusbar)
        self.actionSave_Settings = QtGui.QAction(Qacam)
        self.actionSave_Settings.setObjectName(_fromUtf8("actionSave_Settings"))
        self.actionSave_Hologram = QtGui.QAction(Qacam)
        self.actionSave_Hologram.setAutoRepeat(False)
        self.actionSave_Hologram.setObjectName(_fromUtf8("actionSave_Hologram"))
        self.action_Quit = QtGui.QAction(Qacam)
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
        self.menuFile.addAction(self.actionSave_Settings)
        self.menuFile.addAction(self.actionSave_Hologram)
        self.menuFile.addAction(self.action_Quit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Qacam)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.action_Quit, QtCore.SIGNAL(_fromUtf8("triggered()")), Qacam.close)
        QtCore.QMetaObject.connectSlotsByName(Qacam)

    def retranslateUi(self, Qacam):
        Qacam.setWindowTitle(_translate("Qacam", "Scanning Acoustic Camera", None))
        self.scan.setText(_translate("Qacam", "Scan", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabScan), _translate("Qacam", "Scanner", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAmplitude), _translate("Qacam", "Amplitude", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPhase), _translate("Qacam", "Phase", None))
        self.labelPolargraph.setText(_translate("Qacam", "Polargraph", None))
        self.labelLockin.setText(_translate("Qacam", "Lockin Amplifier", None))
        self.menuFile.setTitle(_translate("Qacam", "File", None))
        self.actionSave_Settings.setText(_translate("Qacam", "Save Settings", None))
        self.actionSave_Settings.setStatusTip(_translate("Qacam", "Save Instrument Settings", None))
        self.actionSave_Settings.setShortcut(_translate("Qacam", "Meta+T", None))
        self.actionSave_Hologram.setText(_translate("Qacam", "Save Hologram ...", None))
        self.actionSave_Hologram.setStatusTip(_translate("Qacam", "Save Hologram", None))
        self.actionSave_Hologram.setShortcut(_translate("Qacam", "Meta+S", None))
        self.action_Quit.setText(_translate("Qacam", "&Quit", None))

from QPolargraph import QPolargraphSettings
from QSR830 import QSR830Settings
from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Qacam = QtGui.QMainWindow()
    ui = Ui_Qacam()
    ui.setupUi(Qacam)
    Qacam.show()
    sys.exit(app.exec_())

