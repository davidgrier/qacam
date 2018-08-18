# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from common.QSettingsWidget import QSettingsWidget
from DS345Settings_UI import Ui_DS345Settings


class QDS345Settings(QSettingsWidget):
    """Configuration for a Stanford Research Systems DS345 function generator"""

    def __init__(self, parent=None, device=None):
        super(QDS345Settings, self).__init__(parent=parent,
                                             device=device,
                                             ui=Ui_DS345Settings())

    def configureUi(self):
        # validate edit fields
        notation = QtGui.DoubleValidator.StandardNotation
        val = QtGui.QDoubleValidator(0.001, 5., 3, self.ui.amplitude)
        val.setNotation(notation)


if __name__ == '__main__':
    import sys
    from DS345 import DS345

    app = QtGui.QApplication(sys.argv)
    try:
        device = DS345()
    except ValueError:
        device = None
    wid = QDS345Settings(device=device)
    wid.show()
    sys.exit(app.exec_())
