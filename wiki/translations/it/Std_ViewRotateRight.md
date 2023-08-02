---
- GuiCommand:
   Name: Std_ViewRotateRight
   Name/it: Ruota a destra
   MenuLocation: Visualizza -> Viste standard -> Ruota a destra
   Shortcut:  **Shift**+**Destra**
   Workbenches: Tutti
   SeeAlso: Std_ViewRotateLeft/it
---

# Std ViewRotateRight/it



## Descrizione

Il comando **Ruota a destra** ruota la camera nella [vista 3D](3D_view/it.md) attiva intorno alla direzione della vista con incrementi di 90 gradi verso destra (in senso orario).



## Utilizzo

1.  Esistono diversi modi per invocare il comando:
    -   Selezionare l\'opzione **Visualizza → Viste standard → <img src="images/Std_ViewRotateRight.svg" width=16px> Ruota a destra** dal menu.
    -   Selezionare l\'opzione **Viste standard → <img src="images/Std_ViewRotateRight.svg" width=16px> Ruota a destra** dal menu contestuale della [vista 3D](3D_view/it.md).
    -   Usare la scorciatoia da tastiera: **Maiusc**+**Destra**.



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per ruotare la vista verso destra, utilizzare il metodo `viewRotateRight` dell\'oggetto ActiveView. Questo metodo non è disponibile se FreeCAD è in modalità console.


```python
import FreeCADGui

FreeCADGui.ActiveDocument.ActiveView.viewRotateRight()
FreeCADGui.ActiveDocument.ActiveView.getCameraOrientation()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ViewRotateRight/it
