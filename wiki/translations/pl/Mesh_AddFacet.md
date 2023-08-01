---
- GuiCommand:
   Name: Mesh AddFacet
   Name/pl: Siatka: Dodaj trójkąt
   MenuLocation: Siatki - Dodaj trójkąt
   Workbenches: [Siatka](Mesh_Workbench/pl.md)
   SeeAlso: [Wypełnienie otworów](Mesh_FillupHoles/pl.md), [Interaktywne wypełnienie otworów](Mesh_FillInteractiveHole/pl.md)
---

# Mesh AddFacet/pl

## Opis

Polecenie Dodaj trójkąt środowiska Siatka dodaje powierzchnie wzdłuż granicy otwartego obiektu siatkowego. Można go użyć do wypełnienia otworów.

## Użycie

1.  Podczas wykonywania polecenia aktywny będzie tryb edycji. W tym trybie nie można obracać ani przesuwać [widoku 3D](3D_view/pl.md), chociaż powiększanie nadal działa. Możesz jednak tymczasowo wyłączyć tryb edycji komendą [Przełącz tryb nawigacja / edycja](Std_ToggleNavigation/pl.md) jeśli potrzebujesz zmienić widok.
2.  Wybierz pojedynczy otwarty obiekt siatki.
3.  Istnieje kilka sposobów na wywołanie polecenia:
    -   Naciśnij przycisk **<img src="images/Mesh_AddFacet.svg" width=16px> [Dodaj trójkąt](Mesh_AddFacet/pl.md)**.
    -   Wybierz opcję z menu **Siatki → <img src="images/Mesh_AddFacet.svg" width=16px> Dodaj trójkąt**.
4.  Jeśli najedziesz kursorem na wierzchołek położony wzdłuż granicy siatki, pojawi się żółty znacznik, a kliknięcie lewym przyciskiem myszy spowoduje jego wybranie.
5.  Wybierz dwa dodatkowe punkty, aby zdefiniować trójkątną ścianę. Kolejność trzech punktów, zgodnie lub przeciwnie do ruchu wskazówek zegara, określa kierunek normalnej ściany.
6.  Wyskakuje menu z następującymi opcjami:
    -   
        **Dodaj trójkąt**
        
        : dodaje ścianę do siatki.

    -   
        **Odwróć wektory normalne**
        
        : odwraca normalną ściany. Po wybraniu tej opcji kliknięcie lewym przyciskiem myszy ponownie wyświetli menu.

    -   
        **Wyczyść**
        
        : usuwa zaznaczone punkty.
7.  Opcjonalnie dodaj więcej ścian.
8.  Wybierz **Zakończ** z menu kontekstowego w oknie widoku 3D, aby zakończyć polecenie.

## Uwagi

-   Aby wyraźnie odróżnić orientację ścian obiektów siatkowych upewnij się, że właściwość **Oświetlenie** obiektów siatkowych jest ustawiona na wartość {{Value|Jedna strona}}. Kolor tylnej strony ich ścian będzie wtedy zależał od ustawień podświetlenia: **Edycja → Preferencje → Wyświetlanie → 3D View → Włącz podświetlenie - Intensywność podświetlenia**. Zobacz również informacje na stronie [Edytor ustawień](Preferences_Editor/pl#3D_View.md).





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh AddFacet/pl
