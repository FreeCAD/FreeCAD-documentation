---
- GuiCommand:
   Name:Part MakeFace‏‎
   Name/de:Part FlächeAusLinienzügen‏‎
   MenuLocation:Formteil - Erstelle Fläche anhand von Kantenzügen
   Workbenches:[Part](Part_Workbench/de.md)
   Version:0.19
   SeeAlso:[Part Regelfläche](Part_RuledSurface/de.md)
---

# Part MakeFace/de

## Beschreibung

**Part MakeFace**‏‎ creates a [plane](Part_Plane.md) in a custom shape. The shape is defined by a closed sketch contour.

It is possible to nest closed contours, for example to have circles inside a polygon. In this case the face will be created between the contours like in this example:

<img alt="" src=images/Part_MakeFace-example.png  style="width:300px;">



*Example of a face created from a nested set of contours.*

## Anwendung

1.  Select a sketch defining at least one closed contour
2.  Press the **<img src="images/Part_MakeFace.svg" width=16px> [Make face from wires](Part_MakeFace.md)** button



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part MakeFace/de
