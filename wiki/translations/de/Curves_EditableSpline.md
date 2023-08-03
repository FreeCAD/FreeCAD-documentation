---
 GuiCommand:
   Name: Curves EditableSpline
   Name/de: Curves EditierbarerSpline
   MenuLocation: Curves , Freehand BSpline
   Workbenches: Curves_Workbench/de
---

# Curves EditableSpline/de



## Beschreibung

Das Werkzeug <img alt="" src=images/Curves_EditableSpline.svg  style="width:24px;"> [Curves EditierbarerSpline](Curves_EditableSpline.md) erstellt eine Freihand-B-Spline-Kurve. Dieses Werkzeug ist Teil des [Externen Arbeitsbereichs](external_workbenches/de.md) [Curves](Curves_Workbench/de.md).



## Anwendung

1.  Zum Arbeitsbereich <img alt="" src=images/Curves_workbench_icon.svg  style="width:24px;"> [Curves](Curves_Workbench/de.md) wechseln (muss mit dem <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon-Manager](Std_AddonMgr/de.md) installiert werden, wenn noch nicht geschehen).
2.  Wahlweise Knotenpunkte, Kanten und/oder Flächen auswählen:
    -   Die Anzahl der Knotenpunkte des Splines entspricht der Anzahl der ausgewählten Elemente.
    -   Die Spline-Knoten rasten auf die ausgewählten Knotenpunkte und die Mittelpunkte der ausgewählten Kanten und Flächen ein.
3.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche <img alt="" src=images/Curves_EditableSpline.svg  style="width:24px;"> in der Curves-Symbolleiste drücken.
    -   Den Menüeintrag **Curves → Freehand BSpline** auswählen.



## Optionen

Während der Ausführung des Befehls ist ein besonderer Bearbeitungsmodus aktiv und es gibt einige Aktionen und Verhaltensweisen, die mit Tasten und Mausklicks gesteuert werden können.

-   To move a vertex or guide line (guide lines are the straight lines between vertexes) press and hold down the left mouse button on it, and move the mouse.
-   The **A** key selects or deselects all vertexes and guide lines.
-   The **I** key will add a vertex to the segment belonging to the selected guide line. The new vertex will be selected.
-   The **T** key sets or un-sets tangent mode for the selected vertexes or guide lines (relative to the view direction).
-   The **P** key aligns selected objects.
-   The **S** key can be used to snap a vertex to a vertex belonging to another B-spline. With a vertex of the B-spline being edited selected, hold down the **Ctrl** key and add the target vertex to the selection, then hit the **S** key. The vertexes are snapped together.
-   To unsnap vertexes, select the snapped vertex pair and again hit the **S** key. The vertex of the B-spline being edited remains selected and can now be moved.
-   The **L** key sets or un-sets the linear interpolation.
-   The **X**, **Y** or **Z** keys can be used to constrain the movement of the object being dragged. While dragging, hit the desired axis key. Hit the same key again to disable the constraint.
-   The **Q** key finishes the command and exits edit mode.



## Einschränkungen



## Eigenschaften



## Skripten





{{Curves Tools navi

}}



---
⏵ [documentation index](../README.md) > [Curves](Category_Curves.md) > Curves EditableSpline/de
