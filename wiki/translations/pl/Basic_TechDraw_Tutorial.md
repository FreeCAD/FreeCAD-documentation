# Basic TechDraw Tutorial/pl
{{TutorialInfo/pl
|Topic=Modelowanie
|Level=początkujący
|Author=[WandererFan](User:WandererFan.md)
|Time=Mniej niż godzinę
|FCVersion=0.17 lub nowszy
|Files=[https://github.com/FreeCAD/Examples/blob/master/Basic_Part_Design_Tutorial_Example_017_Files/Basic_Part_Design_Tutorial_017.fcstd  Basic Part Design for v0.17 Sample]<br />[https://github.com/FreeCAD/Examples/blob/master/Basic_TechDraw_Tutorial_Example_Files/Basic_TechDraw_Tutorial.fcstd Basic TechDraw Tutorial Sample]
}}

## Wprowadzenie

Ten poradnik ma za zadanie zapoznać nowego użytkownika z wybranymi narzędziami i technikami używanymi w środowisku pracy **<img src="images/Workbench_TechDraw.svg" width=24px> [Rysunek Techniczny](TechDraw_Workbench/pl.md)**. Ten poradnik nie jest kompletnym i wyczerpującym przewodnikiem po środowisku pracy Rysunek Techniczny i nie obejmuje wielu narzędzi i możliwości. Poradnik przeprowadzi użytkownika przez kroki niezbędne do wykonania rysunków technicznych części na przykładzie [Poradnika projektowania części - podstawy](Basic_Part_Design_Tutorial/pl.md).

## Nim zaczniesz 

Pobierz przykładowy [plik projektu](https://github.com/FreeCAD/Examples/blob/master/Basic_Part_Design_Tutorial_Example_017_Files/Basic_Part_Design_Tutorial_017.fcstd) z poradnika dotyczącego projektowania części *(środowisko pracy Part)*.

## Zadanie

W tym poradniku będziesz używał Środowiska pracy **<img src="images/Workbench_TechDraw.svg" width=24px> [Rysunek techniczny](TechDraw_Workbench/pl.md)** do tworzenia rysunków 2D dla modelu 3D. Stworzymy wiele widoków detalu i dodamy kluczowe wymiary. Ten poradnik nie będzie wykorzystywał każdej funkcji i narzędzia dostępnego w ramach Środowiska pracy **<img src="images/Workbench_TechDraw.svg" width=24px> [Rysunek techniczny](TechDraw_Workbench/pl.md)**, ale powinien dostarczyć użytkownikowi niezbędnych podstaw do zbudowania jego wiedzy i umiejętności.

## Model detalu 

![](images/Tut17_final_refined.png )

## Tworzenie Rysunku 

### Rozpoczynamy

-   Możesz chcieć dostosować ustawienia [konfiguracji](TechDraw_Preferences.md) przed rozpoczęciem pracy. Patrz uwaga 1.
-   Otwórz najpierw plik zawierający nasz detal w 3D. Następnie upewnij się, że znajdujesz się w Środowisku pracy TechDraw.
-   W oknie rysunku i/lub panelu widoku połączonego będziesz wybierał elementy. Zaznaczenie w Środowisku TechDraw działa tak samo jak w oknie widoku 3D. Elementy zmieniają kolor na żółty, gdy kursor znajduje się w pozycji umożliwiającej ich wybranie, i zmieniają kolor na zielony, gdy są wybrane. Aby wybrać wiele elementów, przytrzymaj klawisz klawiatury **Ctrl** podczas klikania.

### Widoki i wymiarowanie 

Wszystkie prace w Środowisku **<img src="images/Workbench_TechDraw.svg" width=24px> [Rysunek Techniczny](TechDraw_Workbench/pl.md)** rozpoczynają się od utworzenia strony. Strony są oparte na Szablonach i zawierają widoki.

1.  Kliknij w przycisk <img alt="" src=images/TechDraw_PageDefault.svg  style="width:32px;"> [Wstaw nową domyślną stronę rysunku](TechDraw_PageDefault/pl.md) aby utworzyć nową stronę.
2.  Kliknij w Zawartość w oknie [widoku 3D](3D_view/pl.md) lub [widoku połączonego](Combo_view.md).
3.  Kliknij w przycisk <img alt="" src=images/TechDraw_View.svg  style="width:32px;"> [Wstaw widok](TechDraw_View/pl.md). Spowoduje to dodanie widoku do strony, którą właśnie utworzyliśmy.

Teraz mamy widok na stronę patrząc w dół na górę bryły. Jest on jednak trochę mały.

![](images/TDTut_TopView1to1.png )

1.  Wybierz utworzona stronę w [widoku połączonym](Combo_view/pl.md) i przewiń do właściwości **Skala** na karcie **Dane**.
2.  Zmień Skalę z 1 na **2** i naciśnij **Enter**. Widok zostanie powiększony.
3.  Odsuń utworzony obraz od bloku dokumentacji, znajdującego się w prawym dolnym rogu strony.

![](images/TDTut_TopView2to1.png )

Wygląda lepiej, jednak widok wciąż pozostaje trochę nudny. Dodajmy więc kilka wymiarów.

1.  Wybierz górny lewy wierzchołek *(mały punkt)* za pomocą **LMB** *(Lewy Przycisk Myszki)*, następnie zaznacz *(**Ctrl**+**LMB**)* również dolny lewy wierzchołek.
2.  Kliknij na <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:32px;"> [Wstaw wymiar pionowy](TechDraw_VerticalDimension/pl.md). Przeciągnij tekst wymiaru z dala od korpusu.
3.  Spróbuj jeszcze raz z lewym górnym i prawym górnym wierzchołkiem i <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:32px;"> [Wstaw wymiar poziomy](TechDraw_HorizontalDimension/pl.md).

![](images/TDTut_TopView2Dims.png )

### Pola tekstowe bloku dokumentacji 

Powinniśmy dodać trochę informacji do naszego rysunku.

1.  Kliknij na mały zielony kwadrat obok tytułu w bloku dokumentacji. Pojawi się wyskakujące okienko, w którym można zmienić tytuł na coś bardziej sensownego.
2.  Aby poćwiczyć wystarczy, że umieścisz swoje imię w polu **Designed by Name** w analogiczny sposób.

![](images/TDTut_DocBlock.png )

Robi się coraz lepiej. Dodajmy trochę tekstu do strony.

1.  Kliknij na narzędzie <img alt="" src=images/TechDraw_Annotation.svg  style="width:32px;"> [Nowa Adnotacja](TechDraw_Annotation/pl.md). Na środku strony pojawi się blok tekstowy.
2.  Przeciągnij blok tekstowy z głównego widoku.
3.  W drzewie dokumentu kliknij na pozycję **Annotation**, widok połączony przewiń do właściwości **Text** na zakładce **Dane**.
4.  Kliknij w obszarze danych, a następnie kliknij na trzykropek po prawej stronie pola. Pojawi się wyskakujące okienko, w którym możesz zmienić tekst na coś bardziej użytecznego.

![](images/TDTut_Annotation.png )

Zanim opuścimy tę stronę, zobaczmy, jak będzie wyglądać, gdy ją wydrukujemy.

1.  Kliknij na narzędzie <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:32px;"> [Przełacz widoczność ramek](TechDraw_ToggleFrame.md). Ramki **Annotation** i **View** znikną. Możesz je odzyskać, klikając ponownie przycisk narzędzia.

![](images/TDTut_Toggle.png )

### Wiele widoków detalu 

Stwórzmy rysunek wielu widoków używając innego szablonu jako punktu startowego. Będziemy używać konwencji **Kąta pierwszego**, ale możesz też przejść na **Kąt trzeci**, jeśli jest to twoja właściwa metoda.

1.  Kliknij na narzędzie <img alt="" src=images/TechDraw_PageTemplate.svg  style="width:32px;"> [Wstaw nową stronę przy uzyciu szablonu](TechDraw_PageTemplate.md) Pojawi się okno dialogowe wyboru plików. Wybierz plik szablonu. Będziemy używać **ANSIB.SVG**. Zostanie utworzona nowa zakładka w dokumencie projektu.
2.  Wybierz **Bryłę** i **Page001** *(jeśli masz więcej niż jedną stronę w swoim dokumencie, musisz powiedzieć TechDraw, której z nich użyć)*.
3.  Kliknij na przycisk <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:32px;"> [Wstaw wiele połączonych widoków](TechDraw_ProjectionGroup/pl.md). Pojawi się dobrze znany mały widok na środku strony, a w panelu zadań pojawi się okno dialogowe.
4.  Kliknij wybrane pola w sekcji Secondary Views w oknie dialogowym.
5.  Przeciągnij widok oznaczony jako \"Front\". Wszystkie inne widoki przesuną się razem z nim.
6.  Zmień skalę ze \"Strona\" na \"Niestandardowa\" i zmień wartość \"Skala niestandardowa\" na 2:1. Naciśnij przycisk **OK**.

![](images/TDTut_ProjGroup21.png )

1.  W widoku oznaczonym jako **TopLeftFront**, wybierz dwa wierzchołki na skrajnych końcach przedniej krawędzi elementu.
2.  Kliknij na narzędzie <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:32px;"> [Wstaw nowy wymiar długości](TechDraw_LengthDimension/pl.md). Przeciągnij tekst wymiarowy z dala od bryły.

### Powiązanie wymiarów z modelem 3D 

Czy widzisz problem z wymiarem, który właśnie powstał?

![](images/TDTut_NewLengthDim.png )

Od pierwszej części tego poradnika wiemy, że przedmiot posiada szerokość **53mm**, ale nasze nowe wymiary to **43,27**. Dzieje się tak dlatego, że model w widoku **TopLeftFront** jest w [projekcji izometrycznej](https://en.wikipedia.org/wiki/Isometric_projection), a naszym rysunkiem podstawowym był model w [projekcji ortogonalnej *(wielowidokowej)*](https://en.wikipedia.org/wiki/Orthographic_projection). Aby uzyskać właściwą wartość, musimy powiązać nasz wymiar bezpośrednio z modelem 3D.

1.  Zwróć uwagę na nazwę naszego wadliwego wymiaru w panelu widoku połączonego. Będziemy go potrzebować za chwilę.
2.  Przejdź do zakładki widoku 3D modelu i wybierz wierzchołki na końcach przedniej krawędzi elementu. Wybierz również zakładkę **Page001**.
3.  Kliknij na narzędzie <img alt="" src=images/TechDraw_LinkDimension.png  style="width:32px;"> [Połącz wymiar z geometrią](TechDraw_LinkDimension/pl.md). W panelu zadań zostanie otwarte okno dialogowe.
4.  W oknie dialogowym, przenieś nasz wymiar z dostępnej kolumny do wybranej kolumny. Naciśnij przycisk **OK**.
5.  Wróć na stronę001. Nasz wymiar powinien teraz odczytać prawidłową wartość 53. *(Jeśli nadal widzisz 43.27, może być konieczne wciśnięcie przycisku **Przelicz** lub trochę przesuń wartość wymiaru na rysunku, aż się zmieni)*.

## Dalsze postępowanie 

W tym samouczku nauczyłeś się wystarczająco dużo o Środowisku pracy **<img src="images/Workbench_TechDraw.svg" width=24px> [TechDraw](TechDraw_Workbench/pl.md)**, aby stworzyć taki rysunek *(autor: [NormandC](User:Normandc.md))*. Uwaga 2.

![](images/TDTut_FC018_TechDraw_Dim_Iso_View_01_NC.png )


**<img src="images/Workbench_TechDraw.svg" width=24px> [TechDraw](TechDraw_Workbench/pl.md)
**

oferuje o wiele więcej funkcjonalności - widoki przekrojów, widoki szczegółów, symbole Svg, obrazy, kreskowanie powierzchni.

## Uwagi

1.  W tym [wpisie na forum](https://www.forum.freecadweb.org/viewtopic.php?f=3&t=30083#p248189) znajduje się doskonały zestaw sugerowanych preferencji.
2.  Ten rysunek został wykonany w wersji **0.18**. Pokazuje wymiary w odpowiednim formacie dla widoku izometrycznego. W wersji **0.17** linie pomocnicze będą prostopadłe do krawędzi, a nie wyrównane z osiami.

## Dodatkowe zasoby 

-   Plik FreeCAD tego ćwiczenia do porównania *(wykonany w wersji programu 0.17)* [Pobierz](https://github.com/FreeCAD/Examples/blob/master/Basic_TechDraw_Tutorial_Example_Files/Basic_TechDraw_Tutorial.fcstd)


{{Tutorials navi

}} {{TechDraw Tools navi}}

---
[documentation index](../README.md) > Basic TechDraw Tutorial/pl
