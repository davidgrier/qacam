# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Polargraph_UI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Polargraph(object):
    def setupUi(self, Polargraph):
        Polargraph.setObjectName("Polargraph")
        Polargraph.resize(333, 205)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Polargraph)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frameSetup = QtWidgets.QFrame(Polargraph)
        self.frameSetup.setFrameShape(QtWidgets.QFrame.Panel)
        self.frameSetup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSetup.setLineWidth(2)
        self.frameSetup.setObjectName("frameSetup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frameSetup)
        self.verticalLayout.setContentsMargins(4, 2, 4, 2)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelSetup = QtWidgets.QLabel(self.frameSetup)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelSetup.setFont(font)
        self.labelSetup.setObjectName("labelSetup")
        self.verticalLayout.addWidget(self.labelSetup)
        self.wSetup = QtWidgets.QWidget(self.frameSetup)
        self.wSetup.setObjectName("wSetup")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.wSetup)
        self.horizontalLayout.setContentsMargins(4, 2, 4, 2)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelL = QtWidgets.QLabel(self.wSetup)
        self.labelL.setObjectName("labelL")
        self.horizontalLayout.addWidget(self.labelL)
        self.L = QtWidgets.QDoubleSpinBox(self.wSetup)
        self.L.setMinimum(0.1)
        self.L.setMaximum(10.0)
        self.L.setSingleStep(0.01)
        self.L.setProperty("value", 1.0)
        self.L.setObjectName("L")
        self.horizontalLayout.addWidget(self.L)
        self.labely0 = QtWidgets.QLabel(self.wSetup)
        self.labely0.setObjectName("labely0")
        self.horizontalLayout.addWidget(self.labely0)
        self.y0 = QtWidgets.QDoubleSpinBox(self.wSetup)
        self.y0.setDecimals(3)
        self.y0.setMinimum(0.01)
        self.y0.setMaximum(1.0)
        self.y0.setSingleStep(0.01)
        self.y0.setProperty("value", 0.1)
        self.y0.setObjectName("y0")
        self.horizontalLayout.addWidget(self.y0)
        self.verticalLayout.addWidget(self.wSetup)
        self.verticalLayout_4.addWidget(self.frameSetup)
        self.frameBelt = QtWidgets.QFrame(Polargraph)
        self.frameBelt.setFrameShape(QtWidgets.QFrame.Panel)
        self.frameBelt.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBelt.setLineWidth(2)
        self.frameBelt.setObjectName("frameBelt")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frameBelt)
        self.verticalLayout_3.setContentsMargins(4, 2, 4, 2)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelBelt = QtWidgets.QLabel(self.frameBelt)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelBelt.setFont(font)
        self.labelBelt.setObjectName("labelBelt")
        self.verticalLayout_3.addWidget(self.labelBelt)
        self.wBelt = QtWidgets.QWidget(self.frameBelt)
        self.wBelt.setObjectName("wBelt")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.wBelt)
        self.gridLayout_2.setContentsMargins(4, 2, 4, 2)
        self.gridLayout_2.setHorizontalSpacing(4)
        self.gridLayout_2.setVerticalSpacing(1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelUnit = QtWidgets.QLabel(self.wBelt)
        self.labelUnit.setObjectName("labelUnit")
        self.gridLayout_2.addWidget(self.labelUnit, 0, 0, 1, 1)
        self.unit = QtWidgets.QDoubleSpinBox(self.wBelt)
        self.unit.setMinimum(1.0)
        self.unit.setMaximum(5.0)
        self.unit.setSingleStep(0.1)
        self.unit.setProperty("value", 2.0)
        self.unit.setObjectName("unit")
        self.gridLayout_2.addWidget(self.unit, 0, 1, 1, 1)
        self.labelCircum = QtWidgets.QLabel(self.wBelt)
        self.labelCircum.setObjectName("labelCircum")
        self.gridLayout_2.addWidget(self.labelCircum, 0, 2, 1, 1)
        self.circumference = QtWidgets.QDoubleSpinBox(self.wBelt)
        self.circumference.setDecimals(0)
        self.circumference.setMinimum(1.0)
        self.circumference.setProperty("value", 25.0)
        self.circumference.setObjectName("circumference")
        self.gridLayout_2.addWidget(self.circumference, 0, 3, 1, 1)
        self.steps = QtWidgets.QDoubleSpinBox(self.wBelt)
        self.steps.setDecimals(0)
        self.steps.setMinimum(100.0)
        self.steps.setMaximum(500.0)
        self.steps.setSingleStep(50.0)
        self.steps.setProperty("value", 200.0)
        self.steps.setObjectName("steps")
        self.gridLayout_2.addWidget(self.steps, 1, 1, 1, 1)
        self.labelStepSpeed = QtWidgets.QLabel(self.wBelt)
        self.labelStepSpeed.setObjectName("labelStepSpeed")
        self.gridLayout_2.addWidget(self.labelStepSpeed, 1, 2, 1, 1)
        self.labelSteps = QtWidgets.QLabel(self.wBelt)
        self.labelSteps.setObjectName("labelSteps")
        self.gridLayout_2.addWidget(self.labelSteps, 1, 0, 1, 1)
        self.stepSpeed = QtWidgets.QDoubleSpinBox(self.wBelt)
        self.stepSpeed.setDecimals(0)
        self.stepSpeed.setMinimum(10.0)
        self.stepSpeed.setMaximum(1000.0)
        self.stepSpeed.setSingleStep(10.0)
        self.stepSpeed.setProperty("value", 500.0)
        self.stepSpeed.setObjectName("stepSpeed")
        self.gridLayout_2.addWidget(self.stepSpeed, 1, 3, 1, 1)
        self.verticalLayout_3.addWidget(self.wBelt)
        self.verticalLayout_4.addWidget(self.frameBelt)
        self.frameScan = QtWidgets.QFrame(Polargraph)
        self.frameScan.setFrameShape(QtWidgets.QFrame.Panel)
        self.frameScan.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameScan.setLineWidth(2)
        self.frameScan.setObjectName("frameScan")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameScan)
        self.verticalLayout_2.setContentsMargins(4, 2, 4, 2)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelScan = QtWidgets.QLabel(self.frameScan)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelScan.setFont(font)
        self.labelScan.setObjectName("labelScan")
        self.verticalLayout_2.addWidget(self.labelScan)
        self.wScan = QtWidgets.QWidget(self.frameScan)
        self.wScan.setObjectName("wScan")
        self.gridLayout = QtWidgets.QGridLayout(self.wScan)
        self.gridLayout.setContentsMargins(4, 2, 4, 2)
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.labelHeight = QtWidgets.QLabel(self.wScan)
        self.labelHeight.setObjectName("labelHeight")
        self.gridLayout.addWidget(self.labelHeight, 0, 0, 1, 1)
        self.labelWidth = QtWidgets.QLabel(self.wScan)
        self.labelWidth.setObjectName("labelWidth")
        self.gridLayout.addWidget(self.labelWidth, 0, 2, 1, 1)
        self.labelStep = QtWidgets.QLabel(self.wScan)
        self.labelStep.setObjectName("labelStep")
        self.gridLayout.addWidget(self.labelStep, 1, 0, 1, 1)
        self.labelSpeed = QtWidgets.QLabel(self.wScan)
        self.labelSpeed.setObjectName("labelSpeed")
        self.gridLayout.addWidget(self.labelSpeed, 1, 2, 1, 1)
        self.height = QtWidgets.QDoubleSpinBox(self.wScan)
        self.height.setMinimum(0.05)
        self.height.setMaximum(10.0)
        self.height.setSingleStep(0.01)
        self.height.setProperty("value", 0.6)
        self.height.setObjectName("height")
        self.gridLayout.addWidget(self.height, 0, 1, 1, 1)
        self.width = QtWidgets.QDoubleSpinBox(self.wScan)
        self.width.setMinimum(0.05)
        self.width.setMaximum(10.0)
        self.width.setSingleStep(0.01)
        self.width.setProperty("value", 0.6)
        self.width.setObjectName("width")
        self.gridLayout.addWidget(self.width, 0, 3, 1, 1)
        self.step = QtWidgets.QDoubleSpinBox(self.wScan)
        self.step.setMinimum(0.01)
        self.step.setMaximum(0.5)
        self.step.setSingleStep(0.01)
        self.step.setObjectName("step")
        self.gridLayout.addWidget(self.step, 1, 1, 1, 1)
        self.speed = QtWidgets.QDoubleSpinBox(self.wScan)
        self.speed.setDecimals(0)
        self.speed.setMinimum(1.0)
        self.speed.setMaximum(200.0)
        self.speed.setSingleStep(1.0)
        self.speed.setProperty("value", 20.0)
        self.speed.setObjectName("speed")
        self.gridLayout.addWidget(self.speed, 1, 3, 1, 1)
        self.verticalLayout_2.addWidget(self.wScan)
        self.verticalLayout_4.addWidget(self.frameScan)

        self.retranslateUi(Polargraph)
        QtCore.QMetaObject.connectSlotsByName(Polargraph)

    def retranslateUi(self, Polargraph):
        _translate = QtCore.QCoreApplication.translate
        Polargraph.setWindowTitle(_translate("Polargraph", "Polargraph"))
        self.frameSetup.setStatusTip(_translate("Polargraph", "Polargraph: Layout of scanner"))
        self.labelSetup.setText(_translate("Polargraph", "Setup"))
        self.labelL.setText(_translate("Polargraph", "L"))
        self.L.setSuffix(_translate("Polargraph", " m"))
        self.labely0.setText(_translate("Polargraph", "<html><head/><body><p>y<span style=\" vertical-align:sub;\">0</span></p></body></html>"))
        self.y0.setSuffix(_translate("Polargraph", " m"))
        self.labelBelt.setText(_translate("Polargraph", "Belt Drive"))
        self.labelUnit.setText(_translate("Polargraph", "unit"))
        self.unit.setStatusTip(_translate("Polargraph", "Polargraph: Tooth size on timing belt"))
        self.unit.setSuffix(_translate("Polargraph", " mm"))
        self.labelCircum.setText(_translate("Polargraph", "circum"))
        self.circumference.setStatusTip(_translate("Polargraph", "Polargraph: Units per motor revolution"))
        self.circumference.setSuffix(_translate("Polargraph", " units"))
        self.steps.setStatusTip(_translate("Polargraph", "Polargraph: Motor steps per revolution"))
        self.labelStepSpeed.setText(_translate("Polargraph", "speed"))
        self.labelSteps.setText(_translate("Polargraph", "steps"))
        self.stepSpeed.setStatusTip(_translate("Polargraph", "Polargraph: Motor steps per second"))
        self.stepSpeed.setSuffix(_translate("Polargraph", " steps/s"))
        self.frameScan.setStatusTip(_translate("Polargraph", "Polargraph: Scan configuration"))
        self.labelScan.setText(_translate("Polargraph", "Scan"))
        self.labelHeight.setText(_translate("Polargraph", "height"))
        self.labelWidth.setText(_translate("Polargraph", "width"))
        self.labelStep.setText(_translate("Polargraph", "Δy"))
        self.labelSpeed.setStatusTip(_translate("Polargraph", "Polargraph: Translation speed"))
        self.labelSpeed.setText(_translate("Polargraph", "speed"))
        self.height.setSuffix(_translate("Polargraph", " m"))
        self.width.setSuffix(_translate("Polargraph", " m"))
        self.step.setSuffix(_translate("Polargraph", " m"))
        self.speed.setSuffix(_translate("Polargraph", " mm/s"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Polargraph = QtWidgets.QWidget()
    ui = Ui_Polargraph()
    ui.setupUi(Polargraph)
    Polargraph.show()
    sys.exit(app.exec_())

