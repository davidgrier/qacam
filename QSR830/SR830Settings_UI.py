# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SR830Settings_UI.ui'
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

class Ui_SR830Settings(object):
    def setupUi(self, SR830Settings):
        SR830Settings.setObjectName(_fromUtf8("SR830Settings"))
        SR830Settings.resize(370, 575)
        self.verticalLayout_4 = QtGui.QVBoxLayout(SR830Settings)
        self.verticalLayout_4.setMargin(4)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.frameInputConfiguration = QtGui.QFrame(SR830Settings)
        self.frameInputConfiguration.setFrameShape(QtGui.QFrame.Panel)
        self.frameInputConfiguration.setFrameShadow(QtGui.QFrame.Raised)
        self.frameInputConfiguration.setLineWidth(2)
        self.frameInputConfiguration.setObjectName(_fromUtf8("frameInputConfiguration"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frameInputConfiguration)
        self.verticalLayout_2.setMargin(4)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelInputConfiguration = QtGui.QLabel(self.frameInputConfiguration)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelInputConfiguration.setFont(font)
        self.labelInputConfiguration.setObjectName(_fromUtf8("labelInputConfiguration"))
        self.verticalLayout_2.addWidget(self.labelInputConfiguration)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setVerticalSpacing(2)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.labelInput = QtGui.QLabel(self.frameInputConfiguration)
        self.labelInput.setObjectName(_fromUtf8("labelInput"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelInput)
        self.input = QtGui.QComboBox(self.frameInputConfiguration)
        self.input.setObjectName(_fromUtf8("input"))
        self.input.addItem(_fromUtf8(""))
        self.input.addItem(_fromUtf8(""))
        self.input.addItem(_fromUtf8(""))
        self.input.addItem(_fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.input)
        self.labelGrounding = QtGui.QLabel(self.frameInputConfiguration)
        self.labelGrounding.setObjectName(_fromUtf8("labelGrounding"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelGrounding)
        self.grounding = QtGui.QComboBox(self.frameInputConfiguration)
        self.grounding.setObjectName(_fromUtf8("grounding"))
        self.grounding.addItem(_fromUtf8(""))
        self.grounding.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.grounding)
        self.labelCoupling = QtGui.QLabel(self.frameInputConfiguration)
        self.labelCoupling.setObjectName(_fromUtf8("labelCoupling"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelCoupling)
        self.coupling = QtGui.QComboBox(self.frameInputConfiguration)
        self.coupling.setObjectName(_fromUtf8("coupling"))
        self.coupling.addItem(_fromUtf8(""))
        self.coupling.addItem(_fromUtf8(""))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.coupling)
        self.labelTimeConstant = QtGui.QLabel(self.frameInputConfiguration)
        self.labelTimeConstant.setObjectName(_fromUtf8("labelTimeConstant"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.labelTimeConstant)
        self.timeConstant = QtGui.QComboBox(self.frameInputConfiguration)
        self.timeConstant.setObjectName(_fromUtf8("timeConstant"))
        self.timeConstant.addItem(_fromUtf8(""))
        self.timeConstant.addItem(_fromUtf8(""))
        self.timeConstant.addItem(_fromUtf8(""))
        self.timeConstant.addItem(_fromUtf8(""))
        self.timeConstant.addItem(_fromUtf8(""))
        self.timeConstant.addItem(_fromUtf8(""))
        self.timeConstant.addItem(_fromUtf8(""))
        self.timeConstant.addItem(_fromUtf8(""))
        self.timeConstant.addItem(_fromUtf8(""))
        self.timeConstant.addItem(_fromUtf8(""))
        self.timeConstant.addItem(_fromUtf8(""))
        self.timeConstant.addItem(_fromUtf8(""))
        self.timeConstant.addItem(_fromUtf8(""))
        self.timeConstant.addItem(_fromUtf8(""))
        self.timeConstant.addItem(_fromUtf8(""))
        self.timeConstant.addItem(_fromUtf8(""))
        self.timeConstant.addItem(_fromUtf8(""))
        self.timeConstant.addItem(_fromUtf8(""))
        self.timeConstant.addItem(_fromUtf8(""))
        self.timeConstant.addItem(_fromUtf8(""))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.timeConstant)
        self.labelSlope = QtGui.QLabel(self.frameInputConfiguration)
        self.labelSlope.setObjectName(_fromUtf8("labelSlope"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.labelSlope)
        self.slope = QtGui.QComboBox(self.frameInputConfiguration)
        self.slope.setObjectName(_fromUtf8("slope"))
        self.slope.addItem(_fromUtf8(""))
        self.slope.addItem(_fromUtf8(""))
        self.slope.addItem(_fromUtf8(""))
        self.slope.addItem(_fromUtf8(""))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.slope)
        self.labelSynchronous = QtGui.QLabel(self.frameInputConfiguration)
        self.labelSynchronous.setObjectName(_fromUtf8("labelSynchronous"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.labelSynchronous)
        self.synchronous = QtGui.QComboBox(self.frameInputConfiguration)
        self.synchronous.setObjectName(_fromUtf8("synchronous"))
        self.synchronous.addItem(_fromUtf8(""))
        self.synchronous.addItem(_fromUtf8(""))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.synchronous)
        self.labelSensitivity = QtGui.QLabel(self.frameInputConfiguration)
        self.labelSensitivity.setObjectName(_fromUtf8("labelSensitivity"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.labelSensitivity)
        self.sensitivity = QtGui.QComboBox(self.frameInputConfiguration)
        self.sensitivity.setObjectName(_fromUtf8("sensitivity"))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.sensitivity.addItem(_fromUtf8(""))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.sensitivity)
        self.labelReserve = QtGui.QLabel(self.frameInputConfiguration)
        self.labelReserve.setObjectName(_fromUtf8("labelReserve"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.labelReserve)
        self.reserve = QtGui.QComboBox(self.frameInputConfiguration)
        self.reserve.setObjectName(_fromUtf8("reserve"))
        self.reserve.addItem(_fromUtf8(""))
        self.reserve.addItem(_fromUtf8(""))
        self.reserve.addItem(_fromUtf8(""))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.reserve)
        self.labelLineFilter = QtGui.QLabel(self.frameInputConfiguration)
        self.labelLineFilter.setObjectName(_fromUtf8("labelLineFilter"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.labelLineFilter)
        self.filter = QtGui.QComboBox(self.frameInputConfiguration)
        self.filter.setObjectName(_fromUtf8("filter"))
        self.filter.addItem(_fromUtf8(""))
        self.filter.addItem(_fromUtf8(""))
        self.filter.addItem(_fromUtf8(""))
        self.filter.addItem(_fromUtf8(""))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.filter)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout_4.addWidget(self.frameInputConfiguration)
        self.frameAuto = QtGui.QFrame(SR830Settings)
        self.frameAuto.setFrameShape(QtGui.QFrame.Panel)
        self.frameAuto.setFrameShadow(QtGui.QFrame.Raised)
        self.frameAuto.setLineWidth(2)
        self.frameAuto.setObjectName(_fromUtf8("frameAuto"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frameAuto)
        self.verticalLayout_3.setMargin(4)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(self.frameAuto)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.autoButtons = QtGui.QWidget(self.frameAuto)
        self.autoButtons.setObjectName(_fromUtf8("autoButtons"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.autoButtons)
        self.horizontalLayout.setMargin(4)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.autoGain = QtGui.QPushButton(self.autoButtons)
        self.autoGain.setObjectName(_fromUtf8("autoGain"))
        self.horizontalLayout.addWidget(self.autoGain)
        self.autoReserve = QtGui.QPushButton(self.autoButtons)
        self.autoReserve.setObjectName(_fromUtf8("autoReserve"))
        self.horizontalLayout.addWidget(self.autoReserve)
        self.autoPhase = QtGui.QPushButton(self.autoButtons)
        self.autoPhase.setObjectName(_fromUtf8("autoPhase"))
        self.horizontalLayout.addWidget(self.autoPhase)
        self.verticalLayout_3.addWidget(self.autoButtons)
        self.verticalLayout_4.addWidget(self.frameAuto)
        self.frameReference = QtGui.QFrame(SR830Settings)
        self.frameReference.setFrameShape(QtGui.QFrame.Panel)
        self.frameReference.setFrameShadow(QtGui.QFrame.Raised)
        self.frameReference.setLineWidth(2)
        self.frameReference.setObjectName(_fromUtf8("frameReference"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frameReference)
        self.verticalLayout.setMargin(4)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelReference = QtGui.QLabel(self.frameReference)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelReference.setFont(font)
        self.labelReference.setObjectName(_fromUtf8("labelReference"))
        self.verticalLayout.addWidget(self.labelReference)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setVerticalSpacing(2)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.labelSource = QtGui.QLabel(self.frameReference)
        self.labelSource.setObjectName(_fromUtf8("labelSource"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelSource)
        self.source = QtGui.QComboBox(self.frameReference)
        self.source.setObjectName(_fromUtf8("source"))
        self.source.addItem(_fromUtf8(""))
        self.source.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.source)
        self.labelFrequency = QtGui.QLabel(self.frameReference)
        self.labelFrequency.setObjectName(_fromUtf8("labelFrequency"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelFrequency)
        self.frequency = QtGui.QLineEdit(self.frameReference)
        self.frequency.setObjectName(_fromUtf8("frequency"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.frequency)
        self.labelAmplitude = QtGui.QLabel(self.frameReference)
        self.labelAmplitude.setObjectName(_fromUtf8("labelAmplitude"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelAmplitude)
        self.amplitude = QtGui.QLineEdit(self.frameReference)
        self.amplitude.setObjectName(_fromUtf8("amplitude"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.amplitude)
        self.labelTrigger = QtGui.QLabel(self.frameReference)
        self.labelTrigger.setObjectName(_fromUtf8("labelTrigger"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.labelTrigger)
        self.trigger = QtGui.QComboBox(self.frameReference)
        self.trigger.setObjectName(_fromUtf8("trigger"))
        self.trigger.addItem(_fromUtf8(""))
        self.trigger.addItem(_fromUtf8(""))
        self.trigger.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.trigger)
        self.labelPhase = QtGui.QLabel(self.frameReference)
        self.labelPhase.setObjectName(_fromUtf8("labelPhase"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.labelPhase)
        self.phase = QtGui.QLineEdit(self.frameReference)
        self.phase.setObjectName(_fromUtf8("phase"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.phase)
        self.labelHarmonic = QtGui.QLabel(self.frameReference)
        self.labelHarmonic.setObjectName(_fromUtf8("labelHarmonic"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.labelHarmonic)
        self.harmonic = QtGui.QSpinBox(self.frameReference)
        self.harmonic.setMinimum(1)
        self.harmonic.setMaximum(19999)
        self.harmonic.setObjectName(_fromUtf8("harmonic"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.harmonic)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.verticalLayout_4.addWidget(self.frameReference)
        self.frameInputConfiguration.raise_()
        self.frameReference.raise_()
        self.frameAuto.raise_()

        self.retranslateUi(SR830Settings)
        QtCore.QMetaObject.connectSlotsByName(SR830Settings)

    def retranslateUi(self, SR830Settings):
        SR830Settings.setWindowTitle(_translate("SR830Settings", "Form", None))
        self.frameInputConfiguration.setStatusTip(_translate("SR830Settings", "SR830: Input Configuration", None))
        self.labelInputConfiguration.setText(_translate("SR830Settings", "Input Configuration", None))
        self.labelInput.setText(_translate("SR830Settings", "Input", None))
        self.input.setItemText(0, _translate("SR830Settings", "A", None))
        self.input.setItemText(1, _translate("SR830Settings", "A-B", None))
        self.input.setItemText(2, _translate("SR830Settings", "I (1 MOhm)", None))
        self.input.setItemText(3, _translate("SR830Settings", "I (100 MOhm)", None))
        self.labelGrounding.setText(_translate("SR830Settings", "Grounding", None))
        self.grounding.setItemText(0, _translate("SR830Settings", "Shield Floating", None))
        self.grounding.setItemText(1, _translate("SR830Settings", "Shield Grounded", None))
        self.labelCoupling.setText(_translate("SR830Settings", "Coupling", None))
        self.coupling.setItemText(0, _translate("SR830Settings", "AC Coupling", None))
        self.coupling.setItemText(1, _translate("SR830Settings", "DC Coupling", None))
        self.labelTimeConstant.setText(_translate("SR830Settings", "Time Constant", None))
        self.timeConstant.setItemText(0, _translate("SR830Settings", "10 µs", None))
        self.timeConstant.setItemText(1, _translate("SR830Settings", "30 µs", None))
        self.timeConstant.setItemText(2, _translate("SR830Settings", "100 µs", None))
        self.timeConstant.setItemText(3, _translate("SR830Settings", "300 µs", None))
        self.timeConstant.setItemText(4, _translate("SR830Settings", "1 ms", None))
        self.timeConstant.setItemText(5, _translate("SR830Settings", "3 ms", None))
        self.timeConstant.setItemText(6, _translate("SR830Settings", "10 ms", None))
        self.timeConstant.setItemText(7, _translate("SR830Settings", "30 ms", None))
        self.timeConstant.setItemText(8, _translate("SR830Settings", "100 ms", None))
        self.timeConstant.setItemText(9, _translate("SR830Settings", "300 ms", None))
        self.timeConstant.setItemText(10, _translate("SR830Settings", "1 s", None))
        self.timeConstant.setItemText(11, _translate("SR830Settings", "3 s", None))
        self.timeConstant.setItemText(12, _translate("SR830Settings", "10 s", None))
        self.timeConstant.setItemText(13, _translate("SR830Settings", "30 s", None))
        self.timeConstant.setItemText(14, _translate("SR830Settings", "100 s", None))
        self.timeConstant.setItemText(15, _translate("SR830Settings", "300 s", None))
        self.timeConstant.setItemText(16, _translate("SR830Settings", "1 ks", None))
        self.timeConstant.setItemText(17, _translate("SR830Settings", "3 ks", None))
        self.timeConstant.setItemText(18, _translate("SR830Settings", "10 ks", None))
        self.timeConstant.setItemText(19, _translate("SR830Settings", "30 ks", None))
        self.labelSlope.setText(_translate("SR830Settings", "Slope", None))
        self.slope.setItemText(0, _translate("SR830Settings", "6 dB/oct", None))
        self.slope.setItemText(1, _translate("SR830Settings", "12 dB/oct", None))
        self.slope.setItemText(2, _translate("SR830Settings", "18 dB/oct", None))
        self.slope.setItemText(3, _translate("SR830Settings", "24 dB/oct", None))
        self.labelSynchronous.setText(_translate("SR830Settings", "Synchronous", None))
        self.synchronous.setItemText(0, _translate("SR830Settings", "Filter Off", None))
        self.synchronous.setItemText(1, _translate("SR830Settings", "Filter On", None))
        self.labelSensitivity.setText(_translate("SR830Settings", "Sensitivity", None))
        self.sensitivity.setItemText(0, _translate("SR830Settings", "2 nV/fA", None))
        self.sensitivity.setItemText(1, _translate("SR830Settings", "5 nV/fA", None))
        self.sensitivity.setItemText(2, _translate("SR830Settings", "10 nV/fA", None))
        self.sensitivity.setItemText(3, _translate("SR830Settings", "20 nV/fA", None))
        self.sensitivity.setItemText(4, _translate("SR830Settings", "50 nV/fA", None))
        self.sensitivity.setItemText(5, _translate("SR830Settings", "100 nV/fA", None))
        self.sensitivity.setItemText(6, _translate("SR830Settings", "200 nV/fA", None))
        self.sensitivity.setItemText(7, _translate("SR830Settings", "500 nV/fA", None))
        self.sensitivity.setItemText(8, _translate("SR830Settings", "1 µV/pA", None))
        self.sensitivity.setItemText(9, _translate("SR830Settings", "2 µV/pA", None))
        self.sensitivity.setItemText(10, _translate("SR830Settings", "5 µV/pA", None))
        self.sensitivity.setItemText(11, _translate("SR830Settings", "10 µV/pA", None))
        self.sensitivity.setItemText(12, _translate("SR830Settings", "20 µV/pA", None))
        self.sensitivity.setItemText(13, _translate("SR830Settings", "50 µV/pA", None))
        self.sensitivity.setItemText(14, _translate("SR830Settings", "100 µV/pA", None))
        self.sensitivity.setItemText(15, _translate("SR830Settings", "200 µV/pA", None))
        self.sensitivity.setItemText(16, _translate("SR830Settings", "500 µV/pA", None))
        self.sensitivity.setItemText(17, _translate("SR830Settings", "1 mV/nA", None))
        self.sensitivity.setItemText(18, _translate("SR830Settings", "2 mV/nA", None))
        self.sensitivity.setItemText(19, _translate("SR830Settings", "5 mV/nA", None))
        self.sensitivity.setItemText(20, _translate("SR830Settings", "10 mV/nA", None))
        self.sensitivity.setItemText(21, _translate("SR830Settings", "20 mV/nA", None))
        self.sensitivity.setItemText(22, _translate("SR830Settings", "50 mV/nA", None))
        self.sensitivity.setItemText(23, _translate("SR830Settings", "100 mV/nA", None))
        self.sensitivity.setItemText(24, _translate("SR830Settings", "200 mV/nA", None))
        self.sensitivity.setItemText(25, _translate("SR830Settings", "500 mV/nA", None))
        self.sensitivity.setItemText(26, _translate("SR830Settings", "1 V/µA", None))
        self.labelReserve.setText(_translate("SR830Settings", "Reserve", None))
        self.reserve.setItemText(0, _translate("SR830Settings", "High", None))
        self.reserve.setItemText(1, _translate("SR830Settings", "Normal", None))
        self.reserve.setItemText(2, _translate("SR830Settings", "Low Noise", None))
        self.labelLineFilter.setText(_translate("SR830Settings", "Line Filter", None))
        self.filter.setItemText(0, _translate("SR830Settings", "No Filter", None))
        self.filter.setItemText(1, _translate("SR830Settings", "Line Notch", None))
        self.filter.setItemText(2, _translate("SR830Settings", "2x Line Notch", None))
        self.filter.setItemText(3, _translate("SR830Settings", "Both", None))
        self.frameAuto.setStatusTip(_translate("SR830Settings", "SR830: Automatic Settings", None))
        self.label.setText(_translate("SR830Settings", "Auto", None))
        self.autoGain.setText(_translate("SR830Settings", "Gain", None))
        self.autoReserve.setText(_translate("SR830Settings", "Reserve", None))
        self.autoPhase.setText(_translate("SR830Settings", "Phase", None))
        self.frameReference.setStatusTip(_translate("SR830Settings", "SR830 Reference Signal", None))
        self.labelReference.setText(_translate("SR830Settings", "Reference", None))
        self.labelSource.setText(_translate("SR830Settings", "Source", None))
        self.source.setItemText(0, _translate("SR830Settings", "External", None))
        self.source.setItemText(1, _translate("SR830Settings", "Internal", None))
        self.labelFrequency.setText(_translate("SR830Settings", "Frequency", None))
        self.labelAmplitude.setText(_translate("SR830Settings", "Amplitude", None))
        self.labelTrigger.setText(_translate("SR830Settings", "Trigger", None))
        self.trigger.setItemText(0, _translate("SR830Settings", "Sine Zero Crossing", None))
        self.trigger.setItemText(1, _translate("SR830Settings", "TTL Rising Edge", None))
        self.trigger.setItemText(2, _translate("SR830Settings", "TTL Falling Edge", None))
        self.labelPhase.setText(_translate("SR830Settings", "Phase", None))
        self.labelHarmonic.setText(_translate("SR830Settings", "Harmonic", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SR830Settings = QtGui.QWidget()
    ui = Ui_SR830Settings()
    ui.setupUi(SR830Settings)
    SR830Settings.show()
    sys.exit(app.exec_())
