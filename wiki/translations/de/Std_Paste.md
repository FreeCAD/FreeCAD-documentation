---
- GuiCommand:
   Name: Std Paste
   Name/de: Std Einfügen
   MenuLocation: Bearbeiten - Einfügen
   Workbenches: Alle
   Shortcut: ** Strg**+**V**
   SeeAlso: [Std Ausschneiden](Std_Cut/de.md), [Std Kopieren](Std_Copy/de.md), [Std AuswahlDuplizieren](Std_DuplicateSelection/de.md)
---

# Std Paste/de



## Beschreibung

Der Befehl **Std Einfügen** fügt Objekte aus der Zwischenablage in das aktuelle Dokument ein.



## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/Std_Paste.svg" width=16px> [Einfügen](Std_Paste/de.md)** drücken.
    -   Den Menüeintrag **Bearbeiten → <img src="images/Std_Paste.svg" width=16px> Einfügen** im Hauptmenü auswählen.
    -   Den Menüeintrag **<img src="images/Std_Paste.svg" width=16px> Einfügen** im Kontextmenü der [Baumansicht](Tree_view/de.md) auswählen. Diese option steht nur dann zur Verfügung, wenn ein vorhandendes Objekt ausgewählt wurde.
    -   Das Tastaturkürzel **Strg**+**V**.



## Hinweise

-   FreeCAD ändert die internen Namen automatisch und, abhängig von den Einstellungen, auch die Label der Objekte, um Namenskonflikte zu vermeiden.
-   Ein Zellen-Alias einer Kalkulationstabelle, der schon in der Tabelle existiert, wird nicht eingefügt.
-   Wenn man in FreeCAD in einem Textfenster, einem Eingabefeld, oder einer Kalkulationstabelle arbeitet, ruft das Tastaturkürzel **Strg**+**V** in fast allen Fällen nicht den Befehl **Std Einfügen** auf, sondern verwendet stattdessen die Funktion Einfügen des Betriebssystems.
-   Es ist nicht möglich mit FreeCAD erzeugte Objekte durch Kopieren und Einfügen zwischen FreeCAD und anderen Anwendungen auszutauschen.



## Einstellungen

-   Duplizierte Label sind erlaubt, wenn **Werkzeuge → Parameter bearbeiten... → BaseApp → Preferences → Document → DuplicateLabels** auf `True` gesetzt ist. Diese Einstellung kann auch im [Voreinstellungseditor](Preferences_Editor/de#Dokument.md) geändert werden.





{{Std Base navi

}}



---
⏵ [documentation index](../README.md) > Std Paste/de
