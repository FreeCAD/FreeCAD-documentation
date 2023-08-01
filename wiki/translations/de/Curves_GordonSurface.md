---
- GuiCommand:
   Name:Curves GordonSurface
   Name/de:Curves GordonFläche
   MenuLocation:Surfaces → Gordon surface
   Workbenches:[Curves](Curves_Workbench/de.md)
---

# Curves GordonSurface/de

## Beschreibung

Das Werkzeug <img alt="" src=images/Curves_GordonSurface.svg  style="width:24px;"> [Curves GordonFläche](Curves_GordonSurface/de.md) erstellt eine Oberfläche, die ein Netzwerk aus Kurven überspannt. Dieses Werkzeug ist Teil des [externen Arbeitsbereichs](external_workbenches/de.md) [Curves](Curves_Workbench/de.md).

<img alt="" src=images/GordonSurf-1.png  style="width:800px;">

## Anwendung

1.  A Gordon surface requires a network of lines or curves that create a support network for the surface.
    -   The surface will be \"tented\" between and over these lines.
2.  In the example above the blue lines (or ribs) represent the shape of the surface at different points along surface.
    -   These can be thought of as cross sections along the surface. Or, like supports that the surface will \"tent\" over.
3.  The yellow lines represent the extent and shape of the surface between the cross sections (\"ribs\") defined by the blue lines.
4.  These lines (blue & yellow) can be created in sketches.
    -   The sketches containing the blue ribs would typically have a placement offset.
        -   Each \"rib\" is in a separate sketch.
    -   The sketches containing the extent/shape (yellow) lines will typically reference external geometry from the \"rib\" sketches for accurate positioning.
5.  These need to be created before the next step.
6.  Switch to the <img alt="" src=images/Curves_workbench_icon.svg  style="width:24px;"> [Curves](Curves_Workbench.md) workbench (install from <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) is necessary, if not previously installed)
7.  Now select all the lines of that will define the surface.
8.  The order of selection defines the stitching or tenting order.
9.  Use multi-select to select all lines defining the surface. (Left click while holding the Ctrl key.)
10. Select the ribs first, in order. (In the example above, select the blue lines from left to right. or right to left.)
11. Continue to hold the Ctrl key and select the extent lines. (Yellow lines in the example above.)
12. To invoke the command, do one of the following:
    -   Press the <img alt="" src=images/Curves_GordonSurface.svg  style="width:24px;"> button
    -   Use the **Surfaces → Gordon surface**

## Eigenschaften

-    **Placement**: Can be used to adjust the placement of the resulting Gordon surface. See: [Placement](Placement.md)

    -   Note: The Placement properties do not adjust the placement of the curves/lines used to create the surface, only the surface.

-    **Label**: User specified label (name) for the surface. (Default: Gordon)

-    **Output**: Defines the output type. (Default: Surface, Options: Surface, Wireframe)

-    **Gordon>Max Ctrl Pts**: (Default: 80)

-    **Gordon>Sources**: User selected lines that are used to create the Gordon surface.

-    **Gordon>Tol3D**: 3D tolerance (Default: 0.01)

-    **Wireframe>Samples U**: Number of samples in the U direction. (Default: 16)

    -   This value is used to determine density of the mesh when the Output property is set to Wireframe.

-    **Wireframe>Samples V**: Number of samples in the V direction. (Default: 16)

    -   This value is used to determine density of the mesh when the Output property is set to Wireframe.
    -   Gordon surface in wire frame mode, U=16, V=16

<img alt="" src=images/GordonSurf-wireframe.png  style="width:600px;">

## Hinweise

-   Die Kurven jeder Gruppe (Rippen und Schienen/Profil- und Leitkurven) sollten alle Kurven der anderen Gruppe berühren.
    -   Mit anderen Worten: Sie müssen ein Gitter oder eine Netzstruktur bilden, wie hier dargestellt:

<img alt="" src=images/grid.png  style="width:200px;">

-   Im Normalfall wird die Flächennormale der resultierenden Gordon-Fläche durch die Richtung der Profilkurven (Rippen) bestimmt.

In diesem Beispiel, der Fläche auf der linken Seite, wurden die Leitkurven (Schienen) von +Y nach -Y gezogen und die resultierende Flächennormale zeigt in Richtung +Z
Auf der rechten Seite wurden die Leitkurven (Schienen) von -Y nach +Y gezogen und die resultierende Flächennormale zeigt in Richtung -Z.

<img alt="" src=images/Normals_shown.png  style="width:600px;">

-   [Part Extrudieren](Part_Extrude/de.md) kann zur Erstellung eines Volumenkörpers aus dieser Fläche verwendet werden.

-   [PartDesign Aufpolsterung](PartDesign_Pad/de.md) kann auch einen Volumenkörper aus der Fläche erstellen. Wird die Fläche in einen Körper gezogen, entsteht ein [Basis Formelement](PartDesign_Body/de#Basis_Formelement.md) (BaseFeature-Objekt), das (zu einem Volumenkörper) aufgedickt werden kann.

## Einschränkungen

## Skripten





{{Curves Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Curves](Category_Curves.md) > Curves GordonSurface/de
