# DAG view/de
## Einleitung




Die [DAG-Ansicht](DAG_view/de.md) ist ein [directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) (DAG) (deutsch: gerichteter azyklischer Graph), der die Beziehungen zwischen verschiedenen Objekten im Dokument zeigt. Er ist hauptsächlich dazu gedacht, zu zeigen, wie bestimmte Objekte in einem komplexen Modell mit vielen Funktionen und Referenzen, wie z.B. denjenigen, die mit dem Arbeitsbereich <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [PartDesign](PartDesign_Workbench/de.md) erstellt werden können, von anderen abhängen.

Die DAG-Ansicht ähnelt dem Graphen, der aus einem Git-Repositorium und seinen Ablegern erzeugt werden kann. Zusammen mit der normalen [Baumansicht](tree_view/de.md) und dem [Abhängigkeitsgraph](Std_DependencyGraph/de.md) ist die DAG-Ansicht ein Werkzeug, um die parametrische Historie von Objekten in einem Dokument zu untersuchen.

## Beispiel

Ein einfaches Modell wird mit verschiedenen Ansichten gezeigt.

![](images/FreeCAD_DAG_view_3D.png ) 
*Modell mit 2D- und 3D-Formen.*

<img alt="" src=images/FreeCAD_DAG_view_Tree_view.png ) ![](images/FreeCAD_DAG_view.png  style="width:" height="500px;">



*Links: Objekte angezeigt in der Standardansicht [Baumansicht](tree_view/de.md). Rechts: Objekte angezeigt in der DAG-Ansicht.*

![](images/FreeCAD_DAG_view_Std_DependencyGraph.png )



*Beziehungen zwischen den im [Abhängigkeitsgraph](Std_DependencyGraph/de.md) gezeigten Objekten.*

## Aktivieren der DAG-Ansicht 

Die DAG-Ansicht wurde in 0.17 als eine experimentelle Funktion für Hauptanwender und Entwickler zur Unterstützung bei der Fehlerbereinigung in komplexen Modellen eingeführt; daher ist die DAG-Ansicht nicht standardmäßig verfügbar.

Um diese Ansicht zu verwenden, verwende den [Parametereditor](Std_DlgParameter/de.md). Erstelle die folgende Untergruppe, wenn sie nicht existiert

-    `BaseApp/Preferences/DockWindows/DAGView`
    

dann füge den Parameter `Enabled` vom Typ `Boolean` hinzu und setze ihn auf `True`.

Restarte FreeCAD und aktiviere die DAG Ansicht: **{{StdMenu|[Ansicht](Std_View_Menu/de.md)** → Paneele → DAG-Ansicht}}.

Im [Parametereditor](Std_DlgParameter/de.md) kannst du auch einige Eigenschaften in der folgenden Untergruppe ändern

-    `BaseApp/Preferences/DAGView`
    

-   SchriftartPunktGrösse - Setze die Größe der Text Schriftart und kann die Lesbarkeit bei hohen DPI-Werten verbessern. Für die Standardschriftgröße auf 0 setzen.

-   AuswahlModus
    -   0 - einfacher Klick wählt ein Element aus. Strg-Klick fügt Elemente zur Auswahl hinzu.
    -   1 - jeder Klick fügt/entfernt ein Element zur Auswahl.

-   Richtung - die Reihenfolge, in der die Elemente angezeigt werden.
    -   1 - Kind oben, Elternteil darunter
    -   -1 - Eltern oben, Kinder darunter

## Verweise

-   [DAGView](https://forum.freecadweb.org/viewtopic.php?f=20&t=11276), Forumsbeitrag zur Vorstellung des neuen Werkzeugs.
-   [Osterei von nächsten PartDesign: DAG Ansicht](https://forum.freecadweb.org/viewtopic.php?t=15375), einschließlich der Ansicht zusammen mit der Aktualisierung von PartDesign.


{{Interface navi

}} {{Std Base navi}}



---
⏵ [documentation index](../README.md) > DAG view/de
