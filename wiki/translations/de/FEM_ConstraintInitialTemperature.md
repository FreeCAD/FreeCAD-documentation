---
 GuiCommand:Container|
{{GuiCommand/de
   Name: FEM ConstraintInitialTemperature
   Name/de: FEM StartbedingungTemperatur
   MenuLocation: Modell , Thermische Randbedingungen und Belastungen , Startbedingung Temperatur
   Workbenches: FEM_Workbench/de
   SeeAlso: FEM_tutorial/de
}}
{{GuiCommandFemInfo/de
   Solvers: CalculiX, Elmer
}}
---

# FEM ConstraintInitialTemperature/de



## Beschreibung

Legt eine Starttemperatur für eine thermo-mechanische Analyse fest.



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ConstraintInitialTemperature.svg" width=16px> [Startbedingung Temperatur](FEM_ConstraintInitialTemperature.md)** drücken.
    -   Den Menüeintrag **Modell → Thermische Randbedingungen und Belastungen → <img src="images/FEM_ConstraintInitialTemperature.svg" width=16px> Startbedingung Temperatur** auswählen.
2.  Den Startwert der Temperatur für die Analyse eingeben.



## Einschränkungen

Dieses Werkzeug ordnet die Starttemperatur allen Knoten im FEA-Modell zu - es ist nicht möglich einzelne Bereiche auszuwählen.



## Hinweise

-   Dieses Werkzeug verwendet die Karte \*INITIAL CONDITIONS in CalculiX. Sie wird unter <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node215.html> erklärt.
-   Die Anfangstemperatur muss für alle thermomechanischen Analysen, die mit CalculiX durchgeführt werden, definiert werden, auch für die stationären Analysen.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintInitialTemperature/de
