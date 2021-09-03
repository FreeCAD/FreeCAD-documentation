---
- GuiCommand:/de
   Name:Draft AddToGroup
   Name/de:Draft ZurGruppeHinzufügen
   MenuLocation:Dienstprogramme → Zur Gruppe hinzufügen...
   Workbenches:[Draft](Draft_Workbench/de.md), [Arch](Arch_Workbench/de.md)
   SeeAlso:[Std Gruppe](Std_Group/de.md), [Draft Zur Konstruktionsgruppe hinzufügen](Draft_AddConstruction/de.md), [Draft Zur Gruppe hinzufügen](Draft_AutoGroup/de.md),  [Entwurf Wähle Gruppe](Draft_SelectGroup/de.md), 
---

## Beschreibung

Der <img alt="" src=images/Draft_AddToGroup.svg  style="width:24px;"> **Draft AddToGroup**-Befehl verschiebt Objekte in eine[Std Gruppe](Std_Group/de.md). Damit können auch Objekte von der aktuellen Gruppe entfernt werden.

In FreeCAD v0.20 kann der Befehl auch gruppenähnliche [Arch](Arch_Workbench/de.md)-Objekte handhaben.

## Anwendung

1.  Um diesen Befehl zu benutzen, muss wenigstens eine Gruppe existieren.
2.  Wähle ein oder mehrere Objekte.
3.  Es gibt mehrere Wege, den Befehl aufzurufen:
    -   Drücke die **<img src="images/Draft_AddToGroup.svg" width=16px> [Draft Zur ](Draft_AddToGroup/de.md)**-Schaltfläche.
    -   Wähle die {{MenuCommand|Utilities → <img src="images/Draft_AddToGroup.svg" width=16px> Move to group...}}-Option aus dem Menü.
    -   Wähle die {{MenuCommand|Utilities → <img src="images/Draft_AddToGroup.svg" width=16px> Move to group...}}-Option aus der [Baumansicht](Tree_view/de.md) oder dem [3D-Ansicht](3D_view/de.md)-Kontextmenü.
4.  Ein Menü wird neben dem Cursor angezeigt. Tue eins der folgenden Dinge:
    -   Wähle die Gruppe, in die Objekte verschoben werden sollen.
    -   Wähle {{MenuCommand|Ungroup}}, um die Objekte aus der/den Gruppe/n zu verschieben, in denen sie sich befinden.

## Hinweise

-   Objekte können auch Drag&Drop in der [Baumansicht](Tree_view/de.md) in die Gruppe verschoben werden.
-   Dieser Befehl kann benutzt werden, um Objekte in die [Draft UmschaltenKonstruktionsmodus](Draft_ToggleConstructionMode/de.md) zu verschieben, aber, im Gegensatz zu [Draft AddConstruction](Draft_AddConstruction/de.md)-Befehl gilt dies nicht für die [construction geometry color](Draft_ToggleConstructionMode/de#Preferences.md).
-   Für weitere Informationen zum organisieren deines Modells siehe [Dokumentstruktur](Document_structure/de.md) und [Arch-Tutorial](Arch_tutorial/de#Organizing_your_model.md).





 
