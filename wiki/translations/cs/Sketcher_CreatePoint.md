# Sketcher CreatePoint/cs
---
- GuiCommand:/cs   Name:Sketcher CreatePoint   Name/cs: Skicář Bod   Workbenches:[[Sketcher Workbench/cs   Skicář]]|MenuLocation:Náčrt → Skicář Konstrukce →  Vytvořit bod   SeeAlso:---


</div>

## Popis


<div class="mw-translate-fuzzy">

Nástroj Bod vytvoří bod v aktuálním listu \"**Skicáře**\".


</div>

[480px\|Point in the sketcher](IMAGE:Sketcher_Point_fr_01.png.md)


<div class="mw-translate-fuzzy">

## Použití


</div>


<div class="mw-translate-fuzzy">

-   Funkci aktivujete stisknutím tlačítka **<img src="images/Sketcher_CreatePoint.svg" width=24px> Bod**.
-   Musí být stisknuto tolikrát, kolik bodů chcete vytvořit.
-   Při podržení klávesy **Ctrl** při kreslení zajistí [zachycení](Draft_Snap/cs.md) bodu k nejbližšímu zachycovacímu bodu, bez ohledu na jeho vzdálenost.
-   Klávesu **Esc** stiskněte pokud chcete přerušit operaci a ukončit funkci.


</div>

## Volby

-   By default points are created as construction geometry and therefore are not visible outside of Sketch editing mode. Use the <img alt="" src=images/Sketcher_ToggleConstruction.svg  style="width:16px;"> [Toggle Construction](Sketcher_ToggleConstruction.md) tool to change them to normal geometry. <small>(v0.19)</small> 
-   A mode to snap to the grid can be set in the [Sketcher Preferences](Sketcher_Preferences.md). The point then snaps to the grid, if it has less than 25% grid distance to a grid line. The snap mode does not fix the point to the grid. It still has two degrees of freedom and can be moved with the mouse or constrained to other locations.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePoint/cs
