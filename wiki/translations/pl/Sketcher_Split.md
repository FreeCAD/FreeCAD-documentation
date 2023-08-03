---
 GuiCommand:
   Name: Sketcher Split
   Name/pl: Szkicownik: Podziel krawędź
   MenuLocation: Szkic , Elementy geometryczne szkicownika , Podziel krawędź
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **Z**
   Version: 0.20
   SeeAlso: Sketcher_Trimming/pl
---

# Sketcher Split/pl



## Opis

To narzędzie dzieli krawędź na dwie, a istniejące wiązania są kopiowane do nowej krawędzi. Pozycja punktu styku krawędzi nie jest objęta wiązaniami. Krzywe okresowe *(tj. koła, elipsy i okresowe krzywe złożone)* są przekształcane na krzywe nieokresowe *(odpowiednio łuki okręgów, łuki elips i nieokresowe krzywe złożone z krzywych złożonych)*.

![](images/SketcherSplitExample1.png ) ![](images/SketcherSplitExample2.png ) ![](images/SketcherSplitExample3.png )



## Użycie

1.  Naciśnij przycisk **[<img src=images/Sketcher_Split.svg style="width:16px"> '''Podziel krawędź'''**. Kursor myszki zmieni się w biały krzyż z czerwonym symbolem podziału.
2.  Kliknij krawędź w miejscu, w którym chcesz ją podzielić.
3.  Z krawędzi linii i łuku zostaną utworzone dwie nowe, połączone w miejscu kliknięcia. Okrąg jest zamieniany na łuk z tym samym punktem środkowym i innymi wiązaniami, które miał oryginalny okrąg.
4.  Naciśnięcie klawisza **Esc** lub wciśnięcie prawego przycisku myszy zakończy działanie funkcji.



## Ograniczenia

-   W FreeDAD{{VersionMinus/pl|0.20}} działanie nie jest obsługiwane dla elips, paraboli, hiperbol i krzywych złożonych.



## Uwagi

-   Wszystkie zbieżności są przenoszone - punkt początkowy, punkt końcowy i punkt środkowy (jeśli dotyczy).
-   Punkt na wiązaniu obiektu jest przenoszony do bliższej, nowo utworzonej krawędzi.
-   Wiązania pionowe i poziome są kopiowane do obu obiektów pochodnych.
-   Wiązania równoległe i prostopadłe są kopiowane dla obu odcinków linii, dla łuku tylko raz, do bliższej części.
-   Wiązanie równości jest przenoszone tylko dla powstałych krawędzi łuku, segmenty linii go nie otrzymują.
-   Wiązanie symetrii nie jest obecnie przenoszone.
-   Wiązanie zablokowania nie jest obecnie przenoszone.
-   Więzy poziome, pionowe i długości pomiędzy punktami są przenoszone na zewnętrzne punkty nowych krawędzi.
-   Wiązania odległości punktów są przypisywane tylko raz, do bliższego odcinka krawędzi.
-   Wiązania promienia i średnicy są kopiowane do każdego powstałego łuku.
-   Wiązanie kąta nie jest obecnie przenoszone.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Split/pl
