---
- GuiCommand:
   Name: Std ToggleObjects
   Name/de: Std ObjekteUmschalten
   MenuLocation: Ansicht - Sichtbarkeit - Alle Objekte umkehren
   Workbenches: Alle
   SeeAlso: [Std SichtbarkeitUmschalten](Std_ToggleVisibility/de.md), [Std AuswahlEinblenden](Std_ShowSelection/de.md), [Std AuswahlAusblenden](Std_HideSelection.md), [Std ObjekteEinblenden](Std_ShowObjects/de.md), [Std ObjekteAusblenden](Std_HideObjects/de.md)
---

# Std ToggleObjects/de



## Beschreibung

Der Befehl **Std ObjekteUmschalten** schaltet die Sichtbarkeit aller Objekte, die zum aktiven Dokument gehören, in den [3D-Ansichten](3D_view.md) um. Der Befehl sollte mit Vorsicht verwendet werden, da auch die Sichtbarkeit der Unterelemente von [PartDesign-Körpern](PartDesign_Body/de.md) und Objekten, die für [Part BoolescheOperationen](Part_Boolean/de.md) verwendet werden, umgeschaltet wird. In den meisten Fällen sollten diese unsichtbar bleiben.



## Anwendung

1.  Menüeintrag **Ansicht → Sichtbarkeit → <img src="images/Std_ToggleObjects.svg" width=16px> Alle Objekte umkehren** auswählen.



## Hinweise

-   Ausgeblendete Objekte werden mit ausgegrauter Benennung und ausgegrautem Symbol in der [Baumansicht](Tree_view/de.md).
-   Objekte, die in einem [Std Part](Std_Part/de.md) eingebettet sind oder einem [Std Link](Std_LinkMake/de.md) zu einer [Std Gruppe](Std_Group/de.md) oder einer LinkGroup und [Formelemente](PartDesign_Feature/de.md) eines [PartDesign Körpers](PartDesign_Body/de.md) sind nur in der [3D-Ansicht](3D_view/de.md) sichtbar, wenn ihr übergeordnetes Objekt auch sichtbar ist. Das heißt, dass ein Formelement in einem PartDesign-Körper, der in einem Std-Part eingebettet ist, nur dann sichtbar ist, wenn sowohl das Formelement selbst als auch der PartDesign-Körper und das Std-Part sichtbar sind. Wenn das Std-Part wiederum in einem anderen Std-Part eingebettet ist, muss auch das letztgenannte sichtbar sein.
-   Wird die Sichtbarkeit einer [Std Gruppe](Std_Group/de.md) (oder eines Objekts, das davon abgeleitet ist, wie ein [Arch Gebäudeteil](Arch_BuildingPart/de.md)) geändert, ändert sich auch die Sichtbarkeit der eingebetteten Objekte entsprechend. Aber ihre Sichtbarkeit kann auch separat geändert werden.
-   Das Ergebnis dieses Befehls kann nicht mit [Std Rückgängig](Std_Undo/de.md) rückgängig gemacht werden.
-   Die Sichtbarkeit eines Objekts kann auch durch die zugehörige {{PropertyData/de|Visibility}} im [Eigenschafteneditor](Property_editor/de.md) oder in der [Combo-Ansicht](Combo_view/de.md) geändert werden.



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Für ein Beispiel-Skript siehe [Std SichbarkeitUmschalten](Std_ToggleVisibility/de.md).





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std ToggleObjects/de
