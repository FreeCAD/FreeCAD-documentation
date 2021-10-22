---
- GuiCommand:/it
   Name:Std_ViewDimetric
   Name/it:Vista dimetrica
   Empty:1
   MenuLocation:Visualizza → Viste standard → Assonometria → Dimetrica
   Workbenches:Tutti
   SeeAlso:[Assonometria isometrica](Std_ViewIsometric/it.md), [Assonometria trimetrica](Std_ViewTrimetric/it.md)
   Empty:1
---

# Std ViewDimetric/it


</div>

## Descrizione

Il comando **Vista dimetrica** orienta la camera della _, ma il comando funziona anche se la vista è in [modalità prospettiva](Std_PerspectiveCamera.md).

![](images/Std_ViewDimetric_example.svg ) 
*Il [sistema di assi](Std_AxisCross.md) e un cubo in vista dimetrica.*

## Utilizzo


<div class="mw-translate-fuzzy">

-   Selezionare l\'opzione **Visualizza → Viste standard → Assonometria → Dimetrica** dal menu.


</div>

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per passare alla vista dimetrica, utilizzare il metodo `viewDimetric` dell\'oggetto ActiveView. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewDimetric()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}

---
[documentation index](../README.md) > Std ViewDimetric/it
