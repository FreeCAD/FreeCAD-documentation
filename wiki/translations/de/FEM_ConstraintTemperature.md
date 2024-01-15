---
 GuiCommand:
   Name: FEM ConstraintTemperature
   Name/de: FEM RandbedingungTemperatur
   MenuLocation: Modell , Thermische Randbedingungen und Belastungen, Randbedingung Temperatur 
   Workbenches: FEM_Workbench/de
   Shortcut: 
   SeeAlso: FEM_tutorial/de
---

# FEM ConstraintTemperature/de



## Beschreibung

Legt eine Randbedingung Temperatur fest oder wahlweise eine konzentrierte Wärmestrombelastung.



## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ConstraintTemperature.svg" width=16px> [Randbedingung Temperatur](FEM_ConstraintTemperature/de.md)** drücken.
    -   Den Menüeintrag **Modell → Thermische Randbedingungen und Belastungen → <img src="images/FEM_ConstraintTemperature.svg" width=16px> Randbedingung Temperatur** auswählen.
2.  In der [3D-Ansicht](3D_view/de.md) die Objekte auswählen, auf die die Randbedingung angewendet werden soll; diese können Knoten (Ecken), Kanten oder Flächen sein.
3.  Einen Wert für die Temperatur eingeben, die den Objekten zugeordnet werden soll.



### Optionen

Standardmäßig legt diese Funktion eine Temperatur fest. Wird die Option **CFlux** verwendet, kann ein Wärmestromwert (in mW) in jedem Knoten angegeben werden, der zur ausgewählten geometrischen Einheit gehört.



## Hinweise

-   Die Randbedingung Temperatur verwendet die \*BOUNDARY-Karte in CalculiX. Sie wird unter <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node163.html> erklärt (engl.)
-   Die Option **CFlux** verwendet die \*CFLUX-Karte in CalculiX: <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node168.html>





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintTemperature/de
