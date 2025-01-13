---
 GuiCommand:Container|
{{GuiCommand/de
   Name: FEM ElementRotation1D
   Name/de: FEM Elementdrehung1D
   MenuLocation: Model , Element-Geometrie , Beam rotation
   Workbenches: FEM_Workbench/de
   SeeAlso: FEM_tutorial/de
}}
{{GuiCommandFemInfo
   Solvers: CalculiX
}}
---

# FEM ElementRotation1D/de



## Beschreibung

Ein **ElementRotation1D**-Objekt wird zum drehen des Balkenprofils um die Achse der Balkenelemente verwendet.



## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ElementRotation1D.svg" width=16px> [Stabdrehung](FEM_ElementRotation1D/de.md)** drücken.
    -   Den Menüeintrag **Modell → Element-Geometrie → <img src="images/FEM_ElementRotation1D.svg" width=16px> Stabdrehung** auswählen.
2.  Den Winkel festlegen, um den das Stabprofil gedreht wird.



## Eigenschaften


{{PropertyData/de|Rotation}}

: Legt den Winkel der Drehung fest.



## Begrenzungen

-   Derzeit werden mehrere Drehungen nicht unterstützt (Eine einzige Drehung wird auf alle Balken im Modell angewendet).



## Hinweise

-   Um den gedrehten Querschnitt sehen zu können, muss die Eigenschaft `Beam Shell Result Output 3D` des [SolverCcxTools](FEM_SolverCalculixCxxtools.md)-Objekts auf `True` gesetzt und die Analyse gestartet werden.
-   Diese Funktion verwendet die [\*BEAM SECTION-Karte in CalculiX](https://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node162.html).





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ElementRotation1D/de
