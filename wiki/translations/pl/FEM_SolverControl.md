---
- GuiCommand:
   Name:FEM SolverControl
   Name/pl:MES: Kontrola Solwera
   MenuLocation:Solve - Solver job control
   Workbenches:[MES](FEM_Workbench/pl.md)
   Shortcut:**S** **T**
   SeeAlso:[Uruchom solver](FEM_SolverRun/pl.md)
---

# FEM SolverControl/pl

## Opis

Polecenie to służy do sterowania solverem FEM *(zapis pliku wejściowego, jego edycja, uruchomienie solvera)*.

## Użycie

1.  Wybierz obiekt Solvera w [Widoku drzewa](Tree_view/pl.md), np. solver CalcuilX <img alt="" src=images/FEM_SolverCalculixCxxtools.svg  style="width:24px;"> **SolverCcxTools**.
2.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/FEM_SolverControl.svg" width=16px> [Kontrola pracy solvera](FEM_SolverControl.md)**.
    -   Wybierz z menu opcję **Rozwiąż → <img src="images/FEM_SolverControl.svg" width=16px> Kontrola pracy solvera**.
    -   Użyj skrótu klawiaturowego: **S** a następnie **T**.
3.  Opcjonalnie, edytuj katalog roboczy.
4.  Opcjonalnie, wybierz typ analizy.
5.  Kliknij **Write .inp file**, aby zapisać plik wejściowy.
6.  Opcjonalnie, kliknij **Edit .inp file**.
    -   Plik wejściowy zostanie otwarty, więc możesz go edytować i zapisać przez **Ctrl**+**S**.
7.  Kliknij **Uruchom CalculiX**, aby uruchomić solver.
    -   Rozwiązanie może zająć sporo czasu dla dużych modeli.

## Uwagi

-   Domyślny katalog roboczy można zmienić w **Edycja → Preferencje ... → MES**.
-   Elementy sterujące dla innych solverów mogą się różnić.
-   Uproszczona wersja polecenia to <img alt="" src=images/FEM_SolverRun.svg  style="width:24px;"> [Uruchom obliczenia solvera](FEM_SolverRun/pl.md).





{{FEM Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverControl/pl
