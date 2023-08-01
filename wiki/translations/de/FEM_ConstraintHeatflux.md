---
- GuiCommand:
   Name:FEM ConstraintHeatflux
   Name/de:FEM ConstraintHeatflux
   MenuLocation:Modell → Thermische Randbedingungen → Randbedingung Wärmestrom
   Workbenches:[FEM](FEM_Workbench/de.md)
   SeeAlso:[FEM Tutorium](FEM_tutorial/de.md)
---

# FEM ConstraintHeatflux/de



## Beschreibung

This constraint specifies film heat transfer of a surface at temperature *T* and with a film coefficient *h* to the environment or sink at temperature *T~0~*. The convective heat flux *q* will satisfy: ***q = h(T -T~0~)***



## Anwendung

1.  Es gibt mehrere Möglichkeiten den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ConstraintHeatflux.svg" width=16px> [Randbedingung Wärmestrom](FEM_ConstraintHeatflux/de.md)** drücken.
    -   Den Menüeintrag **Modell → Thermische Randbedingungen → <img src="images/FEM_ConstraintHeatflux.svg" width=16px> Randbedingung Wärmestrom** auswählen.
2.  In der [3D-Ansicht](3D_view/de.md) die Fläche(n) auswählen, auf die die Randbedingung angewendet werden soll.
3.  Die gewünschte Oberflächentemperatur, den Wärmeübergangskoeffizienten und die Umgebungstemperatur eingeben.



## Hinweise

-   The constraint uses the \*FILM card in CalculiX. The heatflux constraint is explained at <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node203.html>





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintHeatflux/de
