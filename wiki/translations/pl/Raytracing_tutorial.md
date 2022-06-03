---
- TutorialInfo   */pl
   Topic   * Raytracing
   Level   * Początkujący
   Time   * 10 minut + czas renderowania
   Author   *[http   *//freecadweb.org/wiki/index.php?title=User   *Drei Drei]
   FCVersion   *0.16  lub nowszy
   Files   *
---

# Raytracing tutorial/pl



## Środowisko pracy Raytracing 


**Środowisko [Raytracing](Raytracing_Workbench/pl.md) zostało zastąpione przez nowe [https   *//github.com/FreeCAD/FreeCAD-render środowisko Render], które ma je zastąpić. Środowisko pracy Render może być zainstalowane poprzez [Menadżer dodatków](Std_AddonMgr/pl.md). Informacja tutaj jest podana, ponieważ domyślnie FreeCAD jest nadal dostarczany ''(od wersji 0.19-24276)'' ze środowiskiem Raytracing, i ponieważ nowy moduł powinien w zasadzie działać w ten sam sposób.**



## Wprowadzenie

Ten poradnik ma na celu zapoznanie czytelnika z podstawowym przepływem pracy w środowisku Raytracing, jak również z większością narzędzi, które są dostępne do tworzenia wyrenderowanego obrazu. **Uwaga**, środowisko Raytracing jest stopniowo zastępowane nowszym [środowisku Render](https   *//github.com/FreeCAD/FreeCAD-render), dostępnym poprzez [Menedżer dodatków](Std_AddonMgr/pl.md).

<img alt="" src=images/Raytracing_tutorial_result.png  style="width   *480px;">

## Wymagania

-   FreeCAD w wersji 0.16 lub wyższej.
-   [POV-Ray](http   *//www.povray.org/) i/lub [LuxRender](https   *//luxcorerender.org/) jest zainstalowany w systemie.
-   W przypadku POV-Ray, nie wystarczy mieć tylko binarny plik wykonywalny na miejscu, ale również **wymagana** jest instalacja **wspierających plików**. W Ubuntu, są one dostarczane przez pakiet z flagą Recommends [povray-includes](https   *//packages.ubuntu.com/search?keywords=povray-includes). Potencjalne problemy były również widziane z instalacjami Linuksa wymagającymi lokalnych plików konfiguracyjnych do ręcznego utworzenia w folderze domowym użytkownika, jak omówiono [na forum](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=27548&start=10#p224576).
-   W przypadku POV-Ray, zalecana jest instalacja [makrodefinicji psicofil\'s](https   *//github.com/psicofil/Macros_FreeCAD).
-   Czytelnik posiada podstawową wiedzę do korzystania z środowisk pracy Część i Projekt Części.

## Sposób postępowania 

### Modelowanie

W tym przykładzie jako obiekt badania używany jest sześcian, ale zamiast niego mogą być używane modele utworzone w Środowiskach pracy [Part](Part_Workbench/pl.md) lub [PartDesign](PartDesign_Workbench/pl.md).

1.  Utwórz nowy dokument.
2.  Aktywuj środowisko pracy Projekt Części.
3.  Utwórz sześcian. Możesz dowolnie zmieniać jego właściwości.

Teraz mamy model, z którym możemy pracować.

### Przygotowanie do renderingu 

1.  Przełącz się do środowiska Raytracing.
2.  Przełączyć widok na **Perspektywę**. Przejdź do menu **Widok** i wybierz **Perspektywa**.
3.  Ustaw lokalizację dla renderera. Przejdź do menu **Edycja → Preferencje**. Kliknij na **Raytracing** i ustaw lokalizację na plik wykonywalny.
4.  Ustaw rozmiar renderowanego obrazu. Przejdź do menu **Edycja → Preferencje**. Kliknij na **Raytracing** i ustaw żądany rozmiar obrazu.

#### POV-Ray 

1.  Wybierz <img alt="" src=images/Raytrace_New.svg  style="width   *32px;"> [Nowy projekt PovRay](Raytracing_New/pl.md). Z menu głównego wybierz **RadiosityNormal**.

#### LuxRender

1.  Wybierz <img alt="" src=images/Raytrace_Lux.svg  style="width   *32px;"> [Nowy projekt LuxRender](Raytracing_Lux/pl.md). Z rozwijanego menu wybierz **LuxClassic**.

### Ustawianie pozycji ujęcia widoku 

1.  Ustaw [widok 3D](3D_view/pl.md) w żądanym miejscu i odległości od modelu. W tym przypadku używamy **widoku aksonometrycznego**.
2.  Wybierz **Folder projektu** w [widoku drzewa](tree_view/pl.md).
3.  Wybierz <img alt="" src=images/Raytrace_ResetCamera.svg  style="width   *32px;"> [Resetuj ujęcie widoku](Raytracing_ResetCamera/pl.md).

### Importowanie modelu 

1.  Wybierz model do renderowania.
2.  Wybierz opcję <img alt="" src=images/Raytrace_NewPartSegment.svg  style="width   *32px;"> [Wstaw część](Raytracing_InsertPart/pl.md)

### Uruchomienie Renderowania 

1.  Wybierz funkcję <img alt="" src=images/Raytrace_Render.svg  style="width   *32px;"> [Renderowanie](Raytracing_Render/pl.md).
2.  Ustaw ścieżkę przechowywania obrazu.
3.  Poczekaj na zakończenie renderowania. Może to chwilę potrwać.

## Przeglądanie wyników 

FreeCAD natychmiast otworzy obraz po zakończeniu renderowania.

Dzięki temu ćwiczeniu poznaliśmy podstawowy przepływ pracy dla środowiska pracy [Raytracing](Raytracing_Workbench/pl.md).  {{Raytracing Tools navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Tutorials](Category_Tutorials.md) > [Raytracing](Raytracing_Workbench.md) > Raytracing tutorial/pl
