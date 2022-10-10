---
- GuiCommand   */de
   Name   *FEM ConstraintBodyHeatSource
   Name/de   *FEM RandbedingungKörperwärmequelle
   MenuLocation   * Modell → Thermische Randbedingungen → Randbedingung Körperwärmequelle
   Workbenches   *[FEM](FEM_Workbench/de.md)
   SeeAlso   *[FEM Tutorium](FEM_tutorial/de.md)
---

# FEM ConstraintBodyHeatSource/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Legt eine intern erzeugte Körperwärme fest, angegeben in W/kg (nicht J/m³).


</div>

## Anwendung


<div class="mw-translate-fuzzy">

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen   *
    -   Die Schaltfläche **<img src="images/FEM_ConstraintBodyHeatSource.svg" width=16px> [Randbedingung Körperwärmequelle](FEM_ConstraintBodyHeatSource/de.md)** drücken.
    -   Den Menüeintrag **Modell → Thermische Randbedingungen → <img src="images/FEM_ConstraintBodyHeatSource.svg" width=16px> Randbedingung Körperwärmequelle** auswählen.
2.  In der [3D-Ansicht](3D_view/de.md) die Objekte auswählen, auf die die Randbedingung angewendet werden soll; diese können Knoten (Ecken), Kanten oder Flächen sein.
3.  Einen Wert für die spezifische Wärme eingeben, die den Objekten zugeordnet werden soll.


</div>

## Limitation


{{VersionMinus|0.20}}

   * The body heat source is applied to the whole model, meaning all bodies of the setup. It is not possible to select an individual body.

## Hinweise


<div class="mw-translate-fuzzy">

-   Für weitere Informationen siehe [this forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=44705&start=490#p422539) und folgende Posts.
-   Elmer Beispiele können auch unter [Elmer GUI Tutorials](https   *//www.nic.funet.fi/pub/sci/physics/elmer/doc/ElmerTutorials.pdf) gefunden werden.


</div>




{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintBodyHeatSource/de
