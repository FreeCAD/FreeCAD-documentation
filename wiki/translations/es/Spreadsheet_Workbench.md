# <img alt="El icono del Ambiente de trabajo Hoja de cálculo" src=images/Workbench_Spreadsheet.svg  style="width:64px;"> Spreadsheet Workbench/es

## Introducción

El <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:24px;"> [Ambiente de trabajo de hojas de cálculo](Spreadsheet_Workbench/es.md) permite crear y editar hojas de cálculo, utilizar datos de la hoja de cálculo como parámetros en un modelo, rellenar la hoja de cálculo con datos recuperados de un modelo, realizar cálculos y exportar los datos a otras aplicaciones de hojas de cálculo como LibreOffice o Microsoft Excel.




<img alt="" src=images/Spreadsheet_screenshot.jpg  style="width:600px;"> 
*Una hoja de cálculo con determinadas celdas rellenas de texto y cantidades*

## Herramientas

-   <img alt="" src=images/Spreadsheet_CreateSheet.svg  style="width:24px;"> [Crear hoja](Spreadsheet_CreateSheet/es.md): crea una nueva hoja de cálculo.

-   <img alt="" src=images/Spreadsheet_Import.svg  style="width:24px;"> [Importar](Spreadsheet_Import/es.md): importa un archivo CSV a una hoja de cálculo.

-   <img alt="" src=images/Spreadsheet_Export.svg  style="width:24px;"> [Exportar](Spreadsheet_Export/es.md): exporta un archivo CSV desde una hoja de cálculo.

-   <img alt="" src=images/Spreadsheet_MergeCells.svg  style="width:24px;"> [Unir celdas](Spreadsheet_MergeCells.md): une las celdas seleccionadas.

-   <img alt="" src=images/Spreadsheet_SplitCell.svg  style="width:24px;"> [Dividir celdas](Spreadsheet_SplitCell.md): divide celdas previamente unidas.

-   <img alt="" src=images/Spreadsheet_AlignLeft.svg  style="width:24px;"> [Alinear a la izquierda](Spreadsheet_AlignLeft.md): alinea el contenido de las celdas seleccionadas a la izquierda.

-   <img alt="" src=images/Spreadsheet_AlignCenter.svg  style="width:24px;"> [Alinear al centro](Spreadsheet_AlignCenter.md): alinea el contenido de las celdas seleccionadas al centro horizontalmente.

-   <img alt="" src=images/Spreadsheet_AlignRight.svg  style="width:24px;"> [Alinear a la derecha](Spreadsheet_AlignRight.md): alinea el contenido de las celdas seleccionadas a la derecha.

-   <img alt="" src=images/Spreadsheet_AlignTop.svg  style="width:24px;"> [Alinear arriba](Spreadsheet_AlignTop.md): alinea el contenido de las celdas seleccionadas hacia arriba.

-   <img alt="" src=images/Spreadsheet_AlignVCenter.svg  style="width:24px;"> [Alinear al centro vertical](Spreadsheet_AlignVCenter.md): alinea el contenido de las celdas seleccionadas al centro vertical.

-   <img alt="" src=images/Spreadsheet_AlignBottom.svg  style="width:24px;"> [Alinear abajo](Spreadsheet_AlignBottom.md): alinea el contenido de las celdas seleccionadas hacia abajo.

-   <img alt="" src=images/Spreadsheet_StyleBold.svg  style="width:24px;"> [Estilo negrita](Spreadsheet_StyleBold.md): establece el contenido de las celdas seleccionadas a negrita.

-   <img alt="" src=images/Spreadsheet_StyleItalic.svg  style="width:24px;"> [Estilo itálica](Spreadsheet_StyleItalic.md): establece el contenido de las celdas seleccionadas a itálica.

-   <img alt="" src=images/Spreadsheet_StyleUnderline.svg  style="width:24px;"> [Estilo subrayar](Spreadsheet_StyleUnderline.md): establece el contenido de las celdas seleccionadas a subrayar.

-   <img alt="" src=images/Spreadsheet_SetAlias.svg  style="width:24px;"> [Establecer alias](Spreadsheet_SetAlias/es.md): establece el alias para una celda seleccionada.

-    **Negro**y **Blanco** establecen los colores de primer plano y de fondo de las celdas seleccionadas.

## Preferencias

-   <img alt="" src=images/Preferences-spreadsheet.svg  style="width:32px;"> [Preferencias](Spreadsheet_Preferences.md): las preferencias para el entorno de trabajo Spreadsheet. <small>(v0.20)</small> 

## Inserte elimine filas y columnas 

Filas y columnas pueden ser insertadas o eliminadas haciendo clic derecho en un encabezado de fila o columna y seleccionando la opción apropiada en el menú contextual. Es posible seleccionar primero varias filas o columnas. Ya sea manteniendo presionado la tecla {{KEY | Ctrl}} al seleccionar los encabezados, o manteniendo presionado el botón del mouse izquierdo y arrastrando.

En FreeCAD versión 0.19 y anteriores las filas son insertadas arriba de las filas seleccionadas, y las columnas a la izquierda de las columnas seleccionadas. En FreeCAD versión 0.20 puede especificar el lugar de inserción.

Tenga en cuenta que eliminar filas o columnas con datos puede romper la hoja de cálculo y su modelo si se basa en la hoja de cálculo. No será advertido previamente si esto sucede.

## Cortar y copiar-pegar celdas 

Las operaciones de cortar y copiar-pegar se pueden usar en las celdas de hojas de cálculo de FreeCAD. Puede usar los atajos normales para estas operaciones: {{KEY | Ctrl}} {{KEY | X}}, {{KEY | Ctrl}} {{KEY | C}} y {{KEY | Ctrl}} {{KEY | V}} respectivamente. Para seleccionar múltiples celdas, mantenga presionada la tecla {{KEY | Ctrl}} mientras selecciona, o mantenga presionado el botón del mouse izquierdo y arrastre para seleccionar un rango de celda rectangular.

Las operaciones de cortar y copiar almacenan el contenido y las propiedades de las celdas en el portapapeles. La operación de pegar escribe los datos de tal manera que el contenido de la celda superior izquierda de los datos almacenados aparezcan en la celda activa. Otro contenido almacenado se coloca en relación con esa celda. Las fórmulas se actualizan en consecuencia.

Note que eliminar celdas con datos puede romper la hoja de cálculo y tu modelo si este se basa en la hoja de cálculo. No será advertido previamente si esto sucede.

En FreeCAD versión 0.19 y anteriores hay un error que puede hacer que FreeCAD se cuelgue si se pega un rango de celdas no rectangular. Es aconsejable guardar su trabajo antes de realizar cualquier operación de pegar.

## Propiedades de la celda 

Las propiedades de una celda de la hoja de cálculo pueden ser editadas haciendo clic derecho en la celda y seleccionando **Propiedades...** del menú contextual. El siguiente cuadro de diálogo aparece:

![](images/SpreadsheetCellPropDialog.png )

Como se indica en las pestañas, se pueden modificar las siguientes propiedades:


<div class="mw-translate-fuzzy">

-   Color: Color del texto y del fondo
-   Alineación: Alineación horizontal y vertical del texto
-   Estilo: Estilo del texto: negrita, cursiva, subrayado
-   Unidades: Muestra las unidades para esta celda. Por favor, lea la sección [Unidades](#Unidades.md) más abajo.
-   Alias: Define un [alias](Spreadsheet_SetAlias/es.md) para esta celda. Este alias se puede utilizar en las fórmulas de las celdas y también en las [expresiones](Expressions/es.md) generales; consulte la sección [Datos de la hoja de cálculo en las expresiones](#Datos_de_hoja_en_expresiónes.md) para obtener más información.


</div>

## Expresiones de la celda 


<div class="mw-translate-fuzzy">

Una celda de la hoja de cálculo puede contener un texto arbitrario o una expresión. Técnicamente, las expresiones deben comenzar con un signo igual \'=\'. Sin embargo, la hoja de cálculo intenta ser inteligente; si se introduce lo que parece una expresión sin el \'=\' inicial, se añadirá uno automáticamente.


</div>


<div class="mw-translate-fuzzy">

Las expresiones de celdas pueden contener números, funciones, referencias a otras celdas y referencias a propiedades del modelo (Pero vea [Limitaciones actuales](#Limitaciones_actuales.md) más abajo). Las celdas se referencian por su columna (letra MAYÚSCULA) y fila (número). Una celda también puede ser referenciada por su [nombre_alias](#nombre_alias.md). Ejemplo: B4 + A6


</div>


<div class="mw-translate-fuzzy">

**Nota:** Las expresiones de celda son tratadas por FreeCAD como código de programación. Por lo tanto, cuando editas una celda el contenido ves que no sigue su configuración de visualización:

-   el separador decimal es siempre un punto
-   el número de decimales mostrados puede diferir de tu configuración de [ajustes de preferencias](Preferences_Editor/es#Unidades.md)


</div>

Las referencias a objetos en el modelo se explican en [Referencias a datos CAD](#Referencias_a_datos_CAD.md) más abajo. El uso de los valores de las celdas de la hoja de cálculo para definir las propiedades del modelo se explica en [Datos de la hoja de cálculo en las expresiones](#Hoja_de_datos_en_expresiones.md) más adelante. Para más información sobre las expresiones y las funciones disponibles, véase [Expresiones](Expressions/es.md).

## Interacción entre las hojas de cálculo y el modelo CAD 

Los datos en las celdas de una hoja de cálculo pueden usarse en expresiones de parámetros del modelo CAD. Por lo tanto, una hoja de cálculo puede usarse como fuente de valores de parámetros utilizados en todo un modelo, recolectando efectivamente los valores en un solo lugar. Cuando los valores se cambian en la hoja de cálculo, se propagan por todo el modelo.

De manera similar, las propiedades de los objetos del modelo CAD pueden usarse en expresiones en celdas de hoja de cálculo. Esto permite el uso de propiedades de objetos como volumen o área en la hoja de cálculo. Si se cambia el nombre de un objeto en el modelo CAD, el cambio se propagará automáticamente a cualquier referencia en expresiones de hoja de cálculo utilizando el nombre al que se cambió.

Se puede usar más de una hoja de cálculo en un documento. Una hoja de cálculo puede ser identificada usando su nombre o su etiqueta.

FreeCAD will automatically assign a unique name to a spreadsheet when it is created. These names follow the pattern `Spreadsheet`, `Spreadsheet001`, `Spreadsheet002` and so on. The name can not be changed, and it is not visible in the properties of the spreadsheet. It can be used to refer to the spreadsheet in an [Expression](Expressions.md) (see [Spreadsheet data in expressions](#Spreadsheet_data_in_expressions.md) below.)

The label of a spreadsheet is automatically set to the name of the spreadsheet upon creation. Unlike the name, the label can be changed, for example in the properties panel or using the context menu action Rename. By default FreeCAD does not accept duplicate labels, but there is a [preference](Preferences_Editor#Document.md) to override this. Spreadsheets with duplicate labels in the same document cannot be referenced by their label.

FreeCAD checks for cyclic dependencies. See [Current limitations](Spreadsheet_Workbench#Current_limitations.md).

### Referencias a los datos CAD 

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

### Datos de la hoja de cálculo en expresiones 

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
    -   You can reference spreadsheet data from an external **.FCStd** file with this syntax: `<nowiki>=NameOfFile#<<MySpreadsheet>>.MyAlias</nowiki>`.
    -   The advantage of having the spreadsheet in another file over switching off recomputes is that the spreadsheet itself does get recomputed.
    -   The disadvantage is that the model won\'t automatically recompute after changes to the spreadsheet.
    -   In the scenario where you first open the \'spreadsheet\' file, change one or more values and then open the \'model\' file, there won\'t be any indication that the model needs to be recomputed. But if both files are open the [Std Refresh](Std_Refresh.md) icon will update correctly for the \'model\' file after changes to the \'spreadsheet\' file.

## Unidades

The Spreadsheet has a notion of dimension (units) associated with cell values. A number entered without an associated unit has no dimension. The unit should be entered immediately following the number value, with no intervening space. If a number has an associated unit, that unit will be used in all calculations. For example, the multiplication of two lengths with the unit mm gives an area with the unit mm².

If a cell contains a value which represents a dimension, it should be entered with its associated unit. While in many simple cases one can get by with a dimensionless value, it is unwise to not enter the unit. If a value representing a dimension is entered without its associated unit, there are some sequences of operations which cause FreeCAD to complain of incompatible units in an expression when it appears the expression should be valid. (This may be better understood by viewing [this thread](https://forum.freecadweb.org/viewtopic.php?f=3&t=34713&p=292455#p292438) in the FreeCAD forums.)

You can change the units displayed for a cell value using the [Cell properties dialog](#Cell_properties.md). This does not change the value contained in the cell; it only converts the existing value for display. The value used for calculations does not change, and the results of formulas using the value do not change. For example, a cell containing the value \"5.08cm\" can be displayed as \"2in\" by changing the units tab value to \"in\".

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

FreeCAD checks for cyclic dependencies when it recomputes. By design, that check stops at the level of the spreadsheet object. As a consequence, you should not have a spreadsheet which contains both cells whose values are used to specify parameters to the model, and cells whose values use output from the model. For example, you cannot have cells specifying the length, width, and height of an object, and another cell which references the total volume of the resulting shape. This restriction can be surmounted by having two spreadsheets: one used as a data-source for input parameters to the model and the other used for calculations based on resultant geometry-data.

## Enlazamiento de celdas 


<small>(v0.20)</small> 

Es posible enlazar el contenido de unas celdas a otras celdas en la hoja de cálculo. Esto puede ser útil cuando se trata de tablas grandes o para obtener contenido de celda de otra hoja de cálculo.

### Crear enlaces 

Para enlazar, por ejemplo, el rango de celdas A3-C4 al rango de celdas B1-D2:

1.  Seleccione el rango de celdas A3-C4.
2.  Clic derecho y seleccione **Enlace...** del menú contextual.
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

## Tablas de configuración 


<small>(v0.20)</small> 

Puedes usar hojas de cálculo para crear tablas de configuración con conjuntos de parámetros predefinidos para tu modelo, y después cambiar dinamicamente que configuración usar. Vea [este post del foro](https://forum.freecadweb.org/viewtopic.php?f=17&t=42183) si quiere saber más sobre el funcionamiento interno de esta característica.


<div class="mw-collapsible mw-collapsed toccolours">

Expandir esta sección para un breve tutorial de como crear una tabla de configuración.


<div class="mw-collapsible-content">

1.  En un nuevo documento, primero cree una [Std Pieza](Std_Part/es.md), después cree un [Part Box](Part_Box/es.md), un [Part Cylinder](Part_Cylinder/es.md) y una hoja de cálculo.
2.  La caja y el cilindro se colocan automáticamente en el contenedor [Std Pieza](Std_Part.md). Coloque manualmente la hoja de cálculo en el contenedor también.
3.  En la hoja de cálculo ingrese the contenido mostrado abajo. Establezca el alias para B2 como {{Value|width}}, C2 como {{Value|length}} y D2 como {{Value|radius}}:
    ![](images/Spreadsheet_configuration_table_screenshot_4.png )
4.  Enlce las [expresiones](Expressions.md){{Value|Spreadsheet.width}} y {{Value|Spreadsheet.length}} a las propiedades **Width** y **Length** de la caja, respectivamente:
    ![](images/Spreadsheet_configuration_table_screenshot_2.png )
5.  Enlace la expresión {{Value|Spreadsheet.radius}} a la propiedad **Radius** del cilindro. Tambieén cambie la **Height** del cilindro a {{Value|5 mm}} para que sea más bajo que la caja.
6.  Clic derecho en la celda A2 en la hoja de cálculo y seleccione **Tabla de configuración...** del menú contextual.
7.  El cuadro de diálogo **Configurar tabl de configuración** se abre.
8.  Ingrese lo siguiente:
    ![](images/Spreadsheet_configuration_table_screenshot_5.png )
9.  Presione **OK**.
10. Se agregará una nueva propiedad llamada **Configuration** al contenedor [Std Part](Std_Part.md) para elegir la configuración como se muestra a continuación:
    ![](images/Spreadsheet_configuration_table_screenshot_6.png )

Puede usar un [Std Link](Std_LinkMake.md) o un [PartDesign SubShapeBinder](PartDesign_SubShapeBinder.md) para instanciar una [Instancia de una Variante](https://forum.freecadweb.org/viewtopic.php?f=17&t=42183&p=532130#p532130) de un objeto configurable con los siguientes pasos:

1.  Cree un [Std Link](Std_LinkMake.md) al contenedor [Std Part](Std_Part.md) y configure su propiedad **Link Copy On Change** a {{Value|Enabled}}.
2.  Mueva el Link a un nuevo lugar cambiando su **Posición** para que sea más fácil distinguirlo del objeto original.
3.  Seleccione una **Configuración** diferente para el Link para crear una instancia de una variante.


<div class="mw-translate-fuzzy">

Pasos similares se aplican a un [PartDesign SubShapeBinder](PartDesign_SubShapeBinder.md), excepto que su propiedad para activar una instancia de una variante se llama **Binder Copy On Change**.


</div>


</div>


</div>

## Scripting básico 


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
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Spreadsheet Workbench/es
