---
 GuiCommand:
   Name: Std SetAppearance
   Name/de: Std Darstellung
   MenuLocation: Ansicht , Darstellung…
   Workbenches: Material_Workbench/de, Part_Workbench/de, PartDesign_Workbench/de und weitere
   Shortcut: **Ctrl**+**D**
   SeeAlso: Std_SetMaterial/de, Part_ColorPerFace/de
---

# Std SetAppearance/de



## Beschreibung

Das Werkzeug **Std Darstellung** legt die Anzeigeeigenschaften der ausgewählten Objekte fest.

Diese Seite wurde für Version 1.0 aktualisiert.

![](images/Std_SetAppearance_Taskpanel.png ) 
*Der Aufgabenbereich Anzeigeeigenschaften*



## Anwendung

1.  Ein oder mehrere Objekt(e) auswählen.
2.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   Den Menüeintrag **Ansicht → <img src="images/Std_SetAppearance.svg" width=16px> Darstellung...** im Hauptmenü auswählen.
    -   Den Menüeintrag **<img src="images/Std_SetAppearance.svg" width=16px> Darstellung...** im Kontextmenü der [Baumansicht](Tree_view.md) (siehe Screenshot) oder im Kontextmenü der [3D-Ansicht](3D_view.md) auswählen.
    -   Das Tastaturkürzel **Ctrl**+**D**.
3.  Das Aufgaben-Fenster **Anzeigeeigenschaften** wird geöffnet. Siehe [Optionen](#Optionen.md).
4.  Eine oder mehrere Anzeigeeigenschaften ändern.
5.  Die Objekte werden sofort aktualisiert.
6.  Wahlweise weitere Objekte auswählen, deren Anzeigeeigenschaften geändert werden sollen.
7.  Schaltfläche **Schließen** drücken, um den Aufgabenbereich zu schließen und den Befehl abzuschließen.



## Optionen



### Ansichtsmodus

-   Einen Wert für die {{PropertyView/de|Display Mode}} (Anzeigemodus) aus der Ausklappliste auswählen. Die vorhandenen Optionen sind: {{Value|Flat lines}}, {{Value|Shaded}} (nicht für [Draft](Draft_Workbench/de.md)-Objekte), {{Value|Wireframe}} und {{Value|Points}}. Siehe Befehl [Std Darstellungsart](Std_DrawStyle/de.md) für weitere Informationen.



### Werkstoff

-   Ein Material in der Liste auswählen.
    1.  Wahlweise eine Kategorie in der Ausklappliste unter der Materialliste auswählen, um die Materialien zu filtern. Die vorhandenen Kategorien sind {{Value|Basic Appearance}}, {{Value|Texture Appearance}} (solche Materialien stehen noch nicht zur Verfügung) und {{Value|Alle Materials}}.
    2.  Wahlweise die Schaltfläche **Launch editor** drücken, um den [Material-Editor](Materials_Edit.md) zu starten.
-   **Custom appearance**: Die Schaltfläche **...** drücken, um das Erscheinungsbild des Materials zu überschreiben. Das Dialogfenster **Material properties** wird geöffnet. Siehe [Part FarbePro Fläche](Part_ColorPerFace/de#Anwendung.md).
-   **Farb-Plot:** Wird derzeit nicht unterstützt.
-   *Linienfarbe:*\' Legt die {{PropertyView/de|Line Color}} fest. Die Schaltfläche drücken, um den Farbauswahldialog zu öffnen.
-   **Punktfarbe:** Legt die {{PropertyView/de|Point Color}}fest. Die Schaltfläche drücken, um den Farbauswahldialog zu öffnen.



### Anzeige

-   **Punktgröße:** Legt die {{PropertyView/de|Point Size}} (in Pixeln) fest.
-   **Linienbreite:** Legt die {{PropertyView/de|Line Width}} (in Pixeln) fest.
-   **Transparenz:** Legt die {{PropertyView/de|Transparency}} (in Prozent) fest. 0% ist opak (undurchsichtig), 100% ist vollständig transparent.
-   **Linientransparenz:** Wird derzeit nicht unterstützt.



## Hinweise

-   Die genannten Ansicht-Eigenschaften können auch im [Eigenschafteneditor](Property_editor/de.md) geändert werden.





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std SetAppearance/de
