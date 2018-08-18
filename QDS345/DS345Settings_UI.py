# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DS345Settings_UI.ui'
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

class Ui_DS345Settings(object):
    def setupUi(self, DS345Settings):
        DS345Settings.setObjectName(_fromUtf8("DS345Settings"))
        DS345Settings.resize(254, 105)
        self.formLayout = QtGui.QFormLayout(DS345Settings)
        self.formLayout.setContentsMargins(0, 2, 0, 2)
        self.formLayout.setSpacing(2)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.labelFrequency = QtGui.QLabel(DS345Settings)
        self.labelFrequency.setObjectName(_fromUtf8("labelFrequency"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelFrequency)
        self.frequency = QtGui.QDoubleSpinBox(DS345Settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frequency.sizePolicy().hasHeightForWidth())
        self.frequency.setSizePolicy(sizePolicy)
        self.frequency.setDecimals(6)
        self.frequency.setMinimum(1e-05)
        self.frequency.setMaximum(100000.0)
        self.frequency.setProperty("value", 1.0)
        self.frequency.setObjectName(_fromUtf8("frequency"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.frequency)
        self.labelAmplitude = QtGui.QLabel(DS345Settings)
        self.labelAmplitude.setObjectName(_fromUtf8("labelAmplitude"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelAmplitude)
        self.amplitude = QtGui.QDoubleSpinBox(DS345Settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.amplitude.sizePolicy().hasHeightForWidth())
        self.amplitude.setSizePolicy(sizePolicy)
        self.amplitude.setMinimum(0.01)
        self.amplitude.setMaximum(5.0)
        self.amplitude.setSingleStep(0.1)
        self.amplitude.setProperty("value", 1.0)
        self.amplitude.setObjectName(_fromUtf8("amplitude"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.amplitude)
        self.labelOffset = QtGui.QLabel(DS345Settings)
        self.labelOffset.setObjectName(_fromUtf8("labelOffset"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelOffset)
        self.offset = QtGui.QDoubleSpinBox(DS345Settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.offset.sizePolicy().hasHeightForWidth())
        self.offset.setSizePolicy(sizePolicy)
        self.offset.setMinimum(-5.0)
        self.offset.setMaximum(5.0)
        self.offset.setSingleStep(0.1)
        self.offset.setObjectName(_fromUtf8("offset"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.offset)
        self.labelWaveform = QtGui.QLabel(DS345Settings)
        self.labelWaveform.setObjectName(_fromUtf8("labelWaveform"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.labelWaveform)
        self.waveform = QtGui.QComboBox(DS345Settings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.waveform.sizePolicy().hasHeightForWidth())
        self.waveform.setSizePolicy(sizePolicy)
        self.waveform.setObjectName(_fromUtf8("waveform"))
        self.waveform.addItem(_fromUtf8(""))
        self.waveform.addItem(_fromUtf8(""))
        self.waveform.addItem(_fromUtf8(""))
        self.waveform.addItem(_fromUtf8(""))
        self.waveform.addItem(_fromUtf8(""))
        self.waveform.addItem(_fromUtf8(""))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.waveform)

        self.retranslateUi(DS345Settings)
        QtCore.QMetaObject.connectSlotsByName(DS345Settings)

    def retranslateUi(self, DS345Settings):
        DS345Settings.setWindowTitle(_translate("DS345Settings", "DS345", None))
        DS345Settings.setStatusTip(_translate("DS345Settings", "DS345: Controls", None))
        self.labelFrequency.setText(_translate("DS345Settings", "Frequency", None))
        self.frequency.setStatusTip(_translate("DS345Settings", "DS345: Frequency [Hz]", None))
        self.frequency.setSuffix(_translate("DS345Settings", " Hz", None))
        self.labelAmplitude.setText(_translate("DS345Settings", "Amplitude", None))
        self.amplitude.setStatusTip(_translate("DS345Settings", "DS345: Amplitude", None))
        self.amplitude.setSuffix(_translate("DS345Settings", " Vpp", None))
        self.labelOffset.setText(_translate("DS345Settings", "Offset", None))
        self.offset.setStatusTip(_translate("DS345Settings", "DS345: Offset", None))
        self.offset.setSuffix(_translate("DS345Settings", " V", None))
        self.labelWaveform.setText(_translate("DS345Settings", "Waveform", None))
        self.waveform.setStatusTip(_translate("DS345Settings", "DS345: Waveform", None))
        self.waveform.setItemText(0, _translate("DS345Settings", "sine", None))
        self.waveform.setItemText(1, _translate("DS345Settings", "square", None))
        self.waveform.setItemText(2, _translate("DS345Settings", "triangle", None))
        self.waveform.setItemText(3, _translate("DS345Settings", "ramp", None))
        self.waveform.setItemText(4, _translate("DS345Settings", "noise", None))
        self.waveform.setItemText(5, _translate("DS345Settings", "arbitrary", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DS345Settings = QtGui.QWidget()
    ui = Ui_DS345Settings()
    ui.setupUi(DS345Settings)
    DS345Settings.show()
    sys.exit(app.exec_())

