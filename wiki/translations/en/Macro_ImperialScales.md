# Macro ImperialScales/en
{{Macro
|Name=ImperialScales
|Description=This macro shows a list of US Imperial Arch scales list with the corresponding factor to apply to TechDraw pages or views
|Author=Yorik
|Date=2021-06-01
|Version=0.1
|FCVersion=0.18+
}}

## Description

This macro pops up a dialog with a list of US Imperial Arch scales list as retrieved from [Archtoolbox CAD Scale Factors](https://www.archtoolbox.com/representation/cad/scalefactor.html), with the corresponding factor to apply to TechDraw pages or views. The scales factors can be double-clicked and copied.

## Code

**Macro\_ImperialScales.FCMacro**


{{MacroCode|code=
<nowiki>
# -*- coding: utf-8 -*-

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Dialog(QDialog):

    def __init__(self):

        QDialog.__init__(self)
        self.resize(221, 413)
        self.verticalLayout = QVBoxLayout(self)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(1)
        qtablewidgetitem = QTableWidgetItem()
        qtablewidgetitem.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, qtablewidgetitem)
        self.tableWidget.setRowCount(11)
        qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, qtablewidgetitem1)
        qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, qtablewidgetitem2)
        qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, qtablewidgetitem3)
        qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, qtablewidgetitem4)
        qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, qtablewidgetitem5)
        qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, qtablewidgetitem6)
        qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, qtablewidgetitem7)
        qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, qtablewidgetitem8)
        qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, qtablewidgetitem9)
        qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, qtablewidgetitem10)
        qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, qtablewidgetitem11)
        qtablewidgetitem12 = QTableWidgetItem()
        qtablewidgetitem12.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, qtablewidgetitem12)
        qtablewidgetitem13 = QTableWidgetItem()
        qtablewidgetitem13.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
        self.tableWidget.setItem(1, 0, qtablewidgetitem13)
        qtablewidgetitem14 = QTableWidgetItem()
        qtablewidgetitem14.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
        self.tableWidget.setItem(2, 0, qtablewidgetitem14)
        qtablewidgetitem15 = QTableWidgetItem()
        qtablewidgetitem15.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
        self.tableWidget.setItem(3, 0, qtablewidgetitem15)
        qtablewidgetitem16 = QTableWidgetItem()
        qtablewidgetitem16.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
        self.tableWidget.setItem(4, 0, qtablewidgetitem16)
        qtablewidgetitem17 = QTableWidgetItem()
        qtablewidgetitem17.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
        self.tableWidget.setItem(5, 0, qtablewidgetitem17)
        qtablewidgetitem18 = QTableWidgetItem()
        qtablewidgetitem18.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
        self.tableWidget.setItem(6, 0, qtablewidgetitem18)
        qtablewidgetitem19 = QTableWidgetItem()
        qtablewidgetitem19.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
        self.tableWidget.setItem(7, 0, qtablewidgetitem19)
        qtablewidgetitem20 = QTableWidgetItem()
        qtablewidgetitem20.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
        self.tableWidget.setItem(8, 0, qtablewidgetitem20)
        qtablewidgetitem21 = QTableWidgetItem()
        qtablewidgetitem21.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
        self.tableWidget.setItem(9, 0, qtablewidgetitem21)
        qtablewidgetitem22 = QTableWidgetItem()
        qtablewidgetitem22.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
        self.tableWidget.setItem(10, 0, qtablewidgetitem22)
        self.tableWidget.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(True)

        self.verticalLayout.addWidget(self.tableWidget)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self,dlg=None):

        self.setWindowTitle(QCoreApplication.translate("Dialog", u"Arch scale factors", None))
        qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Factor", None))
        qtablewidgetitem1 = self.tableWidget.verticalHeaderItem(0)
        qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"1/16\" = 1'-0\"", None))
        qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(1)
        qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"3/32\" = 1'-0\"", None))
        qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(2)
        qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"1/8\" = 1'-0\"", None))
        qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(3)
        qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"3/16\" = 1'-0\"", None))
        qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(4)
        qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"1/4\" = 1'-0\"", None))
        qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(5)
        qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"3/8\" = 1'-0\"", None))
        qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(6)
        qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"1/2\" = 1'-0\"", None))
        qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(7)
        qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"3/4\" = 1'-0\"", None))
        qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(8)
        qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"1\" = 1'-0\"", None))
        qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(9)
        qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"1 1/2\" = 1'-0\"", None))
        qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(10)
        qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"3\" = 1'-0\"", None))

        sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        qtablewidgetitem12 = self.tableWidget.item(0, 0)
        qtablewidgetitem12.setText(QCoreApplication.translate("Dialog", u"1/192", None))
        qtablewidgetitem13 = self.tableWidget.item(1, 0)
        qtablewidgetitem13.setText(QCoreApplication.translate("Dialog", u"1/128", None))
        qtablewidgetitem14 = self.tableWidget.item(2, 0)
        qtablewidgetitem14.setText(QCoreApplication.translate("Dialog", u"1/96", None))
        qtablewidgetitem15 = self.tableWidget.item(3, 0)
        qtablewidgetitem15.setText(QCoreApplication.translate("Dialog", u"1/64", None))
        qtablewidgetitem16 = self.tableWidget.item(4, 0)
        qtablewidgetitem16.setText(QCoreApplication.translate("Dialog", u"1/48", None))
        qtablewidgetitem17 = self.tableWidget.item(5, 0)
        qtablewidgetitem17.setText(QCoreApplication.translate("Dialog", u"1/32", None))
        qtablewidgetitem18 = self.tableWidget.item(6, 0)
        qtablewidgetitem18.setText(QCoreApplication.translate("Dialog", u"1/24", None))
        qtablewidgetitem19 = self.tableWidget.item(7, 0)
        qtablewidgetitem19.setText(QCoreApplication.translate("Dialog", u"1/16", None))
        qtablewidgetitem20 = self.tableWidget.item(8, 0)
        qtablewidgetitem20.setText(QCoreApplication.translate("Dialog", u"1/12", None))
        qtablewidgetitem21 = self.tableWidget.item(9, 0)
        qtablewidgetitem21.setText(QCoreApplication.translate("Dialog", u"1/8", None))
        qtablewidgetitem22 = self.tableWidget.item(10, 0)
        qtablewidgetitem22.setText(QCoreApplication.translate("Dialog", u"1/4", None))
        self.tableWidget.setSortingEnabled(sortingEnabled)

dlg = Dialog()
dlg.show()
</nowiki>
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro ImperialScales/en
