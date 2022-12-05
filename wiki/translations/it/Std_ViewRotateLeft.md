---
- GuiCommand:/it
   Name:Std_ViewRotateLeft
   Name/it:Ruota a sinistra
   MenuLocation:Visualizza → Viste standard → Ruota a sinistra
   Shortcut: **Shift**+**Sinistra**
   Workbenches:Tutti
   SeeAlso:[Ruota a destra](Std_ViewRotateRight/it.md)
---

# Std ViewRotateLeft/it

## Descrizione

Il comando **Ruota a sinistra** ruota la camera nella [vista 3D](3D_view/it.md) attiva intorno alla direzione della vista con incrementi di 90 gradi verso sinistra (in senso antiorario).

## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Selezionare l\'opzione **Visualizza → Viste standard → <img src="images/Std_ViewRotateLeft.svg" width=16px> Ruota a sinistra** dal menu.
    -   Selezionare l\'opzione **Viste standard → <img src="images/Std_ViewRotateLeft.svg" width=16px> Ruota a sinistra** dal menu contestuale della [vista 3D](3D_view/it.md).
    -   Usare la scorciatoia da tastiera: **Maiusc**+**Sinistra**.

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per ruotare la vista a sinistra, utilizzare il metodo `viewRotateLeft` dell\'oggetto ActiveView. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRotateLeft()
FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewRotateLeft/it
