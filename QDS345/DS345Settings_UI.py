# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DS345Settings_UI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DS345Settings(object):
    def setupUi(self, DS345Settings):
        DS345Settings.setObjectName("DS345Settings")
        DS345Settings.resize(442, 441)
        self.verticalLayout = QtWidgets.QVBoxLayout(DS345Settings)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupOutput = QtWidgets.QGroupBox(DS345Settings)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupOutput.setFont(font)
        self.groupOutput.setObjectName("groupOutput")
        self.gridLayout = QtWidgets.QGridLayout(self.groupOutput)
        self.gridLayout.setContentsMargins(4, 2, 4, 2)
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.labelFrequency = QtWidgets.QLabel(self.groupOutput)
        self.labelFrequency.setObjectName("labelFrequency")
        self.gridLayout.addWidget(self.labelFrequency, 0, 0, 1, 1)
        self.frequency = QtWidgets.QDoubleSpinBox(self.groupOutput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frequency.sizePolicy().hasHeightForWidth())
        self.frequency.setSizePolicy(sizePolicy)
        self.frequency.setDecimals(6)
        self.frequency.setMinimum(1e-05)
        self.frequency.setMaximum(100000.0)
        self.frequency.setProperty("value", 1.0)
        self.frequency.setObjectName("frequency")
        self.gridLayout.addWidget(self.frequency, 0, 1, 1, 1)
        self.labelAmplitude = QtWidgets.QLabel(self.groupOutput)
        self.labelAmplitude.setObjectName("labelAmplitude")
        self.gridLayout.addWidget(self.labelAmplitude, 1, 0, 1, 1)
        self.amplitude = QtWidgets.QDoubleSpinBox(self.groupOutput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.amplitude.sizePolicy().hasHeightForWidth())
        self.amplitude.setSizePolicy(sizePolicy)
        self.amplitude.setMinimum(0.0)
        self.amplitude.setMaximum(5.0)
        self.amplitude.setSingleStep(0.1)
        self.amplitude.setProperty("value", 1.0)
        self.amplitude.setObjectName("amplitude")
        self.gridLayout.addWidget(self.amplitude, 1, 1, 1, 1)
        self.labelOffset = QtWidgets.QLabel(self.groupOutput)
        self.labelOffset.setObjectName("labelOffset")
        self.gridLayout.addWidget(self.labelOffset, 2, 0, 1, 1)
        self.offset = QtWidgets.QDoubleSpinBox(self.groupOutput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.offset.sizePolicy().hasHeightForWidth())
        self.offset.setSizePolicy(sizePolicy)
        self.offset.setMinimum(-5.0)
        self.offset.setMaximum(5.0)
        self.offset.setSingleStep(0.1)
        self.offset.setObjectName("offset")
        self.gridLayout.addWidget(self.offset, 2, 1, 1, 1)
        self.labelWaveform = QtWidgets.QLabel(self.groupOutput)
        self.labelWaveform.setObjectName("labelWaveform")
        self.gridLayout.addWidget(self.labelWaveform, 3, 0, 1, 1)
        self.waveform = QtWidgets.QComboBox(self.groupOutput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.waveform.sizePolicy().hasHeightForWidth())
        self.waveform.setSizePolicy(sizePolicy)
        self.waveform.setObjectName("waveform")
        self.waveform.addItem("")
        self.waveform.addItem("")
        self.waveform.addItem("")
        self.waveform.addItem("")
        self.waveform.addItem("")
        self.waveform.addItem("")
        self.gridLayout.addWidget(self.waveform, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupOutput)
        self.labelFrequency.setBuddy(self.frequency)
        self.labelAmplitude.setBuddy(self.amplitude)
        self.labelOffset.setBuddy(self.offset)
        self.labelWaveform.setBuddy(self.waveform)

        self.retranslateUi(DS345Settings)
        QtCore.QMetaObject.connectSlotsByName(DS345Settings)

    def retranslateUi(self, DS345Settings):
        _translate = QtCore.QCoreApplication.translate
        DS345Settings.setWindowTitle(_translate("DS345Settings", "DS345"))
        DS345Settings.setStatusTip(_translate("DS345Settings", "DS345: Controls"))
        self.groupOutput.setTitle(_translate("DS345Settings", "Output Configuration"))
        self.labelFrequency.setText(_translate("DS345Settings", "Frequency"))
        self.frequency.setStatusTip(_translate("DS345Settings", "DS345: Frequency [Hz]"))
        self.frequency.setSuffix(_translate("DS345Settings", " Hz"))
        self.labelAmplitude.setText(_translate("DS345Settings", "Amplitude"))
        self.amplitude.setStatusTip(_translate("DS345Settings", "DS345: Amplitude"))
        self.amplitude.setSuffix(_translate("DS345Settings", " Vpp"))
        self.labelOffset.setText(_translate("DS345Settings", "Offset"))
        self.offset.setStatusTip(_translate("DS345Settings", "DS345: Offset"))
        self.offset.setSuffix(_translate("DS345Settings", " V"))
        self.labelWaveform.setText(_translate("DS345Settings", "Waveform"))
        self.waveform.setStatusTip(_translate("DS345Settings", "DS345: Waveform"))
        self.waveform.setItemText(0, _translate("DS345Settings", "sine"))
        self.waveform.setItemText(1, _translate("DS345Settings", "square"))
        self.waveform.setItemText(2, _translate("DS345Settings", "triangle"))
        self.waveform.setItemText(3, _translate("DS345Settings", "ramp"))
        self.waveform.setItemText(4, _translate("DS345Settings", "noise"))
        self.waveform.setItemText(5, _translate("DS345Settings", "arbitrary"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DS345Settings = QtWidgets.QWidget()
    ui = Ui_DS345Settings()
    ui.setupUi(DS345Settings)
    DS345Settings.show()
    sys.exit(app.exec_())

