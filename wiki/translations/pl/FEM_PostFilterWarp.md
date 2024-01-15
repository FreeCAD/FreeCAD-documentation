---
 GuiCommand:
   Name: FEM PostFilterWarp
   Name/pl: Filtr wizualizacji deformacji
   MenuLocation: Wyniki , Filtr wizualizacji deformacji
   Workbenches: FEM_Workbench/pl
   SeeAlso: FEM_PostPipelineFromResult/pl, FEM_tutorial/pl
---

# FEM PostFilterWarp/pl



## Opis

Wyświetla zdeformowany kształt modelu używając podanego współczynnika skali. Zatem filtr wizualizacji deformacji ma wpływ tylko na wektory wyników, które deformują siatkę.

Rezultat będzie taki sam jak w przypadku suwaka *Przemieszczenie* w oknie dialogowym [obiektu wyników](FEM_ResultShow/pl.md) z tą różnicą, że przemieszczenie dla filtra wizualizacji deformacji jest w metrach. Przykładowo, jeśli używasz [układu jednostek](Preferences_Editor/pl#Jednostki.md), w którym jednostką długości jest mm i ustawisz współczynnik deformacji 100 w oknie dialogowym [obiektu wyników](FEM_ResultShow/pl.md), musisz ustawić współczynnik 100.000 dla filtra wizualizacji deformacji żeby uzyskać ten sam efekt.

![](images/FEM_Warp-Filter-Example.gif )

*Filtr wizualizacji deformacji w przypadku belki wspornikowej.*



## Użycie

1.  Zaznacz wcześniej utworzony [obiekt prezentacji graficznej wyników](FEM_PostPipelineFromResult/pl.md).
2.  Wywołaj polecenie poprzez:
    -   Wciśnięcie przycisku **<img src="images/FEM_PostFilterWarp.svg" width=16px> '''Filtr wizualizacji deformacji'''**.
    -   Wybranie opcji **Wyniki → <img src="images/FEM_PostFilterWarp.svg" width=16px> Filtr wizualizacji deformacji** z menu.
3.  Dostosuj **Opcje wyświetlania wyników** tak jak dla [obiektu prezentacji graficznej wyników](FEM_PostPipelineFromResult/pl.md). Ukryj obiekt prezentacji graficznej wyników żeby zobaczyć efekty filtra wizualizacji deformacji.
4.  Podaj **Współczynnik deformacji geometrii** bezpośrednio lub użyj suwaka żeby go ustawić. Pola **Min. deformacja geometrii** i **Max. deformacja geometrii** pozwalają Ci dostosować zakres suwaka.
5.  Wciśnij przycisk **OK** aby zakończyć polecenie.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostFilterWarp/pl
