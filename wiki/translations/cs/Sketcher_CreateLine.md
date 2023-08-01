# Sketcher CreateLine/cs
---
- GuiCommand:/cs   Name:Sketcher CreateLine   Name/cs:Skicář Přímka   Workbenches:[MenuLocation:Náčrt → Skicář Konstrukce → Vytvořit přímku   SeeAlso:[[Sketcher CreatePolyline/cs|Skicář Lomená čára](Sketcher_Workbench/cs___Skicář]].md)---


</div>



## Popis


<div class="mw-translate-fuzzy">

Tento nástroj nakreslí přímku zadáním dvou bodů ve 3D pohledu. Při spuštění nástroje se ukazatel myši změní na bílý křížek s ikonou červené přímky. Vedle jsou zobrazeny souřadnice v reálném čase.


</div>

![](images/Sketcher_LineExample1.png‎ )

The created line object starts and ends at the given points, but the line is infinite regarding the constraints [Tangent](Sketcher_ConstrainTangent.md), [Point On Object](Sketcher_ConstrainPointOnObject.md) and [Internal Angle](Sketcher_ConstrainAngle.md). This means for example, that a point with the constraint [Point On Object](Sketcher_ConstrainPointOnObject.md) may not be located between the two given points but can lie outside of the two points on the extension of the drawn line.




<div class="mw-translate-fuzzy">

## Použití


</div>


<div class="mw-translate-fuzzy">

-   Zadejte body na prázdné ploše ve 3D pohledu nebo na existujícím objektu (v okně Úkolů musí být aktivní automatická vazba (auto constraint)).
-   Stisknutím klávesy **Esc** nebo kliknutím na pravé tlačítko myši se funkce přeruší.


</div>





{{Sketcher Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreateLine/cs
