---
 GuiCommand:
   Name: Draft AddToGroup
   Name/de: Draft ZurGruppeHinzufügen
   MenuLocation: Dienstprogramme , Zur Gruppe hinzufügen...
   Workbenches: Draft_Workbench/de
   SeeAlso: Std_Group/de, Draft_AddNamedGroup/de, Draft_AddConstruction/de, Draft_AutoGroup/de
---

# Draft AddToGroup/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_AddToGroup.svg  style="width:24px;"> **Draft ZuGruppeHinzufügen** verschiebt Objekte in eine [Std Gruppe](Std_Group/de.md) oder ein gruppenartiges [BIM](BIM_Workbench/de.md)-Objekt. Damit können auch Objekte aus einer Gruppe entfernt werden.



## Anwendung

1.  Ein oder mehrere Objekte auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Draft_AddToGroup.svg" width=16px> [In Gruppe verschieben...](Draft_AddToGroup/de.md)** drücken.
    -   Den Menüeintrag **Dienstprogramme → <img src="images/Draft_AddToGroup.svg" width=16px> In Gruppe verschieben...** auswählen oder die Menüoption im Kontextmenü der [Baumansicht](Tree_view/de.md) oder [3D-Ansicht](3D_view/de.md) auswählen.
3.  Ein Menü wird neben dem Cursor angezeigt. Eine der folgenden Möglichkeiten auswäheln:
    -   
        **Gruppierung aufheben**
        
        auswählen, um die Objekte aus den Gruppen, in denen sie sich befinden, heraus zu bewegen.

    -   Die Gruppe auswählen, in die die Objekte verschoben werden sollen.

    -   
        **+ Neue Gruppe hinzufügen**
        
        auswählen, um die Objekte in eine neue Gruppe zu bewegen:

        1.  Der Aufgaben-Bereich **Gruppe hinzufügen** wird geöffnet.
        2.  Einen **Gruppennamen** eingeben.
        3.  Die Schaltfläche **OK** drücken.



## Hinweise

-   Objekte können auch Drag&Drop in der [Baumansicht](Tree_view/de.md) in die Gruppe verschoben werden.
-   Dieser Befehl kann benutzt werden, um Objekte in die [Draft UmschaltenKonstruktionsmodus](Draft_ToggleConstructionMode/de.md) zu verschieben, aber, im Gegensatz zu [Draft AddConstruction](Draft_AddConstruction/de.md)-Befehl gilt dies nicht für die [construction geometry color](Draft_ToggleConstructionMode/de#Preferences.md).
-   Für weitere Informationen zum organisieren deines Modells siehe [Dokumentstruktur](Document_structure/de.md) und [Arch-Tutorial](Arch_tutorial/de#Organizing_your_model.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft AddToGroup/de
