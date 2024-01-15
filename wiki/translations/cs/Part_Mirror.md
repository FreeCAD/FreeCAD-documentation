# Part Mirror/cs
---
 GuiCommand:   Name: Part Mirror   Name/cs: Díl Zrcadlení   MenuLocation: Díl -> Zrcadlení   Workbenches: Part_Workbench/cs   Díl, Kompletace|SeeAlso: ---


</div>

## Description


<div class="mw-translate-fuzzy">

## Úvod

\'Zrcadlit objekt\' - Tento nástroj vytváří nový objekt, který je odrazem (obrazem) původního objektu (zdroje). Obraz objektu je vytvořen za rovinou zrcadlení. Rovina zrcadlení může být standardní rovina (**XY**, **YZ**, or **XZ**) nebo jakákoliv rovina paralení ke standardní rovině.


</div>

Příklad:

![](images/PARTMirrorBeforev11.png )



*Before*

![](images/PARTMirrorAfterv11.png )



*After mirrored through YZ plane*



## Použití

![](images/PartMirroring_Scr1.png )


<div class="mw-translate-fuzzy">

Ze seznamu vyberte zdrojový objekt. Vyberte standardní **Mirror plane** z rozbalovacího seznamu.


</div>

When the select button label says **Selecting** you are in reference selection mode and there is a selection gate in effect, which disallows the selection of unsupported reference objects. Click the button to toggle the selection gate off, the button label then changes to **Select reference**.

The mirror plane is defined by a **Normal** (direction) and a **Base** (position). When the **Mirror Plane** property contains a reference object these properties are made read-only as they are then computed based on that object. The plane is infinite even if the reference object is not.

A reference object can be a planar face, such as the face of a [Part Box](Part_Box.md), a circular edge, a [Datum Plane](PartDesign_Plane.md), an [origin plane](App_OriginGroupExtension.md) of a [Std Part](Std_Part.md) container, or any object with a single planar face or single circular edge. There is also support for [Links](App_Link.md). Note, however, that B-spline surfaces, such as [ruled surfaces](Part_RuledSurface.md) or [loft faces](Part_Loft.md) are not supported.

## Options


<div class="mw-translate-fuzzy">

## Volby

Políčka **Základní bod** mohou být použity pro posunutí roviny zrcadlení vzhledem ke standardní rovině zdrcadlení. Pouze jedno z políček **X**, **Y**, nebo **Z** je platné pro danou standardní rovinu.


</div>


<div class="mw-translate-fuzzy">

  Standardní rovina   Základní políčko   Vliv
    
  **XY**              **Z**              Posune rovinu zrcadlení podle osy Z.
  **XY**              **X**, **Y**       Žádný vliv.
  **XZ**              **Y**              Posune rovinu zrcadlení podle osy Y.
  **XZ**              **X**, **Z**       Žádný vliv.
  **YZ**              **X**              Posune rovinu zrcadlení podle osy X.
  **YZ**              **Y**, **Z**       Žádný vliv.


</div>

## Notes


<div class="mw-translate-fuzzy">

## Omezení

-   Jiné roviny zrcadlení (např. to co nejsou paralelní se standardními rovinami) nejsou podporovány (k verzi FC 0.13).


</div>



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Mirror/cs
