# <img alt="El icono del Ambiente de trabajo Hoja de cálculo" src=images/Workbench_Spreadsheet.svg  style="width:64px;"> Spreadsheet Workbench/es

## Introducción

El <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:24px;"> [Ambiente de trabajo de hojas de cálculo](Spreadsheet_Workbench/es.md) permite crear y editar hojas de cálculo, utilizar datos de la hoja de cálculo como parámetros en un modelo, rellenar la hoja de cálculo con datos recuperados de un modelo, realizar cálculos y exportar los datos a otras aplicaciones de hojas de cálculo como LibreOffice o Microsoft Excel.


{{TOCright}}

<img alt="" src=images/Spreadsheet_screenshot.jpg  style="width:600px;"> 
*Una hoja de cálculo con determinadas celdas rellenas de texto y cantidades*

## Herramientas

-   <img alt="" src=images/Spreadsheet_CreateSheet.svg  style="width:24px;"> [Crear hoja](Spreadsheet_CreateSheet/es.md): crea una nueva hoja de cálculo.

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


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Spreadsheet_SetAlias.svg  style="width:24px;"> [Establecer alias](Spreadsheet_SetAlias/es.md): establece un alias para las celdas seleccionadas.


</div>


<div class="mw-translate-fuzzy">

-    **Negro**y **Blanco** establecen los colores de primer plano y de fondo de las celdas seleccionadas.


</div>

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

## Propiedades de la celda 

Las propiedades de una celda de la hoja de cálculo pueden editarse haciendo clic con el botón derecho del ratón en una celda. Aparece el siguiente cuadro de diálogo:

![](images/SpreadsheetCellPropDialog.png )

Como se indica en las pestañas, se pueden modificar las siguientes propiedades:

-   Color: Color del texto y del fondo
-   Alineación: Alineación horizontal y vertical del texto
-   Estilo: Estilo del texto: negrita, cursiva, subrayado
-   Unidades: Muestra las unidades para esta celda. Por favor, lea la sección [Unidades](#Unidades.md) más abajo.
-   Alias: Define un [alias](Spreadsheet_SetAlias/es.md) para esta celda. Este alias se puede utilizar en las fórmulas de las celdas y también en las [expresiones](Expressions/es.md) generales; consulte la sección [Datos de la hoja de cálculo en las expresiones](#Datos_de_hoja_en_expresiónes.md) para obtener más información.

## Expresiones de la celda 

Una celda de la hoja de cálculo puede contener un texto arbitrario o una expresión. Técnicamente, las expresiones deben comenzar con un signo igual \'=\'. Sin embargo, la hoja de cálculo intenta ser inteligente; si se introduce lo que parece una expresión sin el \'=\' inicial, se añadirá uno automáticamente.

Las expresiones de celdas pueden contener números, funciones, referencias a otras celdas y referencias a propiedades del modelo (Pero vea [Limitaciones actuales](#Limitaciones_actuales.md) más abajo). Las celdas se referencian por su columna (letra MAYÚSCULA) y fila (número). Una celda también puede ser referenciada por su [nombre\_alias](#nombre_alias.md) (más abajo). Ejemplo: B4 + A6

**Nota:** Las expresiones de celda son tratadas por FreeCAD como código de programación. Por lo tanto, cuando editas una celda el contenido ves que no sigue su configuración de visualización:

-   el separador decimal es siempre un punto
-   el número de decimales mostrados puede diferir de tu configuración de [ajustes de preferencias](Preferences_Editor/es#Unidades.md)

Las referencias a objetos en el modelo se explican en [Referencias a datos CAD](#Referencias_a_datos_CAD.md) más abajo. El uso de los valores de las celdas de la hoja de cálculo para definir las propiedades del modelo se explica en [Datos de la hoja de cálculo en las expresiones](#Hoja_de_datos_en_expresiones.md) más adelante. Para más información sobre las expresiones y las funciones disponibles, véase [Expresiones](Expressions/es.md).

## Interacción entre las hojas de cálculo y el modelo CAD 

Data in the cells of a spreadsheet may be used in CAD model parameter expressions. Thus, a spreadsheet may be used as the source for parameter values used throughout a model, effectively gathering the values in one place. When values are changed in the spreadsheet, they are propagated throughout the model.

Similarly, properties from CAD model objects may be used in expressions in spreadsheet cells. This allows use of object properties like volume or area in the spreadsheet. If the name of an object in the CAD model is changed, the change will automatically be propagated to any references in spreadsheet expressions using the name which was changed.

More than one spreadsheet may be used in a document. A spreadsheet can be identified using either its name or its label.

FreeCAD will automatically assign a unique name to a spreadsheet when it is created. These names follow the pattern `Spreadsheet`, `Spreadsheet001`, `Spreadsheet002` and so on. The name can not be changed manually, and it is not visible in the properties of the spreadsheet. It can be used to refer to the spreadsheet in an [Expression](Expressions.md) (see [Spreadsheet data in expressions](#Spreadsheet_data_in_expressions.md) below.)

The label of a spreadsheet is automatically set to the name of the spreadsheet upon creation. Unlike the name, the label can be changed, for example in the properties panel or using the context menu action Rename. Note that the label of a spreadsheet within a document has to be unique; if you try to change the label to a label already used by another spreadsheet, FreeCAD will not accept the new label.

FreeCAD checks for cyclic dependencies. See [Current limitations](Spreadsheet_Workbench#Current_limitations.md).

### Referencias a los datos CAD 

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

### Datos de la hoja de cálculo en expresiones 

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

### Modelos complejos y recálculos 

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

## Unidades

The Spreadsheet has a notion of dimension (units) associated with cell values. A number entered without an associated unit has no dimension. The unit should be entered immediately following the number value, with no intervening space. If a number has an associated unit, that unit will be used in all calculations. For example, the multiplication of two lengths with the unit mm gives an area with the unit mm².

If a cell contains a value which represents a dimension, it should be entered with its associated unit. While in many simple cases one can get by with a dimensionless value, it is unwise to not enter the unit. If a value representing a dimension is entered without its associated unit, there are some sequences of operations which cause FreeCAD to complain of incompatible units in an expression when it appears the expression should be valid. (This may be better understood by viewing [this thread](https://forum.freecadweb.org/viewtopic.php?f=3&t=34713&p=292455#p292438) in the FreeCAD forums.)

You can change the units displayed for a cell value using the properties dialog [units tab](#units_tab.md) (above). This does not change the value contained in the cell; it only converts the existing value for display. The value used for calculations does not change, and the results of formulas using the value do not change. For example, a cell containing the value \"5.08cm\" can be displayed as \"2in\" by changing the units tab value to \"in\".

A dimensionless number cannot be changed to a number with a unit by the cell properties dialog. One can put in a unit string, and that string will be displayed; but the cell still contains a dimensionless number. In order to change a dimensionless value to a value with a dimension, the value itself must be re-entered with its associated unit.

Occasionally it may be desirable to get rid of a dimension in an expression. This can be done by multiplying by 1 with a reciprocal unit.

## Importación y exportación 

### CSV format 

FreeCAD spreadsheets can be imported and exported to the [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) format which can also be read and written by most other spreadsheet applications such as Microsoft Excel or LibreOffice Calc. See [Spreadsheet Import](Spreadsheet_Import.md) and [Spreadsheet Export](Spreadsheet_Export.md) for more information.

### XLSX format 

Spreadsheets in the Excel-format XLSX can be imported with the [Std Import](Std_Import.md) command or the [Std Open](Std_Open.md) command. The following features are supported:

-   All functions that are also available in the FreeCAD spreadsheet. Other functions give an error in the corresponding cell after import.
-   Alias names for cells.
-   More than one sheet in the Excel-spreadsheet. In this case one FreeCAD spreadsheet is created for each Excel sheet.

Other functionality is not imported into the FreeCAD spreadsheet.

## Impresión

To handle the page setup necessary for printing, FreeCAD spreadsheets are printed by inserting them into a [TechDraw Spreadsheet View](TechDraw_SpreadsheetView.md).

## Limitaciones actuales 

FreeCAD checks for cyclic dependencies. By design, that check stops at the level of the spreadsheet object. As a consequence, you should not have a spreadsheet which contains both cells whose values are used to specify parameters to the model, and cells whose values use output from the model. For example, you cannot have cells specifying the length, width, and height of an object, and another cell which references the total volume of the resulting shape. This restriction can be surmounted by having two spreadsheets: one used as a data-source for input parameters to the model and the other used for calculations based on resultant geometry-data.

## Guión básicos 


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

[<img src="images/Property.png" style="width:16px"> Workbenches](Category_Workbenches.md)

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Spreadsheet Workbench/es
