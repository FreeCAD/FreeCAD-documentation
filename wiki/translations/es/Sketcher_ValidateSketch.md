---
 GuiCommand:
   Name: Sketcher ValidateSketch
   Name/es: Croquizador ValidarCroquis
   MenuLocation: Croquizador , Validar Croquis
   Workbenches: Sketcher_Workbench/es, PartDesign_Workbench/es
   SeeAlso: Sketcher_ConstrainCoincident/es, Topological_naming_problem/es
---

# Sketcher ValidateSketch/es


</div>



## Descripción


<div class="mw-translate-fuzzy">

La utilidad **Validar croquis** puede utilizarse para analizar y reparar un croquis que ya no es editable o que tiene restricciones no válidas, o para añadir las restricciones [coincidentes](Sketcher_ConstrainCoincident/es.md) que faltan a un croquis creado a partir de geometría importada, como los archivos DXF. También puede ser útil para localizar una coincidencia que falta en un boceto nativo que genera un error de \"no se puede validar la cara rota\" al intentar aplicar una función de DiseñoPieza.


</div>

<img alt="" src=images/Sketcher_ValidateSketch_taskpanel.png  style="width:" height="500px;"> 
*El panel de tareas de validación de Croquizador*



## Utilización

1.  This tool cannot be used while a sketch is in edit mode. To finish edit mode see [Sketcher LeaveSketch](Sketcher_LeaveSketch.md).
2.  Select a sketch.
3.  There are several ways to invoke the tool:
    -   Press the **<img src="images/Sketcher_ValidateSketch.svg" width=16px> [Validate sketch...](Sketcher_ValidateSketch.md)** button.
    -   Select the **Sketch → <img src="images/Sketcher_ValidateSketch.svg" width=16px> Validate sketch...** option from the menu.
4.  The **Sketcher validation** task panel opens. See [Options](#Options.md) for more information.
5.  Press the **Close** button to finish.



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
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher ValidateSketch/es
