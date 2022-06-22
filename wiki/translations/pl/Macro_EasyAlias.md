# Macro EasyAlias/pl
{{Macro
|Name=EasyAlias
|Icon=easy-alias-icon.png
|Description=Use this to quickly and easily create aliases for cells in your spreadsheets. It takes the text labels you will have already created in one column and uses those labels as aliases in the next column.
|Author=TheMarkster
|Version=2022.03.21
|Date=2022-13-21
|FCVersion=All
|Download=[https   *//www.freecadweb.org/wiki/images/5/5e/Easy-alias-icon.png ToolBar Icon]
}}

## Description

Use this to quickly and easily create aliases for cells in your spreadsheets. It takes the text labels you will have already created in one column and uses those labels as aliases in the next column. For example, the text labels in Column A can be used to create aliases for the cells in Column B. Since version 2022.03.21 if you include text inside parentheses only that text will be the alias. For example, \"Height of top end (topHeight)\" as the label (without the quotes) would make the alias of topHeight in the next column.

## Usage

Highlight the cells containing the text labels and run the macro. Adjacent cells in the next column will now contain aliases made from the text values from the highlighted cells.

<img alt="" src=images/EasyAlias-scr1.png  style="width   *600px;"> 
*EasyAlias screenshot1, Text labels from Column A are used to create the aliases in Column B.*

## Script

ToolBar icon ![](images/easy-alias-icon.png )

**Macro\_EasyAlias.FCMacro**


{{MacroCode|code=
# -*- coding   * utf-8 -*-
import FreeCAD
from PySide import QtGui

"""
EasyAlias.FCMacro.py

This macro can be used to easily create aliases based on the content of selected spreadsheet 
cells in the previous column.  As an example, suppose you wish to have the following   *

A1   * content = 'radius', B1   * content = '5', alias = 'radius'
A2   * content = 'height', B1   * content = '15', alias = 'height'

The traditional way to set this up would be   *
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

Using this macro, the work flow becomes   *
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
__url__ = "https   *//wiki.freecadweb.org/Macro_EasyAlias"
__Wiki__ = "https   *//wiki.freecadweb.org/Macro_EasyAlias"
__date__ = "2022.03.21" #year.month.date
__version__ = __date__


def getSelected(selected_sheet)   *
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
    for i in subw   *
        if i.widget().metaObject().className() == "SpreadsheetGui   *   *SheetView"   *
            widgets.append(i.widget())
    if len(widgets) > 1   *
        FreeCAD.Console.PrintError("Having more than one spreadsheet view open at a time can confuse the macro.  Close the other sheet views and try again\n")
        return None
    elif len(widgets) == 1   *
        return widgets[0].findChild(QtGui.QTableView).selectedIndexes()
    return None

def getSelectedCellIndices(selected_sheet)   *
    """returns selected cell indices in the form of a list of tuples (row,col)
    or None if no cells are selected.  Raises exception if more than one column selected.
"""
    sel = getSelected(selected_sheet)
    if not sel   *
        FreeCAD.Console.PrintWarning('Select the spreadsheet in the tree view in addition to selecting the cells in the active view.\n')
        return []
    elif sel[0].column() != sel[-1].column()   *
        raise Exception('Multiple columns selected.  Only cells from a single column are supported.')

    col = sel[0].column()
    cellIndices=[] #will be list of tuples in form of (row,col)
    for c in sel   *
        cellIndices.append((c.row(),c.column()))
    return cellIndices

def getCellIndexNextColumn(ci)   *
   return (ci[0],ci[1]+1) #(ci[0],ci[1]+1) gets cellIndex of the next cell to the right (next column)


def getSpreadsheet()   *
    """return first selected spreadsheet object in document or None if none selected."""
    selObj = FreeCADGui.Selection.getSelectionEx()
    if not selObj   *
        return None
    for obj in selObj   *
        if 'Spreadsheet   *   *Sheet' in obj.Object.TypeId   *
            return obj.Object
        elif "App   *   *Link" in obj.Object.TypeId   *
            if 'Spreadsheet   *   *Sheet' in obj.Object.LinkedObject.TypeId   *
                return obj.Object.LinkedObject

def getCellContent(sheet, cellIndex)   *
    """sheet is the spreadsheet object, cellIndex is a tuple in the form of (row,col), e.g. (3,2) to get cell
contents of cell(3,2) of sheet, in other words C2.  Return value is content of cell."""
    address = cellIndexToAddress(cellIndex)
    return sheet.get(address)

def cellIndexToAddress(cellIndex)   *
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    r,c = cellIndex
    if c > 26   *
        raise StandardError('Columns beyond Z are not supported at this time.')
    address = chars[c]+str(r+1)
    return address

#thanks to Ouriço for this modification to allow parentheses to define the alias
#within the substring
def setAlias(sheet, cellIndex, alias)   *
    address = cellIndexToAddress(cellIndex)
    # extract any text between () and use that as the alias.
    # If brackets not found then use the original alias.
    firstidx  = alias.find('(')
    secondidx = alias.find(')')
    if (firstidx != -1) and (secondidx != -1) and (firstidx < secondidx)   *
        alias = alias[firstidx + 1    * secondidx]
    sheet.setAlias(address, alias)

s = getSpreadsheet()
if not s   *
    raise Exception('No spreadsheet selected.  Please select a spreadsheet in the tree view.')
cellIndices = getSelectedCellIndices(s)
if len(cellIndices) == 0   *
    FreeCAD.Console.PrintWarning("Unable to get selected cell indices.\n");
s.Document.openTransaction("EasyAlias")
for ci in cellIndices   *
    #FreeCAD.Console.PrintMessage("setting alias   * "+s.Name+'['+str(cellIndexToAddress(getCellIndexNextColumn(ci)))+"] ---> "+getCellContent(s,ci).replace(' ','_')+"\n")
    try   *
        setAlias(s, getCellIndexNextColumn(ci), str(getCellContent(s,ci).replace(' ','_').replace('.','_')))  #use e.g. content of A5 as alias for B5
    except   *
        FreeCAD.Console.PrintError("Error.  Unable to set alias   * "+getCellContent(s,ci).replace(' ','_')+" for spreadsheet   * "+str(s)+" cell "+cellIndexToAddress(getCellIndexNextColumn(ci))+"\n")
        FreeCAD.Console.PrintError("Remember, aliases cannot begin with a numeral or an underscore or contain any invalid characters.\n")
s.Document.commitTransaction()

App.ActiveDocument.recompute()
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro EasyAlias/pl
