# Part Mirror/cs
---
- GuiCommand   */cs   Name   *Part Mirror   Name/cs   *Díl Zrcadlení   MenuLocation   *Díl -> Zrcadlení   Workbenches   *[[Part_Workbench/cs   Díl]], Kompletace|SeeAlso   *---


</div>

## Description


<div class="mw-translate-fuzzy">

## Úvod

\'Zrcadlit objekt\' - Tento nástroj vytváří nový objekt, který je odrazem (obrazem) původního objektu (zdroje). Obraz objektu je vytvořen za rovinou zrcadlení. Rovina zrcadlení může být standardní rovina (**XY**, **YZ**, or **XZ**) nebo jakákoliv rovina paralení ke standardní rovině.


</div>

Příklad   *

![Před](images/PARTMirrorBeforev11.png )


<div class="mw-translate-fuzzy">

![Po (zrcadleno přes rovinu **YZ**)](images/PARTMirrorAfterv11.png ) 


</div>




## Použití

![](images/PARTMirrorDialogv11.png )


<div class="mw-translate-fuzzy">

Ze seznamu vyberte zdrojový objekt. Vyberte standardní **Mirror plane** z rozbalovacího seznamu.


</div>




## Options


<div class="mw-translate-fuzzy">

## Volby

Políčka **Základní bod** mohou být použity pro posunutí roviny zrcadlení vzhledem ke standardní rovině zdrcadlení. Pouze jedno z políček **X**, **Y**, nebo **Z** je platné pro danou standardní rovinu.


</div>

  Standardní rovina   Základní políčko   Vliv
    
  **XY**              **Z**              Posune rovinu zrcadlení podle osy Z.
  **XY**              **X**, **Y**       Žádný vliv.
  **XZ**              **Y**              Posune rovinu zrcadlení podle osy Y.
  **XZ**              **X**, **Z**       Žádný vliv.
  **YZ**              **X**              Posune rovinu zrcadlení podle osy X.
  **YZ**              **Y**, **Z**       Žádný vliv.

## Notes


<div class="mw-translate-fuzzy">

## Omezení

-   Jiné roviny zrcadlení (např. to co nejsou paralelní se standardními rovinami) nejsou podporovány (k verzi FC 0.13).


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Mirror/cs
