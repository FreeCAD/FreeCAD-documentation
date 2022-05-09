---
- GuiCommand   */ro
   Name   *Arch ToggleIfcBrepFlag
   Name/ro   *Arch ToggleIfcBrepFlag
   MenuLocation   *Arch → Utilities → Toggle Ifc Brep flag
   Workbenches   *[Arch](Arch_Workbench/ro.md)
   Shortcut   *
   SeeAlso   *
---

# Arch ToggleIfcBrepFlag/ro


</div>

## Descriere


<div class="mw-translate-fuzzy">

Acest instrument permite / dezactivează funcția IfcBrep a unui obiect Arch selectat (valoarea implicită este întotdeauna dezactivată). Dacă indicatorul/steagul este activat la exportul obiectului în format IFC, obiectul va fi exportat ca IfcFacetedBrep, chiar dacă este posibil un export de nivel superior, cum ar fi IfcExtrudedAreaSolid sau IfcBooleanResult. Deși obiectele IfcFacetedBrep sunt mai grele și mai puțin editabile (pierd informații de geometrie cum ar fi istoricul de modelare), ele sunt mai puțin predispuse la erori. În unele cazuri, setarea acestui indicator rezolvă probleme cu obiectele care nu sunt exportate corect atunci când acest indicator nu este setat.


</div>


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Selectați un obiect Arch
2.  Selectați meniul pe traseul Arch → Utilities → **<img src="images/Arch_ToggleIfcBrepFlag.png" width=16px> [Toggle IfcBrepFlag](Arch_ToggleIfcBrepFlag.md)
**


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch ToggleIfcBrepFlag/ro
