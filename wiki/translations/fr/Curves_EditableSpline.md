---
- GuiCommand:/fr
   Name:Curves EditableSpline
   Name/fr:Curves Modifier une B-spline
   MenuLocation:Curves → Freehand BSpline
   Workbenches:[Curves](Curves_Workbench/fr.md)
---

# Curves EditableSpline/fr

## Description


<div class="mw-translate-fuzzy">

<img alt="" src=images/Curves_EditableSpline.svg  style="width:24px;"> [Curves Modifier une B-spline](Curves_EditableSpline/fr.md) crée une courbe B-Spline à main levée. Cet outil fait partie des [ateliers externes](External_workbenches/fr.md) appelé [Curves](Curves_Workbench/fr.md).


</div>

## Utilisation

1.  Passer à l\'atelier <img alt="" src=images/Curves_workbench_icon.svg  style="width:24px;"> [Curves](Curves_Workbench/fr.md) (à installer à partir du <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Gestionnaire d\'Addon](Std_AddonMgr/fr.md) si ce n\'est pas déjà fait)
2.  Pour appeler la commande, effectuez l\'une des opérations suivantes:
    -   Appuyez sur le bouton <img alt="" src=images/Curves_EditableSpline.svg  style="width:24px;"> dans la barre d\'outils Curves.
    -   Utilisez l\'entrée **Curves → Freehand BSpline** dans le menu déroulant.

## Options

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

## Propriétés

## Script





{{Curves Tools navi

}}

---
[documentation index](../README.md) > Curves EditableSpline/fr
