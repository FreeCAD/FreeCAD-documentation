 {{TutorialInfo/de
|Topic= Import von Text und Geometrie aus Inkscape
|Level= Anfänger
|Time= 30 Minuten
|Author=r-frank
|FCVersion=0.16.6704
|Files=
}}

## Einführung

Dieses Tutorium soll zeigen, wie Text oder Geometrie, die mit InkScape im svg-Format erstellt wurden, in FreeCAD importiert werden können.
Für diese Bearbeitungen werden Inkscape 0.91 und FreeCAD 0.16.6704 unter Windows verwendet.

## Allgemeine Tips zum Importieren aus inkscape 

-   der svg-Import in FreeCAD kann eine svg Datei mit einer Auflösung von mehr als 45 dpi nicht verarbeiten, überprüfe daher die Einstellungen in inkscape
-   wenn das Importieren von Pfadobjekten, die in der 3D Ansicht in FreeCAD erscheinen, nicht sehr glatt verläuft, kann es eine Frage der FreeCAD Einstellungen für die Formansicht sein.
    -   in FreeCAD wähle ** Bearbeiten** → ** Voreinstellungen** → ** Part Design** → ** Formansicht**
    -   wie für \"Tesselation\", die \"Maximale Abweichung je nach Modell Bindungs Kasten\" ist der Standardwert \"0,5 %\".
    -   die Einstellung auf einen niedrigeren Wert erhöht die Glätte des Modells in der 3D Ansicht (und verbraucht mehr PC Leistung)
    -   verwende keine Werte unter \"0,01 %\", dies wird höchstwahrscheinlich FreeCAD zum Absturz bringen.
    -   in diesem Fall löst das Löschen von \"system.cfg\" und \"user.cfg\" in deinem FreeCAD Benutzer Verzeichnis dieses Problem

-   In inkscape nach dem Einfügen von Text (und vielleicht nach dem Anwenden von Effekten wie Biegen oder etwas anderem) stelle sicher das
    -   wähle deinen Text aus und wähle ** Pfad** → ** Objekt zu Pfad**
    -   Gruppierung deiner Objekte aufheben
    -   speichere als \"Einfaches SVG (\*.svg)\" Dateiformat
-   Öffne die Datei in FreeCAD und wähle die Option \"SVG als Geometrie (importSVG)\".
-   ein Pfadobjekt für jeden Buchstaben/jede Zahl/jedes Zeichen wird in der Baumansicht erstellt
-   verwende [Entwurf](Draft_Workbench/de.md) [upgrade Werkzeug](Draft_Upgrade/de.md) auf jedem Pfadobjekt, um Flächen zu erzeugen
-   verwende Polster oder [Part](Part_Workbench/de.md) [Extrusionswerkzeug](Part_Extrude/de.md) auf den Flächen verwenden, um Volumenkörper zu erhalten
-   Du kannst deine Objekte verschmelzen oder Verbund verwenden, je nachdem, was du für deine weitere Arbeit vorhast

## Importieren von Geometrie aus InkScape 

Da inkscape und FreeCAD unterschiedliche Ansätze zur Anwendung von Bemaßungen auf svg-Objekte zu haben scheinen, scheint der empfohlene Arbeitsablauf zu sein:

-   Gruppiere alle Objekte in inkscape
-   wähle alle Objekte in inkscape aus
-   wende einen Strichstil mit einer Breite von 0 mm (ja, das sind null Millimeter) auf alle Objekte an
-   als \"Inkscape SVG (\*.svg)\" oder \"Einfaches SVG (\*.svg)\" Dateiformat speichern
-   Öffne die Datei in FreeCAD und wähle die Option \"SVG als Geometrie (importSVG)\".
-   die Abmessungen der Objekte in inkscape und in FreeCAD sollten jetzt identisch sein

## Danksagungen

Dank an die Benutzer \"freecad-heini-1\" und \"herbk\" für die Tests und die wertvolle Rückmeldung.




