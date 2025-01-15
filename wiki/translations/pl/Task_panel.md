# Task panel/pl
## Wprowadzenie

[Panel zadań](Task_panel/pl.md) pojawia się w osobnym panelu [dokowalnym](Combo_view/pl#Zadokuj_Panel_zadań_w_górnej_części_Widoku_połączonego.md) o nazwie **Zadania**. Jest to przestrzeń, którą można dostosować i która może zawierać różne typy widżetów graficznych, takich jak pola wejściowe, pola wyboru, suwaki, przyciski, etykiety, obrazy i inne elementy, w zależności od aktywnego narzędzia.

<img alt="" src=images/FreeCAD_Combo_view_Task_panel.png  style="width:" height="250px;">



*Panel zadań prezentujący różne narzędzia, gdy aktywne jest środowisko pracy [Projekt Części](PartDesign_Workbench/pl.md) i wybrano [szkic](Sketch/pl.md).*



## Praca z panelem zadań 

Panel zadań jest zwykle otwierany, gdy aktywowane jest narzędzie wymagające danych wejściowych użytkownika. Jeśli narzędzie nie wymaga danych wprowadzanych przez użytkownika, wygeneruje wynik lub zakończy działanie, ale nie wyświetli panelu zadań. Dane wprowadzane przez użytkownika mogą być dowolne, takie jak tekst, współrzędne punktów 3D, elementy z listy, powierzchnie z kształtu lub opcje modyfikujące sposób działania narzędzia.

Istnieje wiele narzędzi wymagających wyboru kształtów lub obiektów. W takich przypadkach panel zadań będzie oczekiwał wybrania przez użytkownika odpowiednich obiektów z [widoku drzewa](Tree_view/pl.md) lub [okna widoku 3D](3D_view/pl.md). Gdy panel zadań jest otwarty, można przełączyć się na [widok drzewa](Tree_view/pl.md) w celu wybrania obiektu. Gdy to zostanie zrobione, można przełączyć się z powrotem do panelu zadań, aby kontynuować korzystanie z narzędzia. Panel zadań zwykle zamyka się po kliknięciu przycisku **OK** lub **Zamknij**, albo po naciśnięciu klawisza {**Esc**} na klawiaturze, w celu zakończenia działania bieżącego narzędzia.

<img alt="" src=images/FreeCAD_Combo_view_Task_panel_ArchComponent.png  style="width:250px;">



*Panel zadań, który otwiera się podczas edycji [Arch Component](Arch_Component.md). Panel czeka, aż użytkownik wybierze obiekty, które można dodać lub odjąć od danego elementu.*



## Uwagi

-   Użytkownicy migrujący z innych rozwiązań CAD, którzy używają klawisza **ESC** w ramach pracy, mogą uzyskać inne wyniki w programie FreeCAD. W programie FreeCAD po naciśnięciu klawisza **ESC**, jeśli panel zadań jest w trybie gotowości, nastąpi automatyczne opuszczenie panelu zadań. Aby wyłączyć tę funkcję, zobacz [Klawisz ESC](Fine-tuning/pl#Skróty_klawiaturowe.md) oraz [ustawienia](Sketcher_Preferences/pl#Ogólne.md).



---
⏵ [documentation index](../README.md) > Task panel/pl
