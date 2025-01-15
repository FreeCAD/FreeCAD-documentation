---
 GuiCommand:
   Name: Arch Nest
   Name/pl: Architektura: Zagnieżdżanie
   MenuLocation: Narzędzia , Narzędzia panelu , Zagnieżdżanie
   Workbenches: BIM_Workbench/pl
   Version: 0.17
   SeeAlso: Arch_Panel/pl, Arch_Panel_Sheet/pl
---

# Arch Nest/pl



## Opis

Narzędzie **Zagnieżdżanie** pozwala na wybranie płaskiego kształtu jako kontenera i serii innych płaskich kształtów do zorganizowania wewnątrz przestrzeni zdefiniowanej przez kształt kontenera. Jest to zwykle potrzebne w operacjach CNC, w których chcesz wyciąć serię elementów z panelu bazowego i musisz zorganizować te elementy w najlepszy możliwy kompaktowy sposób, aby zajmowały mniej miejsca na panelu.

Algorytm stojący za narzędziem Zagnieżdżanie, jest w ciągłej ewolucji i obecnie nie jest w pełni zoptymalizowany. W przyszłości wydajność tego narzędzia powinna być znacznie lepsza.

<img alt="" src=images/Arch_Nest_example.jpg  style="width:600px;">

*Powyższy obraz przedstawia serię kształtów przed i po operacji zagnieżdżania.*



## Użycie

1.  Wybierz opcję w menu **Narzędzia → Narzędzia panelu → <img src="images/Arch_Nest.svg" width=16px> '''Zagnieżdżanie'''**.
2.  Wybierz obiekt, który będzie kontenerem. Obiekt ten musi być płaski i w tym momencie prostokątny.
3.  Kliknij przycisk **Wybierz zaznaczone**, aby użyć tego obiektu jako kontenera.
4.  Wybierz serię innych płaskich obiektów, które chcesz umieścić wewnątrz kontenera. Wszystkie te obiekty muszą być płaskie i znajdować się w tej samej płaszczyźnie co kontener.
5.  Dostosuj żądane opcje poniżej.
6.  Rozpocznij proces obliczania.
7.  Po zakończeniu obliczeń kliknij przycisk **Podgląd**, aby utworzyć tymczasowy podgląd wyniku.
8.  Jeśli chcesz zastosować wynik *(przenieść i obrócić rzeczywiste kształty na miejsce)*, kliknij przycisk **OK**.

<img alt="" src=images/Arch_Nest_panel.jpg  style="width:800px;"> 
*Panel widoku zadań dla narzędzia '''Zagnieżdżanie'''*



## Uwagi

-   Wszystkie obiekty muszą mieć powierzchnię.
-   W tej chwili narzędzie będzie działać tylko z płaskimi obiektami, które mają taką samą orientację.
-   W tej chwili kontener musi być prostokątny.
-   W tej chwili marginesy / odstępy między elementami nie są jeszcze zaimplementowane.
-   Obliczenia mogą zająć dużo czasu w przypadku wielu obiektów. Zostanie to zoptymalizowane w przyszłości.



---
⏵ [documentation index](../README.md) > Arch Nest/pl
