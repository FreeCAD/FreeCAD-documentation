

## Einleitung

Die [Berichtsansicht](Report_view/de.md) ist eine Konsole, die Textnachrichten von FreeCAD Prozessen und Werkzeugen anzeigt. Sie ist im Menü {{MenuCommand|{{StdMenu|[Ansicht](Std_View_Menu/de.md)}} verfügbar. → Konsole → Berichtsansicht}}.

Bestimmte Eigenschaften dieser Konsole, wie die Farbe des Textes und ob er bei Warnungen oder Fehlern automatisch angezeigt werden soll, können im {{MenuCommand|Allgemein→ Ausgabefenster}} Reiter des [Einstellungseditor](Preferences_Editor/de.md) konfiguriert werden.

<img alt="" src=images/FreeCAD_Report_view.png  style="width:800px;">


*Die Berichtsansicht zeigt Meldungen an, wenn FreeCAD gerade gestartet wurde.*

## Meldungen


**Siehe auch:**

[Konsole API](Console_API/de.md), und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Die Berichtsansicht zeigt Meldungen der internen FreeCAD `Console` Klasse an.

-    `FreeCAD.Console.PrintMessage("text")`, druckt jede Art von informativer Meldung, die kein Fehlverhalten impliziert; z.B. die Koordinaten von Punkten, das Ergebnis einer Abstandsberechnung, die Anzahl der Scheitelpunkte in einer Form, usw. Standardmäßig in schwarzer Farbe.

-    `FreeCAD.Console.PrintWarning("text")`, druckt Meldungen, die den Benutzer vor seltsamem Verhalten in der Anwendung warnen sollen. Warnungen sollten angezeigt werden, wenn eine bestimmte Funktionalität fehlt, die Software aber noch akzeptabel funktioniert. Standardmäßig in gelber Farbe.

-    `FreeCAD.Console.PrintError("text")`, druckt Meldungen, die als Fehlermeldungen gedacht sind, d.h. wenn eine kritische Komponente fehlt, die eine bestimmte Operation fehlschlagen lässt. Standardmäßig in roter Farbe.

-    `FreeCAD.Console.PrintLog("text")`, druckt Meldungen, die in die Logs gehen. Diese Meldungen können alles sein, was für die zukünftige Fehlersuche durch das Lesen der Logs nützlich ist, z. B. das Starten oder Schließen einer Workbench. Standardmäßig in blauer Farbe.

Diese Funktionen können direkt von der [Python Konsole](Python_console/de.md) oder von [Makros](Macros/de.md) und benutzerdefinierten Arbeitsbereichen aus verwendet werden.

<img alt="" src=images/FreeCAD_Report_view_example.png  style="width:800px;">


*Beispielmeldungen in der Berichtsansicht: eine allgemeine Meldung, eine Warnung, ein Fehler und eine protokollierte Meldung.*

## Maßnahmen

Rechtsklick auf die Berichtsansicht zeigt einige Befehle:

-    {{MenuCommand|Optionen}}: Protokollierung, Warnung, Fehler, Python Ausgabe umleiten, Python Fehler umleiten, zum Ende gehen.

-    {{MenuCommand|Kopieren}}: speichert den markierten Text in der Zwischenablage zum späteren Einfügen; er ist deaktiviert, wenn nichts markiert ist.

-    {{MenuCommand|Alles markieren}}: wählt den gesamten Text in der Berichtsansicht aus.

-    {{MenuCommand|Löschen}}: löscht alle Meldungen in der Berichtsansicht. Dies ist nützlich, wenn du eine Fehlersuche bei einem Werkzeug durchführen willst, das Meldungen in der Berichtsansicht ausgibt, und sicher sein willst, dass keine alten Meldungen von früheren Werkzeugen vorhanden sind.

-    {{MenuCommand|Speichern als}}: speichert die Meldungen in der Berichtsansicht in einer Textdatei.


{{Interface navi

}} {{Std Base navi}} 
