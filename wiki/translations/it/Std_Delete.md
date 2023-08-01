---
- GuiCommand:
   Name:Std_Delete
   Name/it:Elimina
   MenuLocation:Modifica - Elimina
   Workbenches:Tutti
   Shortcut:**Canc**
---

# Std Delete/it

## Descrizione

Il comando **Elimina** elimina gli oggetti selezionati.

## Utilizzo

1.  Selezionare uno o più oggetti.
2.  Esistono diversi modi per invocare il comando::
    -   Selezionare l\'opzione **Modifica → <img src="images/Std_Delete.svg" width=16px> Elimina** dal menu.
    -   Selezionare l\'opzione **<img src="images/Std_Delete.svg" width=16px> Elimina** nel menu contestuale della [vista ad albero](Tree_view/it.md) o della [vista 3D](3D_view/it.md).
    -   Usare la scorciatoia da tastiera: **Canc**.

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

Per eliminare un oggetto utilizzare il metodo `removeObject` dell\'oggetto documento.


```python
import FreeCAD

FreeCAD.ActiveDocument.removeObject("myObjectName")
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std Delete/it
