# Macro EasyAlias/fr
{{Macro/fr
|Name=EasyAlias
|Icon=easy-alias-icon.png
|Description=Utilisez cette fonction pour créer rapidement et facilement des alias pour les cellules de vos feuilles de calcul. Elle prend les étiquettes de texte que vous avez déjà créées dans une colonne et les utilise comme alias dans la colonne suivante.
|Author=TheMarkster
|Version=2020.10.06
|Date=2020-10.06
|FCVersion=Tous
|Download=[https://www.freecadweb.org/wiki/images/5/5e/Easy-alias-icon.png Icône de la barre d'outils]
}}

## Description

Utilisez cette fonction pour créer rapidement et facilement des alias pour les cellules de vos feuilles de calcul. Elle prend les étiquettes de texte que vous avez déjà créées dans une colonne et les utilise comme alias dans la colonne suivante. Par exemple, les étiquettes de texte de la colonne A peuvent être utilisées pour créer des alias pour les cellules de la colonne B.

## Utilisation

Mettez en surbrillance les cellules contenant les étiquettes de texte et exécutez la macro. Les cellules adjacentes de la colonne suivante contiennent désormais des alias créés à partir des valeurs de texte des cellules mises en surbrillance.

<img alt="" src=images/EasyAlias-scr1.png  style="width:600px;"> 
*Capture d'écran EasyAlias1, les étiquettes de texte de la colonne A sont utilisées pour créer les alias de la colonne B.*

## Script

ToolBar icon ![](images/easy-alias-icon.png )

**Macro\_EasyAlias.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
import FreeCAD
from PySide import QtGui

"""
EasyAlias.FCMacro.py

This macro can be used to easily create aliases based on the content of selected spreadsheet 
cells in the previous column.  As an example, suppose you wish to have the following:

A1: content = 'radius', B1: content = '5', alias = 'radius'
A2: content = 'height', B1: content = '15', alias = 'height'

The traditional way to set this up would be:
Select A1
Enter radius
Select B1
Enter 5
Right-click B1
Select properties
Select Alias
Enter radius
click OK
Select A2
Enter height
Select B2
Enter 15
Right-click B2
Select Properties
Select Alias
Enter height
Click OK

Using this macro, the work flow becomes:
Select A1
Enter radius
Select B1
Enter 5
Select A2
Enter height
Select B2
Enter 15
Select A1 through A2
Run the EasyAlias macro
Done

"""

__title__ = "EasyAlias"
__author__ = "TheMarkster"
__url__ = "https://wiki.freecadweb.org/Macro_EasyAlias"
__Wiki__ = "https://wiki.freecadweb.org/Macro_EasyAlias"
__date__ = "2020.10.06" #year.month.date
__version__ = __date__


def getSelected(selected_sheet):
    """returns a QModelIndex object or None if none are selected
   use [0] to get at first cell in the selection
   use [0].row() to get first cell's row
   use [0].column() to get first cell's column
   use [-1] to get last cell in the selection
"""
    mw=FreeCADGui.getMainWindow()
    mdiarea=mw.findChild(QtGui.QMdiArea)
    subw=mdiarea.subWindowList()
    widgets = []
    for i in subw:
        if i.widget().metaObject().className() == "SpreadsheetGui::SheetView":
            widgets.append(i.widget())
    if len(widgets) > 1:
        FreeCAD.Console.PrintError("Having more than one spreadsheet view open at a time can confuse the macro.  Close the other sheet views and try again\n")
        return None
    elif len(widgets) == 1:
        return widgets[0].findChild(QtGui.QTableView).selectedIndexes()
    return None

def getSelectedCellIndices(selected_sheet):
    """returns selected cell indices in the form of a list of tuples (row,col)
    or None if no cells are selected.  Raises exception if more than one column selected.
"""
    sel = getSelected(selected_sheet)
    if not sel:
        FreeCAD.Console.PrintWarning('Select the spreadsheet in the tree view in addition to selecting the cells in the active view.\n')
        return []
    elif sel[0].column() != sel[-1].column():
        raise Exception('Multiple columns selected.  Only cells from a single column are supported.')

    col = sel[0].column()
    cellIndices=[] #will be list of tuples in form of (row,col)
    for c in sel:
        cellIndices.append((c.row(),c.column()))
    return cellIndices

def getCellIndexNextColumn(ci):
   return (ci[0],ci[1]+1) #(ci[0],ci[1]+1) gets cellIndex of the next cell to the right (next column)


def getSpreadsheet():
    """return first selected spreadsheet object in document or None if none selected."""
    selObj = FreeCADGui.Selection.getSelectionEx()
    if not selObj:
        return None
    for obj in selObj:
        if 'Spreadsheet.Sheet' in str(type(obj.Object)):
            return obj.Object

def getCellContent(sheet, cellIndex):
    """sheet is the spreadsheet object, cellIndex is a tuple in the form of (row,col), e.g. (3,2) to get cell
contents of cell(3,2) of sheet, in other words C2.  Return value is content of cell."""
    address = cellIndexToAddress(cellIndex)
    return sheet.get(address)

def cellIndexToAddress(cellIndex):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    r,c = cellIndex
    if c > 26:
        raise StandardError('Columns beyond Z are not supported at this time.')
    address = chars[c]+str(r+1)
    return address
    
def setAlias(sheet, cellIndex, alias):
    address = cellIndexToAddress(cellIndex)
    sheet.setAlias(address,alias)

s = getSpreadsheet()
if not s:
    raise Exception('No spreadsheet selected.  Please select a spreadsheet in the tree view.')
cellIndices = getSelectedCellIndices(s)
if len(cellIndices) == 0:
    FreeCAD.Console.PrintWarning("Unable to get selected cell indices.\n");
for ci in cellIndices:
    #FreeCAD.Console.PrintMessage("setting alias: "+s.Name+'['+str(cellIndexToAddress(getCellIndexNextColumn(ci)))+"] ---> "+getCellContent(s,ci).replace(' ','_')+"\n")
    try:
        setAlias(s, getCellIndexNextColumn(ci), str(getCellContent(s,ci).replace(' ','_').replace('.','_')))  #use e.g. content of A5 as alias for B5
    except:
        FreeCAD.Console.PrintError("Error.  Unable to set alias: "+getCellContent(s,ci).replace(' ','_')+" for spreadsheet: "+str(s)+" cell "+cellIndexToAddress(getCellIndexNextColumn(ci))+"\n")
        FreeCAD.Console.PrintError("Remember, aliases cannot begin with a numeral or an underscore or contain any invalid characters.\n")

App.ActiveDocument.recompute()
}}

---
[documentation index](../README.md) > Macro EasyAlias/fr
