# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Polargraph_UI.ui'
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

class Ui_Polargraph(object):
    def setupUi(self, Polargraph):
        Polargraph.setObjectName(_fromUtf8("Polargraph"))
        Polargraph.resize(327, 145)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Polargraph)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.frameSetup = QtGui.QFrame(Polargraph)
        self.frameSetup.setFrameShape(QtGui.QFrame.Panel)
        self.frameSetup.setFrameShadow(QtGui.QFrame.Raised)
        self.frameSetup.setLineWidth(2)
        self.frameSetup.setObjectName(_fromUtf8("frameSetup"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frameSetup)
        self.verticalLayout.setMargin(4)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelSetup = QtGui.QLabel(self.frameSetup)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelSetup.setFont(font)
        self.labelSetup.setObjectName(_fromUtf8("labelSetup"))
        self.verticalLayout.addWidget(self.labelSetup)
        self.wSetup = QtGui.QWidget(self.frameSetup)
        self.wSetup.setObjectName(_fromUtf8("wSetup"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.wSetup)
        self.horizontalLayout.setMargin(6)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelL = QtGui.QLabel(self.wSetup)
        self.labelL.setObjectName(_fromUtf8("labelL"))
        self.horizontalLayout.addWidget(self.labelL)
        self.L = QtGui.QLineEdit(self.wSetup)
        self.L.setObjectName(_fromUtf8("L"))
        self.horizontalLayout.addWidget(self.L)
        self.labely0 = QtGui.QLabel(self.wSetup)
        self.labely0.setObjectName(_fromUtf8("labely0"))
        self.horizontalLayout.addWidget(self.labely0)
        self.y0 = QtGui.QLineEdit(self.wSetup)
        self.y0.setObjectName(_fromUtf8("y0"))
        self.horizontalLayout.addWidget(self.y0)
        self.verticalLayout.addWidget(self.wSetup)
        self.verticalLayout_3.addWidget(self.frameSetup)
        self.frameScan = QtGui.QFrame(Polargraph)
        self.frameScan.setFrameShape(QtGui.QFrame.Panel)
        self.frameScan.setFrameShadow(QtGui.QFrame.Raised)
        self.frameScan.setLineWidth(2)
        self.frameScan.setObjectName(_fromUtf8("frameScan"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frameScan)
        self.verticalLayout_2.setMargin(4)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelScan = QtGui.QLabel(self.frameScan)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelScan.setFont(font)
        self.labelScan.setObjectName(_fromUtf8("labelScan"))
        self.verticalLayout_2.addWidget(self.labelScan)
        self.wScan = QtGui.QWidget(self.frameScan)
        self.wScan.setObjectName(_fromUtf8("wScan"))
        self.gridLayout = QtGui.QGridLayout(self.wScan)
        self.gridLayout.setMargin(6)
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelHeight = QtGui.QLabel(self.wScan)
        self.labelHeight.setObjectName(_fromUtf8("labelHeight"))
        self.gridLayout.addWidget(self.labelHeight, 0, 0, 1, 1)
        self.height = QtGui.QLineEdit(self.wScan)
        self.height.setObjectName(_fromUtf8("height"))
        self.gridLayout.addWidget(self.height, 0, 1, 1, 1)
        self.labelWidth = QtGui.QLabel(self.wScan)
        self.labelWidth.setObjectName(_fromUtf8("labelWidth"))
        self.gridLayout.addWidget(self.labelWidth, 0, 2, 1, 1)
        self.width = QtGui.QLineEdit(self.wScan)
        self.width.setObjectName(_fromUtf8("width"))
        self.gridLayout.addWidget(self.width, 0, 3, 1, 1)
        self.labelStep = QtGui.QLabel(self.wScan)
        self.labelStep.setObjectName(_fromUtf8("labelStep"))
        self.gridLayout.addWidget(self.labelStep, 1, 0, 1, 1)
        self.step = QtGui.QLineEdit(self.wScan)
        self.step.setObjectName(_fromUtf8("step"))
        self.gridLayout.addWidget(self.step, 1, 1, 1, 1)
        self.labelSpeed = QtGui.QLabel(self.wScan)
        self.labelSpeed.setObjectName(_fromUtf8("labelSpeed"))
        self.gridLayout.addWidget(self.labelSpeed, 1, 2, 1, 1)
        self.speed = QtGui.QLineEdit(self.wScan)
        self.speed.setObjectName(_fromUtf8("speed"))
        self.gridLayout.addWidget(self.speed, 1, 3, 1, 1)
        self.verticalLayout_2.addWidget(self.wScan)
        self.verticalLayout_3.addWidget(self.frameScan)

        self.retranslateUi(Polargraph)
        QtCore.QMetaObject.connectSlotsByName(Polargraph)

    def retranslateUi(self, Polargraph):
        Polargraph.setWindowTitle(_translate("Polargraph", "Form", None))
        self.frameSetup.setStatusTip(_translate("Polargraph", "Polargraph: Layout of scanner", None))
        self.labelSetup.setText(_translate("Polargraph", "Setup", None))
        self.labelL.setText(_translate("Polargraph", "L [m]", None))
        self.L.setStatusTip(_translate("Polargraph", "Polargraph: Separation between stepper motors", None))
        self.labely0.setText(_translate("Polargraph", "y<sub>0 </sub>[m]", None))
        self.y0.setStatusTip(_translate("Polargraph", "Polargraph: Initial vertical displacement", None))
        self.frameScan.setStatusTip(_translate("Polargraph", "Polargraph: Scan configuration", None))
        self.labelScan.setText(_translate("Polargraph", "Scan", None))
        self.labelHeight.setText(_translate("Polargraph", "height [m]", None))
        self.height.setStatusTip(_translate("Polargraph", "Polargraph: height of scan area", None))
        self.labelWidth.setText(_translate("Polargraph", "width [m]", None))
        self.width.setStatusTip(_translate("Polargraph", "Polargraph: Width of scan area", None))
        self.labelStep.setText(_translate("Polargraph", "Δy [m]", None))
        self.step.setStatusTip(_translate("Polargraph", "Polargraph: vertical separation between scans", None))
        self.labelSpeed.setText(_translate("Polargraph", "Speed", None))
        self.speed.setStatusTip(_translate("Polargraph", "Polargraph: speed of stepper motors", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Polargraph = QtGui.QWidget()
    ui = Ui_Polargraph()
    ui.setupUi(Polargraph)
    Polargraph.show()
    sys.exit(app.exec_())

