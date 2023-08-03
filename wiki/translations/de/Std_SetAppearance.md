---
 GuiCommand:
   Name: Std SetAppearance
   Name/de: Std Darstellung
   MenuLocation: Ansicht , Darstellung…
   Workbenches: Alle
   Shortcut: Ctrl + D
   SeeAlso: Part_FaceColors/de
---

# Std SetAppearance/de

## Beschreibung

Das Werkzeug **Darstellung** zeigt im [Aufgabenbereich](Task_panel.md) die Anzeigeeigenschaften der ausgewählten Objekte an.

<img alt="" src=images/DlgDisplayProperties.png  style="width:250px;"> 
*Der Aufgabenbereich Anzeigeeigenschaften*

## Anwendung

1.  Ein oder mehrere Objekt(e) auswählen.
2.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   Den Menüeintrag **Ansicht → <img src="images/Std_SetAppearance.svg" width=16px> Darstellung...** im Hauptmenü auswählen.
    -   Den Menüeintrag **<img src="images/Std_SetAppearance.svg" width=16px> Darstellung...** im Kontextmenü der [Baumansicht](Tree_view.md) (siehe Screenshot) oder im Kontextmenü der [3D-Ansicht](3D_view.md) auswählen.
    -   Das Tastaturkürzel **Ctrl**+**D**.
3.  Eine oder mehrere Anzeigeeigenschaften ändern. Siehe [Optionen](#Optionen.md). Die Objekte werden sofort aktualisiert.
4.  Optional können weitere Objekte ausgewählt werden, deren Anzeigeeigenschaften geändert werden sollen.
5.  Schaltfläche **Schließen** drücken, um den Aufgabenbereich zu schließen und den Befehl abzuschließen.

## Optionen

### Ansichtsmodus

-   Einen **Anzeigemodus** Aus der Ausklappliste auswählen. Die vorhandenen Optionen sind: \'Flat lines\', \'Shaded\' (nicht für [Draft](Draft_Workbench/de.md)-Objekte), \'Wireframe\' and \'Points\'. Siehe Befehl [Std Zeichenstil](Std_DrawStyle/de.md) für weitere Informationen.

### Werkstoff

-   Ein vorgefertigtes Material aus dem Ausklappmenü auswählen (\'Standard\', \'Aluminium\', \'Messing\', \'Bronze\', etc.).
-   Die Schaltfläche **...** drücken, um das Dialogfeld Material zu öffnen und die Werte für Umgebungsfarbe, Streufarbe, Ausstrahlfarbe und Glanzfarbe sowie Glanz zu bearbeiten.
-   **Farb-Plot:** Wird derzeit nicht unterstützt.
-   **Flächenfarbe:** Legt die {{PropertyView/de|Shape Color}} fest. Die Schaltfläche drücken, um den Farbauswahldialog zu öffnen.
-   *Linienfarbe:*\' Legt die {{PropertyView/de|Line Color}} fest. Die Schaltfläche drücken, um den Farbauswahldialog zu öffnen.
-   **Punktfarbe:** Legt die {{PropertyView/de|Point Color}}fest. Die Schaltfläche drücken, um den Farbauswahldialog zu öffnen.

### Anzeige

-   **Punktgröße:** Legt die {{PropertyView/de|Point Size}} (in Pixeln) fest.
-   **Linienbreite:** Legt die {{PropertyView/de|Line Width}} (in Pixeln) fest.
-   **Transparenz:** Legt die {{PropertyView/de|Transparency}} (in Prozent) fest. 0% ist opak (undurchsichtig), 100% ist vollständig transparent.
-   **Linientransparenz:** Wird derzeit nicht unterstützt.

## Hinweise

-   Die genannten Anzeigeeigenschaften können auch im [Eigenschafteneditor](Property_editor/de.md) oder in der [Combo-Ansicht](Combo_view/de.md) geändert werden.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std SetAppearance/de
