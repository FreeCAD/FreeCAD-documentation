---
- GuiCommand:/es
   Name:Part CheckGeometry‏‎
   Name/es:Pieza ComprobarGeometría
   MenuLocation:Pieza → Comprobar geometría
   Workbenches:[Pieza](Part_Workbench/es.md)
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

**Note:** FreeCAD has no automatic repair methods for solids, so you need to look at the steps involved to model this specific geometry and try to fix the error on your own.

## Options

### Skip settings page 

If ticked, subsequent invocations of the tool skip showing the **Settings** task panel.

### Run BOP check 


<div class="mw-translate-fuzzy">

La función ComprobarGeometría comprueba si la _) del modelo es válida. Adicionalmente a esta comprobación de BRep, es posible tener una comprobación adicional de BOP (BOP= Boolean OPerations).


</div>

### Log errors 

If ticked, any errors found are also logged in the [report view](Report_view.md). <small>(v0.19)</small> 


<div class="mw-translate-fuzzy">





</div>

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part CheckGeometry/es
