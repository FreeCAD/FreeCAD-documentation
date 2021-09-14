# TechDraw pitch circle tutorial/pl




{{TutorialInfo/pl
|Topic=Rysunek Techniczny
|Level=Początkujący
|Time=10 minut
|Author=Andergrin
|FCVersion=0.19
}}

## Wprowadzenie

Ten poradnik wyjaśnia jak dodać okrąg podziałowy do widoku <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [Rysunku Technicznego](TechDraw_Workbench/pl.md). Zakłada on, że model jest obiektem środowiska <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [Projekt Części](PartDesign_Body/pl.md) z co najmniej trzema otworami w układzie kołowym. Dla okręgu zostanie utworzony osobny szkic. Podobna procedura może być użyta w innych sytuacjach oraz do dodawania innych elementów podobnych do adnotacji na widoku [Rysunku Technicznego](TechDraw_Workbench/pl.md).

<img alt="" src=images/Circle.png  style="width:250px;"> <img alt="" src=images/Pitch_Circle.png  style="width:300px;">

## Tworzenie szkicu okręgu 

1.  Aktywuj <img alt="" src=images/PartDesign_Body.svg  style="width:24px;"> [Zawartość](PartDesign_Body/pl.md).
2.  Jeśli to konieczne: przełącz się na środowisko pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md).
3.  W oknie [widoku 3D](3D_view/pl.md) wybierz odpowiednią ścianę należącą do zawartości.
4.  Utwórz nowy szkic za pomocą polecenia <img alt="" src=images/PartDesign_NewSketch.svg  style="width:24px;"> [Utwórz szkic](PartDesign_NewSketch/pl.md).
5.  Szkic zostanie dołączony do wybranej ściany.
6.  Wywołaj polecenie <img alt="" src=images/Sketcher_External.svg  style="width:24px;"> [Geometria zewnętrzna](Sketcher_External/pl.md).
7.  Wybierz trzy okrągłe krawędzie *(otwory)* z zawartości.
8.  Użyj polecenia <img alt="" src=images/Sketcher_Create3PointCircle.svg  style="width:24px;">[Utwórz okrąg](Sketcher_Create3PointCircle/pl.md), aby utworzyć okrąg związany do punktów środkowych geometrii zewnętrznej.
9.  Szkic powinien być teraz w pełni związany.
10. Zamknij szkic.

## Tworzenie widoku Rysunku Technicznego 

1.  Przełącz się na środowisko pracy <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [Rysunek Techniczny](TechDraw_Workbench/pl.md).
2.  Jeśli jeszcze nie masz: stwórz <img alt="" src=images/TechDraw_PageDefault.svg  style="width:24px;"> [stronę](TechDraw_PageDefault/pl.md).
3.  Upewnij się, że okno [widoku 3D](3D_view.md) jest prawidłowo wyrównane.
4.  Przytrzymaj klawisz **Ctrl** i w [widoku drzewa](Tree_view/pl.md) wybierz bryłę i szkic, który właśnie został utworzony.
5.  Wstaw nowy widok wywołując polecenie <img alt="" src=images/TechDraw_View.svg  style="width:24px;"> [Widok](TechDraw_View/pl.md).
6.  Przełącz się na stronę [Rysunku Technicznego](TechDraw_Workbench/pl.md)
7.  Wybierz okrąg.
8.  Wywołaj polecenie <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:24px;"> [Zmień wygląd linii](TechDraw_DecorateLine/pl.md)
9.  Zmień **Styl** i **Wage** okręgu.


{{TechDraw Tools navi

}} 
