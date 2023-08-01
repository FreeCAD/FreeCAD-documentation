---
- GuiCommand:
   Name: Std_ViewBottom
   Name/it: Vista dal basso
   MenuLocation: Visualizza - Viste standard - Dal basso
   Workbenches: Tutti
   Shortcut: **5**
   SeeAlso: [Vista da dietro](Std_ViewRear/it.md), [Vista da sinistra](Std_ViewLeft/it.md)
---

# Std ViewBottom/it

## Descrizione

Il comando **Vista dal basso** orienta la fotocamera della [Vista 3D](3D_view/it.md) che guarda dal basso verso l\'alto, nella direzione dell\'asse Z positivo.

![](images/FreeCAD_views_rear.svg ) 
*La freccia 5 punta nella direzione della vista dal basso.*

## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Premere il pulsante **<img src="images/Std_ViewBottom.svg" width=16px> Vista dal basso**.
    -   Selezionare l\'opzione **Visualizza → Viste standard → <img src="images/Std_ViewBottom.svg" width=16px> Dal basso** dal menu.
    -   Selezionare l\'opzione **Viste standard → <img src="images/Std_ViewBottom.svg" width=16px> Dal basso** dal menu contestuale della [vista 3D](3D_view/it.md).
    -   Usare la scorciatoia da tastiera: **5**.

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per passare alla vista dal basso usare il metodo `viewBottom` dell\'oggetto ActiveView. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewBottom()
FreeCADGui.ActiveDocument.ActiveView.getViewDirection()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewBottom/it
