# Spreadsheet Workbench/en

{{Page_in_progress}}






<img alt="Spreadsheet workbench icon" src=images/Workbench_Spreadsheet.svg  style="width:128px;">

## Introduction

The <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:24px;"> [Spreadsheet Workbench](Spreadsheet_Workbench.md) allows you to create and edit spreadsheets, use data from the spreadsheet as parameters in a model, fill the spreadsheet with data retrieved from a model, perform calculations, and export the data to other spreadsheet applications such as LibreOffice or Microsoft Excel.


{{TOCright}}

<img alt="" src=images/Spreadsheet_screenshot.jpg  style="width:600px;"> 
*A spreadsheet with certain cells filled with text and quantities*

## Tools

-   <img alt="" src=images/Spreadsheet_CreateSheet.svg  style="width:24px;"> [Create sheet](Spreadsheet_CreateSheet.md): create a new spreadsheet.

-   <img alt="" src=images/Spreadsheet_Import.svg  style="width:24px;"> [Import](Spreadsheet_Import.md): import a tab-separated values file into a spreadsheet.
-   <img alt="" src=images/Spreadsheet_Export.svg  style="width:24px;"> [Export](Spreadsheet_Export.md): export a tab-separated values file from a spreadsheet.

-   <img alt="" src=images/Spreadsheet_MergeCells.svg  style="width:24px;"> [Merge cells](Spreadsheet_MergeCells.md): merge selected cells.
-   <img alt="" src=images/Spreadsheet_SplitCell.svg  style="width:24px;"> [Split cell](Spreadsheet_SplitCell.md): split previously merged cells.

-   <img alt="" src=images/Spreadsheet_AlignLeft.svg  style="width:24px;"> [Align left](Spreadsheet_AlignLeft.md): align the contents of selected cells to the left.
-   <img alt="" src=images/Spreadsheet_AlignCenter.svg  style="width:24px;"> [Align center](Spreadsheet_AlignCenter.md): align the contents of selected cells to the center horizontally.
-   <img alt="" src=images/Spreadsheet_AlignRight.svg  style="width:24px;"> [Align right](Spreadsheet_AlignRight.md): align the contents of selected cells to the right.
-   <img alt="" src=images/Spreadsheet_AlignTop.svg  style="width:24px;"> [Align top](Spreadsheet_AlignTop.md): align the contents of selected cells to the top.
-   <img alt="" src=images/Spreadsheet_AlignVCenter.svg  style="width:24px;"> [Align vertical center](Spreadsheet_AlignVCenter.md): align the contents of selected cells to the center vertically.
-   <img alt="" src=images/Spreadsheet_AlignBottom.svg  style="width:24px;"> [Align bottom](Spreadsheet_AlignBottom.md): top align the contents of selected cells to the bottom.

-   <img alt="" src=images/Spreadsheet_StyleBold.svg  style="width:24px;"> [Style bold](Spreadsheet_StyleBold.md): set the contents of selected cells to bold.
-   <img alt="" src=images/Spreadsheet_StyleItalic.svg  style="width:24px;"> [Style italic](Spreadsheet_StyleItalic.md): set the contents of selected cells to italic.
-   <img alt="" src=images/Spreadsheet_StyleUnderline.svg  style="width:24px;"> [Style underline](Spreadsheet_StyleUnderline.md): set the contents of selected cells to underlined.

-   <img alt="" src=images/Spreadsheet_SetAlias.svg  style="width:24px;"> [Set alias](Spreadsheet_SetAlias.md): set alias for selected cells.

-    **Black**and **White** set the foreground and the background colors of the selected cells.

-   Context-menu of the spreadsheet rows and columns: right-click onto the header of a row or column to insert a new row above or a new column at the left, or to delete the current row/column. You can also select several rows or columns to delete them.<small>(v0.20)</small>  You can also select where the the new rows/columns will be inserted. Furthermore, to insert for example 3 new columns at once, select 3 columns and use the context-menu that will now offer to insert 3 columns.

## Spreadsheet editing 

As noted above under Tools, right click on a row or column header produces a pulldown menu that allows you to delete the row/column or insert a new blank one. Formula references to cells that get moved by these operations get patched to refer to the new location, You will get a warning and a request to confirm if a row or column deletion would abolish a reference that\'s used in your model.

Cut/copy/paste can be used to edit data. Cut and copy will both operate on single cells, rows, columns, rectangles, or indeed any selection group of cells you set up. Cut clears the content of selected cells; both cut and copy stash the cell content in an internal paste buffer. A paste operation writes the buffered data in such a way that the content of the uppermost-leftmost cell of the buffered set is dropped in the cell where the cursor is when you paste; other buffered content is dropped where it will have the same relationship to that target as it originally did to the upper-left cell of your cut/paste set.

An important caveat: Cut/copy/paste operations do *not* fix up formula references. If you move the content of a cell, formulas which referred to the old location will break. If the old location becomes empty, the breakage will become visible as the expression evaluator will display \#ERR in dependent cells. Properties are also not carried along.

The Undo key can be use to back out any of these operations. However, it undoes a cell at a time - thus, multiple Undos may be requited to back out a single copy or paste.

## Cell properties 

The properties of a spreadsheet cell can be edited with a right-click on a cell. The following dialog pops up:

![](images/SpreadsheetCellPropDialog.png )

As indicated by the tabs, the following properties can be changed:

-   Color: Text color and background color
-   Alignment: Text horizontal and vertical alignment
-   Style: Text style: bold, italic, underline
-   Units: Display units for this cell. Please read the [Units](#Units.md) section below.
-   Alias: Define an [alias](Spreadsheet_SetAlias.md) for this cell. This alias can be used in cell formulas and also in general [expressions](Expressions.md); see section [Spreadsheet data in expressions](#Spreadsheet_data_in_expressions.md) for more information.

## Cell expressions 

A spreadsheet cell may contain arbitrary text or an expression. Technically, expressions must start with an equals \'=\' sign. However, the spreadsheet attempts to be intelligent; if you enter what looks like an expression without the leading \'=\', one will be added automatically.

Cell expressions may contain numbers, functions, references to other cells, and references to properties of the model (But see [Current limitations](#Current_limitations.md) below). Cells are referenced by their column (CAPITAL letter) and row (number). A cell may also be referenced by its [alias-name](#alias_name.md) (below). Example: B4 + A6

**Note:** Cell expressions are treated by FreeCAD as programming code. Therefore, when you edit a cell the content you see that it is not following your display settings:

-   the decimal separator is always a dot
-   the number of displayed decimals can differ from your [preferences settings](Preferences_Editor#Units.md)

References to objects in the model are explained under [References to CAD-data](#References_to_CAD-data.md) below. Using spreadsheet cell values to define model properties are explained under [Spreadsheet data in expressions](#Spreadsheet_data_in_expressions.md) below. For more information on expressions and the available functions, see [Expressions](Expressions.md).

## Interaction between spreadsheets and the CAD model 

Data in the cells of a spreadsheet may be used in CAD model parameter expressions. Thus, a spreadsheet may be used as the source for parameter values used throughout a model, effectively gathering the values in one place. When values are changed in the spreadsheet, they are propagated throughout the model.

Similarly, properties from CAD model objects may be used in expressions in spreadsheet cells. This allows use of object properties like volume or area in the spreadsheet. If the name of an object in the CAD model is changed, the change will automatically be propagated to any references in spreadsheet expressions using the name which was changed.

More than one spreadsheet may be used in a document. A spreadsheet can be identified using either its name or its label.

FreeCAD will automatically assign a unique name to a spreadsheet when it is created. These names follow the pattern `Spreadsheet`, `Spreadsheet001`, `Spreadsheet002` and so on. The name can not be changed manually, and it is not visible in the properties of the spreadsheet. It can be used to refer to the spreadsheet in an [Expression](Expressions.md) (see [Spreadsheet data in expressions](#Spreadsheet_data_in_expressions.md) below.)

The label of a spreadsheet is automatically set to the name of the spreadsheet upon creation. Unlike the name, the label can be changed, for example in the properties panel or using the context menu action Rename. Note that the label of a spreadsheet within a document has to be unique; if you try to change the label to a label already used by another spreadsheet, FreeCAD will not accept the new label.

FreeCAD checks for cyclic dependencies. See [Current limitations](Spreadsheet_Workbench#Current_limitations.md).

### References to CAD-data 

As indicated above, one can reference data from the CAD model in spreadsheet expressions.

Computed expressions in spreadsheet cells start with an equals (\'=\') sign. However, the spreadsheet entry mechanism attempts to be smart. An expression may be entered without the leading \'=\'; if the string entered is a valid expression, an \'=\' is automatically added when the final **Enter** is typed. If the string entered is not a valid expression (often the result of entering something with the wrong case, e.g. \"MyCube.length\" instead of \"MyCube.Length\"), no leading \'=\' is added and it is treated as simply a text string.

**Note:** The above behavior (auto insert of \'=\') has some unpleasant ramifications:

-   If you want to keep a column of names corresponding to the [alias-names](#alias_name.md) in an adjacent column of values, you must enter the name in the label column *before* giving the cell in the value column its alias-name. Otherwise, when you enter the alias-name in the label column the spreadsheet will assume it is an expression and change it to \"=\"; and the displayed text will be the value from the  cell.
-   If you make an error when entering the name in the label column and wish to correct it, you cannot simply change it to the alias-name. Instead, you must first change the alias-name to something else, then fix the text name in the label column, then change the alias-name in the value column back to its original.

One way to side-step these issues is to prefix text labels corresponding to alias-names with a fixed string, thereby making them different. Note that \"\_\" will not work, as it is converted to \"=\". However, a blank, while invisible, will work.

The following table shows some examples assuming the model has a feature named \"MyCube\":

  CAD-Data                                     Cell in Spreadsheet            Result
  -------------------------------------------- ------------------------------ ----------------------------------
  Parametric Length of a Part-Workbench Cube   =MyCube.Length                 Length with units mm
  Volume of the Cube                           =MyCube.Shape.Volume           Volume in mm³ without units
  Type of the Cube-shape                       =MyCube.Shape.ShapeType        String: Solid
  Label of the Cube                            =MyCube.Label                  String: MyCube
  x-coordinate of center of mass of the Cube   =MyCube.Shape.CenterOfMass.x   x-coordinate in mm without units

### Spreadsheet data in expressions 

In order to use spreadsheet data in other parts of FreeCAD, you will usually create an [Expression](Expressions.md) that refers to the spreadsheet and the cell that contains the data you want to use. You can identify spreadsheets by name or by label, and you can identify the cells by position or by alias. Autocompletion is available for all forms of referencing.

+------------------+-----------------------------------------------------+--------------------------------------------------------+
|                  | Spreadsheet by Name                                 | Spreadsheet by Label                                   |
+==================+=====================================================+========================================================+
| Cell by Position |                                      |                                         |
|                  | `<nowiki>=Spreadsheet042.B5</nowiki>`      | `<nowiki>=<<MySpreadsheet>>.B5</nowiki>`      |
|                  |                                                  |                                                     |
+------------------+-----------------------------------------------------+--------------------------------------------------------+
| Cell by Alias    |                                      |                                         |
|                  | `<nowiki>=Spreadsheet042.MyAlias</nowiki>` | `<nowiki>=<<MySpreadsheet>>.MyAlias</nowiki>` |
|                  |                                                  |                                                     |
+------------------+-----------------------------------------------------+--------------------------------------------------------+


<div class="mw-collapsible mw-collapsed">

The recommended way to refer to spreadsheet data is to use the spreadsheet label and cell alias name. For a more in-depth explanation of the pros and cons of the addressing modes, see the expanded section below.


<div class="mw-collapsible-content">

Using the spreadsheet label has the advantage that it can be freely changed to describe the contents of the spreadsheet. It is also easier to identify the spreadsheet that is being used since the text in the expression matches the label shown in the model and property views. If you decide to change the label of a spreadsheet, existing references to the contents of the spreadsheet will be updated, so you won\'t break your expressions by renaming the spreadsheet. The internal name of the spreadsheet is not readily available anywhere except within the expression editor, so if you use the internal name and later decide to rename the spreadsheets, you might have a hard time tracing your expression data back to its source.

Be aware that when you create a new spreadsheet, the name and the label are the same, so it is easy to accidentally use the spreadsheet name instead of the label. A simple way to avoid this is to give the spreadsheet a meaningful name before starting to use it in expressions.

While you may use the row and column number in an expression to reference a cell, best practice is to give the cell an alias name and use that. See [Cell Properties](#Cell_Properties.md) above on how to set the alias. For example, if the data in cell B1 contained the length parameter for an object, an alias name of `MyObject_Length` would allow the value to be referred to as `<<MyParams>>.MyObject_Length` instead of `Spreadsheet.B1`. Besides being much easier to read and understand, alias names are also much easier to change if you decide to adjust the structure of your spreadsheet. Using an alias also has the advantage that it is reasier to see which cells are used to control other parts of the document. Note that FreeCAD will automatically adjust the positional references in expressions if you insert or remove rows and columns in the spreadsheet, so even if you use row and column numbers in an expression, you can insert rows and columns without breaking the references to the surrounding cells.


</div>


</div>

### Complex models and recomputes 

Editing a spreadsheet will trigger a recompute of the 3D model, even if the changes do not affect the model. For a complex model a recompute can take a long time, and having to wait after every single edit is of course quite annoying.

There are three solutions to deal with this:

1.  Temporarily skip recomputes:
    -   In the [Tree view](Tree_view.md) right-click the <img alt="" src=images/Document.svg  style="width:24px;"> document that contains the spreadsheet.
    -   Select the **Skip recomputes** option from the context menu.
    -   There is a big disadvantage to this solution. New values entered in the spreadsheet will not be displayed until the document is recomputed. Instead `#PENDING` is shown.
    -   You can either recompute manually, using the [Std Refresh](Std_Refresh.md) command, or disable **Skip recomputes** when you are done editing.
2.  Use a macro to automatically skip recomputes while editing a spreadsheet:
    -   Download and run [skipSheet.FCMacro](https://forum.freecadweb.org/viewtopic.php?f=8&t=48600#p419301).
    -   This solution saves a few steps compared to the first solution, but also has the mentioned disadvantage.
3.  Put the spreadsheet in a separate [FreeCAD file](File_Format_FCStd.md):
    -   You can reference spreadsheet data from an external {{FileName|.FCStd}} file with this syntax: `<nowiki>=NameOfFile#<<MySpreadsheet>>.MyAlias</nowiki>`.
    -   The advantage of having the spreadsheet in another file over switching off recomputes is that the spreadsheet itself does get recomputed.
    -   The disadvantage is that the model won\'t automatically recompute after changes to the spreadsheet.
    -   In the scenario where you first open the \'spreadsheet\' file, change one or more values and then open the \'model\' file, there won\'t be any indication that the model needs to be recomputed. But if both files are open the [Std Refresh](Std_Refresh.md) icon will update correctly for the \'model\' file after changes to the \'spreadsheet\' file.

## Units

The Spreadsheet has a notion of dimension (units) associated with cell values. A number entered without an associated unit has no dimension. The unit should be entered immediately following the number value, with no intervening space. If a number has an associated unit, that unit will be used in all calculations. For example, the multiplication of two lengths with the unit mm gives an area with the unit mm².

If a cell contains a value which represents a dimension, it should be entered with its associated unit. While in many simple cases one can get by with a dimensionless value, it is unwise to not enter the unit. If a value representing a dimension is entered without its associated unit, there are some sequences of operations which cause FreeCAD to complain of incompatible units in an expression when it appears the expression should be valid. (This may be better understood by viewing [this thread](https://forum.freecadweb.org/viewtopic.php?f=3&t=34713&p=292455#p292438) in the FreeCAD forums.)

You can change the units displayed for a cell value using the properties dialog [units tab](#units_tab.md) (above). This does not change the value contained in the cell; it only converts the existing value for display. The value used for calculations does not change, and the results of formulas using the value do not change. For example, a cell containing the value \"5.08cm\" can be displayed as \"2in\" by changing the units tab value to \"in\".

A dimensionless number cannot be changed to a number with a unit by the cell properties dialog. One can put in a unit string, and that string will be displayed; but the cell still contains a dimensionless number. In order to change a dimensionless value to a value with a dimension, the value itself must be re-entered with its associated unit.

Occasionally it may be desirable to get rid of a dimension in an expression. This can be done by multiplying by 1 with a reciprocal unit.

## Importing and exporting 

Sheets can be imported and exported to the [csv](https://en.wikipedia.org/wiki/Comma-separated_values) format which can also be read and written by most other spreadsheet applications such as Microsoft Excel or LibreOffice Calc. When importing files into FreeCAD, the delimiter (the character that is used to separate columns) must be the TAB character (this can be set when exporting from other applications). The import of a CSV-file is available from the menu **Spreadsheet → Import Spreadsheet** or by clicking on the icon <img alt="" src=images/SpreadsheetImport.svg  style="width:24px;">. This import function does not open Excel files or any other spreadsheet format.

Spreadsheets in Excel-format \"xlsx\" can be imported via the menu **File → Import...**. Excel-spreadsheets can also be opened by clicking in the menu **File → Open...** or by clicking on the icon <img alt="" src=images/Document-open.svg  style="width:24px;">. In these cases a new document with a spreadsheet inside is created. The following features are supported:

-   all functions that are also available in the FreeCAD spreadsheet. Other functions give an error in the corresponding cell after the import.
-   Alias names for cells
-   More than one \"Sheet\" in the Excel-spreadsheet. In this case one FreeCAD spreadsheet is created for each Excel sheet.

Other functionality is not imported into the FreeCAD spreadsheet. The Excel-import is <small>(v0.17)</small>  of FreeCAD.

## Printing

To handle the page setup necessary for printing, FreeCAD spreadsheets are printed by inserting them into a [TechDraw Spreadsheet View](TechDraw_SpreadsheetView.md).

## Current limitations 

FreeCAD checks for cyclic dependencies. By design, that check stops at the level of the spreadsheet object. As a consequence, you should not have a spreadsheet which contains both cells whose values are used to specify parameters to the model, and cells whose values use output from the model. For example, you cannot have cells specifying the length, width, and height of an object, and another cell which references the total volume of the resulting shape. This restriction can be surmounted by having two spreadsheets: one used as a data-source for input parameters to the model and the other used for calculations based on resultant geometry-data.

## Scripting basics 


```python
import Spreadsheet
sheet = App.ActiveDocument.addObject("Spreadsheet::Sheet","MySpreadsheet")
sheet.Label = "Dimensions"

sheet.set('A1','10mm')
sheet.recompute()
sheet.get('A1')

sheet.setAlias('B1','Diameter')
sheet.set('Diameter','20mm')
sheet.recompute()
sheet.get('Diameter')
```





{{Spreadsheet_Tools_navi

}} 

[Category:Workbenches](Category:Workbenches.md)
