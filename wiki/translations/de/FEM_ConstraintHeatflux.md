---
 GuiCommand:
   Name: FEM ConstraintHeatflux
   Name/de: FEM RandbedingungWärmestrom
   MenuLocation: Modell , Thermische Randbedingungen und Belastungen , Wärmestrombelastung
   Workbenches: FEM_Workbench/de
   SeeAlso: FEM_tutorial/de
---

# FEM ConstraintHeatflux/de



## Beschreibung

Defines a convective heat flux load on a surface at a temperature *T* with a film coefficient *h* and with the environment (sink) temperature *T~0~*. The convective heat flux *q* will satisfy: ***q = h(T -T~0~)***. Optionally, can also define a regular surface heat flux load.



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ConstraintHeatflux.svg" width=16px> [Wärmestrombelastung](FEM_ConstraintHeatflux/de.md)** drücken.
    -   Den Menüeintrag **Modell → Thermische Randbedingungen und Belastungen → <img src="images/FEM_ConstraintHeatflux.svg" width=16px> Wärmestrombelastung** auswählen.
2.  In der [3D-Ansicht](3D_view/de.md) die Fläche(n) auswählen, auf die die Wärmestrombelastung angewendet werden soll.
3.  Die gewünschten Werte für Wärmeübergangskoeffizient und Umgebungstemperatur eingeben.

### Option

By default, this feature defines a convective heat flux. By using the option **Surface heat flux**, one can specify a heat flux value in Watts per surface area (W/m\^2).



## Hinweise

-   The heat flux load uses the \*FILM card in CalculiX. It is explained at <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node203.html>
-   The **Surface heat flux** option uses the \*DFLUX card in CalculiX: <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node188.html>





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintHeatflux/de
