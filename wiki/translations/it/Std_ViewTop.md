---
- GuiCommand:/it
   Name:Std_ViewTop
   Name/it:Vista dall'alto
   MenuLocation:Visualizza → Viste standard → Dall'alto
   Workbenches:Tutti
   Shortcut:**2**
   SeeAlso:[Vista frontale](Std_ViewFront/it.md), [Vista da destra](Std_ViewRight/it.md)
---

# Std ViewTop/it

## Descrizione

Il comando **Vista dall\'alto** orienta la fotocamera della [Vista 3D](3D_view/it.md) che guarda dall\'alto verso il basso, nella direzione dell\'asse Z negativo.

![](images/FreeCAD_views_front.svg ) 
*La freccia 2 punta nella direzione della vista dall'alto.*

## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Std_ViewTop.svg" width=16px> Vista dall'alto**.
    -   Selezionare l\'opzione **Visualizza → Viste standard → <img src="images/Std_ViewTop.svg" width=16px> Dall'alto** dal menu.
    -   Selezionare l\'opzione **Viste standard → <img src="images/Std_ViewTop.svg" width=16px> Dall'alto** dal menu contestuale della [vista 3D](3D_view/it.md).
    -   Usare la scorciatoia da tastiera: **2**.

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per passare alla vista dall\'alto utilizzare il metodo `viewTop` dell\'oggetto ActiveView. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewTop()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewTop/it
