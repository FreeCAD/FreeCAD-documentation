---
 GuiCommand:
   Name: FEM SolverZ88
   Name/pl: Solver Z88
   MenuLocation: Rozwiąż , Solver Z88
   Workbenches: FEM_Workbench/pl
   Shortcut: **S** **Z**
   SeeAlso: FEM_tutorial/pl
---

# FEM SolverZ88/pl



## Opis

Polecenie **SolverZ88** umożliwia użycie solvera [Z88](https://en.wikipedia.org/wiki/Z88_FEM_software). Może być wykorzystane do:

1.  Ustawienia parametrów analizy.
2.  Wybrania katalogu roboczego.
3.  Uruchomienia solvera Z88.



## Instalacja

Do korzystania z solvera Z88 musi być zainstalowana otwarta wersja Z88 *(Z88OS)*:

1.  Pobierz plik ZIP ze [strony Z88OS](https://en.z88.de/download-z88os).
2.  Rozpakuj plik ZIP do wybranego folderu.
3.  W [preferencjach MES](FEM_Preferences/pl.md) przejdź do zakładki Z88 i ustaw tam ścieżkę do pliku wykonywalnego **z88r**. Jeśli korzystasz z systemu Windows, będzie to ścieżka do pliku **z88r.exe** w podfolderze **~\bin\win64** katalogu, do którego rozpakowałeś plik ZIP.



## Użycie

1.  Po utworzeniu <img alt="" src=images/FEM_Analysis.svg  style="width:16px;"> [kontenera analizy](FEM_Analysis/pl.md), skorzystaj z jednej z następujących możliwości:
    -   Wybierz opcję **Rozwiąż → <img src="images/FEM_SolverZ88.svg" width=x16px> Solver Z88** z menu.
    -   Wciśnij klawisz **S** a następnie **Z**.
2.  Dwukrotnie kliknij na obiekcie <img alt="" src=images/FEM_SolverZ88.svg  style="width:" height="16px;"> SolverZ88.
3.  Wybierz **Typ analizy**.
4.  Wciśnij przycisk **Zapisz**.
5.  Wciśnij przycisk **Uruchom**.

W wyniku tych czynności uw [widoku drzewa](Tree_view/pl.md) zyskasz obiekt nazwany *Z88_xxx_results* *(w zależności od uruchomionej symulacji)*. To ten sam rodzaj obiektu jaki uzyskuje się uruchamiając [solver CalculiX](FEM_SolverCalculixCxxtools/pl.md). Zaczynając od tego, możesz wizualizować wyniki przy pomocy [prezentacji graficznej wyników](FEM_PostPipelineFromResult/pl.md) i [filtrów przycinania](FEM_Workbench/pl#Menu__Wyniki.md).



## Preferencje

Zobacz [preferencje Z88](FEM_Preferences/pl#Z88.md) aby znaleźć możliwe do ustawienia parametry solvera, takie jak używana metoda rozwiązywania.





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM SolverZ88/pl
