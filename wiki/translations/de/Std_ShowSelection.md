---
 GuiCommand:
   Name: Std ShowSelection
   Name/de: Std AuswahlEinblenden
   MenuLocation: Ansicht , Sichtbarkeit , Auswahl einblenden
   Workbenches: Alle
   SeeAlso: Std_ToggleVisibility/de, Std_HideSelection/de, Std_ToggleObjects/de, Std_ShowObjects/de, Std_HideObjects/de
---

# Std ShowSelection/de



## Beschreibung

Der Befehl **Std AuswahlEinblenden** zeigt ausgewählte Objekte in der [3D-Ansicht](3D_view.md) an.



## Anwendung

1.  Ein oder mehrere Objekte auswählen.
    -   Ausgeblendete Objekte können in der [Baumansicht](Tree_view/de.md) ausgewählt werden.
    -   Aufgepasst, bei der Auswahl aller Objekte in der Baumansicht mit der Tastenkombination **Ctrl**+**A**; diese wählt auch Unterelemente von [PartDesign-Körpern](PartDesign_Body/de.md) aus und Objekte, die in [Part-Boolesche-Verknüpfungen](Part_Boolean/de.md) verwendet werden. In den meisten Fällen sollten diese unsichtbar bleiben.
    -   Objekte, die in [Part-Boolesche-Verknüpfungen](Part_Boolean/de.md) verwendet werden, **Ctrl**+**A** in einer 3D-Ansicht verwendet wird.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Den Menüeintrag **Ansicht → Sichtbarkeit → <img src="images/Std_ShowSelection.svg" width=16px> Auswahl einblenden** auswählen.
    -   Die Menüoption **<img src="images/Std_ShowSelection.svg" width=16px> Auswahl einblenden** im Kontextmenü der Baumansicht auswählen. Diese Option ist im Arbeitsbereich [PartDesign](PartDesign_Workbench/de.md) nicht verfügbar.



## Hinweise

-   Ausgeblendete Objekte werden mit ausgegrauter Benennung und ausgegrautem Symbol in der [Baumansicht](Tree_view/de.md) dargestellt.
-   Objekte, die in einem [Std-Part](Std_Part/de.md) eingebettet sind oder ein [Std-Link](Std_LinkMake/de.md) zu einer [Std-Gruppe](Std_Group/de.md) oder eine Verknüpfungsgruppe (LinkGroup) und [PartDesign-Formelemente](PartDesign_Feature/de.md) eines [PartDesign Körpers](PartDesign_Body/de.md) sind in der [3D-Ansicht](3D_view/de.md) nur dann sichtbar, wenn ihr übergeordnetes Objekt ebenfalls sichtbar ist. Dies bedeutet, dass ein Formelement in einem PartDesign-Körper, der in einem Std-Part eingebettet ist, wird nur dann in 3D-Ansichten sichtbar sein, wenn das Formelement selbst, der PartDesign-Körper und das Std-Part alle sichtbar sind. Und wenn das Std-Part wiederum in einem weiteren Std-Part eingebettet ist, muss auch das letztgenannte Objekt auch sichtbar sein.
-   Wenn die Sichtbarkeit einer [Std-Gruppe](Std_Group/de.md) (oder eines von einer solchen abgeleiteten Objekts, wie ein [Arch Gebäudeteil](Arch_BuildingPart/de.md)) geändert wird, ändert sich die Sichtbarkeit der eingebetteten Objekte entsprechend. Ihre Sichtbarkeit kann aber auch einzeln geändert werden.
-   Die Ausführung dieses Befehls kann nicht mit [Std-Rückgängig](Std_Undo/de.md) zurückgenommen werden.
-   Die Sichtbarkeit eines Objekts kann auch durch die zugehörige {{PropertyData/de|Visibility}} im [Einstellungseditor](Property_editor/de.md) oder der [Combo-Ansicht](Combo_view/de.md) geändert werden.



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Für ein Beispiel-Skript siehe [Std SichbarkeitUmschalten](Std_ToggleVisibility/de.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ShowSelection/de
