---
- GuiCommand:
   Name: Std_ViewFront
   Name/it: Vista frontale
   MenuLocation: Visualizza - Viste standard - Di fronte
   Workbenches: Tutti
   Shortcut: **1**
   SeeAlso: [Vista dall'alto](Std_ViewTop/it.md), [Vista da destra](Std_ViewRight/it.md)
---

# Std ViewFront/it

## Descrizione

Il comando **Vista frontale** orienta la camera della [Vista 3D](3D_view/it.md) nella direzione dell\'asse Y positivo.

![](images/FreeCAD_views_front.svg ) 
*La freccia 1 punta nella direzione della vista frontale.*

## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Std_ViewFront.svg" width=16px> Vista frontale**.
    -   Selezionare l\'opzione **Visualizza → Viste standard → <img src="images/Std_ViewFront.svg" width=16px> Di fronte** dal menu.
    -   Selezionare l\'opzione **Viste standard → <img src="images/Std_ViewFront.svg" width=16px> Di fronte** dal menu contestuale della [vista 3D](3D_view/it.md).
    -   Usare la scorciatoia da tastiera: **1**.

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per passare alla vista frontale usare il metodo `viewFront` dell\'oggetto ActiveView. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewFront()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewFront/it
