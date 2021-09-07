---
- GuiCommand:/pl
   Name:Sketcher Trimming
   Name/pl:Szkicownik: Przytnij krawędź
   MenuLocation:Szkic → Elementy geometryczne szkicownika → Przytnij krawędź
   Workbenches:[Sketcher](Sketcher_Workbench/pl.md)
   Version:0.12
   SeeAlso:[Rozszerz krawędź](Sketcher_Extend/pl.md)
---

## Opis

To narzędzie przycina krawędź do najbliższej nachodzącej krawędzi.

![](images/SketcherTrimExample1.png ) ![](images/SketcherTrimExample2.png ) ![](images/SketcherTrimExample3.png )

## Użycie

1.  Naciśnij przycisk **<img src=images/Sketcher_Trimming.svg style="width:16px"> [przycinania krawędzi](Sketcher_Trimming.md)**. Kursor myszki zmieni się w biały krzyżyk z czerwonym symbolem przycięcia.
2.  Kliknij krawędź, którą chcesz przyciąć.
3.  Segment linii zostanie przycięty do najbliższej zachodzącej na siebie linii. Jeśli po obu stronach klikniętej pozycji znajdują się inne elementy szkicu, kliknięty element jest wycinany.
4.  Naciśnięcie klawisza **Esc** lub naciśnięcie prawego klawisza myszki zakończy działanie funkcji.

## Ograniczenia

-    {{VersionMinus/pl|0.18}}Łuki hiperboli, łuki paraboli i B-spliny nie mogą być przycięte.





{{Sketcher Tools navi

}}  