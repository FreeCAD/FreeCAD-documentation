---
 GuiCommand:
   Name: TechDraw ShowAll
   Name/pl: Rysunek Techniczny: Pokaż / ukryj niewidoczne krawędzie
   MenuLocation: Rysunek Techniczny , Dodaj linie , Pokaż / ukryj niewidoczne krawędzie
   Workbenches: TechDraw_Workbench/pl
   Version: 0.19
   SeeAlso: TechDraw_DecorateLine/pl
---

# TechDraw ShowAll/pl



## Opis

służy do tymczasowego wyświetlania, a następnie ukrywania niewidocznych linii w widoku. Linie mogą być ukryte za pomocą narzędzia [Zmień wygląd linii](TechDraw_DecorateLine/pl.md). Należy pamiętać, że \"niewidoczność\" jest stanem kosmetycznym, którego nie należy mylić z ukrytymi liniami, które są konstrukcjami geometrycznymi.



## Użycie

1.  Wybierz widok z niewidocznymi liniami na stronie lub w oknie [Widok drzewa](Tree_view/pl.md).
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_ShowAll.svg" width=16px> '''Pokaż / Ukryj niewidoczne krawędzie'''**.
    -   Wybierz opcję z menu **Rysunek Techniczny → Dodaj linie → <img src="images/TechDraw_ShowAll.svg" width=16px> Pokaż / Ukryj niewidoczne krawędzie**.
3.  Wszystkie niewidoczne linie w widoku są wyświetlane lub ukrywane.



## Uwagi

-   Aby trwale uwidocznić niewidoczne linie, użyj narzędzia <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:16px;"> [Zmień wygląd linii](TechDraw_DecorateLine/pl.md).



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
