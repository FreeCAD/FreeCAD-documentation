---
 GuiCommand:
   Name: Std ProjectInfo
   Name/de: Std Projektinformationen
   MenuLocation: Datei , Dokumentinformationen...
   Workbenches: Alle
   Shortcut: -
   SeeAlso: Std_New/de
---

# Std ProjectInfo/de



## Beschreibung

Der Befehl **Std Projektinformationen** öffnet ein Dialogfeld mit Einzelheiten zum aktiven Dokument. Einige der Informationen können bearbeitet werden.



## Anwendung

1.  Den Menüeintrag **Datei → <img src="images/Std_ProjectInfo.svg" width=16px> Dokumentinformationen...** auswählen.
2.  EinDialogfenster mit den folgenden Informationen wird geöffnet:
    -   **Name**: Der Name des Dokuments. Entspricht der Eigenschaft Label des Dokuments. *Nicht überschreibbar.*
    -   **Pfad**: Der vollständige Dateipfad. Leer, wenn die Datei noch nicht gespeichert wurde. *Nicht überschreibbar.*
    -   **UUID**: FreeCADs automatisch erstellter Checksummenwert. *Nicht überschreibbar.*
    -   **Programmversion**: Die FreeCAD-Version, die beim Speichern der Datei verwendet wurde. Leer, wenn die Datei noch nicht gespeichert wurde. *Nicht überschreibbar.*
    -   **Einheitensystem**: Das Einheitensystem des Dokuments. *Ausgangswert hängt von der Einstellung [Standard-Einheitensystem](Preferences_Editor#Allgemein_2.md) ab.* <small>(v1.0)</small> 
    -   **Erstellt von**: Zur Eingabe des Namens des Bearbeiters. *Kann voreingestellt werden.*
    -   **Erstelldatum**: FreeCAD trägt automatisch das korrekte Datum ein. *Nicht überschreibbar.*
    -   **Zuletzt geändert von**: Zur Eingabe des Namens des Bearbeiters. *Kann voreingestellt werden.*
    -   **Zuletzt geändert am**: FreeCAD trägt automatisch das korrekte Datum ein. *Nicht überschreibbar.*
    -   **Firma**: Zur Eingabe eines Firmennamens. *Kann voreingestellt werden.*
    -   **Lizenzinformationen**: Zum Auswählen einer Lizenz in dem Ausklappmenü. *Kann voreingestellt werden.*
    -   **Lizenz-URL**: URL ändert sich automatisch entsprechend der ausgewählten Lizenz, kann aber überschrieben werden. *Kann voreingestellt werden.*
    -   **Kommentar**: Zur Eingabe eines geeigneten Kommentars.
3.  Die erforderlichen Informationen eintragen und die Schaltfläche **OK** drücken.



## Optionen

-   Drücke die **esc**-Taste oder klicke auf die Schaltfläche **Abbrechen** um abzubrechen.



## Einstellungen

Siehe auch: [Voreinstellungseditor](Preferences_Editor/de.md).

-   Einige der Dokumenteigenschaften wie Name, Firma und Lizenzinformationen, können voreingestellt werden: **Bearbeiten → Einstellungen... → Allgemein → Dokument → Autorenschaft und Lizenz**.





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std ProjectInfo/de
