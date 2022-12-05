# Task panel/pl
{{TOCright}}

## Wprowadzenie

[Panel zadań](Task_panel/pl.md) pojawia się w zakładce **Zadania** okienka [widoku łączonego](combo_view/pl.md), jednego z najważniejszych paneli [interfejsu użytkownika](interface/pl.md). Jest to konfigurowalna przestrzeń, która może zawierać dowolny typ graficznego widżetu, jak składane okienka, tabele, pola wejściowe, pola wyboru, pola tekstowe, przyciski, etykiety, obrazy i inne elementy, w zależności od aktualnie aktywnego [Środowiska pracy](Workbenches/pl.md), oraz aktualnie aktywnego narzędzia.

<img alt="" src=images/FreeCAD_Combo_view_Task_panel.png  style="width:" height="550px;">



*Panel zadań prezentujący różne polecenia, gdy aktywne jest Środowisko pracy [PartDesign](PartDesign_Workbench/pl.md) i wybrano [szkicownik](Sketch/pl.md).*

## Praca z panelem zadań 

Panel zadań zwykle otwiera się, gdy narzędzie wymagające wprowadzenia danych przez użytkownika jest aktywowane. Odbywa się to poprzez naciśnięcie przycisku na pasku narzędzi lub podwójne kliknięcie obiektu. Jeśli narzędzie nie wymaga wprowadzania danych przez użytkownika, wygeneruje swój wynik lub zakończy działanie, ale nie wyświetli panelu zadań.

Użytkownik może wprowadzać dowolne dane, takie jak tekst, współrzędne punktów w przestrzeni 3D, elementy z listy, ściany z kształtu lub opcje modyfikacji sposobu działania narzędzia.

![](images/FreeCAD_Combo_view_Task_panel_Sketcher.png )



*Panel zadań, który otwiera się, gdy edytowany jest [szkic](Sketch/pl.md). Prezentowane są różne rodzaje informacji, takie jak komunikaty o rozwiązaniach, opcje siatki, wiązania i elementy geometryczne.*

Istnieje wiele poleceń wymagających wyboru kształtów lub obiektów obecnych w dokumencie. W takich przypadkach panel zadań będzie oczekiwał wybrania przez użytkownika odpowiednich obiektów z [widoku drzewa](Tree_view/pl.md) lub [okna widoku 3D](3D_view/pl.md). Gdy panel zadań jest otwarty, można przełączyć się na zakładkę **Model**, aby wyświetlić [widok drzewa](Tree_view/pl.md) w celu wybrania obiektu. Gdy to zostanie zrobione, można przełączyć się z powrotem na zakładkę **zadania**, aby kontynuować wykonywanie polecenia. Panel zadań zwykle zamyka się po kliknięciu przycisku **OK** lub **Zamknij**, albo po naciśnięciu klawisza {**Esc**} na klawiaturze, w celu przerwania wykonywania bieżącego polecenia.

![](images/FreeCAD_Combo_view_Task_panel_ArchComponent.png )



*Panel zadań, który otwiera się podczas edycji [Arch Component](Arch_Component.md). Panel czeka, aż użytkownik wybierze obiekty, które można dodać lub odjąć od danego elementu.*

**Uwaga:** Proszę zauważyć, że przełączenie z zakładki **Zadania** do zakładki **Model** nie kończy aktywnego polecenia. Zadanie nadal będzie działać w tle. Użytkownik jest odpowiedzialny za prawidłowe zakończenie lub przerwanie aktywnego polecenia przed rozpoczęciem innego zadania. Pozostawienie uruchomionego zadania może spowodować błędy podczas próby uruchomienia innych narzędzi.

## Uwagi

-   Użytkownicy migrujący z innych rozwiązań CAD, którzy używają klawisza **ESC** w ramach pracy, mogą uzyskać inne wyniki w programie FreeCAD. W programie FC po naciśnięciu klawisza **ESC**, jeśli panel zadań jest w trybie gotowości, nastąpi automatyczne opuszczenie panelu zadań. Aby wyłączyć tę funkcję, zobacz [Klawisz ESC](Fine-tuning/pl#Skróty_klawiaturowe.md).

## Tworzenie skryptów 


**Proszę przeformułować i zaktualizować tę sekcję**

Zobacz [wątek na forum](https://forum.freecadweb.org/viewtopic.php?f=10&t=44170&p=376759#p376759) Aby zamknąć Widok Zadań, należy użyć widżetu Widok Zadań. Można go zamknąć za pomocą *przycisku-\>close()*, ale zamyka on tylko dolną część widoku, a nie całe okno.

Użycie Python: 
```python
Gui.Control.closeDialog()
```

Użycie C++: 
```python
Gui::Control().closeDialog();
```


{{Interface navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Task panel/pl
