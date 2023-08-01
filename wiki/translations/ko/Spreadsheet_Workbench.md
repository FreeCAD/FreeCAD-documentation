# <img alt="Spreadsheet workbench icon" src=images/Workbench_Spreadsheet.svg  style="width:64px;"> Spreadsheet Workbench/ko

## Introduction

The <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:24px;"> [Spreadsheet Workbench](Spreadsheet_Workbench.md) allows you to create and edit spreadsheets, use data from the spreadsheet as parameters in a model, fill the spreadsheet with data retrieved from a model, perform calculations, and export the data to other spreadsheet applications such as LibreOffice or Microsoft Excel.


{{TOCright}}

<img alt="" src=images/Spreadsheet_screenshot.jpg  style="width:600px;"> 
*A spreadsheet with certain cells filled with text and quantities*

## Tools

-   <img alt="" src=images/Spreadsheet_CreateSheet.svg  style="width:24px;"> [Create sheet](Spreadsheet_CreateSheet.md): create a new spreadsheet.

-   <img alt="" src=images/Spreadsheet_Import.svg  style="width:24px;"> [Import](Spreadsheet_Import.md): import a CSV file into a spreadsheet.

-   <img alt="" src=images/Spreadsheet_Export.svg  style="width:24px;"> [Export](Spreadsheet_Export.md): export a CSV file from a spreadsheet.

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

-   <img alt="" src=images/Spreadsheet_SetAlias.svg  style="width:24px;"> [Set alias](Spreadsheet_SetAlias.md): set the alias for a selected cell.

-    **Black**and **White** set the foreground and the background colors of selected cells.

## Preferences

-   <img alt="" src=images/Preferences-spreadsheet.svg  style="width:32px;"> [Preferences](Spreadsheet_Preferences.md): the preferences for the Spreadsheet Workbench. <small>(v0.20)</small> 

## Insert and remove rows and columns 

Rows and columns can be inserted or removed by right-clicking a row or column header and selecting the appropriate option from the contex menu. It is possible to select multiple rows or columns first. Either by holding down the **Ctrl** key while selecting the headers, or by holding down the left mouse button and dragging.

In FreeCAD version 0.19 and earlier rows are inserted above the selected rows, and columns on the left of the selected columns. In FreeCAD version 0.20 you can specify the insertion side.

Note that removing rows or columns with data can break the spreadsheet and your model if it relies on the spreadheet. You are not prewarned if this happens.

## Cut and copy-paste cells 

Cut and copy-paste operations can be used on cells in FreeCAD spreadsheets. You can use the normal shortcuts for these operations: **Ctrl**+**X**, **Ctrl**+**C** and **Ctrl**+**V** respectively. To select multiple cells hold down the **Ctrl** key while selecting, or hold down the left mouse button and drag to select a rectangular cell range.

The cut and copy operations store the contents and properties of the cells on the Clipboard. The paste operation writes the data in such a way that the content of the top left cell of the stored data is dropped in the active cell. Other stored content is placed relative to that cell. Formulas are updated accordingly.

Note that removing cells with data can break the spreadsheet and your model if it relies on the spreadheet. You are not prewarned if this happens.

In FreeCAD version 0.19 and earlier there is a bug that can cause FreeCAD to hang if a non-rectangular cell range is pasted. It is advisable to save your work before performing any paste operations.

## Cell properties 

The properties of a spreadsheet cell can be edited by right-clicking the cell and selecting **Properties...** from the context menu. The following dialog pops up:

![](images/SpreadsheetCellPropDialog.png )

As indicated by the tabs, the following properties can be changed:

-   Color: Text color and background color
-   Alignment: Text horizontal and vertical alignment
-   Style: Text style: bold, italic, underline
-   Units: Display units for this cell. Please read the [Units](#Units.md) section below.
-   Alias: Define an [alias](Spreadsheet_SetAlias.md) for this cell. This alias can be used in cell formulas and also in general [expressions](Expressions.md); see section [Spreadsheet data in expressions](#Spreadsheet_data_in_expressions.md) for more information.

## Cell expressions 

A spreadsheet cell may contain a number, a text or an expression. Expressions must start with an equal sign \'=\'.

Cell expressions may contain numbers, functions, references to other cells, and references to properties of the model (But see [Current limitations](#Current_limitations.md) below). A cell can be referenced by its address (CAPITAL column letter + row number, e.g. B4) or by its [alias](Spreadsheet_SetAlias.md).

**Note:** Cell expressions are treated by FreeCAD as programming code. Therefore, when you edit a cell the content you see may not follow your display settings:

-   The decimal separator is always a dot. But commas can also be used when entering values.
-   The number of displayed decimals can differ from your [preferences settings](Preferences_Editor#Units.md).

References to objects in the model are explained under [References to CAD-data](#References_to_CAD-data.md) below. Using spreadsheet cell values to define model properties are explained under [Spreadsheet data in expressions](#Spreadsheet_data_in_expressions.md) below. For more information on expressions and the available functions, see [Expressions](Expressions.md).

## Interaction between spreadsheets and the CAD model 

Data in the cells of a spreadsheet may be used in CAD model parameter expressions. Thus, a spreadsheet may be used as the source for parameter values used throughout a model, effectively gathering the values in one place. When values are changed in the spreadsheet, they are propagated throughout the model.

Similarly, properties from CAD model objects may be used in expressions in spreadsheet cells. This allows use of object properties like volume or area in the spreadsheet. If the name of an object in the CAD model is changed, the change will automatically be propagated to any references in spreadsheet expressions using the name which was changed.

More than one spreadsheet may be used in a document. A spreadsheet can be identified using either its name or its label.

FreeCAD will automatically assign a unique name to a spreadsheet when it is created. These names follow the pattern `Spreadsheet`, `Spreadsheet001`, `Spreadsheet002` and so on. The name can not be changed, and it is not visible in the properties of the spreadsheet. It can be used to refer to the spreadsheet in an [Expression](Expressions.md) (see [Spreadsheet data in expressions](#Spreadsheet_data_in_expressions.md) below.)

The label of a spreadsheet is automatically set to the name of the spreadsheet upon creation. Unlike the name, the label can be changed, for example in the properties panel or using the context menu action Rename. By default FreeCAD does not accept duplicate labels, but there is a [preference](Preferences_Editor#Document.md) to override this. Spreadsheets with duplicate labels in the same document cannot be referenced by their label.

FreeCAD checks for cyclic dependencies. See [Current limitations](Spreadsheet_Workbench#Current_limitations.md).

### References to CAD-data 

As indicated above, one can reference data from the CAD model in spreadsheet expressions.

The following table shows some examples assuming the model has a feature named \"MyCube\":

++++
| CAD-Data                                       | Cell in Spreadsheet                                      | Result                         |
+================================================+==========================================================+================================+
| Parametric Length of a Part-Workbench Cube     |                                           | Length with units mm           |
|                                                | {{Incode|<nowiki>=MyCube.Length</nowiki>}}               |                                |
|                                                |                                                       |                                |
++++
| Volume of the Cube                             |                                           | Volume in mm³ without units    |
|                                                | {{Incode|<nowiki>=MyCube.Shape.Volume</nowiki>}}         |                                |
|                                                |                                                       |                                |
++++
| Type of the Cube-shape                         |                                           | String: Solid                  |
|                                                | {{Incode|<nowiki>=MyCube.Shape.ShapeType</nowiki>}}      |                                |
|                                                |                                                       |                                |
++++
| Label of the Cube                              |                                           | String: MyCube                 |
|                                                | {{Incode|<nowiki>=MyCube.Label</nowiki>}}                |                                |
|                                                |                                                       |                                |
++++
| X coordinate of the center of mass of the Cube |                                           | Coordinate in mm without units |
|                                                | {{Incode|<nowiki>=MyCube.Shape.CenterOfMass.x</nowiki>}} |                                |
|                                                |                                                       |                                |
++++

### Spreadsheet data in expressions 

In order to use spreadsheet data in other parts of FreeCAD, you will usually create an [Expression](Expressions.md) that refers to the spreadsheet and the cell that contains the data you want to use. You can identify spreadsheets by name or by label, and you can identify the cells by address or by alias. Autocompletion is available for all forms of referencing.

++++
|                 | Spreadsheet by Name                                 | Spreadsheet by Label                                   |
+=================+=====================================================+========================================================+
| Cell by Address |                                      |                                         |
|                 | `<nowiki>=Spreadsheet042.B5</nowiki>`      | `<nowiki>=<<MySpreadsheet>>.B5</nowiki>`      |
|                 |                                                  |                                                     |
++++
| Cell by Alias   |                                      |                                         |
|                 | `<nowiki>=Spreadsheet042.MyAlias</nowiki>` | `<nowiki>=<<MySpreadsheet>>.MyAlias</nowiki>` |
|                 |                                                  |                                                     |
++++


<div class="mw-collapsible mw-collapsed">

The recommended way to refer to spreadsheet data is to use the spreadsheet label and cell alias name. For a more in-depth explanation of the pros and cons of the referencing modes, see the expanded section below.


<div class="mw-collapsible-content">

Using the spreadsheet label has the advantage that it can be freely changed to describe the contents of the spreadsheet. It is also easier to identify the spreadsheet that is being used since the text in the expression matches the label shown in the model and property views. If you decide to change the label of a spreadsheet, existing references to the contents of the spreadsheet will be updated, so you won\'t break your expressions by renaming the spreadsheet. The internal name of the spreadsheet is not readily available anywhere except within the expression editor, so if you use the internal name and later decide to rename the spreadsheets, you might have a hard time tracing your expression data back to its source.

Be aware that when you create a new spreadsheet, the name and the label are the same, so it is easy to accidentally use the spreadsheet name instead of the label. A simple way to avoid this is to give the spreadsheet a meaningful name before starting to use it in expressions.

While you may use the row and column number in an expression to reference a cell, best practice is to give the cell an alias name and use that. See [Cell properties](#Cell_properties.md) on how to set the alias. For example, if the data in cell B1 contained the length parameter for an object, an alias name of `MyObject_Length` would allow the value to be referred to as `<<MyParams>>.MyObject_Length` instead of `Spreadsheet.B1`. Besides being much easier to read and understand, alias names are also much easier to change if you decide to adjust the structure of your spreadsheet. Using an alias also has the advantage that it is reasier to see which cells are used to control other parts of the document. Note that FreeCAD will automatically adjust the positional references in expressions if you insert or remove rows and columns in the spreadsheet, so even if you use row and column numbers in an expression, you can insert rows and columns without breaking the references to the surrounding cells.


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
    -   You can reference spreadsheet data from an external **.FCStd** file with this syntax: `<nowiki>=NameOfFile#<<MySpreadsheet>>.MyAlias</nowiki>`.
    -   The advantage of having the spreadsheet in another file over switching off recomputes is that the spreadsheet itself does get recomputed.
    -   The disadvantage is that the model won\'t automatically recompute after changes to the spreadsheet.
    -   In the scenario where you first open the \'spreadsheet\' file, change one or more values and then open the \'model\' file, there won\'t be any indication that the model needs to be recomputed. But if both files are open the [Std Refresh](Std_Refresh.md) icon will update correctly for the \'model\' file after changes to the \'spreadsheet\' file.

## Units

The Spreadsheet has a notion of dimension (units) associated with cell values. A number entered without an associated unit has no dimension. The unit should be entered immediately following the number value, with no intervening space. If a number has an associated unit, that unit will be used in all calculations. For example, the multiplication of two lengths with the unit mm gives an area with the unit mm².

If a cell contains a value which represents a dimension, it should be entered with its associated unit. While in many simple cases one can get by with a dimensionless value, it is unwise to not enter the unit. If a value representing a dimension is entered without its associated unit, there are some sequences of operations which cause FreeCAD to complain of incompatible units in an expression when it appears the expression should be valid. (This may be better understood by viewing [this thread](https://forum.freecadweb.org/viewtopic.php?f=3&t=34713&p=292455#p292438) in the FreeCAD forums.)

You can change the units displayed for a cell value using the [Cell properties dialog](#Cell_properties.md). This does not change the value contained in the cell; it only converts the existing value for display. The value used for calculations does not change, and the results of formulas using the value do not change. For example, a cell containing the value \"5.08cm\" can be displayed as \"2in\" by changing the units tab value to \"in\".

A dimensionless number cannot be changed to a number with a unit by the cell properties dialog. One can put in a unit string, and that string will be displayed; but the cell still contains a dimensionless number. In order to change a dimensionless value to a value with a dimension, the value itself must be re-entered with its associated unit.

Occasionally it may be desirable to get rid of a dimension in an expression. This can be done by multiplying by 1 with a reciprocal unit.

## Importing and exporting 

### CSV format 

FreeCAD spreadsheets can be imported and exported to the [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format which can also be read and written by most other spreadsheet applications such as Microsoft Excel or LibreOffice Calc. See [Spreadsheet Import](Spreadsheet_Import.md) and [Spreadsheet Export](Spreadsheet_Export.md) for more information.

### XLSX format 

Spreadsheets in the Excel-format XLSX can be imported with the [Std Import](Std_Import.md) command or the [Std Open](Std_Open.md) command. The following features are supported:

-   All functions that are also available in the FreeCAD spreadsheet. Other functions give an error in the corresponding cell after import.
-   Alias names for cells.
-   More than one sheet in the Excel-spreadsheet. In this case one FreeCAD spreadsheet is created for each Excel sheet.

Other functionality is not imported into the FreeCAD spreadsheet.

## Printing

To handle the page setup necessary for printing, FreeCAD spreadsheets are printed by inserting them into a [TechDraw Spreadsheet View](TechDraw_SpreadsheetView.md).

## Current limitations 

FreeCAD checks for cyclic dependencies when it recomputes. By design, that check stops at the level of the spreadsheet object. As a consequence, you should not have a spreadsheet which contains both cells whose values are used to specify parameters to the model, and cells whose values use output from the model. For example, you cannot have cells specifying the length, width, and height of an object, and another cell which references the total volume of the resulting shape. This restriction can be surmounted by having two spreadsheets: one used as a data-source for input parameters to the model and the other used for calculations based on resultant geometry-data.

## Cell binding 


<small>(v0.20)</small> 

It is possible to bind the content of cells to other spreadsheet cells. This can be useful when dealing with large tables or to get cell content from another spreadsheet.

### Create binding 

To bind, for example, the cell range A3-C4 to the cell range B1-D2:

1.  Select the cell range A3-C4.
2.  Right-click and select **Bind...** from the context menu.
3.  The **Bind Spreadsheet Cells** dialog opens.
4.  Set the range B1-D2 for the **To cells**:
    ![](images/Spreadsheet_binding-dialog.png )
5.  Press **OK**.
6.  Bound cells have a blue border to highlight the binding.
7.  If you now enter something in cell C1, the same will immediately appear in cell B3.

![](images/Spreadsheet_binding-result.png ) 
*The spreadsheet may now look like this*

### Change binding 

1.  Right-click a bound cell (there is no need to highlight the whole bound range) and select **Bind...** from the context menu.
2.  The **Bind Spreadsheet Cells** dialog opens.
3.  Change one or more options. Note that the **Bind cells**, the bound cell range, cannot be changed.
4.  Press **OK**.

### Remove binding 

1.  Right-click a bound cell (there is no need to highlight the whole bound range) and select **Bind...** from the context menu.
2.  The **Bind Spreadsheet Cells** dialog opens.
3.  Press **Unbind**.

### Notes

-   The **Hide dependency of binding** option can be used to prevent problems with cyclic dependencies between spreadsheets. Selecting it is necessary when, for example, cells in *Spreadsheet A* are bound to *Spreadsheet B*, while cells in *Spreadsheet B*, in turn, are bound to some other cells in *Spreadsheet A*. This option should be used with caution:
    -   Hiding dependencies can be dangerous because broken dependencies can damage your FreeCAD file. For example, when you delete a spreadsheet you will not be warned about hidden dependencies.
    -   When you open a document with a spreadsheet containing a hidden dependency, you will get the spreadsheet marked to be recomputed. This is because a cyclic dependency cannot be recomputed automatically. To recompute the [Std Refresh](Std_Refresh.md) tool must be used.
-   The cell binding has a range check and warns you about mismatched ranges. For example binding 1x3 cells to 3x2 cells cannot work because it is unknown which 3 cells of the original 6 cells should be used.
-   You cannot change the cell range of an existing binding. You must first unbind the cells and then create a new binding.
-   The frame color indicating the binding cannot be changed yet.

## Configuration tables 


<small>(v0.20)</small> 

You can use Spreadsheets to create configuration tables with sets of predefined parameters for your model, and then dynamically change which configuration to use. See [this Forum post](https://forum.freecadweb.org/viewtopic.php?f=17&t=42183) if you want to know more about the inner workings of this feature.


<div class="mw-collapsible mw-collapsed toccolours">

Expand this section for a brief tutorial on creating a configuration table.


<div class="mw-collapsible-content">

1.  In a new document, first create a [Std Part](Std_Part.md), then create a [Part Box](Part_Box.md), a [Part Cylinder](Part_Cylinder.md) and a Spreadsheet.
2.  The Box and the Cylinder are automatically placed in the [Std Part](Std_Part.md) container. Manually put the Spreadsheet in the container as well.
3.  In the Spreadsheet enter the content as shown below. Set the alias for B2 as {{Value|width}}, C2 as {{Value|length}} and D2 as {{Value|radius}}:
    ![](images/Spreadsheet_configuration_table_screenshot_4.png )
4.  Bind the [expressions](Expressions.md) {{Value|Spreadsheet.width}} and {{Value|Spreadsheet.length}} to the Box\'s properties **Width** and **Length**, respectively:
    ![](images/Spreadsheet_configuration_table_screenshot_2.png )
5.  Bind the expression {{Value|Spreadsheet.radius}} to the Cylinder\'s property **Radius**. Also change the **Height** of the Cylinder to {{Value|5 mm}} so that it is lower than the Box.
6.  Right-click the cell A2 in the Spreadsheet and select **Configuration table...** from the context menu.
7.  The **Setup Configuration Table** dialog opens.
8.  Enter the following:
    ![](images/Spreadsheet_configuration_table_screenshot_5.png )
9.  Press **OK**.
10. A new property called **Configuration** is be added to the [Std Part](Std_Part.md) container to choose the configuration as shown below:
    ![](images/Spreadsheet_configuration_table_screenshot_6.png )

You can use either a [Std Link](Std_LinkMake.md) or a [PartDesign SubShapeBinder](PartDesign_SubShapeBinder.md) to instantiate a [Variant Instance](https://forum.freecadweb.org/viewtopic.php?f=17&t=42183&p=532130#p532130) of a configurable object with the following steps:

1.  Create a [Std Link](Std_LinkMake.md) to the [Std Part](Std_Part.md) container and set its **Link Copy On Change** property to {{Value|Enabled}}.
2.  Move the Link to a new place by changing its **Placement** so that it is easier to distinguish from the original object.
3.  Select a different **Configuration** for the Link to create a variant instance.

Similar steps apply to a [PartDesign SubShapeBinder](PartDesign_SubShapeBinder.md), except that its property for activating a variant instance is called **Bind Copy On Change**.


</div>


</div>

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



---
![](images/Button_right.svg) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Spreadsheet Workbench/ko
