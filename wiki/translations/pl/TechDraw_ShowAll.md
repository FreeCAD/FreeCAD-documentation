---
 GuiCommand:
   Name: TechDraw ShowAll
   Name/pl: Rysunek Techniczny: Pokaż / ukryj niewidoczne krawędzie
   MenuLocation: Rysunek Techniczny , Pokaż / ukryj niewidoczne krawędzie
   Workbenches: TechDraw_Workbench/pl
   Version: 0.19
   SeeAlso: TechDraw_DecorateLine/pl
---

# TechDraw ShowAll/pl


</div>



## Opis


<div class="mw-translate-fuzzy">

Narzędzie **Pokaż / ukryj niewidoczne krawędzie** pokazuje lub ukrywa niewidoczne linie w widoku. Należy pamiętać, że \"niewidoczne\" to stan kosmetyczny, którego nie należy mylić z ukrytymi liniami, które są konstrukcjami geometrycznymi.


</div>



## Użycie


<div class="mw-translate-fuzzy">

1.  Wybierz widok na stronie lub w widoku drzewa.
2.  Naciśnij przycisk **<img src="images/TechDraw_ShowAll.svg" width=16px> '''Pokaż / Ukryj niewidoczne krawędzie'''**.
3.  Stan niewidocznych linii w widoku zostanie odwrócony.


</div>

## Notes

-   To make invisible lines permanently visible use <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:16px;"> [TechDraw DecorateLine](TechDraw_DecorateLine.md).



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Efekt działania funkcji **Pokaż / ukryj niewidoczne krawędzie** może być powielony przez [makrodefinicje](Macros/pl.md) lub konsoli z [Python](Python/pl.md). 
```python
v = App.ActiveDocument.View
vvo = v.ViewObject
vvo.ShowAllEdges = True
App.ActiveDocument.recompute()
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ShowAll/pl
