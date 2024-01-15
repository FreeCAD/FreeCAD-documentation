---
 GuiCommand:
   Name: Curves EditableSpline
   Name/pl: Krzywe: Edytowalna krzywa złożona
   MenuLocation: Curves , Freehand BSpline
   Workbenches: Curves_Workbench/pl
---

# Curves EditableSpline/pl



## Opis

Polecenie <img alt="" src=images/Curves_EditableSpline.svg  style="width:24px;"> **Edytowalna krzywa złożona** tworzy krzywą złozoną kreśloną \"odręcznie\". Narzędzie to jest częścią [zewnętrznego środowiska pracy](External_workbenches/pl.md) o nazwie [Krzywe](Curves_Workbench/pl.md).



## Użycie

1.  Przełącz się do środowiska pracy <img alt="" src=images/Curves_workbench_icon.svg  style="width:24px;"> [Krzywe](Curves_Workbench/pl.md) *(instalacja za pomocą <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Menadżera dodatków](Std_AddonMgr/pl.md) jest konieczna, jeśli nie zainstalowano go wcześniej)*.
2.  Opcjonalnie wybierz wierzchołki, krawędzie i/lub ściany:
    -   Liczba wierzchołków krzywej będzie zgodna z liczbą wybranych elementów.
    -   Wierzchołki krzywej zostaną przyciągnięte do wybranych wierzchołków oraz do punktów środkowych wybranych krawędzi i powierzchni.
3.  Aby wywołać polecenie, wykonaj jedną z następujących czynności:
    -   Naciśnij przycisk <img alt="" src=images/Curves_EditableSpline.svg  style="width:24px;"> na pasku narzędzi Krzywe.
    -   Użyj pozycji **Curves → Freehand BSpline** w menu.



## Opcje

Podczas wykonywania polecenia aktywny jest specjalny tryb edycji, w którym dostępnych jest kilka akcji i zachowań, które można kontrolować za pomocą klawiszy i kliknięć myszą.

-   Aby przesunąć wierzchołek lub linię prowadzącą *(linie prowadzące to linie proste między wierzchołkami)*, naciśnij i przytrzymaj lewy przycisk myszy, a następnie przesuń kursor myszy.
-   Klawisz **A** zaznacza lub odznacza wszystkie wierzchołki i linie prowadzące.
-   Klawisz **I** doda wierzchołek do segmentu należącego do wybranej linii prowadzącej. Nowy wierzchołek zostanie zaznaczony.
-   Klawisz **T** ustawia lub wyłącza tryb styczny dla wybranych wierzchołków lub linii pomocniczych *(względem kierunku widoku)*.
-   Klawisz **P** wyrównuje wybrane obiekty.
-   Klawisz **S** może być użyty do przyciągnięcia wierzchołka do wierzchołka należącego do innej krzywej złożónej. Po zaznaczeniu wierzchołka edytowanej krzywej złozonej, przytrzymaj klawisz **Ctrl** i dodaj wierzchołek docelowy do zaznaczenia, a następnie naciśnij klawisz **S**. Wierzchołki zostaną ze sobą połączone.
-   Aby odłączyć wierzchołki, zaznacz przyciągniętą parę wierzchołków i ponownie naciśnij klawisz **S**. Wierzchołek edytowanej krzywej złozonej pozostaje zaznaczony i może być teraz przesuwany.
-   Klawisz **L** ustawia lub wyłącza interpolację liniową.
-   Klawisze **X**, **Y** lub **Z** mogą być użyte do ograniczenia ruchu przeciąganego obiektu. Podczas przeciągania naciśnij żądany klawisz osi. Ponowne naciśnięcie tego samego klawisza wyłącza ograniczenie.
-   Klawisz **Q** kończy polecenie i wychodzi z trybu edycji.



## Ograniczenia



## Właściwości



## Tworzenie skryptów 





{{Curves Tools navi

}}



---
⏵ [documentation index](../README.md) > [Curves](Category_Curves.md) > Curves EditableSpline/pl
