---
 GuiCommand:
   Name: FEM PostFilterDataAlongLine
   Name/pl: Filtr przycięcia linią
   MenuLocation: Wyniki , Filtr przycięcia linią
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_PostPipelineFromResult/pl, FEM_tutorial/pl
---

# FEM PostFilterDataAlongLine/pl



## Opis

Tworzy wykres wartości pola wzdłuż wskazanej linii.

![](images/FEM_Line-Clip-Filter-Example.png )

*Filtr przycięcia linią w [filtrze przycięcia obszaru](FEM_PostFilterClipRegion/pl.md).
Filtr przycięcia obszaru jest półprzezroczysty.
Część linii poza filtrem przycięcia obszaru jest ustawiona na wartość zero i dlatego wyświetla się na niebiesko.*



## Użycie

1.  Zaznacz wcześniej utworzony [obiekt prezentacji graficznej wyników](FEM_PostPipelineFromResult/pl.md) lub inny filtr.
2.  Wywołaj polecenie poprzez:
    -   Wciśnięcie przycisku **<img src="images/FEM_PostFilterDataAlongLine.svg" width=16px> '''Filtr przycięcia linią'''**.
    -   Wybranie opcji **Wyniki → <img src="images/FEM_PostFilterDataAlongLine.svg" width=16px> Filtr przycięcia linią**.
3.  Wprowadź współrzędne dwóch punktów definiujących linię, wzdłuż której wyniki mają być uzyskane. Opcjonalnie, wciśnij przycisk **Wybierz punkty** i wskaż punkty ręcznie na powierzchni siatki.
4.  Opcjonalnie, podaj **Rozdzielczość**.
5.  Wybierz **Pole** z listy rozwijanej.
6.  Wciśnij przycisk **Utwórzy wykres**. Wykres XY wartości pola w funkcji długości linii zostanie utworzony w osobnym oknie.
7.  Wciśnij przycisk **OK** aby zakończyć polecenie.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterDataAlongLine/pl
