# 3D view/de


## Einleitung


{{TOCright}}

Die [3D Ansicht](3D_view/de.md) von FreeCAD ist eine Instanz von Coin3D [Szenegraph](Scenegraph/de.md) die das wichtigste Fenster in der [Benutzeroberfläche](interface/de.md) bildet. Coin3D ist eine Bibliothek, die den OpenInventor 2.1 Szenenbeschreibungsstandard implementiert.

Bestimmte Eigenschaften der Ansicht, wie Hintergrundfarbe, [Mausnavigation](Mouse_navigation/de.md) Stil und Zoomschritte, können in der Datei [Voreinstellungseditor](Preferences_Editor/de.md).

<img alt="" src=images/FreeCAD_3D_view.png  style="width:600px;">


*Die [Arbeitsbereich Entwurf](3D_view]]_ist_ein_Bestandteil_der_FreeCAD__[[interface]]. Standardmäßig zeigt sie ein kleines Widget mit Koordinatenachsen und den Navigationswürfel ebenfalls mit Koordinatenachsen; das Raster kann durch Laden der [[Draft Workbench/de.md) angezeigt und konfiguriert werden.*

## Maßnahmen


**Hinweis:**

Verknüpfe Aktionen <small>(v0.19)</small> .

Since the [Baumansicht](tree_view/de.md) listet die meisten Objekte auf, die in der 3D-Ansicht sichtbar sind, viele der Aktionen sind identisch mit denen, die über die Funktion [Baumansichtausgeführt](tree_view/de.md) werden können.

Wenn die Standardeinstellung [Arbeitsbereich Start](Start_Workbench/de.md) aktiv ist, zeigt ein Rechtsklick auf die 3D-Ansicht nur einen Befehl:

-    **[Navigationsstile](Mouse_navigation.md)**: verschiedene Tastenstile zur Verwendung mit einer 3-Tasten-Maus oder einem Laptop Trackpad.

Sobald jedoch ein [Arbeitsbereich](Workbenches/de.md) geladen ist, gibt es zusätzliche Befehle:

-    {{MenuCommand/de|Link Aktionen}}: [Link erstellen](Std_LinkMake/de.md).

    -   
        {{MenuCommand/de|Link Gruppe erstellen}}
        
        : [Einfache Gruppe](Std_LinkMakeGroup/de.md),

[Group mit Links](Std_LinkMakeGroup/de.md), [Gruppe mit Transformations Links](Std_LinkMakeGroup/de.md).

-    {{MenuCommand/de|[Einpassen Alles](Std_ViewFitAll/de.md)}}: schwenkt und zoomt die Ansicht so, dass alle Objekte im Dokument auf dem Bildschirm angezeigt werden.

-    {{MenuCommand/de|[Anpassung Auswahl](Std_ViewFitSelection/de.md)}}: schwenkt und zoomt die Ansicht, um das aktuell ausgewählte Objekt auf dem Bildschirm festzuhalten.

-    {{MenuCommand/de|[Zeichenstil](Std_DrawStyle/de.md)}}: wie es ist, flache Linien, schattiert, Drahtgitter, Punkte, versteckte Linie, keine Schattierung.

-    {{MenuCommand/de|[Standardansichten](Std_View_Menu/de.md)}}: [Isometrisch](Std_ViewIsometric/de.md), [Front](Std_ViewFront/de.md), [Top](Std_ViewTop/de.md), [Right](Std_ViewRight/de.md), [Rear](Std_ViewRear/de.md), [Bottom](Std_ViewBottom/de.md), [Links](Std_ViewLinks/de.md), [Links drehen](Std_ViewRotateLinks/de.md), [Rechts drehen](Std_ViewRotateRechts/de.md).

-    {{MenuCommand/de|Messung}}: [Toggle Messung](View_Measure_Toggle_All/de.md), [clear measurement](View_Measure_Clear_All/de.md).

-    {{MenuCommand/de|Dokumentenfenster}}: [docked](Std_ViewDockUndockFullscreen/de.md), [undocked](Std_ViewDockUndockFullscreen/de.md) und [fullscreen](Std_ViewDockUndockFullscreen/de.md).

Darüber hinaus können je nach aktivem Arbeitsbereich und aktivem Objekt weitere kontextabhängige Befehle verfügbar werden.

Zum Beispiel mit dem [Part Arbeitsbereich](Part_Workbench/de.md) und ein Objekt ausgewählt:

-    {{MenuCommand/de|[Erscheinungsbild](Std_SetAppearance/de.md)}}: startet den Dialog zum Ändern der Farbe und Größe von Linien und Eckpunkten sowie der Farbe von Flächen.

-    {{MenuCommand/de|[Sichtbarkeit umschalten](Std_ToggleVisibility/de.md)}}: macht das Objekt in der 3D Ansicht sichtbar oder unsichtbar.

-    {{MenuCommand/de|[Wählbarkeit umschalten](Std_ToggleSelectability/de.md)}}: macht das Objekt in der 3D Ansicht nicht mehr auswählbar; verwende diesen Befehl erneut, um den Effekt aufzuheben. Es setzt die Parameter des Objekts. `Selectable` verweise auf `True` oder `False`. Ändere die Eigenschaft durch Umschalten {{PropertyView/de|Wählbar}} im [Eigenschaftseditor](property_editor/de.md).

-    {{MenuCommand/de|[Gehe zu Auswahl](Std_TreeSelection/de.md)}}: erweitere die [Baumansicht](tree_view/de.md) um das ausgewählte Objekt in der Hierarchie anzuzeigen.

-    {{MenuCommand/de|[Zufällige Farbe](Std_RandomColor/de.md)}}: weist dem Objekt eine zufällige Farbe zu. Es setzt die Parameter des Objekts. `ShapeColor` Attribut zu einem Tupel `(r,g,b)` mit 3 Zufalls Gleitkommas zwischen 0 und 1. Ändere die Eigenschaft durch Ändern von{{PropertyView/de|Form Farbe}} im [Eigenschaftseditor](property_editor/de.md).

-    {{MenuCommand/de|[Löschen](Std_Delete/de.md)}}: entfernt das Objekt aus dem Dokument und aus der 3D Ansicht, indem es die `removeObject()` Methode des Dokuments aufruft.

Ein weiteres Beispiel, mit der [Draft Arbeitsbereich](Draft_Workbench/de.md) und einem ausgewählten Objekt, zeigt es die gleichen Befehle wie mit der [Part Arbeitsbereich](Part_Workbench/de.md), aber auch:

-    {{MenuCommand/de|Entwurf}}: Befehle zur Objekterstellung und -änderung aus der [Draft Arbeitsbereich](Draft_Workbench/de.md).

-    {{MenuCommand/de|Hilfsmittel}}: Zusätzliche kontextuelle Befehle, die von der [Draft Arbeitsbereich](Draft_Workbench/de.md) zur Verfügung gestellt werden.

## Details

FreeCAD verwendet die Viertel Bibliothek, um Coin3D in einer Qt-Umgebung zu verwenden.

Es ist möglich, direkt mit der 3D-Szenegrafik von der [Python-Konsole](Python_console.md) aus zu interagieren, indem Sie die Python-Bibliothek Pivy verwenden.

Weitere Informationen findest Du in der Dokumentation erfahrener Nutzer:

-   [Szenengraph](Scenegraph/de.md), Beschreibung von Coin3D.
-   [Pivy](Pivy/de.md), Verwendung von Coin3D über die Python Konsole.
-   [Drittanbieter Bibliotheken](Third_Party_Libraries/de.md), die von FreeCAD verwendet werden.
-   [Coin3D](https://grey.colorado.edu/coin3d/index.html) C++ Dokumentation.


{{Interface navi

}} 
