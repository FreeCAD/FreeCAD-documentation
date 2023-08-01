---
- GuiCommand:
   Name:FEM ConstraintTemperature
   Name/de:FEM RandbedingungTemperatur
   MenuLocation:Modell - Thermische Randbedingungen - Randbedingung Temperatur 
   Workbenches:[FEM](FEM_Workbench/de.md)
   Shortcut:
   SeeAlso:[FEM Tutorium](FEM_tutorial/de.md)
---

# FEM ConstraintTemperature/de

## Beschreibung

Creates a FEM constraint for a temperature boundary condition.

## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ConstraintTemperature.svg" width=16px> [Randbedingung Temperatur](FEM_ConstraintTemperature/de.md)** drücken.
    -   Den Menüeintrag **Modell → Thermische Randbedingungen → <img src="images/FEM_ConstraintTemperature.svg" width=16px> Randbedingung Temperatur** auswählen.
2.  In der [3D-Ansicht](3D_view/de.md) die Objekte auswählen, auf die die Randbedingung angewendet werden soll; diese können Knoten (Ecken), Kanten oder Flächen sein.
3.  Einen Wert für die Temperatur eingeben, die den Objekten zugeordnet werden soll.

### Optionen

By default the constraint defines a temperature. By using the option **Concentrated heat Flux** a heat flux trough the area of the face (Watt per face area) can be specified.

## Hinweise

-   The temperature constraint uses the \*BOUNDARY card in CalculiX. the temperature constraint is explained at <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node163.html>





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintTemperature/de
