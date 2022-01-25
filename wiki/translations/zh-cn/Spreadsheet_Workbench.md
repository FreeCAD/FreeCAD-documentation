# <img alt="Spreadsheet workbench icon" src=images/Workbench_Spreadsheet.svg  style="width:64px;"> Spreadsheet Workbench/zh-cn

## Introduction


<div class="mw-translate-fuzzy">


<small>(v0.15)</small> 

电子表格工作台允许您创建和编辑电子表格、执行计算以及从模型中检索数据, 并将其数据导出到其他电子表格应用程序 (如 LibreOffice 或 Microsoft Excel)。


</div>


<div class="mw-translate-fuzzy">

![](images/Spreadsheet_screenshot.jpg )


</div>

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

In FreeCAD version 0.19 and earlier rows are inserted above the selected rows, and colomns on the left of the selected columns. In FreeCAD version 0.20 you can specify the insertion side.

Note that removing rows or columns with data can break the spreadsheet and your model if it relies on the spreadheet. You are not prewarned if this happens.

## Cut and copy-paste cells 

Cut and copy-paste operations can be used on cells in FreeCAD spreadsheets. You can use the normal shortcuts for these operations: **Ctrl**+**X**, **Ctrl**+**C** and **Ctrl**+**V** respectively. To select multiple cells hold down the **Ctrl** key while selecting, or hold down the left mouse button and drag to select a rectangular cell range.

The cut and copy operations store the contents and properties of the cells on the Clipboard. The paste operation writes the data in such a way that the content of the top left cell of the stored data is dropped in the active cell. Other stored content is placed relative to that cell. Formulas are updated accordingly.

Note that removing cells with data can break the spreadsheet and your model if it relies on the spreadheet. You are not prewarned if this happens.

In FreeCAD version 0.19 and earlier there is a bug that can cause FreeCAD to hang if a non-rectangular cell range is pasted. It is advisable to save your work before performing any paste operations.


<div class="mw-translate-fuzzy">

## 单元格的属性


</div>

可以使用右键单击单元格来编辑电子表格单元格的属性。以下对话框弹出:

![](images/SpreadsheetCellPropDialog.png )


<div class="mw-translate-fuzzy">

它有几个选项卡。可以更改以下属性:


</div>


<div class="mw-translate-fuzzy">

-   文本颜色和背景颜色
-   文本水平和垂直对齐 \* 文本样式: 粗体、斜体、下划线
-   此单元格的显示单位。请阅读下面的章节。
-   为此单元格定义别名。此别名可用于单元格公式, 也可以在 FreeCAD 表达式中中使用 <small>(v0.16)</small> 


</div>

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


<div class="mw-translate-fuzzy">

## 对 CAD 数据的引用 


</div>


<div class="mw-translate-fuzzy">

可以在电子表格中使用结构中的数据。 下表显示了一些示例, 假设模型有一个名为 \"立方体\" 的功能 (请注意, 这是功能的内部名称, 而不是用户指定的标签):

  CAD-Data                     在电子表格中调用             结果
    
  零件工作台立方体的参数长度   =Cube.Length                 长度单位 mm
  立方体的体积                 =Cube.Shape.Volume           没有单位 mm³ 体积
  立方体形状的类型             =Cube.Shape.ShapeType        String: Solid
  立方体的标签                 =Cube.Label                  String: Cube
  立方体质量中心的 x 坐标      =Cube.Shape.CenterOfMass.x   无单位 mm 的 x 坐标


</div>

Computed expressions in spreadsheet cells start with an equals (\'=\') sign. However, the spreadsheet entry mechanism attempts to be smart. An expression may be entered without the leading \'=\'; if the string entered is a valid expression, an \'=\' is automatically added when the final **Enter** is typed. If the string entered is not a valid expression (often the result of entering something with the wrong case, e.g. \"MyCube.length\" instead of \"MyCube.Length\"), no leading \'=\' is added and it is treated as simply a text string.

**Note:** The above behavior (auto insert of \'=\') has some unpleasant ramifications:

-   If you want to keep a column of names corresponding to the [alias-names](#alias_name.md) in an adjacent column of values, you must enter the name in the label column *before* giving the cell in the value column its alias-name. Otherwise, when you enter the alias-name in the label column the spreadsheet will assume it is an expression and change it to \"=\"; and the displayed text will be the value from the  cell.
-   If you make an error when entering the name in the label column and wish to correct it, you cannot simply change it to the alias-name. Instead, you must first change the alias-name to something else, then fix the text name in the label column, then change the alias-name in the value column back to its original.

One way to side-step these issues is to prefix text labels corresponding to alias-names with a fixed string, thereby making them different. Note that \"\_\" will not work, as it is converted to \"=\". However, a blank, while invisible, will work.

The following table shows some examples assuming the model has a feature named \"MyCube\":

  CAD-Data                                     Cell in Spreadsheet            Result
    
  Parametric Length of a Part-Workbench Cube   =MyCube.Length                 Length with units mm
  Volume of the Cube                           =MyCube.Shape.Volume           Volume in mm³ without units
  Type of the Cube-shape                       =MyCube.Shape.ShapeType        String: Solid
  Label of the Cube                            =MyCube.Label                  String: MyCube
  x-coordinate of center of mass of the Cube   =MyCube.Shape.CenterOfMass.x   x-coordinate in mm without units


<div class="mw-translate-fuzzy">

## 在表达式中的电子表格数据


</div>

In order to use spreadsheet data in other parts of FreeCAD, you will usually create an [Expression](Expressions.md) that refers to the spreadsheet and the cell that contains the data you want to use. You can identify spreadsheets by name or by label, and you can identify the cells by position or by alias. Autocompletion is available for all forms of referencing.

++++
|                  | Spreadsheet by Name                                 | Spreadsheet by Label                                   |
+==================+=====================================================+========================================================+
| Cell by Position |                                      |                                         |
|                  | `<nowiki>=Spreadsheet042.B5</nowiki>`      | `<nowiki>=<<MySpreadsheet>>.B5</nowiki>`      |
|                  |                                                  |                                                     |
++++
| Cell by Alias    |                                      |                                         |
|                  | `<nowiki>=Spreadsheet042.MyAlias</nowiki>` | `<nowiki>=<<MySpreadsheet>>.MyAlias</nowiki>` |
|                  |                                                  |                                                     |
++++


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

## 单位


<div class="mw-translate-fuzzy">

电子表格使用单位。如果一个数字有一个单位, 这个单位将用于所有的计算。 两个单位 mm 的长度相乘将会赋一个以 mm² 为单位的值给区域。


</div>

If a cell contains a value which represents a dimension, it should be entered with its associated unit. While in many simple cases one can get by with a dimensionless value, it is unwise to not enter the unit. If a value representing a dimension is entered without its associated unit, there are some sequences of operations which cause FreeCAD to complain of incompatible units in an expression when it appears the expression should be valid. (This may be better understood by viewing [this thread](https://forum.freecadweb.org/viewtopic.php?f=3&t=34713&p=292455#p292438) in the FreeCAD forums.)


<div class="mw-translate-fuzzy">

您可以在对话框中将长度单位从 mm 切换到英寸, 然后在单元格上右键单击。 单元格现在将显示长度 (以英寸为单位)。用于计算的值不会更改。 当输入的显示单位更改时, 使用该值的公式的结果不会更改。结果仍按 mm 的长度计算。


</div>


<div class="mw-translate-fuzzy">

单元格属性对话框不能在带单位的数字中更改一个没有单位的数字。 没有单位的数字可以放在一个单位字符串, 这也将显示, 但单元格仍然只包含一个数字没有单位。


</div>


<div class="mw-translate-fuzzy">

有时是刻意, 以摆脱一个单位。这只能通过乘以1与一个倒数单位来完成。


</div>

## 导入与导出

### CSV format 


<div class="mw-translate-fuzzy">

可以将工作表导入并导出到 [csv](https://en.wikipedia.org/wiki/Comma-separated_values) 格式, 这些形式也可以由大多数其他电子表格应用程序 (如 Microsoft Excel 或 LibreOffice 计算器) 读取和写入。将文件导入 FreeCAD 时, 分隔符 (用于分隔列的字符) 必须是 TAB 字符 (可以在从其他应用程序导出时设置)。


</div>

### XLSX format 


<div class="mw-translate-fuzzy">

Excel 中的电子表格-格式 \"xlsx \" 可以导入到 FreeCAD 文档中。Excel 电子表格也可以通过 FreeCAD 打开。在这种情况下将创建一个带有电子表格的新文档。支持以下功能:


</div>


<div class="mw-translate-fuzzy">

-   FreeCAD 电子表格中还提供的所有功能。其他函数在导入后的相应单元格中会出现错误。
-   单元格的别名
-   在 Excel 工作表中有多个表。在这种情况下, 将创建更多的 FreeCAD 电子表格。


</div>


<div class="mw-translate-fuzzy">

其他功能不会被导入到 FreeCAD 电子表格中。Excel 导入是 FreeCAD <small>(v0.17)</small>  的功能。


</div>

## Printing

To handle the page setup necessary for printing, FreeCAD spreadsheets are printed by inserting them into a [TechDraw Spreadsheet View](TechDraw_SpreadsheetView.md).


<div class="mw-translate-fuzzy">

## 当前限制


</div>


<div class="mw-translate-fuzzy">

这是不可能提供一个几何的数据, 例如一个长度, 在电子表格和检索在同一个电子表格中生成形状的体积。这将创建一个循环引用。这是一个设计决定。但是, 可以使用两个不同的电子表格: 一个是几何图形的数据源, 另一个用于报告几何数据。


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


<div class="mw-translate-fuzzy">





</div>


{{Spreadsheet_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Spreadsheet Workbench/zh-cn
