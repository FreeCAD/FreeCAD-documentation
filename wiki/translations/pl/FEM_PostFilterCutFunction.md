---
 GuiCommand:
   Name: FEM PostFilterCutFunction
   Name/pl: Filtr cięcia funkcją
   MenuLocation: Wyniki , Filtr cięcia funkcją
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_PostPipelineFromResult/pl, FEM_PostCreateFunctions/pl, FEM_tutorial/pl
---

# FEM PostFilterCutFunction/pl



## Opis

Wyświetla wyniki na sferze lub płaszczyźnie przecinającej model.

<img alt="" src=images/FEM_Function-Cut-Filter-Example.png  style="width:400px;">

*Filtr cięcia funkcją ze sferą jako funkcją cięcia.Oryginalny obiekt prezentacji graficznej wyników jest półprzezroczysty.*



## Użycie

1.  Zaznacz wcześniej utworzony [obiekt prezentacji graficznej wyników](FEM_PostPipelineFromResult/pl.md).
2.  Wywołaj polecenie poprzez:
    -   Wciśnięcie przycisku **<img src="images/FEM_PostFilterCutFunction.svg" width=16px> '''Filtr cięcia funkcją'''**.
    -   Wybranie opcji **Wyniki → <img src="images/FEM_PostFilterCutFunction.svg" width=16px> Filtr cięcia funkcją** z menu.
3.  Dostosuj **Opcje wyświetlania wyników** jak dla [obiektu prezentacji graficznej wyników](FEM_PostPipelineFromResult/pl.md). Może być konieczne ukrycie obiektu prezentacji graficznej wyników żeby zobaczyć efekt filtra cięcia funkcją w podglądzie.
4.  Skorzystaj z jednego z poniższych podejśćː
    -   Jeśli [funkcja filtra](FEM_PostCreateFunctions/pl.md) nie jest jeszcze zdefiniowana, wciśnij przycisk **<img src="images/List-add.svg" width=16px> Utwórz
** i wybierz **<img src="images/FEM_PostCreateFunctionPlane.svg" width=16px> Płaszczyzna** lub **<img src="images/FEM_PostCreateFunctionSphere.svg" width=16px> Sfera**
    -   Wybierz istniejącą funkcję filtra z listy. Jeśli to konieczne, dostosuj parametry cięcia aby upewnić się, że model jest przecinany. Pamiętaj, że zmienione parametry cięcia wpłyną również na parametry używanej funkcji filtra.
5.  Wyniki zostaną wyświetlone na powierzchni funkcji filtra.
6.  Wciśnij przycisk **OK** aby zakończyć polecenie.

**Uwaga**: **Pole** może być ustawione tylko jeśli funkcja filtra istnieje i została zastosowana przy pomocy <img alt="" src=images/FEM_PostApplyChanges.svg  style="width:16px;"> [Zastosuj zmiany](FEM_PostApplyChanges/pl.md). Alternatywnie, możesz ponownie otworzyć okno dialogowe filtra.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterCutFunction/pl
