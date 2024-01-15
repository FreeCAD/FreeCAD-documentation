---
 GuiCommand:
   Name: FEM PostFilterClipScalar
   Name/pl: Filtr przycinania skalarnego
   MenuLocation: Wyniki , Filtr przycinania skalarnego
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_PostPipelineFromResult/pl, FEM_tutorial/pl
---

# FEM PostFilterClipScalar/pl



## Opis

Przycina pole używając podanej wartości skalarnej.

<img alt="" src=images/FEM_Scalar-Clip-Filter-Example.png  style="width:400px;">

*Rezultat filtra przycinania skalarnego.Oryginalny obiekt prezentacji graficznej wyników jest półprzezroczysty.*

Filtr przycinania skalarnego może być łączony z innymi filtrami. Przykładowo, filtr przycinania skalarnego na [filtrze wizualizacji deformacji](FEM_PostFilterWarp/pl.md) (półprzezroczysty):

<img alt="" src=images/FEM_Scalar-Clip-Filter-On-Warp-Example.png  style="width:600px;">



## Użycie

1.  Zaznacz wcześniej utworzony [obiekt prezentacji graficznej wyników](FEM_PostPipelineFromResult/pl.md) lub inny dodany filtr.
2.  Wywołaj polecenie poprzez:
    -   Wciśnięcie przycisku **<img src="images/FEM_PostFilterClipScalar.svg" width=16px> '''Filtr przycinania skalarnego'''**.
    -   Wybranie opcji **Wyniki → <img src="images/FEM_PostFilterClipScalar.svg" width=16px> Filtr przycinania skalarnego**.
3.  Dostosuj **Opcje wyświetlania wyników** jak dla [obiektu prezentacji graficznej wyników](FEM_PostPipelineFromResult/pl.md). Ukryj obiekt prezentacji graficznej wyników żeby zobaczyć efekt filtra przycinania skalarnego.
4.  Wybierz typ **Skalar** z listy rozwijanej.
5.  Zdefiniuj wartość **Skalar do przycinania** bezpośrednio lub przy pomocy suwaka.
6.  Domyślnie wszystkie obszary z wartościami pola poniżej podanej wartości zostaną ukryte. Zaznacz opcję **Przytnij na drugą stronę** żeby odwrócić wyświetlanie i ukryć obszary z wartościami powyżej podanej.
7.  Wciśnij przycisk **OK** żeby zakończyć polecenie.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterClipScalar/pl
