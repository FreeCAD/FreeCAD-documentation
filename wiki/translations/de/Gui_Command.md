# Gui Command/de
Der Gui Befehl ist eine der wichtigsten Funktionen von FreeCAD. im Hauptinteraktionspunkt des Benutzers. Jedes Mal, wenn der Benutzer einen Menüpunkt auswählt oder eine Schaltfläche in der Werkzeugleiste drückt , die einen Gui Befehl aktiviert. Einige der Attribute eines Gui Befehls sind:

-   Definiert einen Namen
-   Enthält ein Symbol
-   Definiert den Umfang für ein Rückgängigmachen/Wiederherstellen.
-   Hat eine Hilfeseite
-   Öffnet und kontrolliert Dialoge
-   Makro Aufnahme
-   und andere.

## Benennung

Der Gui Befehl wird standardmäßig benannt: *ModuleName\_CommandName*. z.B. \"[Base\_Open](Base_Open/de.md)\" Dies ist der Open Gui Befehl im Basissystem. Der Gui Befehl in einem bestimmten Modul wird mit dem Modulnamen benannt. davor z.B. \"[Teil Zylinder](Part_Cylinder/de.md)\"

Wenn die Dokumentation noch nicht fertig ist, verwende _.

## Hilfeseite

Jeder Gui Befehl muss eine Hilfeseite haben. Die Hilfeseite wird auf der Seite FreeCAD Dokumentations Wiki. Der Artikel hat den gleichen Namen wie der Gui Befehl, z.B. [Draft ShapeString](Draft_ShapeString.md).

Um Deine eigenen Hilfeseiten zu erstellen, kannst Du die Vorlage [GuiCommand model](GuiCommand_model.md) verwenden.

Beispiel:

-   [Entwurf FormString](Draft_ShapeString/de.md)
-   [Entwurfslinie](Draft_Line/de.md)

## Symbole

<img alt="" src=images/Tango-Palette.png  style="width:400px;">

Jeder GuiBefehl muss ein Symbol haben. Wir verwenden das [Tango Symbolsatz](http://tango-project.org/Tango_Desktop_Project/) und seine Richtlinien. Auf der rechten Seite siehst du die Tango Farbpalette.

Alle Symbole sollten im Format [SVG](SVG.md) mit einer Vektorbildanwendung, wie beispielsweise [Inkscape](http://inkscape.org), erstellt werden. Dies erleichtert die Übernahme von Änderungen und die Ableitung von Änderungen. zusätzliche Symbole im gleichen Anwendungsbereich.

### Symbol Farbkodierungstabelle 

<img alt="" src=images/Colorchart.png  style="width:200px;">

Wir versuchen so weit wie möglich, dieses Diagramm zu respektieren, so dass die Farbe der Symbole eine direkte Bedeutung hat.

## Qualitätsanforderungen


**Die [Complete Workbench](Complete_Workbench/de.md) ist veraltet, sie enthält nicht mehr jeden der Befehle in FreeCAD.**

Es gibt viele Gui Befehle (Werkzeuge) in FreeCAD, die experimentell sind. oder für kurze Zeit genutzt werden, um die Implementierung neuer Funktionen zu testen. Diese Gui Befehle befinden sich meist in den zugeordneten Arbeitsbereichen wie Part, Mesh oder Cam. Um ein gutes Benutzererlebnis zu gewährleisten, wurde der Arbeitsbereich *Complete* erstellt. Dieser Arbeitsbereich enthält alle Gui Befehle die bestimmte Qualitätsanforderungen erfüllen, die hier beschrieben werden:

-   Der Befehl oder die Funktion muss \"fertig\" sein, d.h. es handelt sich nicht um eine laufende Arbeit.
-   Es muss ein geeignetes Symbol und eine korrekte Menüposition eingerichtet werden.
-   Es muss eine Hilfeseite haben, wie [Draft ShapeString](Draft_ShapeString/de.md).
    -   Alle Felder in _ müssen ausgefüllt werden.
    -   Es sollte eine detaillierte Beschreibung des Befehls und aller Parameter und Einstellungen enthalten.
    -   Es sollte ein Bild der Dialoge haben, die der Befehl erzeugen wird.
    -   Es sollte eine Beschreibung der zugehörigen [Python](Python.md) Schnittstellen und Klassen mit Beispielcode enthalten.

Hoffentlich wird dies für alle Gui Befehle in der [List of Commands](List_of_Commands/de.md). wahr.


{{Powerdocnavi

}}

---
[documentation index](../README.md) > Gui Command/de
