# Macro SpreadsheetTools/fr
{{Macro/fr
|Name=Macro SpreadsheetTools
|Icon=Macro_SpreadsheetTools.png
|Description=Cette macro permet de gérer les cellules dans Spreadsheet-workbench de FreeCAD.
|Author=Wilfried Hortschitz
|Version=0.2.08
|Date=2017-11-03
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/3/35/Macro_SpreadsheetTools.png ToolBar Icon]
}}

## Description

Cette macro permet de gérer les cellules dans Spreadsheet-workbench de FreeCAD. Il aide à gérer les cellules dans le tableur Spreadsheet de FreeCAD. Avec son aide, on est capable de:

-   Couper/supprimer des données et/ou des informations d\'alias dans la zone sélectionnée des cellules.
-   Copier des données et/ou des informations d\'alias dans la zone sélectionnée des cellules dans le presse-papier.
-   Collez les données et/ou les informations d\'alias dans la zone sélectionnée des cellules du presse-papiers.

Plus d\'informations dans la page sur le forums: <http://forum.freecadweb.org/> and particular on <https://forum.freecadweb.org/viewtopic.php?f=22&t=20508&hilit=spreadsheet#p158443> and on Github on <https://github.com/HoWilgh/FCSpreadsheetTools/blob/master/README.md> .

![](images/Screenshot_from_2017-09-02_20-01-49.png )

## Script

ToolBar Icon ![](images/Macro_SpreadsheetTools.png )

**Macro SpreadsheetTools.FCMacro**


{{MacroCode|code=
# ============================================================================================================
# ============================================================================================================
# ==                                                                                                        ==
# ==                                       Spreadsheet tools                                                ==
# ==                                                                                                        ==
# ============================================================================================================
# ============================================================================================================
# ABOUT
# ============================================================================================================
# version v0.2.08 !!! This is beta version code so backup your data first!!! The author assumes no liability for data loss.
#
# Macro developed for FreeCAD (http://www.freecadweb.org/).
# This macro helps managing cells inside FreeCAD Spreadsheet workbench. It is able to:
#        - Cut/delete data and/or alias fields in a selected area of cells
#        - Copy data and/or alias fields in a selected area of cells to clipboard
#        - Paste data and/or alias fields in a selected area of cells from cliboard
# More information might be found on FreeCAD forums: http://forum.freecadweb.org/
#
#
# LICENSE
# ============================================================================================================
#
# This work is licensed under GNU Lesser General Public License (LGPL).
# To view a copy of this license, visit https://www.gnu.org/licenses/lgpl-3.0.html.
# 
# ============================================================================================================
__title__   = "Spreadsheet_tools"
__author__  = "HoWil"
__version__ = "0.2.08"
__date__    = "2017-09-02"

__Comment__ = "This macro helps managing cells inside a single spreadsheet of FreeCAD Spreadsheet workbench. It is able to cut/delete, copy and paste an area of cells including format, alias and units. Merged cells are not supported."

__Status__ = "stable"
__Requires__ = "FreeCAD 0.17"

from PySide import QtGui, QtCore

import FreeCADGui
#import FreeCAD
import FreeCAD as App

import string


'''
*Working* Cut/delete the selected area
*Working* Copy to clipboard
*Working* Paste from clipboard
*Working* Copy and paste alias

TODO:
* Check if something is overwritten and show a warning.
* Use shortcuts like Ctrl-c.
* Test if pandas is installed and offer import-export if available.

* Right click menu??
* Copy and paste formating???

Known limitations:
* Does work only with one opened FC-Spreadsheet.
* A cell has to be selected before selecting one of the options of Spreadsheet_tools.
* Does not work on merged cells.
'''


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


# ===== Global variables ==============================================
alphabet_list = list(string.ascii_uppercase)

column_list = [] # is filled with A, B, C,.... AA, AB, AC,...
for i in range(0,26):
    column_list.append(alphabet_list[i])

for i in range(0,26):
    for j in range(0,26):
        column_list.append(alphabet_list[i] + alphabet_list[j])


class Spreadsheet_Tools(QtGui.QDialog):
    """"""
    def __init__(self, MainWindow):
        super(Spreadsheet_Tools, self).__init__()
        self.window = MainWindow

        #MainWindow.setObjectName(_fromUtf8("MainWindow"))
        #MainWindow.resize(400, 450)
        #MainWindow.setMinimumSize(QtCore.QSize(400, 450))
        #MainWindow.setMaximumSize(QtCore.QSize(400, 450))
        #self.widget = QtGui.QWidget(MainWindow)
        #self.widget.setObjectName(_fromUtf8("widget"))


        self.init_UI()


    def init_UI(self):
        FreeCAD.Console.PrintMessage("init_UI")

        option3Button = QtGui.QPushButton("Copy to clipboard")
        option3Button.clicked.connect(self.copy_to_clipboard)
        option1Button = QtGui.QPushButton("Cut to clipboard/Delete selection")
        option1Button.clicked.connect(self.cut_delete_selection)
        option2Button = QtGui.QPushButton("Paste from clipboard")
        option2Button.clicked.connect(self.paste_from_clipboard)
        option4Button = QtGui.QPushButton("Close this dialog")
        option4Button.clicked.connect(self.close_dialog)

        buttonBox = QtGui.QDialogButtonBox()
        buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Vertical)
        buttonBox.setGeometry(QtCore.QRect(00, 100, 210, 200))
        buttonBox.addButton(option3Button, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(option1Button, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(option2Button, QtGui.QDialogButtonBox.ActionRole)
        buttonBox.addButton(option4Button, QtGui.QDialogButtonBox.ActionRole)



        self.groupBox = QtGui.QGroupBox()                                        # this is the group for associate
        self.groupBox.setGeometry(QtCore.QRect(00, 220, 125, 200))                          # coordinates position
        self.groupBox.setObjectName(_fromUtf8("groupBox"))                                  # name of window groupBox

#        section checkBox 1
        self.checkBox_1 = QtGui.QCheckBox(self.groupBox)                                    # create object QRadioButton in groupBox
        self.checkBox_1.setGeometry(QtCore.QRect(0, 0, 150, 20))                         # coordinates position
        self.checkBox_1.setObjectName(_fromUtf8("Copy/paste/cut visible cell-content"))                              # name of object
        self.checkBox_1.setChecked(True)                                                    # Check by default True or False

        self.checkBox_1.setToolTip(_translate("MainWindow", "Copy/paste/cut visible cell-content", None))
        self.checkBox_1.setText(_translate("MainWindow", "Use visible content", None))
        #self.checkBox_1.clicked.connect(self.on_checkBox_1_clicked)

#        section checkBox 2
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox)                                    # create object QRadioButton in groupBox
        self.checkBox_2.setGeometry(QtCore.QRect(160, 0, 150, 20))                         # coordinates position
        self.checkBox_2.setObjectName(_fromUtf8("Copy/paste/cut cell-alias"))                              # name of object
        self.checkBox_2.setChecked(True)                                                    # Check by default True or False

        self.checkBox_2.setToolTip(_translate("MainWindow", "Use alias", None))
        self.checkBox_2.setText(_translate("MainWindow", "Use alias", None))
        #self.checkBox_2.clicked.connect(self.on_checkBox_2_clicked)

        self.checkBox_3 = QtGui.QCheckBox(self.groupBox)                                    # create object QRadioButton in groupBox
        self.checkBox_3.setGeometry(QtCore.QRect(280, 0, 150, 20))                         # coordinates position
        self.checkBox_3.setObjectName(_fromUtf8("Copy/paste/cut cell-alias"))                              # name of object
        self.checkBox_3.setChecked(True)                                                    # Check by default True or False

        self.checkBox_3.setToolTip(_translate("MainWindow", "Use formatting", None))
        self.checkBox_3.setText(_translate("MainWindow", "Use formatting", None))
        #self.checkBox_3.clicked.connect(self.on_checkBox_3_clicked)

        mainLayout = QtGui.QVBoxLayout()

        mainLayout.addWidget(self.groupBox)
        mainLayout.addWidget(buttonBox)

        self.setLayout(mainLayout)
        # define window     xLoc,yLoc,xDim,yDim
        self.setGeometry(   500, 500, 450, 220)
        self.setWindowTitle("Pick a Button")


    def get_selection(self):

        mw = FreeCADGui.getMainWindow()
        mdiarea = mw.findChild(QtGui.QMdiArea)

        subw = mdiarea.subWindowList()

        for i in subw:
            if i.widget().metaObject().className() == "SpreadsheetGui::SheetView":
                sheet = i.widget()

                table = sheet.findChild(QtGui.QTableView)
        ind = table.selectedIndexes()

        self.mw = mw    # mainwindow
        self.sheet = sheet  # spreadsheet
        self.table = table  # table
        self.ind = ind

        l_elements = len(ind)

        first_element = ind.__getitem__(0)
        fe_col = first_element.column()
        fe_row = first_element.row()
        fe_alphanum = column_list[fe_col] + str(fe_row+1)

        last_element = ind.__getitem__(l_elements-1)
        le_col = last_element.column()
        le_row = last_element.row()
        le_alphanum = column_list[le_col] + str(le_row+1)

        self.fe_alphanum = fe_alphanum
        self.fe_col = fe_col # numeric representation of column, D=>3
        self.fe_row = fe_row # numeric representation of row

        self.le_alphanum = le_alphanum
        self.le_col = le_col
        self.le_row = le_row


    def delete_selection(self):
        # Delete selection
        self.get_selection()

        ind = self.ind

        rows = range(self.fe_row, self.le_row+1)
        columns = range(self.fe_col, self.le_col+1)


        for row in rows:
            for column in columns:
                cell = column_list[column] + str(row+1)
                if self.checkBox_1.isChecked():
                    App.ActiveDocument.Spreadsheet.set(cell, str(' ') )
                if self.checkBox_2.isChecked():
                    try:
                        App.ActiveDocument.Spreadsheet.setAlias(cell, None)
                    except:
                        FreeCAD.Console.PrintMessage("\nCould not delete alias.")
                if self.checkBox_3.isChecked():
                    try:
                        App.ActiveDocument.Spreadsheet.set(cell, '')
                    except:
                        FreeCAD.Console.PrintMessage("\nCould not delete formatting.")

        App.activeDocument().recompute()


    def cut_delete_selection(self):
        # Cut selection
        self.copy_to_clipboard()
        self.delete_selection()


    def paste_from_clipboard(self):
        # Paste from clipboard

        self.get_selection()

        clipboard = QtGui.QApplication.clipboard()

        if clipboard.mimeData().hasText():

            cbtext = clipboard.mimeData().text()
            cbtext_split = [s.split('\t') for s in cbtext.splitlines()]

            if self.checkBox_1.isChecked() and self.checkBox_2.isChecked() and self.checkBox_3.isChecked():

                n_cells = len(cbtext_split)/3

                index_col = self.fe_col
                for n_line, line in zip(range(n_cells), cbtext_split[0:n_cells]):
                    for n_word, col in zip(range(len(line)), line):
                        cell = column_list[index_col+n_word] + str(self.fe_row+n_line+1)
                        App.ActiveDocument.Spreadsheet.set(cell, str(col) )

                for n_line, line in zip(range(n_cells), cbtext_split[n_cells:n_cells*2]):
                    for n_word, col in zip(range(len(line)), line):
                        cell = column_list[index_col+n_word] + str(self.fe_row+n_line+1)
                        try:
                            App.ActiveDocument.Spreadsheet.setAlias(cell, str(col))
                        except:
                            FreeCAD.Console.PrintMessage("\nCould not set/paste alias.")

                for n_line, line in zip(range(n_cells), cbtext_split[n_cells*2:]):
                    for n_word, col in zip(range(len(line)), line):
                        cell = column_list[index_col+n_word] + str(self.fe_row+n_line+1)
                        import ast
                        col = ast.literal_eval(col)

                        try:
                            if not(col['style'] == 'None'):
                                eval("App.ActiveDocument.Spreadsheet.setStyle('"+cell+"', "+col['style']+")")
                            if not(col['alignment'] == 'None'):
                                eval("App.ActiveDocument.Spreadsheet.setAlignment('"+cell+"', "+col['alignment']+")")
                        except:
                            FreeCAD.Console.PrintMessage("\nCould not set formatting (style, alignment).")

                        try:
                            if not(col['foreground'] == 'None'):
                                App.ActiveDocument.Spreadsheet.setForeground(cell, ast.literal_eval(col['foreground']))
                            if not(col['background'] == 'None'):
                                eval("App.ActiveDocument.Spreadsheet.setBackground('"+cell+"', "+col['background']+")")
                        except:
                            FreeCAD.Console.PrintMessage("\nCould not set formatting ( background, foreground).")

                        try:
                            if not(col['contents'] == ''):
                                App.ActiveDocument.Spreadsheet.set(cell, col['contents'])
                            if not(col['displayunit'] == 'None'):
                                App.ActiveDocument.Spreadsheet.setDisplayUnit(cell, col['displayunit'])
                        except:
                            FreeCAD.Console.PrintMessage("\nCould not set formatting (displayunit and contents).")


            if self.checkBox_1.isChecked() and (not self.checkBox_2.isChecked()):
                n_cells = len(cbtext_split)

                index_col = self.fe_col
                for n_line, line in zip(range(n_cells), cbtext_split[0:n_cells]):
                    for n_word, col in zip(range(len(line)), line):
                        cell = column_list[index_col+n_word] + str(self.fe_row+n_line+1)
                        App.ActiveDocument.Spreadsheet.set(cell, str(col) )

            if (not self.checkBox_1.isChecked()) and self.checkBox_2.isChecked():
                n_cells = len(cbtext_split)

                index_col = self.fe_col
                for n_line, line in zip(range(n_cells), cbtext_split[0:n_cells]):
                    for n_word, col in zip(range(len(line)), line):
                        cell = column_list[index_col+n_word] + str(self.fe_row+n_line+1)
                        try:
                            App.ActiveDocument.Spreadsheet.setAlias(cell, str(col))
                        except:
                            FreeCAD.Console.PrintMessage("\nCould not set/paste alias.")

            App.activeDocument().recompute()

        else:
            clipboard.setText(tr("Cannot display data! No proper information stored in clipboard."))


    def copy_to_clipboard(self):
        # Copy to clipboard

        self.get_selection()

        if len(self.ind) > 0:
            # sort select indexes into rows and columns
            previous = self.ind[0]
            columns = []
            rows = []
            clipboard = ""

            if self.checkBox_1.isChecked():

                for index in self.ind:
                    if previous.column() != index.column():
                        columns.append(rows)
                        rows = []
                    rows.append(index.data())

                    idx_col = index.column()
                    idx_row = index.row()
                    idx_alphanum = column_list[idx_col] + str(idx_row+1)

                    previous = index

                columns.append(rows)
                cell_content = columns
                self.cell_content = cell_content

                # add rows and columns to clipboard
                nrows = len(cell_content[0])
                ncols = len(cell_content)
                for r in xrange(nrows):
                    for c in xrange(ncols):
                        if cell_content[c][r] is not None:
                            clipboard += cell_content[c][r]
                        else:
                            clipboard += ''
                        if c != (ncols-1):
                            clipboard += '\t'
                    clipboard += '\n'

            previous_alias = self.ind[0]
            columns_alias = []
            rows_alias = []
            clipboard_alias = ""

            if self.checkBox_2.isChecked():

                for index in self.ind:
                    if previous_alias.column() != index.column():
                        columns_alias.append(rows_alias)
                        rows_alias = []

                    idx_col = index.column()
                    idx_row = index.row()
                    idx_alphanum = column_list[idx_col] + str(idx_row+1)
                    rows_alias.append(App.ActiveDocument.Spreadsheet.getAlias(idx_alphanum))

                    previous_alias = index

                columns_alias.append(rows_alias)
                cell_content_alias = columns_alias
                self.cell_content_alias = cell_content_alias

                # add rows and columns to clipboard
                nrows = len(cell_content_alias[0])
                ncols = len(cell_content_alias)
                for r in xrange(nrows):
                    for c in xrange(ncols):
                        if cell_content_alias[c][r] is not None:
                            clipboard_alias += cell_content_alias[c][r]
                        else:
                            clipboard_alias += ''
                        if c != (ncols-1):
                            clipboard_alias += '\t'
                    clipboard_alias += '\n'

            previous_formatting = self.ind[0]
            columns_formatting = []
            rows_formatting = []
            clipboard_formatting = ""

            if self.checkBox_3.isChecked():

                for index in self.ind:
                    if previous_formatting.column() != index.column():
                        columns_formatting.append(rows_formatting)
                        rows_formatting = []

                    idx_col = index.column()
                    idx_row = index.row()
                    idx_alphanum = column_list[idx_col] + str(idx_row+1)
                    formatting_dict = {'style':str(App.ActiveDocument.Spreadsheet.getStyle(idx_alphanum)),
                                        'foreground':str(App.ActiveDocument.Spreadsheet.getForeground(idx_alphanum)),
                                        'background':str(App.ActiveDocument.Spreadsheet.getBackground(idx_alphanum)),
                                        'contents':str(App.ActiveDocument.Spreadsheet.getContents(idx_alphanum)),
                                        'displayunit':str(App.ActiveDocument.Spreadsheet.getDisplayUnit(idx_alphanum)),
                                        'alignment':str(App.ActiveDocument.Spreadsheet.getAlignment(idx_alphanum))}
                    rows_formatting.append(formatting_dict)

                    previous_formatting = index

                columns_formatting.append(rows_formatting)
                cell_content_formatting = columns_formatting
                self.cell_content_formatting = cell_content_formatting
                FreeCAD.Console.PrintMessage(cell_content_formatting)
                # add rows and columns to clipboard
                nrows = len(cell_content_formatting[0])
                ncols = len(cell_content_formatting)
                for r in xrange(nrows):
                    for c in xrange(ncols):

                        if cell_content_formatting[c][r] is not None:
                            clipboard_formatting += str( cell_content_formatting[c][r] )
                        else:
                            clipboard_formatting += ''
                        if c != (ncols-1):
                            clipboard_formatting += '\t'

                    clipboard_formatting += '\n'

            # copy to the system clipboard
            sys_clip = QtGui.QApplication.clipboard()
            sys_clip.setText(clipboard + clipboard_alias + clipboard_formatting)

    def close_dialog(self):
        self.close()

MainWindow = QtGui.QMainWindow()
form = Spreadsheet_Tools(MainWindow)
form.show()
}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro SpreadsheetTools/fr
