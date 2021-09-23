---
- GuiCommand:/it
   Name:Std_ViewTrimetric
   Name/it:Vista trimetrica
   Empty:1
   MenuLocation:[Visualizza](Std_View_Menu/it.md) → Viste standard → Assonometria → Trimetrica
   Workbenches:Tutti
   SeeAlso:[Assonometria isometrica](Std_ViewIsometric/it.md), [Assonometria dimetrica](Std_ViewDimetric/it.md)

---

# Std ViewTrimetric/it


</div>

## Descrizione

Il comando **Vista trimetrica** orienta la camera della [vista 3D](3D_view/it.md) in proiezione [assonometria trimetrica](https://en.wikipedia.org/wiki/Axonometric_projection#Three_types). Per una vista veramente trimetrica la vista 3D deve essere in [modalità ortografica](Std_OrthographicCamera/it.md), ma il comando funziona anche se la vista è in [modalità prospettiva](Std_PerspectiveCamera.md).

![](images/Std_ViewTrimetric_example.svg ) *Il [sistema di assi](Std_AxisCross.md) e un cubo in vista trimetrica.*

## Utilizzo


<div class="mw-translate-fuzzy">

-   Selezionare l\'opzione **Visualizza → Viste standard → Assonometria → Trimetrica** dal menu.


</div>

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per passare alla vista trimetrica, utilizzare il metodo `viewTrimetric` dell\'oggetto ActiveView. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewTrimetric()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}

---
[documentation index](../README.md) > Std ViewTrimetric/it
