---
 GuiCommand:
   Name: Sketcher_MapSketch
   Name/pl: Szkicownik: Mapuj szkic na powierzchnię
   Workbenches: Sketcher_Workbench/pl, PartDesign_Workbench/pl
   MenuLocation: Projekt Części / Szkicownik , Mapuj szkic na powierzchnię ...
   SeeAlso: Sketcher_ReorientSketch/pl, Sketcher_NewSketch/pl
---

# Sketcher MapSketch/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_MapSketch.svg  style="width:24px;"> **Mapuj szkic na powierzchnię** dołącza szkic do wybranej geometrii.

Proszę zauważyć, że narzędzie to nie jest używane do tworzenia nowych szkiców. Mapuje ono jedynie lub przekształca istniejący szkic na powierzchnię bryły lub funkcji Part Design. Typowe przypadki użycia to:

-   Szkic został stworzony na standardowej płaszczyźnie *(XY, XZ, YZ)* i chcesz go dołączyć na powierzchni bryły, aby zbudować na niej obiekt.
-   Szkic został dołączony na konkretnej powierzchni bryły, ale trzeba go dołączyć na innej powierzchni.
-   Zepsuty model wymaga naprawy.

<img alt="" src=images/Sketcher_MapSketch_00.png  style="width:480px;">



## Użycie

-   Wybierz powierzchnię elementu Part Design lub bryły.
-   Kliknij na ikonę **<img src="images/Sketcher_MapSketch.svg" width=16px> [Mapuj szkic na powierzchnię](Sketcher_MapSketch.md)** na pasku narzędzi *(lub przejdź do menu PartDesign lub Sketch w zależności od tego, które Środowisko pracy jest aktywne)*.

1.  Wybierz obiekt z kształtem, lub jeden lub więcej wierzchołków, krawędzi, i/lub ścian, oraz/lub płaszczyznę.
2.  Istnieje kilka sposobów, aby uruchomić narzędzie:
    -   Kliknij przycisk **<img src="images/Sketcher_MapSketch.svg" width=16px> '''Mapuj szkic na powierzchnię'''**.
    -   Wybierz opcję z menu **Szkic → <img src="images/Sketcher_MapSketch.svg" width=16px> Mapuj szkic na powierzchnię**.
3.  Otwiera się okno dialogowe **Wybierz szkic**.
4.  Wybierz szkic z rozwijanej listy.
5.  Naciśnij przycisk **OK**.
6.  Otwiera się okno dialogowe **Dołączanie szkicu**.
7.  Wybierz [metodę dołączania](Part_EditAttachment/pl#Tryby_dołączenia.md) z listy rozwijanej. Lub wybierz **Nie dołączaj**, aby odłączyć szkic.
8.  Naciśnij przycisk **OK**.





{{Sketcher Tools navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher MapSketch/pl
