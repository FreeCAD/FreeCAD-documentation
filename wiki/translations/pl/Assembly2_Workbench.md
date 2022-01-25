# Assembly2 Workbench/pl
**Środowisko pracy Złożenie 2 jest przestarzałe. Jego autor już go nie utrzymuje, więc może nie działać z FreeCAD w wersji 0.17 i wyższej. Informacje na tej stronie nie są utrzymywane, są one tylko przechowywane dla celów historycznych.**


{{Message|Alternatywę można znaleźć w [A2plus](A2plus_Workbench/pl.md). To środowisko pracy jest forkiem Assembly2, ale nie jest z nim kompatybilne. Jeśli masz starsze modele, które musisz otworzyć, powinieneś pozostać przy FreeCAD w wersji 0.16 i środowisku Złożenie 2. Nowsze modele powinny być tworzone w całości i otwierane za pomocą A2plus.<br/>

Więcej opcji znajdziesz w [Złożenie 3](Assembly3_Workbench/pl.md) lub [Złożenie 4](Assembly4_Workbench/pl.md). Te środowiska pracy są również inspirowane środowiskiem Złożenie 2, ale nie są z nim kompatybilne.}}

## Wprowadzenie

[Złożenie 2](Assembly2_Workbench/pl.md) jest środowiskiem montażowym dla FreeCAD v0.15 z obsługą importu części z plików zewnętrznych.

Jak podaje jego autor [na forum](https://forum.freecadweb.org/viewtopic.php?f=17&t=16591), nie jest on już utrzymywany od 2016 roku, dlatego może mieć problemy z FreeCAD od wersji **0.17**. Dobrą alternatywą jest nowszy i aktywnie utrzymywany [A2plus](A2plus_Workbench/pl.md).

![](images/Assembly2_example.jpg )

## Użycie

Zamierzony przepływ pracy:

-   każda część w złożeniu jest projektowana w swoim własnym pliku FreeCAD,
-   tworzony jest oddzielny plik FreeCAD dotyczący złożenia,
-   części są importowane do tego pliku przy użyciu Assembly 2,
-   dodawane są następnie wiązania przestrzenne w celu złożenia importowanych części.

Cechy:

-   okrągłe umocowanie krawędzi,
-   wiązanie osiowe,
-   wiązanie płaskie,
-   import części,
-   aktualizacja już zaimportowanych części.

Ograniczenia

-   Słaby solver wiązań, który może zawieść lub zajmować zbyt dużo czasu dla skomplikowanych złożeń,
-   nieobsługiwane cofanie i inne podobne funkcje.

## Bibliografia

-   Autor: hamish
-   Strona domowa: [Złożenie 2](https://github.com/hamish2014/FreeCAD_assembly2)
-   Kod źródłowy na githubie: [Złożenie 2](https://github.com/hamish2014/FreeCAD_assembly2)

## Przybory

Pasek narzędzi

![](images/Assembly2-menu-orizz.png )

Menu rozwijane

![](images/Assembly2-menu-vert.png )

-   <img alt="" src=images/Assembly2_ImportPart.png  style="width:32px;"> Importuj część z innego dokumentu FreeCAD
-   <img alt="" src=images/Assembly2_UpdatePart.png  style="width:32px;"> Aktualizuj części zaimportowane do zespołu
-   <img alt="" src=images/Assembly2_Move.png  style="width:32px;"> Przenieś
-   <img alt="" src=images/Assembly2_CircularEdgeConstraint.png  style="width:32px;"> Dodaj ograniczenie okrągłej krawędzi (Add circular edge constraint)
-   <img alt="" src=images/Assembly2_PlaneConstraint.png  style="width:32px;"> Dodaj wiązanie płaszczyznowe
-   <img alt="" src=images/Assembly2_AxialConstraint.png  style="width:32px;"> Dodaj wiązanie osiowe
-   <img alt="" src=images/Assembly2_AngularConstraint.png  style="width:32px;"> Utwórz wiązanie kątowe pomiędzy dwoma płaszczyznami
-   <img alt="" src=images/Assembly2_SphericalSurfaceConstraint.png  style="width:32px;"> Dodaj wiązanie powierzchni sferycznej
-   <img alt="" src=images/Assembly2_DOFAnimation.png  style="width:32px;"> Animacja stopni swobody
-   <img alt="" src=images/Assembly2_Assembly2Constraint.png  style="width:32px;"> Rozwiąż wiązanie Assembly2
-   <img alt="" src=images/Assembly2_Mux.png  style="width:32px;"> Połącz zespół w jeden obiekt 
*(użyj do stworzenia rysunku zespołu, i tak dalej\...)*
-   <img alt="" src=images/Assembly2_ListParts.png  style="width:32px;"> Tworzy listę części z obiektów zaimportowanych za pomocą programu Assembly2.
-   <img alt="" src=images/Assembly2_Ceck.png  style="width:32px;"> Sprawdzenie zespołu pod kątem nakładania się części/interferencji

Dodatkowe

-   <img alt="" src=images/Assembly2_BoltMultipleCircularEdges.png  style="width:32px;"> Śruby z wieloma okrągłymi krawędziami
-   <img alt="" src=images/Assembly2_FlipConstraint.png  style="width:32px;"> Przerzucanie wiązań
-   <img alt="" src=images/Assembly2_LockRotation.png  style="width:32px;"> Zablokuj obrót
-   <img alt="" src=images/Assembly2_Preferences.png  style="width:32px;"> Preferencje
-   <img alt="" src=images/Assembly2_Assembly2.png  style="width:32px;"> Ikonka środowiska pracy Złożenie 2

## Instalacja

### Instalacja automatyczna 

To środowisko pracy można zainstalować z [Menadżera dodatków](Std_AddonMgr/pl.md).

### Z GitHub\'a 

Aby użyć tego środowiska pracy sklonuj to repozytorium git pod swoim katalogiem FreeCAD Mod i zainstaluj biblioteki python pyside i numpy. W systemie Linux opartym na Debianie, takim jak Ubuntu, instalacja może być wykonana przez BASH w następujący sposób:


```python
sudo apt-get install git python-numpy python-pyside
mkdir ~/.FreeCAD/Mod
cd ~/.FreeCAD/Mod
git clone https://github.com/hamish2014/FreeCAD_assembly2.git
```

W FreeCAD będziesz miał teraz nową pozycję środowiska pracy o nazwie \"Assembly 2\". Po zainstalowaniu, użyj git aby zaktualizować do najnowszej wersji poprzez BASH w następujący sposób:


```python
cd ~/.FreeCAD/Mod/FreeCAD_assembly2
git pull
rm *.pyc
```

Alternatywnie, w systemie Ubuntu można użyć freecad-community PPA:


```python
Add ppa:freecad-community/ppa to your software sources
sudo apt-get update
sudo apt-get install freecad-extras-assembly2
```

W Windows

-   pobierz repozytorium git jako ZIP,
-   zakładając, że FreeCAD jest zainstalowany w 
```python C:\PortableApps\FreeCAD 0_15\```, przejdź do \"C:\\PortableApps\\FreeCAD 0\_15\\Mod\" w Eksploratorze Windows,
-   utwórz nowy katalog o nazwie \"assembly2\",
-   rozpakuj pobrane repozytorium w 
```pythonC:\PortableApps\FreeCAD 0_15\Mod\assembly2```

FreeCAD będzie teraz posiadał nową pozycję środowiska pracy o nazwie \" Assembly 2\".

Pyside i Numpy są zintegrowane z FreeCAD 0.15 dev-Snapshots, więc te pakiety Pythona nie muszą być instalowane indywidualnie.

Aby wykonać aktualizację do najnowszej wersji, należy usunąć folder assembly2 i ponownie pobrać repozytorium git.

## Odnośniki internetowe 

-   Wiki środowisk pracy:
-   Wiki FreeCAD:
-   Forum FreeCAD: <http://forum.freecadweb.org/viewtopic.php?f=10&t=8577>
-   Poradniki:
-   Filmy: [Środowisko pracy FreeCAD Złożenie 2 w akcji](https://www.youtube.com/watch?v=dhaYJKDk4GI), [Złożenie 2 demonstracja nowego solvera](http://youtu.be/ufhyUxQkeC0)
-   Pliki:
-   Zgłaszanie błędów: Proszę zgłaszać błędy na [Github](https://github.com/hamish2014/FreeCAD_assembly2/issues)

## Inne użyteczne odnośniki 

-   [Animacja](http://www.freecadweb.org/wiki/index.php?title=Sandbox:Animation): To środowisko pracy może być używane do tworzenia sekwencji obrazów.
-   [ExplodedAnimation](http://www.freecadweb.org/wiki/index.php?title=Sandbox:ExplodedAnimation): Środowisko pracy FreeCAD do tworzenia widoków rozłożonych i animacji złożeń.
-   [Zewnętrzne środowiska pracy](External_workbenches/pl.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Assembly2 Workbench/pl
