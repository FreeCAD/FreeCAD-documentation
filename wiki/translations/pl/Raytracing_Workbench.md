# Raytracing Workbench/pl
**Środowisko pracy Raytracing jest w zasadzie przestarzałe. Nowe zmiany zachodzą w [https   *//github.com/FreeCAD/FreeCAD-render Środowisku pracy Render], które ma ma być następcą. Jest ono w pełni oprogramowane w Pythonie, więc znacznie łatwiej jest je rozbudowywać.

Niemniej jednak informacje zawarte na tej stronie są użyteczne dla nowego Środowiska pracy, ponieważ oba moduły działają zasadniczo w ten sam sposób.
**

<img alt="Ikonka FreeCAD dla Środowiska pracy Raytracing" src=images/Workbench_Raytracing.svg  style="width   *128px;">

## Wprowadzenie


{{TOCright}}

Narzędzie <img alt="" src=images/Workbench_Raytracing.svg  style="width   *24px;"> [Środowisko pracy Raytracing](Raytracing_Workbench/pl.md) służy do generowania fotorealistycznych obrazów modeli poprzez przetwarzanie ich za pomocą zewnętrznego programu renderującego.

Środowisko pracy Raytracing współpracuje z [szablonami](Raytracing_templates.md), które są plikami projektu definiującymi scenę dla Twojego modelu 3D. Można w nich umieszczać światła i geometrię, takie jak płaszczyzny podłoża, a także zawiera symbole zastępcze dla położenia kamery oraz dla informacji o materiale obiektów w scenie. Projekt może być następnie wyeksportowany do pliku gotowego do dalszej obróbki lub wyrenderowany bezpośrednio w programie FreeCAD.

Obecnie obsługiwane są dwa systemy renderowania   * [POV-Ray](POV-Ray.md) i [LuxRender](LuxRender.md). Aby móc renderować z poziomu FreeCAD, przynajmniej jeden z tych programów musi być zainstalowany i skonfigurowany w Twoim systemie. Jednakże, jeśli żaden renderer nie jest zainstalowany, nadal będziesz mógł wyeksportować plik projektu, który będzie renderowany w innym czasie.

Stanowisko pracy Raytracing jest w zasadzie przestarzałe. Zmiany zachodzą w [Render Workbench](https   *//github.com/FreeCAD/FreeCAD-render), który ma go zastąpić. To Środowisko pracy jest w pełni zaprogramowane w Pythonie, więc o wiele łatwiej jest je rozszerzyć niż obecne stanowisko pracy, które jest zaprogramowane w C++. Niemniej jednak, informacje zawarte na tej stronie są generalnie użyteczne dla nowego Środowiska pracy, ponieważ oba moduły działają w zasadzie w ten sam sposób.

<img alt="" src=images/Raytracing_example.jpg  style="width   *1024px;">

## Typowy przepływ pracy 

1.  Utwórz lub otwórz projekt FreeCAD, dodaj kilka obiektów brył w środowisku *([Część](Part_Workbench/pl.md) lub [Projekt Części](PartDesign_Workbench/pl.md))*, siatki nie są obecnie obsługiwane.
2.  Utwórz projekt Raytrackingu *(povray lub luxrender)*.
3.  Wybierz obiekty, które chcesz dodać do projektu Raytracing i dodaj je.
4.  Eksportuj plik projektu lub renderuj go bezpośrednio.

<img alt="" src=images/Raytracing_Workbench_workflow.svg  style="width   *600px;">



*Przepływ pracy Środowiska pracy Raytracing; <br />Środowisko to  przygotowuje plik projektu z danego szablonu, a następnie wywołuje zewnętrzny program w celu wytworzenia rzeczywistego renderingu sceny. Zewnętrzny renderer może być używany niezależnie od FreeCAD.*

## Przybory

### Narzędzia projektu 

Są to główne narzędzia do eksportowania projektu 3D do zewnętrznych rendererów.

-   <img alt="" src=images/Raytrace_New.svg  style="width   *32px;"> [Wstaw nowy projekt PovRay \...](Raytracing_New/pl.md)   * Wstawia nowy projekt PovRay do dokumentu.
-   <img alt="" src=images/Raytrace_Lux.svg  style="width   *32px;"> [Wstaw nowy projekt LuxRender \...](Raytracing_Lux/pl.md)   * Wstawia nowy projekt LuxRender do dokumentu.
-   <img alt="" src=images/Raytrace_NewPartSegment.svg  style="width   *32px;"> [Wstaw nową część do projektu](Raytracing_InsertPart/pl.md)   * Wstawienie widoku części do projektu raytracingu.
-   <img alt="" src=images/Raytrace_ResetCamera.svg  style="width   *32px;"> [Ustawia widok kamery z wybranego projektu \...](Raytracing_ResetCamera/pl.md)   * Dopasowuje pozycję kamery projektu raytracingu do aktualnego widoku.
-   <img alt="" src=images/Raytrace_ExportProject.svg  style="width   *32px;"> [Eksport projektu Raytracing do pliku](Raytracing_ExportProject/pl.md)   * Eksportuje projekt raytracingu do pliku sceny w celu renderowania w zewnętrznym programie renderującym.
-   <img alt="" src=images/Raytrace_Render.svg  style="width   *32px;"> [Renderuje obecny projekt \...](Raytracing_Render/pl.md)   * Renderuje projekt raytracingu za pomocą zewnętrznego programu renderującego.

### Przydatne narzędzia 

Są to narzędzia pomocnicze do ręcznego wykonywania określonych zadań.

-   <img alt="" src=images/Raytracing_WriteView.svg  style="width   *32px;"> [Eksport widoku do Povray](Raytracing_WriteView.md)   * Zapisuje aktywny widok 3D z kamerą i całą jego zawartością do pliku Povray.
-   <img alt="" src=images/Raytracing_WriteCamera.svg  style="width   *32px;"> [Eksport widoku kamery do Povray](Raytracing_WriteCamera.md) Eksportuj pozycję kamery z aktywnego widoku 3D w formacie POV-Ray do pliku.
-   <img alt="" src=images/Raytracing_WritePart.svg  style="width   *32px;"> [Exksport części do Povray](Raytracing_WritePart.md)   * Zapisz wybraną część *(obiekt)* jako plik Povray.

## Ustawienia

-   <img alt="" src=images/Preferences-raytracing.svg  style="width   *32px;"> [Preferenje](Raytracing_Preferences.md)   * Preferencje dostępne dla narzędzia Raytracing.

## Poradniki

-   [Basic Raytracing tutorial](Raytracing_tutorial.md)
-   [Intermediate Raytracing tutorial](Tutorial_FreeCAD_POV_ray.md)

## Ręczne tworzenie pliku Povray 

Opisane powyżej narzędzia użytkowe pozwalają na wyeksportowanie bieżącego widoku 3D i całej jego zawartości do pliku [Povray](http   *//www.povray.org/). Najpierw należy załadować lub utworzyć dane CAD i ustawić orientację widoku 3D według własnego uznania. Następnie wybierz z menu Raytracing \"Narzędzia → Eksportuj widok\...\".

![](images/FreeCAD_Raytracing.jpg )

Zostaniesz poproszony o podanie lokalizacji do zapisania pliku wynikowego \*.pov. Następnie można go otworzyć w programie [Povray](http   *//www.povray.org/) i wyrenderować   * ![](images/Povray.jpg )

Jak zwykle w programie renderującym, można wykonywać duże i ładne zdjęcia   * <img alt="" src=images/Scharniergreifer_render.jpg  style="width   *800px;">

## Tworzenie skryptów 

Informacje na temat tworzenia scen w sposób programowy można znaleźć w [Przykład API Raytracing](Raytracing_API_example.md).

## Odnośniki internetowe 

### POV-Ray 

-   [POV-Ray strona na Wiki](POV-Ray.md)
-   <http   *//www.spiritone.com/~english/cyclopedia/>
-   <http   *//www.povray.org/>
-   <http   *//en.wikipedia.org/wiki/POV-Ray>

### Luxrender

-   [LuxRender strona na Wiki](LuxRender.md)
-   <http   *//www.luxrender.net/>

### Kolejne możliwe do wdrożenia w przyszłości programy renderujące 

-   <http   *//www.yafaray.org/>
-   <http   *//www.mitsuba-renderer.org/>
-   <http   *//www.kerkythea.net/>
-   <http   *//www.artofillusion.org/>

## Eksport do Kerkythea 

Chociaż bezpośredni eksport do formatu XML-File-Format Kerkythea nie jest jeszcze obsługiwany, możesz wyeksportować swoje obiekty jako Mesh-Files *(.obj)*, a następnie zaimportować je do Kerkythea.

-   jeśli używasz Kerkythea dla Linuksa, pamiętaj, aby zainstalować Pakiet WINE *(wymagany przez Kerkythea w systemie Linux)*.
-   możesz przekonwertować swoje modele za pomocą Środowiska pracy Mesh na siatkę, a następnie wyeksportować te siatki jako pliki .obj.
-   Jeśli twój eksport siatki spowodował błędy *(przerzucanie wektorów normalnych, dziury\...)* możesz spróbować szczęścia z [Netfabb Studio Basic](http   *//www.netfabb.com/downloadcenter.php?basic=1)

   *   Darmowy do użytku osobistego, dostępny dla systemów Linux, Mac OSX i Windows.
   *   Posiada standardowe narzędzia naprawcze, które naprawią Twój model w większości przypadków.

-   inny dobry program do analizy/naprawiania siatki to [Meshlab](http   *//sourceforge.net/projects/meshlab/)

   *   Open Source, dostępny dla systemów, Linux, Mac OSX i Windows.
   *   Posiada standardowe narzędzia naprawcze, które naprawią model w większości przypadków *(wypełnianie dziur, reorientacja wektorów normalnych, itp.)*.

-   możesz użyć **make compound**, a następnie **make single copy** lub możesz scalić bryły, aby je pogrupować przed przekształceniem w siatki.
-   pamiętaj o ustawieniu w Kerkythea współczynnika importowego **0,001** dla modelu obj, ponieważ Kerkythea oczekuje, że plik obj będzie w metrach *(ale standardowy schemat jednostek w FreeCAD jest w mm)*.

   *   Wewnątrz WIndows 7 64-bitowy Kerkythea nie wydaje się być w stanie zapisać tych ustawień.
   *   Więc pamiętaj o tym, za każdym razem, gdy rozpoczniesz pracę z programem Kerkythea.

-   jeśli importujesz wiele obiektów w Kerkythea możesz użyć polecenia w programie Kerkythea \"Plik → Połącz\".

## Opracowanie i rozwój 

Strony te odnoszą się do nowego Środowiska pracy, zaprogramowanego w Pythonie, które ma zastąpić obecny Raytracing Workbench.

-   [Środowisko pracy Render](https   *//github.com/FreeCAD/FreeCAD-render)
-   [Środowisko pracy Render](https   *//forum.freecadweb.org/viewtopic.php?f=9&t=25933) (announcement only, no discussion)
-   [Ulepszenia środowiska Renderer programu FreeCAD](https   *//forum.freecadweb.org/viewtopic.php?t=39168)





{{Raytracing Tools navi

}} 

[Category   *Workbenches](Category_Workbenches.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [Raytracing](Category_Raytracing.md) > Raytracing Workbench/pl
