# Spreadsheet Workbench/es
{{Page_in_progress}}






<img alt="El icono del Ambiente de trabajo Hoja de cálculo" src=images/Workbench_Spreadsheet.svg  style="width:128px;">

## Introducción

El <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:24px;"> [Ambiente de trabajo de hojas de cálculo](Spreadsheet_Workbench/es.md) permite crear y editar hojas de cálculo, utilizar datos de la hoja de cálculo como parámetros en un modelo, rellenar la hoja de cálculo con datos recuperados de un modelo, realizar cálculos y exportar los datos a otras aplicaciones de hojas de cálculo como LibreOffice o Microsoft Excel.


{{TOCright}}

<img alt="" src=images/Spreadsheet_screenshot.jpg  style="width:600px;"> 
*Una hoja de cálculo con determinadas celdas rellenas de texto y cantidades*

## Herramientas

-   <img alt="" src=images/Spreadsheet_CreateSheet.svg  style="width:24px;"> [Crear hoja](Spreadsheet_CreateSheet/es.md): crea una nueva hoja de cálculo.

-   <img alt="" src=images/Spreadsheet_Import.svg  style="width:24px;"> [Importar](Spreadsheet_Import/es.md): importar un archivo de valores separados por tabulaciones a una hoja de cálculo.
-   <img alt="" src=images/Spreadsheet_Export.svg  style="width:24px;"> [Exportar](Spreadsheet_Export/es.md): exportar un archivo de valores separados por tabulaciones de una hoja de cálculo.

-   <img alt="" src=images/Spreadsheet_MergeCells.svg  style="width:24px;"> [Fusionar celdas](Spreadsheet_MergeCells/es.md): fusiona las celdas seleccionadas.
-   <img alt="" src=images/Spreadsheet_SplitCell.svg  style="width:24px;"> [Dividir celda](Spreadsheet_SplitCell/es.md): divide las celdas previamente fusionadas.

-   <img alt="" src=images/Spreadsheet_AlignLeft.svg  style="width:24px;"> [Alinear a la izquierda](Spreadsheet_AlignLeft/es.md): alinea el contenido de las celdas seleccionadas a la izquierda.
-   <img alt="" src=images/Spreadsheet_AlignCenter.svg  style="width:24px;"> [Alinear al centro](Spreadsheet_AlignCenter/es.md): alinea el contenido de las celdas seleccionadas al centro horizontalmente.
-   <img alt="" src=images/Spreadsheet_AlignRight.svg  style="width:24px;"> [Alinear a la derecha](Spreadsheet_AlignRight/es.md): alinea el contenido de las celdas seleccionadas a la derecha.
-   <img alt="" src=images/Spreadsheet_AlignTop.svg  style="width:24px;"> [Alinear arriba](Spreadsheet_AlignTop/es.md): alinea el contenido de las celdas seleccionadas a la parte superior.
-   <img alt="" src=images/Spreadsheet_AlignVCenter.svg  style="width:24px;"> [Alinear centro vertical](Spreadsheet_AlignVCenter/es.md): alinear el contenido de las celdas seleccionadas al centro verticalmente.
-   <img alt="" src=images/Spreadsheet_AlignBottom.svg  style="width:24px;"> [Alinear abajo](Spreadsheet_AlignBottom/es.md): alinea el contenido de las celdas seleccionadas hacia abajo.

-   <img alt="" src=images/Spreadsheet_StyleBold.svg  style="width:24px;"> [Estilo negrita](Spreadsheet_StyleBold/es.md): establece el contenido de las celdas seleccionadas en negrita.
-   <img alt="" src=images/Spreadsheet_StyleItalic.svg  style="width:24px;"> [Estilo cursiva](Spreadsheet_StyleItalic/es.md): establece el contenido de las celdas seleccionadas en cursiva.
-   <img alt="" src=images/Spreadsheet_StyleUnderline.svg  style="width:24px;"> [Estilo subrayado](Spreadsheet_StyleUnderline/es.md): establece el contenido de las celdas seleccionadas como subrayado.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Spreadsheet_SetAlias.svg  style="width:24px;"> [Establecer alias](Spreadsheet_SetAlias/es.md): establece un alias para las celdas seleccionadas.


</div>

-    **Negro**y **Blanco** establecen los colores de primer plano y de fondo de las celdas seleccionadas.

-   Menú contextual de las filas y columnas de la hoja de cálculo: haga clic con el botón derecho del ratón en la cabecera de una fila o columna para insertar una nueva fila arriba o una nueva columna a la izquierda, o para eliminar la fila/columna actual. También puede seleccionar varias filas o columnas para eliminarlas.{{Version/es|0.20}} También puede seleccionar dónde se insertarán las nuevas filas/columnas. Además, para insertar, por ejemplo, 3 nuevas columnas a la vez, seleccione 3 columnas y utilice el menú contextual que ahora le ofrecerá insertar 3 columnas.

## Spreadsheet editing 

As noted above under Tools, right click on a row or column header produces a pulldown menu that allows you to delete the row/column or insert a new blank one. Formula references to cells that get moved by these operations get patched to refer to the new location.

Cut/copy/paste can be used to edit data. Cut and copy will both operate on single cells, rectangles, or indeed any selection group of cells you set up. Cut clears the content of selected cells; both cut and copy store the cell\'s content and properties in the Clipboard. A paste operation writes the buffered data in such a way that the content of the uppermost-leftmost cell of the buffered set is dropped in the cell where the cursor is when you paste; other buffered content is dropped where it will have the same relationship to that target as it originally did to the upper-left cell of your cut/paste set.

An important caveat: Cut/copy/paste operations do *not* fix up formula references. If you move the content of a cell, formulas which referred to the old location will break. If the old location becomes empty, the breakage will become visible as the expression evaluator will display \#ERR in dependent cells.

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

Sheets can be imported and exported to the [csv](https://en.wikipedia.org/wiki/Comma-separated_values) format which can also be read and written by most other spreadsheet applications such as Microsoft Excel or LibreOffice Calc. When importing files into FreeCAD, the delimiter (the character that is used to separate columns) must be the TAB character (this can be set when exporting from other applications). The import of a CSV-file is available from the menu **Spreadsheet → Import Spreadsheet** or by clicking on the icon <img alt="" src=images/SpreadsheetImport.svg  style="width:24px;">. This import function does not open Excel files or any other spreadsheet format.

Spreadsheets in Excel-format \"xlsx\" can be imported via the menu **File → Import...**. Excel-spreadsheets can also be opened by clicking in the menu **File → Open...** or by clicking on the icon <img alt="" src=images/Document-open.svg  style="width:24px;">. In these cases a new document with a spreadsheet inside is created. The following features are supported:

-   all functions that are also available in the FreeCAD spreadsheet. Other functions give an error in the corresponding cell after the import.
-   Alias names for cells
-   More than one \"Sheet\" in the Excel-spreadsheet. In this case one FreeCAD spreadsheet is created for each Excel sheet.

Other functionality is not imported into the FreeCAD spreadsheet. The Excel-import is <small>(v0.17)</small>  of FreeCAD.

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

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Spreadsheet Workbench/es
