# <img alt="Ikonka FreeCAD dla środowiska pracy Render" src=images/Render_workbench_icon.svg  style="width:64px;"> Render Workbench/pl






## Wprowadzenie

Środowisko pracy Render umożliwia tworzenie wysokiej jakości obrazów z modeli FreeCAD przy użyciu zewnętrznych silników renderujących o otwartym kodzie źródłowym.

Image:Pabellon_de_Barcelona.png\|Pawilon Barcelona
Zrzut ekranu Image:Pabellon_de_Barcelona_Pov_large.png\|Pawilon Barcelona
Obraz renderowany przez Povray. Image:Pabellon_de_Barcelona_Cycles.png\|Barcelona pavilion
Obraz renderowany przez Cycles. Image:Asm_V4.png\|Asm V4
Zrzut ekranu Image:Asm_V4_lux.png\|Asm v4
Obraz renderowany przez LuxCore. Image:Asm_V4_ospray2.png\|Asm v4
Obraz renderowany przez Ospray. Image:Church_of_the_light.png\|Kościół światłości
Zrzut ekranu Image:Church_of_the_light_lux2.png\|Kościół światłości
Obraz renderowany przez LuxCore. Image:Church_of_the_light_cycles.png\|Kościół światłości
Obraz renderowany przez Cycles. Image:Car.png\|Samochód
Zrzut ekranu Image:Car_ospray.png\|Samochód
Obraz renderowany przez Ospray. Image:Car_lux.png\|Samochód
Obraz renderowany przez LuxCore. Image:Brick_assembly.png\|Zestaw klocków
Zrzut ekranu Image:Brick_assembly_appleseed.png\|Zestaw klocków
Obraz renderowany przez Appleseed. Image:Brick_assembly_luxcore.png\|Zestaw klocków
Obraz renderowany przez Luxcore. Image:VillaSavoye.png\|Villa Savoye
Zrzut ekranu Image:VillaSavoye appleseed.png\|Villa Savoye
Obraz renderowany przez Appleseed. Image:VillaSavoye Cycles.png\|Villa Savoye
Obraz renderowany przez Cycles.

Środowisko pracy Render, czysty Python, jest płynnie zintegrowane z FreeCAD: cała scena renderowania - obiekty, oświetlenie, materiały, kamera itp. - można opisać za pomocą obiektów FreeCAD, które można wyeksportować do zewnętrznych silników renderujących.

W porównaniu z innymi podejściami opartymi na aplikacjach graficznych trzeciej części, Render ma na celu:

-   Uniknięcie konieczności uczenia się przez użytkownika innego oprogramowania 3D / grafiki komputerowej: wszystko, co trzeba wiedzieć, znajduje się we FreeCAD.
-   Uproszczenie przepływu pracy renderowania i uwolnienie użytkownika od wszelkich pośrednich manipulacji plikami - takich jak import, eksport, retusz sceny itp.
-   Utrwalenie konfiguracji sceny, a zwłaszcza zapobieganie przeróbkom w zewnętrznym narzędziu za każdym razem, gdy model został zmodyfikowany.



## Obsługiwane silniki renderujące 

Obecnie obsługiwanych jest sześć silników renderujących:

-   LuxCoreRender,
-   Appleseed,
-   Cycles *(wersja samodzielna)*,
-   Pov-Ray,
-   Intel Ospray Studio,
-   Pbrt-v4 *(eksperymentalny)*.



## Użycie

W trybie szybkiego uruchamiania, po prawidłowym zainstalowaniu środowiska pracy, renderowanie modelu FreeCAD jest tylko 4-etapowym procesem:

1.  **Utwórz projekt renderowania:** Naciśnij przycisk na pasku narzędzi odpowiadający twojemu rendererowi i wybierz szablon odpowiedni dla twojego renderera *(możesz zacząć od smaku \"studio\", takiego jak **appleseed_studio_light.appleseed**, **cycles_studio_light.xml**, **luxcore_studio_light.cfg**, **povray_studio_light.pov** itd.)*
2.  **Dodawanie widoków obiektów do projektu renderowania:** Wybierz zarówno obiekty, jak i projekt, a następnie naciśnij przycisk **Dodaj widok**.
3.  **Ustaw kierunek patrzenia:** [Nawiguj w oknie widoku 3D](Manual:Navigating_in_the_3D_view/pl.md) do żądanej pozycji i przełącz widok na tryb [perspektywy](Std_PerspectiveCamera/pl.md).
4.  **Renderowanie:** Wybierz projekt i naciśnij przycisk **Renderuj** na pasku narzędzi *(dostępny również z menu kontekstowego projektu)*.

**Teraz powinieneś otrzymać pierwszy render swojego modelu**.

Więcej instrukcji można znaleźć w repozytorium [GitHub](https://github.com/FreeCAD/FreeCAD-render) lub w pomocy online.



## Właściwości

Właściwości obejmują, ale nie ograniczają się do:

-   Oświetlenie: światła punktowe, światła obszarowe, niebo słoneczne i wstępnie ustawione szablony oświetlenia.
-   Kamery *(ujęcia widoku)*.
-   Zarządzanie materiałami *(przy użyciu zwykłych shaderów: matowych, błyszczących, szklanych, pryncypialnych itp.)*
-   Tryb wsadowy / tryb UI.
-   Odszumianie.
-   Warunek zatrzymania *(próbka na piksel)*.
-   Kontrola siatki: ugięcia kątowe i liniowe, automatyczne wygładzanie.



## Odnośniki internetowe 

Potrzebujesz więcej informacji? Wystarczy kliknąć: <https://github.com/FreeCAD/FreeCAD-render>



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Command Reference](Category_External%20Command%20Reference.md) > [External Workbenches](Category_External%20Workbenches.md) > Render Workbench/pl
