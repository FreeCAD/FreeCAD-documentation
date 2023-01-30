# 3D view/de
## Einleitung


{{TOCright}}

Die [3D-Ansicht](3D_view/de.md) von FreeCAD ist eine Instanz eines Coin3D-[Szenengraph](Scenegraph/de.md), und stellt das wichtigste Fenster in der [Benutzeroberfläche](interface/de.md) dar. Coin3D ist eine Bibliothek, die den OpenInventor 2.1 Szenenbeschreibungsstandard implementiert.

Bestimmte Eigenschaften der Ansicht, wie Hintergrundfarbe, Art der [Mausnavigation](Mouse_navigation/de.md) und Zoom-Schritte, können im [Voreinstellungseditor](Preferences_Editor/de.md) konfiguriert werden.

<img alt="" src=images/FreeCAD_3D_view.png  style="width:600px;">



*Die [3D-Ansicht](3D_view/de.md) ist ein Bestandteil der FreeCAD- [Benutzerschnittstelle](interface/de.md). Standardmäßig zeigt sie ein kleines Widget mit Koordinatenachsen und den Navigationswürfel, ebenfalls mit Koordinatenachsen; das Raster kann durch Laden des Arbeitsbereichs [Draft](Draft_Workbench/de.md) angezeigt und konfiguriert werden.*



## Maßnahmen


**Hinweis:**

Verknüpfe Aktionen <small>(v0.19)</small> .

Da die [Baumansicht](tree_view/de.md) die meisten Objekte auflistet, die in der 3D-Ansicht sichtbar sind, sind viele der Aktionen identisch mit denen, die über die [Baumansicht](tree_view/de.md) ausgeführt werden können.

Wenn der Standardarbeitsbereich [Start](Start_Workbench/de.md) aktiv ist, zeigt ein Rechtsklick auf die 3D-Ansicht nur einen Befehl:

-    **[Navigationsstile](Mouse_navigation.md)**: verschiedene Tastenstile zur Verwendung mit einer 3-Tasten-Maus oder einem Laptop-Trackpad.

Sobald jedoch ein [Arbeitsbereich](Workbenches/de.md) geladen ist, gibt es zusätzliche Befehle:

-    {{MenuCommand/de|Link Aktionen}}: [Verknüpfung erstellen](Std_LinkMake/de.md).

    -   
        {{MenuCommand/de|Link Gruppe erstellen}}
        
        : [Einfache Gruppe](Std_LinkMakeGroup/de.md), [Group mit Links](Std_LinkMakeGroup/de.md), [Gruppe mit Transformations Links](Std_LinkMakeGroup/de.md).

-    {{MenuCommand/de|[Einpassen](Std_ViewFitAll/de.md)}}: schwenkt und zoomt die Ansicht so, dass alle Objekte im Dokument auf dem Bildschirm angezeigt werden.

-    {{MenuCommand/de|[Auswahl einpassen](Std_ViewFitSelection/de.md)}}: schwenkt und zoomt die Ansicht, um das aktuell ausgewählte Objekt auf den Bildschirm einzupassen.

-    {{MenuCommand/de|[Zeichenstil](Std_DrawStyle/de.md)}}: Original, Flache Linien, Schattiert, Drahtgitter, Punkte, Versteckte Linie, Keine Schattierung.

-    {{MenuCommand/de|[Standardansichten](Std_View_Menu/de.md)}}: [Isometrisch](Std_ViewIsometric/de.md), [Vorne](Std_ViewFront/de.md), [Oben](Std_ViewTop/de.md), [Rechts](Std_ViewRight/de.md), [Hinten](Std_ViewRear/de.md), [Unten](Std_ViewBottom/de.md), [Links](Std_ViewLeft/de.md), [Nach links drehen](Std_ViewRotateLeft/de.md), [Nach rechts drehen](Std_ViewRotateRight/de.md).

-    {{MenuCommand/de|Messen}}: [Messen ein-/ausschalten](View_Measure_Toggle_All/de.md), [Messung löschen](View_Measure_Clear_All/de.md).

-    {{MenuCommand/de|Dokumentfenster}}: [Angedockt](Std_ViewDockUndockFullscreen/de.md), [Abgedockt](Std_ViewDockUndockFullscreen/de.md) und [Vollbild](Std_ViewDockUndockFullscreen/de.md).

Darüber hinaus können je nach aktivem Arbeitsbereich und aktivem Objekt weitere kontextabhängige Befehle verfügbar werden.

Zum Beispiel mit dem Arbeitsbereich [Part](Part_Workbench/de.md) und einem Objekt ausgewählt:

-    {{MenuCommand/de|[Darstellung](Std_SetAppearance/de.md)}}: Startet den Dialog zum Ändern der Farbe und Größe von Linien und Eckpunkten sowie der Farbe von Flächen.

-    {{MenuCommand/de|[Ein/Ausblenden](Std_ToggleVisibility/de.md)}}: Macht das Objekt in der 3D-Ansicht sichtbar oder unsichtbar.

-    {{MenuCommand/de|[Selektierbarkeit an/aus](Std_ToggleSelectability/de.md)}}: Macht das Objekt in der 3D Ansicht nicht mehr auswählbar; diesen Befehl erneut verwenden, um den Effekt aufzuheben. Es setzt das Attribut `Selectable` des Objekts auf `True` oder `False`. Die Eigenschaft wird durch Umschalten der {{PropertyView/de|Selectable}} im [Eigenschaftseditor](property_editor/de.md) geändert.

-    {{MenuCommand/de|[Gehe zu Selektion](Std_TreeSelection/de.md)}}: Erweitert die [Baumansicht](tree_view/de.md) um das ausgewählte Objekt in der Hierarchie anzuzeigen.

-    {{MenuCommand/de|[Zufällige Farbe](Std_RandomColor/de.md)}}: Weist dem Objekt eine zufällige Farbe zu. Es setzt das Attribut `ShapeColor` des Objekts auf ein Tupel `(r,g,b)` mit 3 zufälligen Gleitkommawerten zwischen 0 und 1. Die Eigenschaft wird durch Ändern der {{PropertyView/de|ShapeColor}} im [Eigenschafteneditor](property_editor/de.md) geändert.

-    {{MenuCommand/de|[Löschen](Std_Delete/de.md)}}: Entfernt das Objekt aus dem Dokument und aus der 3D-Ansicht, indem es die Methode `removeObject()` des Dokuments aufruft.

Ein weiteres Beispiel, mit dem Arbeitsbereich [Draft](Draft_Workbench/de.md) und einem Objekt ausgewählt, zeigt es die gleichen Befehle wie mit dem Arbeitsbereich [Part](Part_Workbench/de.md), aber auch noch:

-    **Draft**: Befehle zur Objekterstellung und -änderung aus dem Arbeitsbereich [Draft](Draft_Workbench/de.md).

-    **Dienstprogramme**: Zusätzliche kontextabhängige Befehle, die vom Arbeitsbereich [Draft](Draft_Workbench/de.md) zur Verfügung gestellt werden.

## Details

FreeCAD verwendet die Bibliothek Quarter, um Coin3D in einer Qt-Umgebung zu verwenden.

Es ist möglich, von der [Python-Konsole](Python_console.md) aus direkt mit dem Szenengraph der 3D-Ansicht zu interagieren, wenn die Python-Bibliothek Pivy verwendet wird.

Weitere Informationen finden sich in der Dokumentation für erfahrene Anwender:

-   [Szenengraph](Scenegraph/de.md), Beschreibung von Coin3D.
-   [Pivy](Pivy/de.md), Verwendung von Coin3D über die Python-Konsole.
-   [Drittanbieter-Bibliotheken](Third_Party_Libraries/de.md), die von FreeCAD verwendet werden.
-   [Coin3D](https://grey.colorado.edu/coin3d/index.html) C++ Dokumentation.


{{Interface navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > 3D view/de
