---
- GuiCommand:
   Name:FEM ElementRotation1D
   MenuLocation:Model → Element Geometry → Beam rotation
   Workbenches:[FEM](FEM_Workbench.md)
   SeeAlso:[FEM tutorial](FEM_tutorial.md)
---

# FEM ElementRotation1D/de

## Beschreibung

Ein **ElementRotation1D**-Objekt wird zum drehen des Balkenprofils um die Achse von Balkenelementen verwendet.

## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ElementRotation1D.svg" width=16px> [Trägerrotation](FEM_ElementRotation1D/de.md)** drücken.
    -   Den Menüeintrag **Modell → Element-Geometrie → <img src="images/FEM_ElementRotation1D.svg" width=16px> Trägerrotation** auswählen.
2.  Den Winkel festlegen, um den das Balkenprofil gedreht wird.

## Optionen

## Eigenschaften

## Begrenzungen

-   Derzeit werden mehrere Drehungen nicht unterstützt (Eine einzige Drehung wird auf alle Balken im Modell angewendet).

## Hinweise

-   To visualize the rotated cross-section it is necessary to set `Beam Shell Result Output 3D` in the [FEM SolverCalculixCxxtools](FEM_SolverCalculixCxxtools.md) to `True` and run the analysis.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementRotation1D/de
