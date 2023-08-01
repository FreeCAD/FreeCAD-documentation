# <img alt="Ikonka FreeCAD dla Środowiska pracy OpenSCAD" src=images/Workbench_OpenSCAD.svg  style="width:64px;"> OpenSCAD Workbench/pl

## Wprowadzenie

<img alt="" src=images/Workbench_OpenSCAD.svg  style="width:24px;"> [Środowisko pracy OpenSCAD](OpenSCAD_Workbench/pl.md) służy do zapewnienia interoperacyjności z oprogramowaniem [OpenSCAD](http://www.openscad.org/). Program ten nie jest częścią projektu FreeCAD i by zapewnić pełną funkcjonalność tego środowiska należy zainstalować go samodzielnie.

OpenSCAD nie powinien być mylony z [OpenCASCADE](OpenCASCADE/pl.md) będącym nierozłącznym komponentem FreeCAD odpowiedzialnym za opis geometrii. Instalacja oprogramowania OpenSCAD jest w pełni opcjonalna.

Zawiera importer formatu [CSG](OpenSCAD_CSG/pl.md), który otwiera pliki CSG z OpenSCAD, oraz eksporter, który tworzy drzewo oparte na CSG. Geometria, która nie jest oparta na operacjach CSG, zostanie wyeksportowana jako siatka.

To środowisko pracy zawiera funkcje do modyfikacji drzewa cech CSG i naprawy modeli. Zawiera także narzędzia ogólnego przeznaczenia, które nie wymagają instalacji OpenSCAD Mogą być one używane w połączeniu z innymi środowiskami pracy. Na przykład, środowiskiem [Projekt Siatki](Mesh_Workbench/pl.md) wewnętrznie używa funkcji OpenSCAD do wykonywania operacji z [siatkami](Mesh/pl.md), ponieważ są one dość stabilne.




![](images/OpenSCADexamaple1.png )

## Zależności

W wersji FreeCAD 0.19 moduł Ply *(Python-Lex-Yacc)*, który jest używany do importowania plików CSG, został usunięty z kodu źródłowego FreeCAD, ponieważ jest to biblioteka zewnętrzna, która nie została opracowana przez zespół FreeCAD. W rezultacie musisz teraz zainstalować Ply przed użyciem środowiska OpenSCAD. W przypadku używania wstępnie spakowanej, stabilnej wersji FreeCAD zależność ta powinna być zainstalowana automatycznie na wszystkich platformach; w innych przypadkach, na przykład podczas [kompilowania](Compiling/pl.md) ze źródeł, może być konieczne zainstalowanie jej z repozytorium online.

W dystrybucjach opartych o openSUSE środowisko może zostać zainstalowane za pomocą:


```python
sudo zypper install python3-ply
```

W dystrybucjach opartych o Debian / Ubuntu środowisko może zostać zainstalowane za pomocą:


```python
sudo apt install python3-ply
```

Ogólna instalacja na wszystkich platformach może być wykonana z indeksu pakietów Pythona.


```python
pip3 install --user ply
```

## Język OpenSCAD i format pliku 

Język OpenSCAD pozwala na używanie zmiennych i pętli. Pozwala on na określenie modułów podrzędnych w celu ponownego użycia geometrii i kodu. Ten wysoki stopień elastyczności sprawia, że parsowanie kodu jest bardzo złożone. Obecnie środowisko OpenSCAD nie obsługuje natywnie języka OpenSCAD. Zamiast tego, jeśli OpenSCAD jest zainstalowany, może być użyty do konwersji danych wejściowych do formatu CSG, który jest podzbiorem języka OpenSCAD i może być użyty jako dane wejściowe do OpenSCAD do dalszej obróbki. Podczas konwersji wszystkie parametry są tracone, co oznacza, że wszystkie nazwy zmiennych są usuwane, pętle rozwijane, a wyrażenia matematyczne obliczane.

## Przybory

-   <img alt="" src=images/OpenSCAD_ColorCodeShape.svg  style="width:32px;"> [Oznacz kształt kolorem](OpenSCAD_ColorCodeShape/pl.md): Zmienia kolor wybranych lub wszystkich kształtów na podstawie ich znaczenia.
-   <img alt="" src=images/OpenSCAD_ReplaceObject.svg  style="width:32px;"> [Zastąp obiekt](OpenSCAD_ReplaceObject/pl.md): Zastępuje obiekt w drzewie cech.
-   <img alt="" src=images/OpenSCAD_RemoveSubtree.svg  style="width:32px;"> [Usuń gałąź drzewa](OpenSCAD_RemoveSubtree/pl.md): Usuwa wybrane obiekty i wszystkie elementy podrzędne, do których nie istnieją odniesienia z innych obiektów.
-   <img alt="" src=images/OpenSCAD_RefineShapeFeature.svg  style="width:32px;"> [Udoskonal siatkę](OpenSCAD_RefineShapeFeature/pl.md): Tworzy cechę udoskonalonego kształtu.
-   <img alt="" src=images/OpenSCAD_MirrorMeshFeature.svg  style="width:32px;"> [Odbicie lustrzane siatki](OpenSCAD_MirrorMeshFeature/pl.md): Tworzy cechę odbicia lustrzanego dla siatki.
-   <img alt="" src=images/OpenSCAD_ScaleMeshFeature.svg  style="width:32px;"> [Skaluj cechę siatki](OpenSCAD_ScaleMeshFeature/pl.md): Skaluje elementy siatki.
-   <img alt="" src=images/OpenSCAD_ResizeMeshFeature.svg  style="width:32px;"> [Zmień rozmiar cechy siatki](OpenSCAD_ResizeMeshFeature/pl.md): Zmień rozmiar elementu siatki.
-   <img alt="" src=images/OpenSCAD_IncreaseToleranceFeature.svg  style="width:32px;"> [Zwiększ tolerancję cechy](OpenSCAD_IncreaseToleranceFeature/pl.md): Zwiększa tolerancję krawędzi / powierzchni / wierzchołków wybranych obiektów..
-   <img alt="" src=images/OpenSCAD_Edgestofaces.svg  style="width:32px;"> [Przekształć krawędzie na ściany](OpenSCAD_Edgestofaces/pl.md): Przekształć krawędzie na powierzchnie. Przydatne do przygotowania importowanej geometrii DXF do wyciągnięcia.
-   <img alt="" src=images/OpenSCAD_ExpandPlacements.svg  style="width:32px;"> [Rozwiń umiejscowienia](OpenSCAD_ExpandPlacements/pl.md): Rozwiń wszystkie umiejscowienia w dół drzewa cech.
-   <img alt="" src=images/OpenSCAD_ExplodeGroup.svg  style="width:32px;"> [Rozbij grupę](OpenSCAD_ExplodeGroup/pl.md): Rozbija elementy pierwotne części scalonych.
-   <img alt="" src=images/OpenSCAD_AddOpenSCADElement.svg  style="width:32px;"> [Dodaj element OpenSCAD](OpenSCAD_AddOpenSCADElement/pl.md): Dodaj element OpenSCAD, wprowadzając kod OpenSCAD do panelu zadań.
-   <img alt="" src=images/OpenSCAD_MeshBoolean.svg  style="width:32px;"> [Operacja logiczna na siatce](OpenSCAD_MeshBoolean/pl.md): Tworzy nowy obiekt siatki za pomocą operacji logicznej z kształtów.
-   <img alt="" src=images/OpenSCAD_Hull.svg  style="width:32px;"> [Hull](OpenSCAD_Hull/pl.md): Stosuje funkcję hull do wybranych kształtów.
-   <img alt="" src=images/OpenSCAD_Minkowski.svg  style="width:32px;"> [Minkowski](OpenSCAD_Minkowski/pl.md): Stosuje sumę minkowskiego do wybranych kształtów.

## Ustawienia

-   <img alt="" src=images/Std_DlgPreferences.svg  style="width:32px;"> [Preferencje](OpenSCAD_Preferences/pl.md): ustawienia dostępne dla środowiska OpenSCAD.

## Ograniczenia

OpenSCAD tworzy konstrukcyjną geometrię bryłową, a także importuje pliki siatek i wytłacza geometrię 2D z plików [DXF](DXF/pl.md). FreeCAD pozwala również na tworzenie formatu CSG za pomocą elementów pierwotnych. Jądro geometrii FreeCAD *(OCCT)* działa w oparciu o reprezentację brzegową. Dlatego konwersja z CSG do BREP teoretycznie powinna być możliwa, natomiast konwersja z BREP do CSG zasadniczo nie jest.

OpenSCAD pracuje wewnętrznie na siatkach. Niektóre operacje, które są przydatne w przypadku siatek, nie mają znaczenia w modelu BREP i nie mogą być w pełni obsługiwane. Należą do nich m.in. kadłub wypukły, suma minkowskiego, przesuwanie i podział. Obecnie w celu wykonania operacji na kadłubie i sumie minkwoskiej uruchamiamy binarny program OpenSCAD i importujemy wynik. Oznacza to, że zaangażowana geometria zostanie poddana triangulacji. W OpenSCAD często stosuje się skalowanie niejednolite, co nie stwarza problemów przy korzystaniu z siatek. W naszym jądrze geometrii elementy pierwotne geometrii (linie, odcinki koliste itp.) są konwertowane na krzywe złożone przed wykonaniem takich deformacji. Te krzywe złożone są znane z tego, że powodują problemy w późniejszych operacjach logicznych. W chwili obecnej nie jest dostępne automatyczne rozwiązanie tego problemu. Jeśli napotkasz takie problemy, napisz o tym na forum. Często takie problemy można rozwiązać, przemodelowując małe części. Zniekształcenie walca można zastąpić wycięciem elipsy.

## Importowanie tekstu 

Importowanie kodu OpenSCAD z tekstami wymaga, aby czcionki, które są używane, były poprawnie zainstalowane w systemie. Można to sprawdzić otwierając OpenSCAD jako samodzielne narzędzie i sprawdzając listę w **Pomoc → Font List**. Lista ta zawiera również prawidłowe nazwy czcionek. Jeżeli po zainstalowaniu czcionka nie pojawia się na liście, może być konieczne ręczne skopiowanie pliku z czcionką do odpowiedniego katalogu systemowego.

Importowanie tekstów jest stosunkowo powolne. Za kulisami FreeCAD korzysta z pliku DXF utworzonego przez OpenSCAD. Im więcej konturów, tym wolniejszy jest import.

Dobrym pomysłem może być zaimportowanie najpierw prostego przykładu testowego *(zamień {{Incode|NameOfFont}} na poprawną nazwę czcionki)*:

    TESTFONT="NameOfFont";
    linear_extrude(0.001) {
      text("A", size=5, font=TESTFONT, script="Latn");
    };

Parametr {{Incode|<nowiki>script="Latn"</nowiki>}} można tutaj pominąć, ale jest on wymagany, jeśli łańcuch tekstowy nie zawiera żadnych liter, a jedynie znaki interpunkcyjne i / lub cyfry.

Należy pamiętać, że deklaracje {{Incode|<nowiki>use <FONT>;</nowiki>}} w plikach źródłowych są ignorowane podczas importu w FreeCAD. W OpenSCAD efektem deklaracji {{Incode|use}} jest tymczasowe dodanie podanego pliku czcionki do listy znanych czcionek *(chociaż nawet tam deklaracja nie działa, gdy skrypt jest modyfikowany interaktywnie)*.

## Wskazówki

Podczas importowania plików w formacie [DXF](DXF/pl.md) ustaw precyzję szkicu na rozsądną wartość, ponieważ będzie to miało wpływ na wykrywanie połączonych krawędzi.

Jeśli program FreeCAD zawiesza się podczas importowania pliku CSG, zaleca się włączenie opcji \"Automatycznie sprawdź model po operacji logicznej\" w menu **Edycja → Preferencje ... → Projekt Części → Ogólne → Ustawienia modelu**.

## Poradniki

-   [Importowanie kodu OpenSCAD](Import_OpenSCAD_code/pl.md)

## Odnośniki internetowe 

-   Oficjalne repozytorium kodu źródłowego projektu OpenSCAD znajduje się na stronie [GitHub](https://github.com/openscad/openscad)
-   Otwórz zgłoszenia oznaczone tagiem \"OpenSCAD\" na [FreeCAD Github issue tracker](https://github.com/FreeCAD/FreeCAD/labels/WB%20OpenSCAD). Istnieją również zgłoszenia na zarchiwizowanym już [mantis bugtracker](https://freecadweb.org/tracker/search.php?tag_string=OpenSCAD).
-   Modele oznaczone tagiem \"OpenSCAD\" w serwisie [Thingiverse](http://www.thingiverse.com/tag:openscad)





{{OpenSCAD Tools navi

}}



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [OpenSCAD](Category_OpenSCAD.md) > OpenSCAD Workbench/pl
