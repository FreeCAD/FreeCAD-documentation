---
- GuiCommand   */it
   Name   *Std_ViewLeft
   Name/it   *Vista da sinistra
   MenuLocation   *Visualizza → Viste standard → Da sinistra
   Workbenches   *Tutti
   Shortcut   ***6**
   SeeAlso   *[Vista da dietro](Std_ViewRear/it.md), [Vista dal basso](Std_ViewBottom/it.md)
---

# Std ViewLeft/it

## Descrizione

Il comando **Vista da sinistra** orienta la camera della [Vista 3D](3D_view/it.md) nella direzione dell\'asse X positivo.

![](images/FreeCAD_views_rear.svg ) 
*La freccia 6 punta nella direzione della vista da sinistra*

## Utilizzo

1.  Esistono diversi modi per invocare il comando   *
    -   Premere il pulsante **<img src="images/Std_ViewLeft.svg" width=16px> Da sinistra**.
    -   Selezionare l\'opzione **Visualizza → Viste standard → <img src="images/Std_ViewLeft.svg" width=16px> Da sinistra** del menu.
    -   Selezionare l\'opzione **Viste standard → <img src="images/Std_ViewLeft.svg" width=16px> Da sinistra** dal menu contestuale della [vista 3D](3D_view/it.md).
    -   Usare la scorciatoia da tastiera   * **6**.

## Script


**Vedere anche   ***

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per passare alla vista da sinistra usa il metodo `viewLeft` dell\'oggetto ActiveView. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewLeft()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewLeft/it
