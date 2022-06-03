---
- GuiCommand   */pl
   Name   *Sketcher_MapSketch
   Name/pl   *Szkicownik   * Mapuj Szkic
   Workbenches   *[Szkicownik](Sketcher_Workbench/pl.md), [Projekt części](PartDesign_Workbench/pl.md)
   MenuLocation   *Projekt części / Szkicownik → Mapuj szkic na powierzchnię
   SeeAlso   *[Utwórz szkic](Sketcher_NewSketch/pl.md)
---

# Sketcher MapSketch/pl

## Opis

To narzędzie mapuje istniejący szkic na powierzchni kształtu. Cechy Part Design stworzone na podstawie tego szkicu zostaną połączone z bryłą podstawową w przypadku cech dodatkowych *(Pad, Revolution)* lub odjęte od bryły podstawowej w przypadku cech odejmowanych *(Pocket, Groove)*.

Proszę zauważyć, że narzędzie to nie jest używane do tworzenia nowych szkiców. Mapuje ono jedynie lub przekształca istniejący szkic na powierzchnię bryły lub funkcji Part Design. Typowe przypadki użycia to   *

-   Szkic został stworzony na standardowej płaszczyźnie *(XY, XZ, YZ)* i chcesz go odwzorować na powierzchni bryły, aby zbudować na niej obiekt.
-   Szkic został zmapowany na konkretnej powierzchni bryły, ale trzeba go zmapować na innej powierzchni.
-   Naprawiając zepsuty model.

<img alt="" src=images/Sketcher_MapSketch_00.png  style="width   *480px;">

## Użycie

-   Wybierz powierzchnię elementu Part Design lub bryły.
-   Kliknij na ikonę **<img src="images/Sketcher_MapSketch.svg" width=16px> [Mapuj szkic na powierzchnię](Sketcher_MapSketch.md)** na pasku narzędzi *(lub przejdź do menu PartDesign lub Sketch w zależności od tego, które Środowisko pracy jest aktywne)*.

## Stosować przy naprawie uszkodzonego modelu 

Funkcja Sketcher   * MapSketch jest często używana przy naprawie uszkodzonego modelu.

Jednym z częstych przypadków zastosowania jest przerwanie wykresu zależności. *(Możesz zobaczyć wykres zależności przez **Narzędzia** → **[Wykres zależności](Std_DependencyGraph/pl.md)**)*. Może się to zdarzyć, gdy usuniesz element na środku drzewa modelu. W poniższym przykładzie uszkodzimy i naprawimy model.

To jest model podstawowy. Ma jedno wyciągnięcie, kieszeń, i wyciągnięcie w tej kieszeni. Zauważ, że wykres zależności jest liniowy.

![](images/JschremppFCADEdit1.png )

Teraz skasowaliśmy kieszeń i szkic, który ją stworzył *(Pocket i Sketch001)*. Zauważ, że wykres zależności jest uszkodzony. Aby naprawić ten model chcemy przymocować Sketch002 do górnej powierzchni Pada. W widoku modelu widać, że łatwo byłoby wybrać niewłaściwą powierzchnię.

![](images/JschremppFCADEdit2.png )

Aby naprawić model, najpierw zmieniamy widoczność brył. Ukrywamy Pad001 i sprawiamy, że Pad jest widoczny.

![](images/JschremppFCADEdit3.png )

Teraz wybieramy górną powierzchnię wyciągnięcia *(Pad)*, kolejnie wybieramy narzędzie *Mapuj szkic na powierzchnię*. W oknie dialogowym, które się pojawi, wybieramy **Sketch002**. Nasz model jest teraz naprawiony. W widoku modelu uwidaczniamy Pad001 i ukrywamy Pad przedstawiony zostanie właściwy model.

![](images/JschremppFCADEdit4.png )





{{Sketcher Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher MapSketch/pl
