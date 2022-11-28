---
- GuiCommand   */de
   Name   *Curves EditableSpline
   Name/de   *Curves EditierbarerSpline
   MenuLocation   *Curves → Freehand BSpline
   Workbenches   *[Curves](Curves_Workbench/de.md)
---

# Curves EditableSpline/de

## Beschreibung

Das Werkzeug <img alt="" src=images/Curves_EditableSpline.svg  style="width   *24px;"> [Curves EditierbarerSpline](Curves_EditableSpline.md) erstellt eine Freihand-B-Spline-Kurve. Dieses Werkzeug ist Teil des [Externen Arbeitsbereichs](external_workbenches/de.md) [Curves](Curves_Workbench/de.md).

## Anwendung

1.  Zum Arbeitsbereich <img alt="" src=images/Curves_workbench_icon.svg  style="width   *24px;"> [Curves](Curves_Workbench/de.md) wechseln (muss mit dem <img alt="" src=images/Std_AddonMgr.svg  style="width   *24px;"> [Addon-Manager](Std_AddonMgr/de.md) installiert werden, wenn noch nicht geschehen)
2.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen   *
    -   Die Schaltfläche <img alt="" src=images/Curves_EditableSpline.svg  style="width   *24px;"> in der Curves-Symbolleiste drücken.
    -   Den Menüeintrag **Curves → Freehand BSpline** auswählen.

## Optionen

During the command a special edit mode is active and there are several actions and behaviors that can be controlled by keys and mouse clicks.

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

## Limitations

## Eigenschaften

## Skripten





{{Curves Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Curves](Category_Curves.md) > Curves EditableSpline/de
