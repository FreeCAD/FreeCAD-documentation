# Drawing Workbench/de
**Der Arbeitsbereich '''Drawing''' ist nach Version 0.20 nicht länger Bestandteil von FreeCAD.<br>
Der Arbeitsbereich [TechDraw](TechDraw_Workbench/de.md) ist sein fortschrittlicherer Ersatz.**

<img alt="Drawing workbench icon" src=images/Workbench_Drawing.svg  style="width:128px;">



## Einführung

Das Zeichnungsmodul erlaubt dir, deine 3D Arbeit zu Papier zu bringen. Das bedeutet, gewählte Ansichten von deinen Modellen in einem 2D Fenster anzeigen und dieses Fenster in eine Zeichnung einzufügen, zum Beispiel in ein Blatt mit einer Umrandung, einem Titel und deinem Logo und druckt schließlich das Blatt.




<img alt="" src=images/Drawing_extraction.png  style="width:600px;">



## Werkzeuge

Diese Werkzeuge ermöglichen das Erstellen, Konfigurieren und exportieren von 2D Zeichnungen

-   <img alt="" src=images/Drawing_New.png  style="width:32px;"> [Skalierbare Vektorgrafik öffnen](Drawing_Open_SVG/de.md): Öffnet ein zuvor als SVG Datei gespeichertes Zeichnungsblatt

-   <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> [Neue A3 Querformat Zeichnung](Drawing_Landscape_A3/de.md): Erzeugt ein neues Zeichnungsblatt aus FreeCADs Standard A3 Vorlage

-   <img alt="" src=images/Drawing_View.png  style="width:32px;"> [Eine Ansicht einfügen](Drawing_View/de.md): Fügt eine Ansicht des ausgewählten Objekts in das aktive Zeichnungsblatt ein

-   <img alt="" src=images/Drawing_Annotation.png  style="width:32px;"> [Anmerkung](Drawing_Annotation/de.md): Fügt eine Anmerkung in das aktuelle Zeichnungsblatt ein

-   <img alt="" src=images/Drawing_Clip.png  style="width:32px;"> [Ausschnitt](Drawing_Clip/de.md): Fügt eine Ausschnittsgruppe in das aktuelle Zeichnungsblatt ein

-   <img alt="" src=images/Drawing_Openbrowser.png  style="width:32px;"> [Browser öffnen](Drawing_Openbrowser/de.md): Öffnet eine Vorschau des aktuellen Zeichnungsblatts in den Browser ein

-   <img alt="" src=images/Drawing_Orthoviews.png  style="width:32px;"> [Orthografische Ansichten einfügen](Drawing_Orthoviews/de.md): Orthografische Projektion eines Bauteils in die aktive Zeichnung einfügen

-   <img alt="" src=images/Drawing_Symbol.png  style="width:32px;"> [Symbol](Drawing_Symbol.md): Fügt den Inhalt einer SVG-Datei als ein Symbol auf das aktuelle Zeichnungsblatt ein.

-   <img alt="" src=images/Drawing_DraftView.png  style="width:32px;"> [Draft View](Draft_Drawing.md): Fügt eine spezielle Entwurfsansicht des ausgewählten Objekts in das aktuelle Zeichenblatt ein.

-   <img alt="" src=images/Drawing_SpreadsheetView.png  style="width:32px;"> [Spreadsheet View](Drawing_SpreadsheetView.md): Fügt eine Ansicht eines ausgewählten Rechenblatts in das aktuelle Zeichenblatt ein.

-   <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [Speichern](Drawing_Save/de.md): Speichert das aktuelle Blatt als SVG-Datei

-   [Project Shape](Drawing_ProjectShape.md): Erstellt eine Projektion des ausgewählten Objekts (Quelle) in der 3D-Ansicht.

-    **Note:**das [Draft Drawing](Draft_Drawing/de.md) Werkzeugt wird mit [Draft objects](Draft_Workbench/de.md) verwendet. Es verfügt über einige zusätzliche Funktionen gegenüber den Zeichenwerkzeugen und unterstützt spezifische Objekte wie[Entwurfsbemaßungen](Draft_Dimension/de.md).

## Arbeitsablauf

Das Dokument enthält ein 3D Formobjekt (Schenkel), von dem wir eine Zeichnung erstellen wollen. Deshalb wird eine \"Seite\" erstellt. Eine Seite wird aus einer Vorlage realisiert, z. B. aus der Vorlage \"A3_Landscape\". Die Vorlage ist ein [SVG](SVG/de.md) Dokument, das einen Seitenrahmen, ein Logo und andere Elemente enthalten kann.

In diese Seite können wir eine oder mehrere Ansichten einfügen. Jede Ansicht hat eine Position auf der Seite, einen Skalierungsfaktor und zusätzliche Eigenschaften. Jedes Mal, wenn sich die Seite oder die Ansicht oder das referenzierte Objekt ändert, wird die Seite regeneriert und die Seitenanzeige aktualisiert.

## Scripting

Im Moment ist der Arbeitsablauf der grafischen Benutzeroberfläche sehr begrenzt, daher ist die Skripten API interessanter.

Siehe die [Zeichnungs API Beispiel](Drawing_API_example/de.md) Seite für eine Beschreibung der Funktionen zum Erstellen von Zeichenblättern und Ansichten.



## Erweiterung des Zeichenmoduls 

Einige Hinweise auf der Programmierseite des Zeichenmoduls werden auf der Seite [Drawing Documentation/de](Drawing_Documentation/de.md) hinzugefügt. Dies soll helfen, die Funktionsweise des Zeichenmoduls schnell zu verstehen, so dass Programmierer schnell mit der Programmierung beginnen können.



## Externe Links 

-   [Einführung in technische Zeichnung auf Youtube - von Normal Universe](https://www.youtube.com/watch?v=1Hm5Zyjmjac)





{{Drawing Tools navi

}}



---
⏵ [documentation index](../README.md) > [Obsolete Workbenches](Category_Obsolete%20Workbenches.md) > [Drawing](Category_Drawing.md) > Drawing Workbench/de
