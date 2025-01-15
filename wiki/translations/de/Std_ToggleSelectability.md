---
 GuiCommand:
   Name: Std ToggleSelectability
   Name/de: Std AuswählbarkeitUmschalten
   MenuLocation: Ansicht , Sichtbarkeit , Selektierbarkeit an/aus
   Workbenches: Alle
---

# Std ToggleSelectability/de



## Beschreibung

Der Befehl **Std AuswählbarkeitUmschalten** schaltet die Auswählbarkeit von Objekten in den [3D-Ansichten](3D_view.md) um.



## Anwendung

1.  Ein oder mehrere Objekte auswählen.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Den Menüeintrag **Ansicht → Sichtbarkeit → <img src="images/Std_ToggleSelectability.svg" width=16px> Selektierbarkeit an/aus** auswählen.
    -   Die Menüoption **<img src="images/Std_ToggleSelectability.svg" width=16px> Selektierbarkeit an/aus** im Kontextmenü der [Baumansicht](Tree_view/de.md) oder der 3D-Ansicht auswählen.



## Hinweise

-   Die Auswählbarkeit eines Objekts kann auch durch die mit ihm verknüpfte {{PropertyData/de|Selectable}} im [Eigenschafteneditor](Property_editor/de.md) geändert werden.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Die Eigenschaft `Selectable` eines Objekts bestimmt seine Auswählbarkeit.


```python
import FreeCADGui

obj = FreeCADGui.ActiveDocument.myObjectName

obj.Selectable = not obj.Selectable
```



---
⏵ [documentation index](../README.md) > Std ToggleSelectability/de
