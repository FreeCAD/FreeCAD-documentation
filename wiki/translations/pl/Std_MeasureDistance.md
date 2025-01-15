---
 GuiCommand:
   Name: Std MeasureDistance
   Name/pl: Std: Wymiarowanie odległości
   MenuLocation: Przybory , Wymiarowanie odległości
   Workbenches: wszystkie
   SeeAlso: Std_Measure/pl,Part_Measure_Linear/pl, Draft_Dimension/pl
---

# Std MeasureDistance/pl



## Opis

Polecenie **Wymiarowanie odległości** tworzy obiekt odległość, który mierzy i wyświetla dystans między dwoma punktami.



## Użycie

1.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Std_MeasureDistance.svg" width=16px> [Wymiarowanie odległości](Std_MeasureDistance/pl.md)**.
    -   Wybierz z menu opcję **Przybory → <img src="images/Std_MeasureDistance.svg" width=16px> Zmierz odległość**.
2.  Wybierz pierwszy punkt pomiarowy w dowolnym miejscu obiektu w oknie [widoku 3D](3D_view/pl.md).
3.  Wybierz drugi punkt pomiarowy w dowolnym miejscu na obiekcie w oknie widoku 3D.
4.  Kolejność wyboru punktów może mieć wpływ na położenie linii wymiarowej.
5.  Opcjonalnie odwróć położenie linii wymiarowej poprzez zmianę właściwości **Odbicie lustrzane** obiektu odległość.



## Uwagi

-   Nie można używać narzędzi przyciągania środowiska pracy [Rysunek Roboczy](Draft_Workbench/pl.md) z tym poleceniem.
-   Aby dodać wymiary do rysunków, użyj narzędzi wymiarowych środowiska pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md).
-   Aby uzyskać bardziej wszechstronne narzędzia pomiarowe, zainstaluj środowisko pracy <img alt="" src=images/Manipulator_workbench_icon.svg  style="width:24px;"> [Manipulator](Manipulator_Workbench/pl.md) *(środowisko [zewnętrzne](External_workbenches/pl.md))*.



## Właściwości



### Dane


{{TitleProperty|Podstawa}}

-    **Etykieta**: domyślnie etykieta zawiera zmierzoną odległość, ale ta odległość nie jest aktualizowana, gdy P1 lub P2 zostaną później przestawione.


{{TitleProperty|Pomiar}}

-    **P1**: pierwszy punkt wymiaru.

-    **P2**: drugi punkt wymiaru.

-    **Odległość**: *(tylko do odczytu)* zmierzona odległość pomiędzy P1 i P2.



### Widok


{{TitleProperty|Podstawa}}

-    **Współczynnik odległości**: współczynnik ten, pomnożony przez zmierzoną odległość, określa przesunięcie linii wymiarowej.

-    **Rozmiar czcionki**: wysokość liter *(wysokość linii w pikselach)*.

-    **Odbicie lustrzane**: jeśli ustawimy wartość {{TRUE/pl}}, to pozycja linii wymiarowej względem P1 i P2 zostanie odwrócona.



---
⏵ [documentation index](../README.md) > Std MeasureDistance/pl
