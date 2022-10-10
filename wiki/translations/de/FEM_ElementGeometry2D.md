---
- GuiCommand   *
   Name   *FEM ElementGeometry2D
   MenuLocation   *Model → Element Geometry → Shell plate thickness
   Workbenches   *[FEM](FEM_Workbench.md)
   Shortcut   ***C** **S**
   SeeAlso   *[FEM tutorial](FEM_tutorial.md)
---

# FEM ElementGeometry2D/de

## Beschreibung

Ein **ElementGeometry2D**-Objekt wird zum Festlegen der Wandstärke von 2D-FEM-Elementen verwendet; alle oder nur die auf einer ausgewählten Oberfläche liegen.

## Anwendung

1.  Es gibt mehrereMöglichkeiten den Befehl aufzurufen   *
    -   Die Schaltfläche **<img src="images/FEM_ElementGeometry2D.svg" width=16px> [Dicke der Schalenplatte](FEM_ElementGeometry2D.md)** drücken.
    -   Den Menüeintrag **Modell → Element-Geometrie → <img src="images/FEM_ElementGeometry2D.svg" width=16px> Dicke der Schalenplatte** auswählen.
2.  Den Parameter der Wandstärke festlegen.
3.  Wahlweise die Schaltfläche **Add** im Aufgabenbereich drücken und danach auf die Fläche klicken, die eine voreingestellte Wandstärke erhalten soll. Wenn die Flächenauswahl leer ist, werden ihr automatisch alle übrigen Flächen (deren Wandstärke nicht durch andere [FEM ElementGeometry2D](FEM_ElementGeometry2D/de.md)-Objekte festgelegt ist) zugeordnet.

## Limitations

-   Analysis combining shell elements with solid or edge elements is not supported in the current version (FreeCAD 0.18).

## Eigenschaften


**Thickness**

   * Legt die Wandstärke der Schale (Hülle) fest.

## Skripten

## Hinweise

For viewing results from CalculiX solver on the mesh expanded to the prescribed thickness, property `Beam Shell Result Output 3D` in the [FEM SolverCalculixCxxtools](FEM_SolverCalculixCxxtools.md) need to be set to `True`.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementGeometry2D/de
