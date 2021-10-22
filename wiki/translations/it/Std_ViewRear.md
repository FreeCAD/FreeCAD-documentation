---
- GuiCommand:/it
   Name:Std_ViewRear
   Name/it:Vista da dietro
   MenuLocation:Visualizza → Viste standard → Da dietro
   Workbenches:Tutti
   Shortcut:**4**
   SeeAlso:[Vista dal basso](Std_ViewBottom/it.md), [Vista da sinistra](Std_ViewLeft/it.md)
---

# Std ViewRear/it

## Descrizione

Il comando **Vista da dietro** orienta la camera della [Vista 3D](3D_view/it.md) nella direzione dell\'asse Y negativo.

![](images/FreeCAD_views_rear.svg ) 
*La freccia 4 indica la direzione della vista posteriore.*

## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Std_ViewRear.svg" width=16px> Da dietro**.
    -   Selezionare l\'opzione **Visualizza → Viste standard → <img src="images/Std_ViewRear.svg" width=16px> Da dietro** del menu.
    -   Selezionare l\'opzione **Viste standard → <img src="images/Std_ViewRear.svg" width=16px> Da dietro** dal menu contestuale della [vista 3D](3D_view/it.md).
    -   Usare la scorciatoia da tastiera: **4**.

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per passare alla vista posteriore utilizzare il metodo `viewRear` dell\'oggetto ActiveView. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRear()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}

---
[documentation index](../README.md) > Std ViewRear/it
