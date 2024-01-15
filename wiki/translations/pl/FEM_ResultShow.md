---
 GuiCommand:
   Name: FEM ResultShow
   Name/pl: Pokaż wyniki
   MenuLocation: Wyniki , Pokaż wyniki
   Workbenches: FEM_Workbench/pl
   Shortcut: **R** **S**
   SeeAlso: FEM_PostPipelineFromResult/pl, FEM_tutorial/pl
---

# FEM ResultShow/pl



## Opis

To polecenie otwiera okno dialogowe dla obiektu wyników MES. Obiekt wyników jest automatycznie tworzony gdy analiza MES jest przeprowadzana przy użyciu solvera [Calculix](FEM_SolverCalculixCxxtools/pl.md) lub [Z88](FEM_SolverZ88/pl.md).

Obiekt wyników zawiera siatkę wynikową i pozwala na wizualizację wyników. Jest stworzony, a więc i ograniczony do wyników termomechanicznych. Oprócz [solvera Elmer](FEM_SolverElmer/pl.md), może być używany jako alternatywa dla [prezentacji graficznej wyników](FEM_PostPipelineFromResult/pl.md). Prezentacja graficzna wyników może być używana do wyświetlania dowolnego typu wyników (również elektrycznych itd.).

Jednostki używane przez obiekt wyników to te ustawione w [systemie jednostek](Preferences_Editor/pl#Jednostki.md), podczas gdy dla prezentacji graficznej wyników są to jednostki [SI](https://pl.wikipedia.org/wiki/Uk%C5%82ad_SI).

Wizualizacja wyników jest aktywna tylko gdy okno dialogowe jest otwarte. Jednak ustawienia okna dialogowego są przechowywane w pliku z modelem FreeCAD.



## Użycie

Aby pokazać okno dialogowe wyników, zaznacz obiekt wyników w [widoku drzewa](Tree_view/pl.md) a następnie wciśnij przycisk **<img src="images/FEM_ResultShow.svg" width=16px> '''Pokaż wyniki'''** lub wybierz opcję **Wyniki → <img src="images/FEM_ResultShow.svg" width=16px> Pokaż wyniki** (skrót **R** a następnie **S**) z menu. Alternatywnie, możesz również kliknąć dwukrotnie na obiekcie wyników w widoku drzewa.

Gdy okno dialogowe jest otwarte, siatka wynikowa jest automatycznie pokazana.

[left\|framed](File:FEM_Result-Object-Dialog.png.md)

Okno dialogowe jest zaprezentowane po lewej i oferuje następujące możliwościː

-   Wybierz typ wyniku a wartości minimalna i maksymalna będą wyświetlone w oknie dialogowym. Siatka wynikowa będzie miała odpowiednią mapę kolorów.

-   Wciśnij przycisk **'''Histogram'''** aby uzyskać histogram pokazujący ile węzłów siatki ma dany wynik. Histogram może być modyfikowany przyciskami w jego pasku narzędzi. Możliwe jest też zapisanie histogramu jako obrazu przy pomocy przycisku zapisu w jego pasku narzędzi.

-   Zaznacz opcję **Pokaż** aby aktywować suwak i zwizualizować deformację siatki wynikowej. Wartość suwaka to współczynnik, przez który wynik *Wielkość przemieszczenia* jest mnożony.**Uwaga**: Suwak wpływa tylko na wielkość przemieszczenia (przemieszczenie wypadkowe), nie na jego składowe X, Y, Z.

-   Przy pomocy przycisku Po wprowadzeniu równania wciśnij przycisk a wynik zostanie pokazany w polach pokazujących wartości minimalną i maksymalną. Mapa kolorów na siatce wynikowej zostanie odpowiednio zmieniona.**Uwaga**: Wyniki obliczeń zawsze mają jednostkę MPa, mm lub T, niezależnie od tego jakiego [układu jednostek](Preferences_Editor/pl#Jednostki.md) używasz.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ResultShow/pl
