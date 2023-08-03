---
 GuiCommand:
   Name: Draft AddToGroup
   Name/de: Draft ZurGruppeHinzufügen
   MenuLocation: Dienstprogramme , Zur Gruppe hinzufügen...
   Workbenches: Draft_Workbench/de, Arch_Workbench/de
   SeeAlso: Std_Group/de, Draft_AddNamedGroup/de, Draft_AddConstruction/de, Draft_AutoGroup/de
---

# Draft AddToGroup/de



## Beschreibung

Der <img alt="" src=images/Draft_AddToGroup.svg  style="width:24px;"> **Draft AddToGroup**-Befehl verschiebt Objekte in eine[Std Gruppe](Std_Group/de.md). Damit können auch Objekte von der aktuellen Gruppe entfernt werden.

In FreeCAD v0.20 kann der Befehl auch gruppenähnliche [Arch](Arch_Workbench/de.md)-Objekte handhaben.



## Anwendung

1.  Ein oder mehrere Objekte auswählen.
2.  Es gibt mehrere Wege, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_AddToGroup.svg" width=16px> [In Gruppe verschhieben...](Draft_AddToGroup/de.md)** drücken.
    -   Den Menüeintrag **Utilities → <img src="images/Draft_AddToGroup.svg" width=16px> In Gruppe verschhieben...** auswählen.
    -   Den Eintrag **Dienstprogramme → <img src="images/Draft_AddToGroup.svg" width=16px> In Gruppe verschhieben...** im Kontextmenü der [Baumansicht](Tree_view/de.md) oder der [3D-Ansicht](3D_view/de.md) auswählen.
3.  Ein Menü wird neben dem Cursor angezeigt. Tue eins der folgenden Dinge:
    -   
        **Ungroup**
        
        auswählen, um die Objekte aus der/den Gruppe/n zu verschieben, in denen sie sich befinden.

    -   Die Gruppe auswählen, in die die Objekte verschoben werden sollen.

    -   
        **+ Neue Gruppe hinzufügen**
        
        auswählen, um die Objekte in eine neue Gruppe zu bewegen: {{Version/de|0.20}}

        1.  Der Aufgaben-Bereich **Gruppe hinzufügen** wird geöffnet.
        2.  Einen **Gruppennamen** eingeben.
        3.  Die Schaltfläche **OK** drücken.



## Hinweise

-   Objekte können auch Drag&Drop in der [Baumansicht](Tree_view/de.md) in die Gruppe verschoben werden.
-   Dieser Befehl kann benutzt werden, um Objekte in die [Draft UmschaltenKonstruktionsmodus](Draft_ToggleConstructionMode/de.md) zu verschieben, aber, im Gegensatz zu [Draft AddConstruction](Draft_AddConstruction/de.md)-Befehl gilt dies nicht für die [construction geometry color](Draft_ToggleConstructionMode/de#Preferences.md).
-   Für weitere Informationen zum organisieren deines Modells siehe [Dokumentstruktur](Document_structure/de.md) und [Arch-Tutorial](Arch_tutorial/de#Organizing_your_model.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft AddToGroup/de
