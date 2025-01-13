---
 GuiCommand:Container|
{{GuiCommand/de
   Name: FEM ConstraintSpring
   Name/de: FEM RandbedingungFeder
   MenuLocation: Modell , Mechanische Randbedingungen und Lasten , Feder
   Workbenches: FEM_Workbench/de
   Shortcut: 
   Version: 0.20
   SeeAlso: 
}}
{{GuiCommandFemInfo/de
   Solvers: Elmer
}}
---

# FEM ConstraintSpring/de



## Beschreibung

Legt eine Randbedingung Feder fest, die für mechanische Analysen mit dem Löser <img alt="" src=images/FEM_SolverElmer.svg  style="width:32px;"> [Elmer](FEM_SolverElmer/de.md) verwendet wird.


{{Version/de|0.21}}

: Die Randbedingung Feder kann für die Gleichungen <img alt="" src=images/FEM_EquationDeformation.svg  style="width:32px;"> [Verformung](FEM_EquationDeformation/de.md) und <img alt="" src=images/FEM_EquationElasticity.svg  style="width:32px;"> [Elastizität](FEM_EquationElasticity/de.md) verwendet werden.



## Anwendung

1.  Entweder die Schaltfläche **<img src="images/FEM_ConstraintSpring.svg" width=16px> [Feder](FEM_ConstraintSpring/de.md)** drücken oder den Menüeintrag **Modell → Mechanische Randbedingungen und Belastungen → <img src="images/FEM_ConstraintSpring.svg" width=16px> Feder** auswählen.
2.  Die Schaltfläche **Hinzufügen** Drücken.
3.  In der [3D-Ansicht](3D_view/de.md) die Flächen auswählen, auf die die Feder angewendet werden soll. Wahlweise die Schaltfläche **Remove** drücken und auf die Objekte klicken, die aus der Auswahl entfernt werden sollen.
4.  Werte für normale oder tangentiale Steifigkeit (in N/m) eingeben und auswählen, welche Elmer verwenden soll.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintSpring/de
