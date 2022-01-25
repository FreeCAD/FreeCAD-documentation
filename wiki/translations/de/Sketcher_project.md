# Sketcher project/de
**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

Dies ist das FreeCAD Skizzierer Entwicklungsprojekt. Es folgt den Regeln des \[<http://en.wikipedia.org/wiki/Getting_Things_Done#Methodology>\| Dinge zu erledigen\] (engl.: Getting Things Done) Prozesses. Die Projekte werden im [Entwicklungsfahrplan](Development_roadmap/de.md) gesammelt.

## Zweck und Prinzipien 

Hierbei handelt es sich um ein Softwareentwicklungsprojekt zur Implementierung von Beschränkungs Skizzierer Funktionen. Es geht um die Implementierung einiger Gui Elemente und die Bindung an den Beschränkungslöser.

Die Entwicklungsschritte werden hier geplant und im Problemverfolgungssystem verfolgt, um ein gut geformtes [Änderungs Protokoll](http://www.freecadweb.org/tracker/) zu erhalten

## Ergebnis

## Ideenfindung

Um die Lösungsleistung des Skizzierers zu verbessern, kann eine graphbasierte Partitionierung des Beschränkungsssystems vorgenommen werden. Der Satz der Beschränkungen und der Satz der unbekannten Parameter kann in einem [bipartite graph](http://en.wikipedia.org/wiki/Bipartite_graph) dargestellt werden, wobei die Beschränkungen den linken Knoten und die Unbekannten den rechten Knoten entsprechen. **FERTIG**

Ein einfacher, aber oft sehr nützlicher Vorverarbeitungsschritt besteht darin, alle disjunkten Untergruppen zu erkennen, so dass sie im Löser getrennt behandelt werden können. **FERTIG**

Außerdem könnte man die Zahl der unbekannten Parameter, die in der Lösung berücksichtigt werden, reduzieren. Zu Beginn einer Lösung sollte geprüft werden, welche Randbedingungen nicht bereits erfüllt sind. Durch eine Graphenanalyse könnte man einen minimalen Satz unbekannter Parameter finden, die berücksichtigt werden sollten, um alle nicht erfüllten Randbedingungen zu erfüllen.

Einen Schritt weiter gehend, konnten starre Unterbereiche einer Skizze erkannt und auf 3 Freiheitsgrade (x,y,Rotation) reduziert werden.

## Organisieren

## Nächste Handlungen 

Für 0.14:

1.  Mausziehen für Mehrfachauswahl
2.  Liste der Geometrien im Aufgabenpaneel (ähnlich wie die Liste der Beschränkungen)
3.  Füge eine Einblendmenüoption hinzu, um eine Beschränkung für deckungsgleiche Punkte in Tangentialitätsbeschränkungen umzuwandeln
4.  Polygonwerkzeug (Bequemlichkeit)
5.  Aktualisierung der Wiki Dokumentation zu Symmetriebeschränkung und Polylinienwerkzeug (m-Taste)

Idee Ideenfindung:

User Interface :

1.  Full Screen Grid (Units aware)
2.  Smarter Auto-constraints:
    1.  Algorithm only considers geometry that is on the screen to increase performance and improve selection
    2.  Prevent constraint conflicts
3.  Hint Lines: horizontal, vertical, perpendicular, tangent constraints?
4.  Overhaul of constraint icons by merging into one SoNode
    1.  Merge into one SoNode to improve performance
    2.  Remove need for ray pick to increase performance
    3.  Share texture memory more efficiently.
    4.  Improve algorithm for preventing overlap
    5.  Tool Bar for toggling constraint visuals independently
5.  Datum Label Improvements:
    1.  Radius label can be positioned at any angle
    2.  Remove need for storing in SoImage which isn\'t needed any more
6.  Fix Grid Edge
7.  Auto constraints whilst dragging (Point on Point, Point on Line Coincident)?
8.  Highlight entities or zoom to over constrained area of sketch
9.  Related to part design (transparent support objects)
10. Implement Sketch Plane Feature with introduction of Assembly module
11. Improve Point Selection by implementing new custom node.
12. Construction lines use dashes instead of solid lines.

For 0.13:

1.  support for arc/arc and arc/circle in the tangent constraint - **DONE** \[logari81\]
2.  support for arcs in the perpendicular constraint - **DONE** \[logari81\]
3.  zoom-independent arrows (symmetry constraint) / dimension lines - **DONE** \[mrlukeparry\]
4.  external geometry / constraints - **DONE** \[logari81\]
5.  box selection - **DONE** \[mrlukeparry\]
6.  mouse dragging of multiple selection - **SKIPPED for 0.14**
7.  better constrainess diagnostics [(Issue \#691)](http://www.freecadweb.org/tracker/view.php?id=691)- **DONE** \[logari81\]
8.  list of Geometries in the task panel (similar to the list of Constraints) - **SKIPPED for 0.14**
9.  support for points as construction geometry - **DONE** \[logari81\]
10. add a popup menu option to convert a coincident points constraint to tangency constraints - **SKIPPED for 0.14**
11. make symmetry constraint to work with symmetry points instead of symmetry lines (useful e.g. for midpoint definition) - **DONE** \[logari81\]

For 0.12:

1.  constraint parameters (datums) editable in the 3D view **DONE** \[jriegel\]
2.  synchronization between listwidgetview selection - 3D view selection - **DONE** \[wmayer\]
3.  avoid overlapping of constraints symbols **DONE** - \[mrlukeparry\]
    1.  make constraints symbols smaller, selectable and avoid overlapping when zooming out **DONE** - \[mrlukeparry\]
    2.  create constraint icons for 3D Inventor view **DONE** - \[mrlukeparry\]
    3.  make datum text size dependant on zoom **DONE** - \[mrlukeparry\]
    4.  make datum text easier to select **DONE** - \[mrlukeparry\]
    5.  Prevent text overlap on Datum Labels **DONE** - \[mrlukeparry\]
4.  testing the new solver in stand alone mode
5.  external constraints (having constraints with references outside the sketch, some edge of the 3D model e.g.) **0.13** \[jriegel\]
6.  auto-constraining **DONE** \[jriegel\]
    1.  auto-constraint for perpendicular **DONE** - \[mrlukeparry\]
7.  visualize tangency constraints **DONE** - \[mrlukeparry\]
8.  visualize point to line distance constraints and point to point distance constraints **DONE** - \[logari81\]
9.  add indexes to the constraints symbols in 3D view in order to distinguish between constraints of the same kind **DONE** - \[mrlukeparry\]
10. radius constraint (including visualization) **DONE** - \[logari81\]
11. angle constraint (including visualization) **DONE** - \[logari81\]
12. implement a fillet tool in the sketcher **DONE** \[mrlukeparry\]
    1.  provide a method of setting fillet radius [(Issue \#437)](http://www.freecadweb.org/tracker/view.php?id=437)
13. implement a trim/extend tool in the sketcher **DONE** \[logari81\]
    1.  implement an extend tool **SKIPPED** \[logari81\]
    2.  trim support on arcs **DONE** \[mrlukeparry\]
14. equal lengths constraint (including visualization) **DONE** - \[logari81\]
15. constrainess diagnostics - degree of freedom counting **DONE** - \[logari81\]
16. symmetry constraint (including visualization) **DONE** - \[logari81\]
17. implement point on object constraint **DONE** - \[mrlukeparry\]
18. Make Snap-Grid less \'greedy\' **DONE** \[mrlukeparry\]
19. Wiki page for the Sketcher Workbench **DONE** \[normandc\]


{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Roadmap](Category_Roadmap.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher project/de
