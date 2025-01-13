---
 GuiCommand:
   Name: Part CheckGeometry‏‎
   Name/es: Pieza ComprobarGeometría
   MenuLocation: Pieza , Comprobar geometría
   Workbenches: Part_Workbench/es
---

# Part CheckGeometry/es


</div>

## Description


<div class="mw-translate-fuzzy">

## Descripción

La herramienta **<img src="images/Part_CheckGeometry.svg" width=16px> [Pieza ComprobarGeometría](Part_CheckGeometry/es.md)** ejecuta una verificación e informa si la geometría es un sólido válido.


</div>



## Utilización


<div class="mw-translate-fuzzy">

1.  Seleccione una pieza (tenga cuidado de seleccionar toda la pieza y no sólo una cara para comprobar que el sólido es válido)
2.  Invocar la herramienta ya sea:
    -   Haciendo clic en el botón **<img src="images/Part_CheckGeometry.svg" width=16px>** disponible en la barra de herramientas de la mesa de trabajo de la pieza.
    -   Utilizando la entrada **Pieza → <img src="images/Part_CheckGeometry.svg" width=16px> Comprobar geometría** en el menú superior.


</div>


<div class="mw-translate-fuzzy">

Resultados se informarán en el [Panel de tareas](Task_panel/es.md).


</div>

## Options

### Skip settings page 

If ticked, subsequent invocations of the tool skip showing the **Settings** task panel.

### Run BOP check 


<div class="mw-translate-fuzzy">

La función ComprobarGeometría comprueba si la [Representación del límite](https://en.wikipedia.org/wiki/Boundary_representation) (BRep o B-rep) del modelo es válida. Adicionalmente a esta comprobación de BRep, es posible tener una comprobación adicional de BOP (BOP= Boolean OPerations).


</div>

### Log errors 

If ticked, any errors found are also logged in the [report view](Report_view.md).

## Shape Content 

In addition to detecting potential geometry errors, this tool shows a range of properties regarding the selected object:

-   Checked object
-   Shape type
-   Number of geometric entities: vertices, edges, wires, faces, shells, solids, compsolids, compounds, total shapes
-   Geometric and mass properties:
    -   Area
    -   Volume
    -   Mass
    -   Length
    -   Center of mass
    -   Orientation
    -   Symmetry axis
    -   Symmetry point
    -   Moments
    -   First axis of inertia
    -   Second axis of inertia
    -   Third axis of inertia
    -   Radius of gyration
    -   Global placement

## Notes

-   [App Link](App_Link.md) objects linked to the appropriate object types and [App Part](App_Part.md) containers with the appropriate visible objects inside can also be checked using this tool. For [App Links](App_Link.md) the shape of the linked object is checked. For [App Part](App_Part.md) containers the visible objects within are checked as compounds. <small>(v0.20)</small> 
-   FreeCAD has no methods to automatically repair geometry. If faults are detected the steps involved to create the model need to be examined and fixed manually.


<div class="mw-translate-fuzzy">





</div>


{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part CheckGeometry/es
