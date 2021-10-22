# Sketcher CreatePolyline/cs
---
- GuiCommand:/cs   Name:Sketcher CreatePolyline   Name/cs:Skicář Lomená čára   Workbenches:[MenuLocation:Náčrt → Skicář Konstrukce → Vytvořit Lomenou čáru   SeeAlso:[[Sketcher CreateLine/cs|Skicář Přímka](Sketcher_Workbench/cs___Skicář]].md)---


</div>

## Popis


<div class="mw-translate-fuzzy">

Tento nástroj funguje podobně jako [Skicář Přímka](Sketcher_CreateLine/cs.md), ale vytváří postupně přímkové segmenty, které jsou spojeny v jejich vrcholech. Při spuštění nástroje se ukazatel myši změní na bílý křížek s červenou ikonou lomené čáry. Souřadnice ukazatele jsou vedle zobrazovány v reálném čase.


</div>

![](images/Sketcher_PolylineExample1.png )



*Polyline started with a line, a tangent arc, a perpendicular arc then a tangent line.*


<div class="mw-translate-fuzzy">

## Použití


</div>

Nástroj má vícenásobný mód, který může bý přepnut klávesou **M**. Například můžete kreslit tečné nebo kolmé oblouky následované přímkovým nebo obloukovým segmentem. Jenom opakovaně stiskáváte **M** pro přepínání mezi různými módy.

1.  Press the **M** key: the new segment is a line which is perpendicular to the previous segment.
2.  Press the **M** key again: the new segment is a line which is tangential to the previous segment.
3.  Press the **M** key again: the new segment is an arc which is tangential to the previous segment.
4.  Press the **M** key again: the new segment is an arc which is perpendicular (left) to the previous segment.
5.  Press the **M** key again: the new segment is an arc which is perpendicular(right) to the previous segment.
6.  Press the **M** key again: You are again in the state where you started; the line is only connected with a coincidence to the previous segment.

-    <small>(v0.18)</small> While in any of the arc modes, holding down the **Ctrl** key (MacOS: **CMD** key) and moving the cursor causes the arc to snap by increments of 45 degrees, relative to the previously created polyline segment.

-   Pick points on an empty area of the 3D view, or on an existing object (auto constraints must be active in TaskView).

-   Pressing **Esc** or clicking the right mouse button *before* closing the polyline to a loop ends the current polyline and you can continue with a new one. Pressing **Esc** or clicking the right mouse button again ends the polyline function.

-   Pressing **Esc** or clicking the right mouse button *after* closing the polyline to a loop ends the polyline function.





{{Sketcher Tools navi

}}

---
[documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePolyline/cs
