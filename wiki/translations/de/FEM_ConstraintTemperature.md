---
 GuiCommand:Container|
{{GuiCommand/de
   Name: FEM ConstraintTemperature
   Name/de: FEM RandbedingungTemperatur
   MenuLocation: Modell , Thermische Randbedingungen und Belastungen, Randbedingung Temperatur 
   Workbenches: FEM_Workbench/de
   Shortcut: 
   SeeAlso: FEM_tutorial/de
}}
{{GuiCommandFemInfo/de
   Solvers: CalculiX, Elmer
}}
---

# FEM ConstraintTemperature/de



## Beschreibung

Legt eine Randbedingung Temperatur fest oder wahlweise eine konzentrierte Wärmestrombelastung.



## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ConstraintTemperature.svg" width=16px> [Randbedingung Temperatur](FEM_ConstraintTemperature/de.md)** drücken.
    -   Den Menüeintrag **Modell → Thermische Randbedingungen und Belastungen → <img src="images/FEM_ConstraintTemperature.svg" width=16px> Randbedingung Temperatur** auswählen.
2.  Die Schaltfläche **Hinzufügen** Drücken.
3.  In der [3D-Ansicht](3D_view/de.md) die Objekte auswählen, auf die die Randbedingung angewendet werden soll; diese können Knoten (Ecken), Kanten oder Flächen sein. Wahlweise die Schaltfläche **Remove** drücken und auf die Objekte klicken, die aus der Auswahl entfernt werden solllen.
4.  Die Art der Randbedingung auswählen und deren Parameter angeben:
    -   *Temperature* (Standardauswahl) - Randbedingung Temperatur, den Wert für *Temperature* in K eingeben.
    -   *CFlux* - concentrated heat flux load, den Wert für *Concentrated heat flux* in mW eingeben - dieser Wert wird durch die Anzahl der Knoten des zugrundeliegenden Elements geteilt, um den Gesamtfluss einer gegebenen Größe dieses Elements zu erhalten.



## Hinweise

-   Die Randbedingung Temperatur verwendet die \*BOUNDARY-Karte in CalculiX. Sie wird unter <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node163.html> erklärt (engl.)
-   Die Option **CFlux** verwendet die \*CFLUX-Karte in CalculiX: <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node168.html>





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintTemperature/de
