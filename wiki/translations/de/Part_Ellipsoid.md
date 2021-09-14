---
- GuiCommand:/de
   Name:Part Ellipsoid   Name/de:Part Ellipsoid
   MenuLocation:Formteil → [Grundkörper erstellen](Part_Primitives/de.md) → Ellipsoid
   Workbenches:[Part](Part_Workbench/de.md), [OpenSCAD](OpenSCAD_Workbench/de.md)
   SeeAlso:[Part Grundkörper Erstellen](Part_Primitives/de.md)
---

## Beschreibung

Der <img alt="" src=images/Part_Ellipsoid.svg  style="width:24px;"> [Part Ellipsoid](Part_Ellipsoid/de.md) Befehl erzeugt einen parametrischen Ellipsoid Festkörper.

The shape produced is limited in FreeCAD to being a solid (optionally truncated) spheroid, the shape you would create by rotating an ellipse around one of its axis. By default it is a [Oblate Spheroid](http://en.wikipedia.org/wiki/Oblate_spheroid), the shape you would create by rotating an ellipse around its minor axis. The parameters can be changed to form a [Prolate Spheroid](http://en.wikipedia.org/wiki/Prolate_spheroid).

The default spheroid in FreeCAD will have a circle for any cross section parallel to the XY plane. The cross section parallel to the other two planes will be an ellipse.

In der Mathematik würde ein [Ellipsoid](http://en.wikipedia.org/wiki/Ellipsoid) einen elliptischen Querschnitt in allen drei Ebenen haben.

## Anwendung


<div class="mw-translate-fuzzy">

Ein parametrischer Ellipsoid Festkörper ist über den Grundkörper erstellen Dialog im Part Arbeitsbereich verfügbar.

1.  Wechsle zum <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Part Arbeitsbereich](Part_Workbench/de.md)
2.  Greife auf den Ellipsoid Befehl auf verschiedene Arten zu:
    -   Über den Grundkörper erstellen Dialog, indem du die <img alt="" src=images/Part_Primitives.svg  style="width:32px;"> [Grundkörper](Part_Primitives/de.md) in der Part Werkzeugleiste.
    -   Unter Verwendung **Part → [Grundkörper erstellen](Part_Primitives/de.md) → Ellipsoid** im Part Menü


</div>

## Eigenschaften

-   Radius 1, by default the minor radius parallel to the Z-axis,
-   Radius 2, by default the major radius parallel to the XY plane, it is also the maximum radius of the circular cross section
-   Angle 1, lower truncation of the ellipsoid, parallel to the circular cross section (-90 degrees in a full spheroid)
-   Angle 2, upper truncation of the ellipsoid, parallel to the circular cross section (90 degrees in a full spheroid)
-   Angle 3, angle of rotation of the elliptical cross section (360 degrees in a full spheroid)

![](images/Part_Ellipsoid_screenshot.jpg )





 
