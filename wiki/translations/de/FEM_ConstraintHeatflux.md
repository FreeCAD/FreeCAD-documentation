---
 GuiCommand:Container|
{{GuiCommand/de
   Name: FEM ConstraintHeatflux
   Name/de: FEM RandbedingungWärmestrom
   MenuLocation: Modell , Thermische Randbedingungen und Belastungen , Wärmestrombelastung
   Workbenches: FEM_Workbench/de
   SeeAlso: FEM_tutorial/de
}}
{{GuiCommandFemInfo/de
   Solvers: CalculiX, Elmer
}}
---

# FEM ConstraintHeatflux/de



## Beschreibung

Definiert standardmäßig einen konvektiven Wärmestrom auf einer Oberfläche bei einer Temperatur $T$ mit einem Filmkoeffizienten $h$ und mit der Umgebungstemperatur (Senke/Umgebung) $T_{0}$. Der konvektive Wärmestrom $q$ erfüllt: $q=h(T-T_{0})$. Optional kann auch eine regelmäßige Oberflächenwärmestrombelastung definiert werden.


<small>(v1.0)</small> 

: Kann auch zur Definition eines Strahlungswärmestroms auf einer Oberfläche verwendet werden. Er erfüllt: $q=\epsilon \sigma(T^{4}-T_{0}^{4})$ wobei $\epsilon$ der Emissionsgrad der Oberfläche und $\sigma$ die Stefan-Boltzmann-Konstante ist.



## Anwendung

1.  Es gibt mehrere Möglichkeiten, den Befehl aufzurufen:
    -   Die Schaltfläche **<img src="images/FEM_ConstraintHeatflux.svg" width=16px> [Wärmestrombelastung](FEM_ConstraintHeatflux/de.md)** drücken.
    -   Den Menüeintrag **Modell → Thermische Randbedingungen und Belastungen → <img src="images/FEM_ConstraintHeatflux.svg" width=16px> Wärmestrombelastung** auswählen.
2.  Die Schaltfläche **Hinzufügen** drücken und in der [3D-Ansicht](3D_view/de.md) die Fläche(n) auswählen, auf die die Wärmestrombelastung angewendet werden soll. Wahlweise die Schaltfläche **Entfernen** drücken, um ausgewählte Flächen aus der Auswahlliste zu entfernen.
3.  Die Art des Wärmeflusses auswählen und die Parameter eingeben.
    -   *Surface Convection* (default) - Konvektionswärmefluss: Nach Wunsch *Film coefficient* (Randschichtbeiwert) und *Ambient temperature* (Umgebunstemperatur) eingeben.

    -   
        <small>(v1.0)</small> 
        
        : *Surface Radiation* - Strahlungswärmefluss: Die *Emissivity* (Emissionsgrad) und *Ambient temperature* (Umgebunstemperatur) eingeben.

    -   *Surface heat flux* - allgemeiner Wärmefluss: Den *Surface heat flux* (Oberflächenwärmefluss) in Watt pro Oberflächenbereich (W/m\^2).



## Hinweise

-   Die Wärmestrombelastung verwendet je nach gewähltem Modus die folgenden CalculiX-Karten:
    -   [\*FILM](http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node203.html) für *Oberflächenkonvektion*

    -   
        <small>(v1.0)</small> 
        
        : [\*RADIATE](http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node234.html) für *Surface Radiation*

    -   [\*DFLUX](http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node188.html) für *Oberflächenwärmestrom*





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintHeatflux/de
