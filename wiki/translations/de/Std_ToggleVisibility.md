---
- GuiCommand   */de
   Name   *Std ToggleVisibility
   Name/de   *Std SichtbarkeitUmschalten
   MenuLocation   *Ansicht → Ein/Ausblenden
   Workbenches   *Alle
   Shortcut   ***Space**
   SeeAlso   *[Std AuswahlEinblenden](Std_ShowSelection/de.md), [Std AuswahlAusblenden](Std_HideSelection/de.md), [Std ObjekteUmschalten](Std_ToggleObjects/de.md), [Std ObjekteEinblenden](Std_ShowObjects/de.md), [Std ObjekteAusblenden](Std_HideObjects/de.md)
---

# Std ToggleVisibility/de

## Beschreibung

Der Befehl **Std SichtbarkeitUmschalten** schaltet die Sichtbarkeit von ausgewählten Objekten in der [3D-Ansicht](3D_view/de.md) ein/aus.

## Anwendung

1.  Ein oder mehrere Objekte auswälen.
    -   Unsichtbare Objekte können in der [Baumansicht](Tree_view/de.md) ausgewählt werden.
    -   Vorsicht bei der Verwendung von **Ctrl**+**A** zur Auswahl von Objekten in der Baumansicht. Dies schließt auch die Unterelemente von [PartDesign Körpern](PartDesign_Body/de.md) und Objekte, die von [Part Boolesche Operationen](Part_Boolean/de.md) verwendet werden, ein. In den meisten Fällen sollten sie unsichtbar bleiben.
    -   Objekte, die von [Part Boolesche Operationen](Part_Boolean/de.md) verwendet werden, werden auch ausgewählt, wenn man **Ctrl**+**A** in einer 3D-Ansicht verwendet.
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen   *
    -   Den Menüeintrag **Ansicht → <img src="images/Std_ToggleVisibility.svg" width=16px> Ein/Ausblenden** auswählen.
    -   Den Menüeintrag **Ansicht → Sichtbarkeit → <img src="images/Std_ToggleVisibility.svg" width=16px> Ein/Ausblenden** auswählen.
    -   Die Option **<img src="images/Std_ToggleVisibility.svg" width=16px> Ein/Ausblenden** im Kontextmenü der Baumansicht auswählen. Diese Option ist im Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md) nicht verfügbar.
    -   Die Option **<img src="images/Std_ToggleVisibility.svg" width=16px> Ein/Ausblenden** im Kontextmenü der 3D-Ansicht auswählen.
    -   Das Tastaturkürzel **Leertaste**.

## Hinweise

-   Invisible objects are displayed with a greyed out label and a greyed out icon in the [Tree view](Tree_view.md).
-   Objects nested in a [Std Part](Std_Part.md), or a [Std Link](Std_LinkMake.md) to a [Std Group](Std_Group.md), or a LinkGroup, and [features](PartDesign_Feature.md) of a [PartDesign Body](PartDesign_Body.md) will only be visible in [3D views](3D_view.md) if their parent is visible as well. This means that a feature in a PartDesign Body that is nested in a Std Part will only be visible in 3D views if the feature itself, the PartDesign Body, and the Std Part are all visible. And if the Std Part is in turn nested in another Std Part, then that last object must also be visible.
-   If the visibility of a [Std Group](Std_Group.md) (or an object derived from it such as an [Arch BuildingPart](Arch_BuildingPart.md)) is changed, the visibility of its nested objects will change accordingly. But their visibility can be changed independently as well.
-   The action of this command cannot be undone with [Std Undo](Std_Undo.md).
-   The visibility of an object can also be changed through its related **Visibility** property in the [Property editor](Property_editor.md) or the [Combo view](Combo_view.md).

## Skripten


**Siehe auch   ***

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Mit den Methoden `show` und `hide` eines Objekts ändert man seine Sichtbarkeit.


```python
import FreeCADGui

obj = FreeCADGui.ActiveDocument.myObjectName

if obj.Visibility == True   *
  obj.hide()
else   *
  obj.show()
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ToggleVisibility/de
