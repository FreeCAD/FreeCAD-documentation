# Report view/de
## Einleitung

Das [Ausgabefenster](Report_view/de.md) ist der Bereich, der Textnachrichten von FreeCAD-Prozessen und -Werkzeugen anzeigt. Es ist im Menü **{{StdMenu|[Ansicht](Std_View_Menu/de.md)** → Paneele → Ausgabefenster}} verfügbar..

Bestimmte Eigenschaften dieses Bereiches, wie die Farbe des Textes und ob er bei Warnungen oder Fehlern automatisch angezeigt werden soll, können im **Allgemein → Ausgabefenster** Reiter des [Einstellungseditors](Preferences_Editor/de#Ausgabefenster.md) konfiguriert werden.

<img alt="" src=images/FreeCAD_Report_view.png  style="width:800px;">



*Die Meldungen des Ausgabefensters nachdem FreeCAD gerade gestartet wurde.*



## Meldungen


**Siehe auch:**

[Console API](Console_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Ausgabefenster zeigt Meldungen der internen FreeCAD-Klasse `Console` an.

-    `FreeCAD.Console.PrintMessage("text")`, druckt jede Art von informativer Meldung, die kein Fehlverhalten impliziert; z.B. die Koordinaten von Punkten, das Ergebnis einer Abstandsberechnung, die Anzahl der Knotenpunkte einer Form usw. Standardmäßig in Schwarz.

-    `FreeCAD.Console.PrintWarning("text")`, druckt Meldungen, die den Benutzer vor ungewöhnlichem Verhalten der Anwendung warnen sollen. Warnungen sollten angezeigt werden, wenn eine bestimmte Funktionalität fehlt, die Software aber noch akzeptabel funktioniert. Standardmäßig in Gelb.

-    `FreeCAD.Console.PrintError("text")`, druckt Meldungen, die als Fehlermeldungen gedacht sind, d.h. wenn eine kritische Komponente fehlt, die eine bestimmte Operation fehlschlagen lässt. Standardmäßig in Rot.

-    `FreeCAD.Console.PrintLog("text")`, druckt Meldungen, die in Berichtsdateien (logs) protokolliert werden. Diese Meldungen können alles sein, was nützlich ist für eine zukünftige Fehlersuche durch Auslesen der Berichtsdateien, z. B. das Starten oder Schließen eines Arbeitsbereichs. Standardmäßig in Blau.

Diese Funktionen können direkt von der [Python-Konsole](Python_console/de.md) aus oder in [Makros](Macros/de.md) und benutzerdefinierten Arbeitsbereichen verwendet werden.

<img alt="" src=images/FreeCAD_Report_view_example.png  style="width:800px;">



*Beispielmeldungen im Ausgabefenster: Eine allgemeine Meldung, eine Warnung, ein Fehler und eine protokollierte Meldung.*



## Maßnahmen

Ein Rechtsklick auf das Ausgabefenster öffnet ein Kontextmenü mit den folgenden Befehlen:

-    **Optionen**:

    -   
        **Nachrichtenarten anzeigen**
        
        : siehe [Voreinstellungseditor](Preferences_Editor/de#Output_window.md).

    -   
        **Show Report view on**
        
        : wie vorher.

    -   
        **Python-Ausgabe umleiten**
        
        : wie vorher.

    -   
        **Python-Fehler umleiten**
        
        : wie vorher.

    -   
        **Go to end**
        
        : Wenn aktiviert, wird zur untersten Zeile gescrollt, wenn eine neue Meldung hinzugefügt wird.

-    **Kopieren**: speichert den markierten Text in der Zwischenablage zum späteren Einfügen; er ist deaktiviert, wenn nichts markiert ist.

-    **Alles auswählen**: wählt den gesamten Text in der Berichtsansicht aus.

-    **Löschen**: löscht alle Meldungen in der Berichtsansicht. Dies ist nützlich, wenn du eine Fehlersuche bei einem Werkzeug durchführen willst, das Meldungen in der Berichtsansicht ausgibt, und sicher sein willst, dass keine alten Meldungen von früheren Werkzeugen vorhanden sind.

-    **Speichern unter**: speichert die Meldungen in der Berichtsansicht in einer Textdatei.


{{Interface navi

}} {{Std Base navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Report view/de
