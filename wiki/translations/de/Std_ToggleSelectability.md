---
- GuiCommand:
   Name:Std ToggleSelectability
   Name/de:Std AuswählbarkeitUmschalten
   MenuLocation:Ansicht - Sichtbarkeit - Selektierbarkeit an/aus
   Workbenches:Alle
---

# Std ToggleSelectability/de



## Beschreibung

Der Befehl **Std AuswählbarkeitUmschalten** schaltet die Auswählbarkeit von Objekten in den [3D-Ansichten](3D_view.md) um.



## Anwendung

1.  Ein oder mehrere Objekte auswählen.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Den Menüeintrag **Ansicht → Sichtbarkeit → <img src="images/Std_ToggleSelectability.svg" width=16px> Selektierbarkeit an/aus** auswählen.
    -   Den Menüeintrag **<img src="images/Std_ToggleSelectability.svg" width=16px> Selektierbarkeit an/aus** im Kontextmenü der [Baumansicht](Tree_view/de.md) auswählen. Dieser Befehl steht im Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md) nicht zur Verfügung.
    -   Den Menüeintrag **<img src="images/Std_ToggleSelectability.svg" width=16px> Toggle selectability** im Kontextmenü der 3D-Ansicht auswählen.



## Hinweise

-   Die Auswählbarkeit eines Objekts kann auch durch die mit ihm verknüpfte {{PropertyData/de|Selectable}} im [Eigenschafteneditor](Property_editor/de.md) oder in der [Combo-Ansicht](Combo_view/de.md) geändert werden.



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Die Eigenschaft `Selectable` eines Objekts bestimmt seine Auswählbarkeit.


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
![](images/Button_right.svg) [documentation index](../README.md) > Std ToggleSelectability/de
