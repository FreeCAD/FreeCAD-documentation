---
- GuiCommand:
   Name:Sketcher ValidateSketch
   Name/es:Croquizador ValidarCroquis
   MenuLocation:Croquizador → Validar Croquis
   Workbenches:[Croquizador](Sketcher_Workbench/es.md), [DiseñoPieza](PartDesign_Workbench/es.md)
   SeeAlso:[Croquizador RestringirCoincidencia](Sketcher_ConstrainCoincident/es.md), [Problema de denominación topológica](Topological_naming_problem/es.md)
---

# Sketcher ValidateSketch/es

## Descripción

La utilidad **Validar croquis** puede utilizarse para analizar y reparar un croquis que ya no es editable o que tiene restricciones no válidas, o para añadir las restricciones [coincidentes](Sketcher_ConstrainCoincident/es.md) que faltan a un croquis creado a partir de geometría importada, como los archivos DXF. También puede ser útil para localizar una coincidencia que falta en un boceto nativo que genera un error de \"no se puede validar la cara rota\" al intentar aplicar una función de DiseñoPieza.

![](images/Sketcher_ValidateSketch_taskpanel.png ) 
*El panel de tareas de validación de Croquizador*

## Utilización

1.  This tool cannot be used on a sketch that is in edit mode. If required exit edit mode by doing one of the following:
    -   Press the **[<img src=images/Sketcher_LeaveSketch.svg style="width:16px"> [Leave sketch](Sketcher_LeaveSketch.md)** button.
    -   Press the **Close** button at the top of the [Task panel](Task_panel.md).
    -   Use the keyboard shortcut: **Esc** (if enabled in the [Sketcher Preferences](Sketcher_Preferences#General.md)).
2.  Select the sketch to be validated from the [Tree view](Tree_view.md) or by clicking on one of its edges in the [3D view](3D_view.md).
3.  To open the validate sketch utility do one of the following:
    -   Select the **Sketch → Validate sketch...** option from the menu.
    -   Press the **[<img src=images/Sketcher_ValidateSketch.svg style="width:16px"> [Validate sketch](Sketcher_ValidateSketch.md)** button (not available in the [PartDesign Workbench](PartDesign_Workbench.md)).
4.  See [Options](#Options.md) below for the available operations.
5.  Press the **Close** button when done.

## Opciones

### Coincidencias Falta 

Finds out missing coincidences for overlapping vertices, and adds them. Press the **Find** button; a pop up dialog will appear to report how many missing coincidences were found; they will be shown in the 3D view as yellow crosses. Press **OK** to close the dialog, then press the **Fix** button to add the missing coincidences.

If necessary, define a larger tolerance value in the drop-down field.

Press **Highlight troublesome vertexes** to highlight vertexes that are outside this tolerance.

This tolerance is also used by the **Find**/**Fix** process.

Leave the \"Ignore construction geometry\" checkbox checked to disregard construction geometry in the analysis.

### Restricciones no válidas 

Checks for malformed constraints.

For example, if there is a Circle-Line-Tangent constraint, but it references two lines, it is considered invalid.

(This sometimes happens due to the [Topological naming problem](Topological_naming_problem.md), i.e. the external geometry changes type).

It also does other checks, such as for empty links.

### Geometría degenerada 

Degenerated geometry can result from solver actions in a sketch.

For instance, if a line is forced to shorten to become almost a point.

Other examples: a zero length line or zero radius circle/arc.

### Geometría externa invertida 

Reversed external geometry can happen because the handling of reversed geometry was changed around revision 0.15.

This process might be helpful if sketches with external-geometry fail to solve because of these changes.

### Bloqueo de la orientación de las restricciones 

Tangent and perpendicular constraints are implemented (via-point).

Internally they work by constraining the angle between tangent vectors. With tangent constraint for example, the angle can be 0 or 180 degrees (co-directed or opposed vectors). The actual angle is remembered in the constraint data (\"constraint orientation is locked\"), it guards against flipping. But the angle can be erased (\"constraint orientation unlock\") or updated; these tools do exactly that.

The locking mechanism typically works well and this tool should not be needed. **It should only used after making a backup of the open document.**





{{Sketcher Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ValidateSketch/es
