---
 GuiCommand:
   Name: Std Measure
   Name/pl: Std: Pomiary
   MenuLocation: Przybory , Pomiary
   Workbenches: wszystkie
   Version: 1.0
   SeeAlso: Draft_Dimension/pl
---

# Std Measure/pl



## Opis

Polecenie **Pomiary** daje dostęp do ujednoliconej funkcjonalności pomiarowej. Zastąpiło ono kilka dotychczasowych narzędzi tego typu, zapewniając wielofunkcyjne narzędzie pomiarowe.



## Użycie

1.  Opcjonalnie, wskaż obiekty geometryczne do użycia w pomiarze.
2.  Istnieje kilka sposobów na wywołanie tego polecenia:
    -   Wciśnij przycisk **<img src="images/Std_Measure.svg" width=16px> [Pomiary](Std_Measure/pl.md)**.
    -   Wybierz opcję **Przybory → <img src="images/Std_Measure.svg" width=16px> Pomiary** z menu.
3.  Otwarty zostanie panel zadań **Measurement**. Zobacz [Opcje](#Options/pl.md) aby uzyskać więcej informacji.
4.  Jeśli nie zostały wcześniej wskazane żadne obiekty geometryczne, wykonaj jedną z poniższych czynności:
    -   Wskaż obiekty geometryczne zostawiając *Tryb* jako *Auto*, aby tryb został automatycznie określony na podstawie wskazania.
    -   Wybierz *Tryb* inny niż *Auto* a następnie wskaż obiekty geometryczne (ponowne kliknięcie pozwala je odznaczyć):
        -   *Distance* - najkrótsza odległość między wskazanymi obiektami, jeśli wskazane są okrągłe krawędzie to mierzona jest odległość między środkami okręgów,
        -   *Distance Free* - odległość między dwoma punktami wskazanymi poprzez kliknięcia w dowolnych miejscach (ale należącymi do różnych obiektów geometrycznych - krawędzi, ścian),
        -   *Angle* - kąt między wskazanymi obiektami,
        -   *Length* - długość wskazanej krawędzi,
        -   *Position* - współrzędne wskazanego wierzchołka,
        -   *Area* - pole powierzchni wskazanej ściany,
        -   *Radius* - promień wskazanej okrągłej krawędzi,
        -   *Center of Mass* - środek masy wskazanej krawędzi, ściany lub bryły (tylko jeśli została wcześniej zaznaczona w drzewie).
5.  Wynik pomiaru zostanie wyświetlony w polu *Wynik* i na etykiecie w [widoku 3D](3D_view/pl.md). Ta etykieta będzie również zawierała ikonę wskazującą typ pomiaru. Etykiety można dostosować w [Preferencjach](Preferences_Editor/pl.md). Mogą zostać przesunięte w widoku 3D poprzez przeciągnięcie ich kursorem myszy.
6.  Wciśnij przycisk **Zresetuj** aby usunąć wymiar lub **Zapisz** aby go zachować. Zapisane wymiary są umieszczane w [grupie](Std_Group/pl.md) Measurements w [widoku drzewa](Tree_view/pl.md).
7.  Wciśnij przycisk **Esc** lub **Zamknij** aby zakończyć polecenie.



## Opcje

-    {{Version/pl|1.1}}Wciśnij przycisk **<img src="images/Preferences-system.svg" width=x16px> <img src="images/Toolbar_flyout_arrow.svg" width=x16px>** aby zmienić ustawienia:

    -   *Auto Save* - jeśli zaznaczone, ostatni pomiar jest zapisywany przy rozpoczynaniu nowego pomiaru (przytrzymanie klawisza **Shift** może tymczasowo wyłączyć to zachowanie),
    -   *Additive Selection* - jeśli zaznaczone, klikanie na kolejnych obiektach geometrycznych dodaje je jako wskazania dla tego samego pomiaru, w innym wypadku trzeba używać klawisza **Ctrl** żeby to osiągnąć.

-   Dla trybów *Distance* i *Distance Free* wyświetlane jest pole **Show Delta**. Jeśli jest ono zaznaczone, właściwość **Show Delta** pomiaru jest ustawiona na {{TRUE/pl}} i 3 dodatkowe rzutowane wymiary są wyświetlane w [widoku 3D](3D_view/pl.md).



## Właściwości



### Dane


{{TitleProperty|Pomiar}}

-    **Element1|LinkSub**: Pierwszy element pomiaru.

-    **Element2|LinkSub**: Drugi element pomiaru.

-    **Distance|Distance**: Odległość między dwoma elementami.

-    **Distance X|Distance**: Odległość w kierunku X (tylko dla pomiarów w trybie *Distance* i *Distance Free*).

-    **Distance Y|Distance**: Odległość w kierunku Y (j.w.).

-    **Distance Z|Distance**: Odległość w kierunku Z (j.w.).

-    **Position1|Vector|Hidden**: Położenie pierwszego mierzonego punktu (tylko do odczytu).

-    **Position2|Vector|Hidden**: Położenie drugiego mierzonego punktu (tylko do odczytu).



### Widok


{{TitleProperty|Wygląd}}

-    **Font Size|Integer**: Definiuje rozmiar czcionki dla etykiety zapisanego wymiaru.

-    **Line Color|Color**: Definiuje kolor linii wymiaru wyświetlanych w widoku 3D.

-    **Show Delta|Bool**: Jeśli {{TRUE/pl}}, zrzutowane wymiary długości są wyświetlane w widoku 3D (tylko dla trybów *Distance* i *Distance Free*).

-    **Text Background Color|Color**: Definiuje kolor tła etykiety wymiaru.

-    **Text Color|Color**: Definiuje kolor tekstu i symbolu w etykiecie wymiaru.



## Uwagi

-   To polecenie jest wynikiem [projektu GSoC 2023](Unified_Measurement_Facility.md).





{{Std_Base_navi

}}



---
⏵ [documentation index](../README.md) > Std Measure/pl
