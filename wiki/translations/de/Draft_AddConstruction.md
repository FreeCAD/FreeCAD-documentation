---
 GuiCommand:
   Name: Draft AddConstruction
   Name/de: Draft HilfsgeometrieHinzufügen
   MenuLocation: Werkzeuge , Zur Hilfsgeometriegruppe hinzufügen<br>Dienstprogramme , Zur Hilfsgeometriegruppe hinzufügen
   Workbenches: Draft_Workbench/de, BIM_Workbench/de
   Version/de: 0.17
   SeeAlso: Draft_ToggleConstructionMode/de, Draft_AddToGroup/de
---

# Draft AddConstruction/de



## Beschreibung

Der Befehl <img alt="" src=images/Draft_AddConstruction.svg  style="width:24px;"> **Draft HilfsgeometrieHinzufügen** verschiebt Objekte in die [Draft-Hilfsgeometriegruppe](Draft_ToggleConstructionMode/de.md). Er wendet auch die [Hilfsgeometriefarbe](Draft_ToggleConstructionMode/de#Einstellungen.md) auf die Objekte an.



## Anwendung

1.  Ein oder mehrere Objekte auswählen.
2.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   [Draft](Draft_Workbench/de.md): Die Schaltfläche **<img src="images/Draft_AddConstruction.svg" width=16px> [Zur Hilfsgeometriegruppe hinzufügen](Draft_AddConstruction/de.md)** drücken.
    -   Draft: Den Menüeintrag **Dienstprogramme → <img src="images/Draft_AddConstruction.svg" width=16px> Zur Hilfsgeometriegruppe hinzufügen** auswählen oder die Menüoption im Kontextmenü der [Baumansicht](Tree_view/de.md) oder der [3D-Ansicht](3D_view/de.md) auswählen.
    -   [BIM](BIM_Workbench/de.md): Den Menüeintrag **Werkzeuge → <img src="images/Draft_AddConstruction.svg" width=16px> Zur Hilfsgeometriegruppe hinzufügen** auswählen.
3.  Falls sie noch nicht existiert, wird die Hilfsgeometriegruppe zuerst erstellt.
4.  Die Objekte werden zur Hilfsgeometriegruppe hinzugefügt und ihre Farbeigenschaften geändert.



## Hinweise

-   Objekte können auch durch ziehen und fallen lassen (drag&drop) auf die Gruppen in der [Baumansicht](Tree_view/de.md) zur Konstruktionsgruppe hinzugefügt werden oder durch Verwendung des [Draft ZurGruppehinzufügen](Draft_AddToGroup/de.md)-Befehls. Allerdings wird in beiden Fällen die [Hilfskonstruktionsfarbe](Draft_ToggleConstructionMode/de#Einstellungen.md) nicht angewendet.
-   Mehr Informationen zur Organisation deines Modells findest du unter [Dokumentstruktur](Document_structure/de.md) und [Arch Tutorium](Arch_tutorial/de#Ihr_Modell_organisieren.md).



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft AddConstruction/de
