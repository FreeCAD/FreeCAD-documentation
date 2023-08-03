---
 GuiCommand:
   Name: Std ToggleVisibility
   Name/de: Std SichtbarkeitUmschalten
   MenuLocation: Ansicht , Ein/Ausblenden
   Workbenches: Alle
   Shortcut: **Space**
   SeeAlso: Std_ShowSelection/de, Std_HideSelection/de, Std_ToggleObjects/de, Std_ShowObjects/de, Std_HideObjects/de
---

# Std ToggleVisibility/de



## Beschreibung

Der Befehl **Std SichtbarkeitUmschalten** schaltet die Sichtbarkeit von ausgewählten Objekten in der [3D-Ansicht](3D_view/de.md) ein/aus.



## Anwendung

1.  Ein oder mehrere Objekte auswälen.
    -   Unsichtbare Objekte können in der [Baumansicht](Tree_view/de.md) ausgewählt werden.
    -   Vorsicht bei der Verwendung von **Ctrl**+**A** zur Auswahl von Objekten in der Baumansicht. Dies schließt auch die Unterelemente von [PartDesign Körpern](PartDesign_Body/de.md) und Objekte, die von [Part Boolesche Operationen](Part_Boolean/de.md) verwendet werden, ein. In den meisten Fällen sollten sie unsichtbar bleiben.
    -   Objekte, die von [Part Boolesche Operationen](Part_Boolean/de.md) verwendet werden, werden auch ausgewählt, wenn man **Ctrl**+**A** in einer 3D-Ansicht verwendet.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Den Menüeintrag **Ansicht → <img src="images/Std_ToggleVisibility.svg" width=16px> Ein/Ausblenden** auswählen.
    -   Den Menüeintrag **Ansicht → Sichtbarkeit → <img src="images/Std_ToggleVisibility.svg" width=16px> Ein/Ausblenden** auswählen.
    -   Die Option **<img src="images/Std_ToggleVisibility.svg" width=16px> Ein/Ausblenden** im Kontextmenü der Baumansicht auswählen. Diese Option ist im Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md) nicht verfügbar.
    -   Die Option **<img src="images/Std_ToggleVisibility.svg" width=16px> Ein/Ausblenden** im Kontextmenü der 3D-Ansicht auswählen.
    -   Das Tastaturkürzel **Leertaste**.



## Hinweise

-   Nicht sichtbare Objekte werden mit ausgegrautem Label und ausgegrautem Symbol in der [Baumansicht](Tree_view/de.md) dargestellt.
-   Objekte, die in einem [Std Teil](Std_Part/de.md) enthalten sind, oder eine [Std Verknüpfung](Std_LinkMake/de.md) zu einer [Std Gruppe](Std_Group/de.md) oder einer LinkGroup, und [Formelemente](PartDesign_Feature/de.md) eines [PartDesign-Körpers](PartDesign_Body/de.md) sind nur dann in den [3D-Ansichten](3D_view/de.md) sichtbar, wenn auch die übergeordneten Bestandteile sichtbar sind. Das heißt, dass ein Formelement in einem PartDesign-Körper, der sich in einem Std Teil befindet, nur dann in 3D-Ansichten zu sehen ist, wenn auch der PartDesign-Körper und das Std Teil sichtbar sind. Befindet sich dieses Std Teil wiederum auch in einem weiteren Std Teil, dann muss auch letzteres sichtbar sein.
-   Wird die Sichbarkeit einer [Std Gruppe](Std_Group/de.md) geändert (oder eines davon abgeleitete Objekts, wie ein [Arch Gebäudeteil](Arch_BuildingPart/de.md)), wird die Sichtbarkeit der enthaltenen Objekte entsprechend geändert. Ihre Schtbarkeit kann aber auch unabhängig geändert werden.
-   Die Ausführung dieses Befehls kann nicht mit [Std Rückgängig](Std_Undo/de.md) rückgängig gemacht werden.
-   Die Sichtbarkeit eines Objekts kann auch durch seine zugehörige {{PropertyData/de|Visibility}} im [Eigenschafteneditor](Property_editor/de.md) oder in der [Combo-Ansicht](Combo_view/de.md) geändert werden.



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Mit den Methoden `show` und `hide` eines Objekts ändert man seine Sichtbarkeit.


```python
import FreeCADGui

obj = FreeCADGui.ActiveDocument.myObjectName

if obj.Visibility == True:
  obj.hide()
else:
  obj.show()
```





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ToggleVisibility/de
