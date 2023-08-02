---
- GuiCommand:
   Name: FEM ElementRotation1D
   Name/de: FEM Elementdrehung1D
   MenuLocation: Model -> Element-Geometrie -> Beam rotation
   Workbenches: FEM_Workbench/de
   SeeAlso: FEM_tutorial/de
---

# FEM ElementRotation1D/de



## Beschreibung

Ein **ElementRotation1D**-Objekt wird zum drehen des Balkenprofils um die Achse der Balkenelemente verwendet.



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

-   Um den gedrehten Querschnitt sehen zu könnent, muss die Eigenschaft `Beam Shell Result Output 3D` des [SolverCcxTools](FEM_SolverCalculixCxxtools.md)-Objekts auf `True` gesetzt und die Analyse gestartet werden.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementRotation1D/de
