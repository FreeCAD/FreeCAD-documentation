---
- GuiCommand:/it
   Name:Std_ViewRight
   Name/it:Vista da destra
   MenuLocation:Visualizza → Viste standard → Da destra
   Workbenches:Tutti
   Shortcut:**3**
   SeeAlso:[Vista da davanti](Std_ViewFront/it.md), [Vista dall'alto](Std_ViewTop/it.md)
---

# Std ViewRight/it

## Descrizione

Il comando **Vista da destra** orienta la fotocamera della [Vista 3D](3D_view/it.md) che guarda da destra verso sinistra, nella direzione dell\'asse X negativo.

![](images/FreeCAD_views_front.svg ) 
*La freccia 3 punta nella direzione della vista destra.*

## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Std_ViewRight.svg" width=16px> Da destra**.
    -   Selezionare l\'opzione **Visualizza → Viste standard → <img src="images/Std_ViewRight.svg" width=16px> Da destra** del menu.
    -   Selezionare l\'opzione **Viste standard → <img src="images/Std_ViewRight.svg" width=16px> Da destra** dal menu contestuale della [vista 3D](3D_view/it.md).
    -   Usare la scorciatoia da tastiera: **3**.

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per passare alla vista da destra usare il metodo `viewRight` dell\'oggetto ActiveView. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRight()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewRight/it
