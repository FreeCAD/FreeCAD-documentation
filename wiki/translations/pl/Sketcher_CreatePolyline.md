---
 GuiCommand:
   Name: Sketcher CreatePolyline
   Name/pl: Szkicownik: Utwórz polilinię
   MenuLocation: Szkic , Elementy geometryczne szkicownika , Utwórz polilinię
   Workbenches: Sketcher_Workbench/pl
   Shortcut: **G** **M**
   SeeAlso: Sketcher_CreateLine/pl
---

# Sketcher CreatePolyline/pl



## Opis

Narzędzie <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:24px;"> **Utwórz polilinię** tworzy serię segmentów linii i łuków połączonych punktami końcowymi. Narzędzie ma kilka trybów.

![](images/Sketcher_PolylineExample1.png )



*Polilinia zaczynała się od linii, łuku stycznego, łuku prostopadłego następnie linii stycznej.*



## Użycie

Zapoznaj się również z informacjami na stronie [Pomoce kreślarskie](Sketcher_Workbench/pl#Pomoce_kreślarskie.md).

1.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/Sketcher_CreatePolyline.svg" width=16px> '''Utwórz polilinię'''**.
    -   Wybierz z menu opcję **Szkic → Elementy geometryczne szkicownika → <img src="images/Sketcher_CreatePolyline.svg" width=16px> Utwórz polilinię**.
    -   Kliknij prawym przyciskiem myszy w oknie [widoku 3D](3D_view/pl.md) i wybierz opcję **<img src="images/Sketcher_CreatePolyline.svg" width=16px> Utwórz polilinię** z menu kontekstowego.
    -   Użyj skrótu klawiaturowego: **G**, a następnie **M**.
2.  Kursor zmieni się w krzyżyk z ikoną narzędzia.
3.  Tryb narzędzia wymaga wcześniejszego segmentu. Wykonaj jedną z następujących czynności:
    -   Wybierz dwa punkty, aby zdefiniować segment linii.
    -   Wybierz punkt końcowy istniejącej linii lub segmentu łuku.
4.  Opcjonalnie naciśnij przycisk **M** jeden lub więcej razy, aby przełączać tryby dla następnego segmentu. Dostępne tryby to:
    -   Linia prostopadła do poprzedniego odcinka.
    -   Linia styczna do poprzedniego segmentu *(jest to tryb początkowy, jeśli poprzedni segment jest łukiem)*.
    -   Łuk styczny do poprzedniego segmentu.
    -   Łuk prostopadły *(w lewo)* do poprzedniego segmentu.
    -   Łuk prostopadły *(w prawo)* do poprzedniego odcinka.
    -   Linia połączona tylko z poprzednim segmentem.
5.  W każdym z trybów łuku można opcjonalnie przytrzymać klawisz **Ctrl**, aby przyciąć łuk w krokach co 45° względem poprzedniego segmentu.
6.  Wybierz punkt końcowy segmentu.
7.  Opcjonalnie powtórz tę czynność, aby utworzyć więcej segmentów.
8.  Aby zakończyć wprowadzanie, wykonaj jedną z poniższych czynności:
    -   Przyciągnij do punktu początkowego, aby utworzyć zamkniętą polilinię.
    -   Kliknij prawym przyciskiem myszy lub naciśnij **Esc** lub uruchom inne narzędzie do tworzenia geometrii lub wiązań.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePolyline/pl
