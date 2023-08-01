---
- GuiCommand:
   Name:Std ToggleSelectability
   Name/it:Std ToggleSelectability
   MenuLocation:Visualizza - Visibilita - Commuta la selezionabilità
   Workbenches:All
---

# Std ToggleSelectability/it



## Descrizione

Il comando **Commuta la selezionabilità** commuta la selezionabilità degli oggetti nella [Vista 3D](3D_view/it.md).



## Utilizzo

1.  Selezionare uno o più oggetti.
2.  Esistono diversi modi per invocare il comando:
    -   Selezionare l\'opzione **Visualizza → Visibilità → <img src="images/Std_ToggleSelectability.svg" width=16px> Commuta la selezionabilità** dal menu.
    -   Selezionare l\'opzione **<img src="images/Std_ToggleSelectability.svg" width=16px> Commuta la selezionabilità** dal menu contestuale [Vista ad albero](Tree_view/it.md). Questa opzione non è disponibile in [PartDesign](PartDesign_Workbench/it.md).
    -   Selezionare l\'opzione **<img src="images/Std_ToggleSelectability.svg" width=16px> Commuta la selezionabilità** dal menu contestuale della vista 3D.



## Note

-   La selezionabilità di un oggetto può anche essere modificata tramite la relativa proprietà **Selectable** nel [Editor delle proprietà](Property_editor/it.md) o nella [Vista combinata](Combo_view/it.md).



## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md)

La proprietà `Selectable` di un oggetto ne determina la selezionabilità.


```python
import FreeCADGui

obj = FreeCADGui.ActiveDocument.myObjectName

if obj.Selectable == True:
  obj.Selectable = False
else:
  obj.Selectable = True
```





{{Std Base navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Std ToggleSelectability/it
