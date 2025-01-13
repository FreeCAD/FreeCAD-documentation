# TechDraw General Examples/pl
## Wprowadzenie

Środowisko pracy <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [Rysunek Techniczny](TechDraw_Workbench/pl.md) posiada wiele narzędzi, ale jakie są wymagane elementy, aby zamienić kartkę papieru w odpowiedni rysunek? Ta strona ma na celu wyjaśnienie i podanie kilku przykładów tego, co potrafi środowisko Rysunek Techniczny.



## Rysunki

Rysunek składa się z jednego lub więcej widoków opisujących część geometrycznie\... Ale to już wiesz, prawda?

Przyjrzyjmy się podstawowym elementom.



### Rysunki tworzone ręcznie 



#### Arkusz papieru 

Rozmiary papieru są znormalizowane i aby móc drukować bez skalowania, format naszego arkusza powinien odpowiadać żądanemu formatowi do drukowania.



#### Ramki

Kiedy rysunki rysowano ręcznie, należało je przypiąć lub przykleić taśmą do deski kreślarskiej. Do gotowego rysunku dodano dziurki, umożliwiające dołączenie złożonego rysunku do pliku lub teczki. Ta część zewnętrzna jest oddzielona prostokątną ramą. Kolejna prostokątna ramka wewnątrz pierwszej wyznacza obszar rysowania. Zwykle pomiędzy obiema ramkami znajduje się zestaw indeksów i separatorów służących do lokalizowania określonych elementów rysunku.



#### Blok tytułowy 

Blok tytułu zawiera pisemne informacje o narysowanej części i rysunku, takie jak numer części, tytuł, autor, właściciel itp.



#### Zestawienie materiałów 

Opcjonalnie rysunki złożeniowe mogą zawierać zestawienie materiałów *(BOM)*. Zestawienie materiałów można również umieścić na osobnym arkuszu rysunkowym lub arkuszu kalkulacyjnym.



#### Rejestr zmian 

Zmiany w części lub rysunku są protokołowane w dzienniku na rysunku lub w oddzielnym dokumencie i powiązane z rysunkiem za pomocą odpowiednich indeksów.



#### Widok

Widoki zawierają geometryczny opis części z określonego kierunku. Większość części wymaga co najmniej dwóch widoków do prawidłowego opisu.



#### Opisy

Dodatkowe teksty, które nie należą do elementów rysunku, wymienionych powyżej.



### Rysunki wykonane w środowisku Rysunek Techniczny 

Środowisko Rysunek Techniczny używa obiektu Strona jako kontenera dla wszystkich elementów związanych z rysowaniem. Nie może on istnieć samodzielnie, ale musi zawierać szablon. Dlatego nie ma polecenia Nowa strona, a nowy obiekt strony jest tworzony automatycznie za każdym razem, gdy wstawiany jest szablon.



#### Szablony

Obiekt [szablon](TechDraw_Templates/pl.md) jest plikiem obrazu [SVG](SVG/pl.md), a jego kod zawiera wszystkie informacje potrzebne do utworzenia wirtualnej kartki papieru z pasującymi ramkami i blokiem tytułowym oraz opcjonalnie zestawieniem materiałów.

Obrazy SVG nie są parametryczne. Oznacza to, że dla każdego formatu należy utworzyć osobny szablon, taki zestaw szablonów jest potrzebny dla każdej odmiany obiektów ramki lub bloku tytułowego. To sporo do kodowania i zarządzania, ale z drugiej strony szablony nie mogą zostać przypadkowo zmienione we FreeCAD.

Szablon można utworzyć na kilka sposobów:

1.  Narysuj go za pomocą programu [Inkscape](https://en.wikipedia.org/wiki/Inkscape), zobacz artykuł [Jak stworzyć własny szablon TechDraw](TechDraw_TemplateHowTo/pl.md).
2.  Napisać go samodzielnie, patrz [Omówienie szablonu](Sandbox_TechDraw_TemplateExplained.md).
3.  Użyj makra, zobacz artykuły [Generator szablonów](TechDraw_TemplateGenerator/pl.md) i [Makrodefinicja: Pomocnik szablonów](Macro_TemplateHelper/pl.md).

<img alt="" src=images/TechDraw_ExampleDrawing-01.png  style="width:400px;">



*Wyjaśnienie wyniku działania szablonu*

<img alt="" src=images/Macro_TemplateHelper_A3+BOM.png  style="width:400px;">



*Wynik działania makrodefinicji ''Pomocnik szablonów'', ISO A3 + zestawienie materiałów*



#### Dotychczasowy rysunek 

Do tego momentu można śmiało powiedzieć, że środowisko pracy Rysunek Techniczny w połączeniu z osadzonymi szablonami SVG może zapewnić odpowiedni arkusz rysunkowy z ramką i blokiem tytułowym. Niektóre wpisy mogą być zmieniane po utworzeniu dzięki edytowalnym tekstom, a niektóre treści mogą być wstawiane automatycznie, jeśli wykorzystywane są odpowiednie makrodefinicje. 

## Widoki

Widoki zawierają geometryczny opis 2D obiektu. Zawartość widoku Rysunku Technicznego może pochodzić z geometrii 3D lub być uzyskana z innego środowiska pracy, takiego jak <img alt="" src=images/TechDraw_ArchView.svg  style="width:16px;"> [Widok architektury](TechDraw_ArchView/pl.md) i <img alt="" src=images/TechDraw_DraftView.svg  style="width:16px;"> [Widoki Rysunku Roboczego](TechDraw_DraftView/pl.md).

Ponieważ FreeCAD jest aplikacją do modelowania 3D, kluczową funkcją środowiska pracy Rysunek Techniczny jest tworzenie widoków 2D z geometrii 3D. Spójrzmy na prosty przykład, część z poradnika [Podstawy dla środowiska pracy Projekt Części](Basic_Part_Design_Tutorial/pl.md), która jest również używana z poradnikiem [Podstawy dla środowiska pracy Rysunek Techniczny](Basic_TechDraw_Tutorial/pl.md):

<img alt="" src=images/Tut17_final_refined.png  style="width:300px;">



*Część z poradnika Podstawy projektowania części*



### Aktywny widok 

Obraz <img alt="" src=images/TechDraw_ActiveView.svg  style="width:32px;"> [Aktyny widok](TechDraw_ActiveView/pl.md) jest mniej więcej zrzutem ekranu [widoku 3D](3D_view/pl.md) w swoim własnym rodzaju widoku Rysunku technicznego.

<img alt="" src=images/TechDraw_ExampleDrawing-02.png  style="width:300px;">



*Element wyświetlany w widoku aktywnym z włączoną opcją Bez tła*



### Widok 

Obraz <img alt="" src=images/TechDraw_View.svg  style="width:32px;"> [Widok](TechDraw_View/pl.md) jest podstawowym obiektem widoku Rysunku technicznego do tworzenia odpowiednich rysunków. W przeciwieństwie do widoku aktywnego, nie jest on ograniczony do widocznych obiektów na ekranie, ale wyświetla również wybrane obiekty poza ekranem. Preferowana skala zależy od dostępnej przestrzeni i poziomu szczegółowości, który ma być wyświetlany.

<img alt="" src=images/TechDraw_ExampleDrawing-03.png  style="width:300px;">



*Element wyświetlany w dowolnym widoku, takim jak Aktywny widok - powyżej*



### Grupa rzutów 

Narzędzie <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:32px;"> [Grupa rzutów](TechDraw_ProjectionGroup/pl.md) dostarcza zestaw widoków. Kierunek każdego widoku jest prostopadły do jego sąsiada i wszystkie domyślnie zależą od kierunku okna 3D. Środowisko pracy Rysunek Techniczny zapewnia sześć widoków pasujących do boków [Kostki nawigacyjnej](Navigation_Cube/pl.md) i cztery widoki izometryczne.

<img alt="" src=images/TechDraw_ExampleDrawing-04.png  style="width:300px;">



*Element wyświetlany w grupie rzutów składającej się z trzech widoków ''(w trybie rzutu pod pierwszym kątem)''*



### Widok przekroju 

Środowisko pracy Rysunek Techniczny zapewnia narzędzia do tworzenia <img alt="" src=images/TechDraw_SectionView.svg  style="width:32px;"> [Widoku przekroju](TechDraw_SectionView/pl.md) lub <img alt="" src=images/TechDraw_ComplexSection.svg  style="width:32px;"> [Widoku przekroju złożonego](TechDraw_ComplexSection/pl.md). Oba rodzaje są zależne od widoku bazowego i narzędzi do definiowania linii przekroju i określania kierunku widoku. Zapoznaj się z omówieniem w [przykładów przekrojów](TechDraw_Section_Examples/pl.md).

<img alt="" src=images/TechDraw_ExampleDrawing-05.png  style="width:300px;">



*Element przecięty wyświetlany w przekroju A-A na podstawie widoku z przodu*



### Widok pomocniczy 

Gdybyśmy potrzebowali widoku pochylonej płaszczyzny, aby zobaczyć jej rzeczywiste długości, zdefiniowalibyśmy kierunek widoku w widoku podstawowym i odpowiednio umieścilibyśmy widok pomocniczy, ale środowisko Rysunek Techniczny nie zapewnia jeszcze narzędzia do widoków pomocniczych.

Dobra wiadomość: jest to dość łatwe do naśladowania przy użyciu narzędzia <img alt="" src=images/TechDraw_SectionView.svg  style="width:32px;"> [Widok przekroju](TechDraw_SectionView/pl.md):

1.  Wybierz widok podstawowy.
2.  Utwórz <img alt="" src=images/TechDraw_SectionView.svg  style="width:16px;"> [Widok przekroju](TechDraw_SectionView/pl.md) z domyślnymi ustawieniami.
3.  Użyj <img alt="" src=images/TechDraw_AngleDimension.svg  style="width:16px;"> [Wstaw wymiar kąta](TechDraw_AngleDimension/pl.md) aby zmierzyć kąt płaszczyzny.
4.  Edytuj kąt widoku przekroju w obszarze Ustaw kierunek widoku w panelu zadań.
5.  Edytuj współrzędne widoku przekroju w obszarze Section Plane Location w panelu zadań. Użyj *małych kroków*, aby przesunąć linię przekroju poza obiekt, w przeciwnym razie FreeCAD może się zawiesić.
6.  Ukryj niechciane elementy adnotacji, takie jak linia przekroju, strzałki przekroju i nazwa przekroju.
7.  Dodaj potrzebne elementy, takie jak strzałka widoku i nazwa widoku.

<img alt="" src=images/TechDraw_ExampleDrawing-06.png  style="width:300px;">



*Domyślny widok przekroju oparty na widoku z lewej strony, wyświetlający kąt linii przekroju*

<img alt="" src=images/TechDraw_ExampleDrawing-07.png  style="width:300px;">



*Widok przekroju z kątem linii przekroju ustawionym na {{value|218,93°* ''(38,93° plus 180° do odwrócenia kierunku)''}}

<img alt="" src=images/TechDraw_ExampleDrawing-08.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleDrawing-09.png  style="width:300px;">



*Widok przekroju z przeniesioną linią przekroju → Gotowy widok pomocniczy*



### Widok szczegółu 

Obiekt <img alt="" src=images/TechDraw_DetailView.svg  style="width:32px;"> [Widok szczegółu](TechDraw_DetailView/pl.md) to kopia obszaru widoku podstawowego, zwykle w celu powiększenia słabo widocznej geometrii.

<img alt="" src=images/TechDraw_ExampleDrawing-10.png  style="width:300px;">



*Szczegół ''(widok)'' Y na podstawie przekroju A-A*



### Niedoskonałości

-   Widok detalu zgodnie ze standardem ISO nie ma ramki/obramowania *(górnej części otaczającego okręgu)*. Uwaga redaktora: co należy przez to rozumieć? Ramki nie są drukowane\...
-   Linia przerwania, która odcina detal od reszty powinna być cienką linią odręczną lub jej odpowiednikiem w programie CAD, cienką linią zygzakowatą. FreeCAD i środowisko pracy Rysunek Techniczny nie zapewniają *(jeszcze)* kreślenia linii odręcznych / zygzakowatych.
-   Obszary zakreskowane w widoku podstawowym powinny być również zakreskowane w widoku szczegółowym.



### Widok architektoniczny 

<img alt="" src=images/TechDraw_ArchView.svg  style="width:32px;"> [Widok architektoniczny](TechDraw_ArchView/pl.md) wyświetla widok <img alt="" src=images/Arch_SectionPlane.svg  style="width:16px;"> [płaszczyzny przekroju](Arch_SectionPlane/pl.md). Jego zawartość jest renderowana przez środowisko pracy <img alt="" src=images/Workbench_BIM.svg  style="width:16px;"> [BIM](BIM_Workbench/pl.md).



### Widok środowiska Rysunek Roboczy 

Obraz <img alt="" src=images/TechDraw_DraftView.svg  style="width:32px;"> [Widok obiektu Rysunku Roboczego](TechDraw_DraftView/pl.md) wyświetla widok wybranego obiektu opartego na środowisku pracy [Część](Part_Workbench/pl.md) lub obiektu grupy. Jest przeznaczony dla obiektów 2D. Jego zawartość jest renderowana przez środowisko <img alt="" src=images/Workbench_Draft.svg  style="width:16px;"> [Rysunek Roboczy](Draft_Workbench/pl.md).

<img alt="" src=images/05_Dr01_Draft_Text_ShapeString.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/06_Dr01_Draft_TechDraw_page.png  style="width:300px;">



*Wybrane elementy szkicu w widoku 3D → Te same elementy wyświetlane w widoku rysunku roboczego na rysunku*



### Widok Arkusza kalkulacyjnego 

-   Wstawia widok wybranego <img alt="" src=images/TechDraw_SpreadsheetView.svg  style="width:32px;"> [Arkusza kalkulacyjnego](TechDraw_SpreadsheetView/pl.md) ze środowiska pracy [Arkusz kalkulacyjny](Spreadsheet_Workbench/pl.md).

<img alt="" src=images/TechDraw_Spreadsheetview.png  style="width:300px;">



*Obiekt środowiska Arkusz kalkulacyjny wyświetlany w widoku arkusza kalkulacyjnego*



### Dotychczasowe widoki 

Środowisko Rysunek Techniczny potrzebuje kilku dodatków, takich jak linie łamania i odpowiednie narzędzie widoku pomocniczego, a także ulepszenia narzędzia widoku szczegółu. Ale nawet w tym stanie możemy opisać nasze obiekty wizualnie całkiem dobrze:

<img alt="" src=images/TechDraw_ExampleDrawing-11.png  style="width:300px;">



*Tak mógłby wyglądać rysunek z zestawem widoków przykładowego elementu*


{{Top}}



## Wymiarowanie

Teraz, gdy nasz przedmiot jest opisany geometrycznie, wymiary zostaną dodane w celu dalszego zdefiniowania kształtu, a tolerancje w celu zdefiniowania dopuszczalnego odchylenia. Środowisko pracy Rysunek Techniczny dostarcza kilka narzędzi do zastosowania wymiarów do dwuwymiarowej reprezentacji naszego przedmiotu:

-   <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Wymiar długości](TechDraw_LengthDimension/pl.md)
-   <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:16px;"> [Wymiar poziomy](TechDraw_HorizontalDimension.md)
-   <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> [Wymiar pionowy](TechDraw_VerticalDimension/pl.md)
-   <img alt="" src=images/TechDraw_RadiusDimension.svg  style="width:16px;"> [Wymiar promienia](TechDraw_RadiusDimension/pl.md)
-   <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width:16px;"> [Wymiar średnicy](TechDraw_DiameterDimension/pl.md)
-   <img alt="" src=images/TechDraw_AngleDimension.svg  style="width:16px;"> [Wymiar kąta](TechDraw_AngleDimension/pl.md)
-   <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width:16px;"> [Trzy punktowy wymiar kąta](TechDraw_3PtAngleDimension/pl.md)

Ich wspólną cechą jest to, że mierzą rzutowany kształt elementu. Jeśli uczyłeś się kreślenia w sposób ręczny, wiesz, jak używać widoków pomocniczych, aby obrócić element do pozycji, w której długości rzutowane są równe długościom rzeczywistym. W przypadku wizualizacji innej niż ta staroszkolna, wymiary można powiązać z geometrią 3D za pomocą narzędzia <img alt="" src=images/TechDraw_DimensionRepair.svg  style="width:16px;"> [Napraw odniesienia do wymiarów](TechDraw_DimensionRepair/pl.md), aby wyświetlić \"rzeczywiste wymiary\".

Dwa inne narzędzia mierzą całkowitą długość odpowiednio poziomo lub pionowo:

-   <img alt="" src=images/TechDraw_HorizontalExtentDimension.svg  style="width:16px;"> [Wstaw wymiar rozpiętości poziomej](TechDraw_HorizontalExtentDimension/pl.md)
-   <img alt="" src=images/TechDraw_VerticalExtentDimension.svg  style="width:16px;"> [Wstaw wymiar rozpiętości pionowej](TechDraw_VerticalExtentDimension/pl.md)

Nie można ich jeszcze łączyć z geometrią 3D.

Zobacz informacje na stronie [Okjnodialogowe](TechDraw_LengthDimension/pl#Okno_dialogowe.md) *(i następującą sekcję właściwości)* dla wszystkich ustawień, które nie zostały wymienione w tym przeglądzie.



### Wymiary podstawowe 

Tekst wymiaru zależy głównie od tych właściwości:

-    **Specyfikator formatu**
    

-    **Format Specyfikacji Nad Tolerancją**
    

-    **Format Specyfikacji Pod Tolerancją**.

:   Domyślnie ich wartości to {{Value|%.2f}}.

Aby \"oszukać\", możemy użyć tych dwóch właściwości:

-    **Dowolnie**
    

:   

    :   Ustaw na {{FALSE/pl}}, aby użyć zawartości **Specyfikator formatu** do sformatowania rzeczywistej wartości wymiaru.
    :   Ustaw na {{TRUE/pl}}, aby użyć zawartości **Specyfikator formatu** do wyświetlenia jako tekst zamiast wartości wymiaru.

-    **Tolerancja dowolnie**: Podobnie jak **Dowolnie**, ale dla tolerancji.

Jeśli potrzebujemy tylko wartości wymiaru, nie pozostaje nic innego, jak zmienić liczbę miejsc po przecinku w razie potrzeby.

:   Na przykład: {{Value|%.2f}} → {{Value|%.3f}}, aby wyświetlić 3 miejsca po przecinku, lub {{Value|%.2f}} → {{Value|%.0f}}, aby wyświetlić liczby całkowite.



#### Wymiar długości 

Dostępne są trzy narzędzia do dodawania wymiarów długości: <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Wymiar długości](TechDraw_LengthDimension/pl.md), <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:16px;"> [Wymiar poziomy](TechDraw_HorizontalDimension/pl.md), oraz <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> [Wymiar pionowy](TechDraw_VerticalDimension/pl.md).

<img alt="" src=images/TechDraw_ExampleDrawing-17.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleDrawing-18.png  style="width:300px;">



*Po lewej: Dwa widoki obiektu z zastosowanymi wymiarami długości → Po prawej: Ten sam widok z przodu obrócony o 20°*

Pokazuje to, że ważne jest, aby obrócić widok z przodu w oknie dialogowym Grupy rzutów, w przeciwnym razie połączone widoki nie będą zgodne. Z drugiej strony ograniczyłoby nas to do obrotów o 90°.

Jeśli wymiar musi przebiegać równolegle do krawędzi, wymaga innej wybieralnej linii prostopadłej do krawędzi i narzędzia <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Wstaw wymiar długości](TechDraw_LengthDimension/pl.md), które może znaleźć najkrótszą \\(= prostopadłą)\\ odległość między punktem a linią. Krawędź nie zostanie automatycznie przedłużona przez umowną linię, więc musimy ręcznie utworzyć linię pomocniczą \\(kosmetyczną)\\. \\(Można również użyć punktu kosmetycznego, ale wymaga to jeszcze więcej pracy)\\.

-   Czarny (punkt do linii) <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Wymiar długości](TechDraw_LengthDimension/pl.md) zależy od linii pomocniczej, która nie obraca się wraz z widokiem *(punkt kosmetyczny też nie byłby pomocny)*.
-   <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:16px;"> [Wymiar poziomy](TechDraw_HorizontalDimension/pl.md) i <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> [Wymiar pionowy](TechDraw_VerticalDimension/pl.md) *(czerwony i zielony)* pozostają w orientacji strony i odpowiednio zmieniają swoje wartości.
-   Niebieski to punkt do linii <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Wymiar długości](TechDraw_LengthDimension/pl.md), ale obraca się wraz z widokiem, ponieważ nie ma geometrii pomocniczej.



#### Wymiar kąta 

Środowisko pracy Rysunek Techniczny udostępnia dwa narzędzia do dodawania wymiarów kątowych: <img alt="" src=images/TechDraw_AngleDimension.svg  style="width:16px;"> [Wymiar kąta](TechDraw_AngleDimension/pl.md) oraz <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width:16px;"> [Trzy punktowy wymiar kąta](TechDraw_3PtAngleDimension/pl.md).

<img alt="" src=images/TechDraw_ExampleDrawing-19.png  style="width:300px;">



*Dwa sposoby dodania wymiaru kąta.*

-   Niebieski: <img alt="" src=images/TechDraw_AngleDimension.svg  style="width:16px;"> [Wymiar kąta](TechDraw_AngleDimension/pl.md) między dwiema krawędziami.
-   Czerwony: <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width:16px;"> [Trzy punktowy wymiar kąta](TechDraw_3PtAngleDimension/pl.md) przy użyciu punktów końcowych i punktu środkowego łuku.



#### Wymiar sfazowania 

Wymiar fazowania można zastosować jako [Wymiar długości](#Wymiar_długości.md) z ręcznie edytowaną właściwością **Specyfikator formatu** lub przy użyciu narzędzia <img alt="" src=images/TechDraw_ExtensionCreateHorizChamferDimension.svg  style="width:16px;"> [Wymiar poziomy sfazowania](TechDraw_ExtensionCreateHorizChamferDimension/pl.md) oraz <img alt="" src=images/TechDraw_ExtensionCreateVertChamferDimension.svg  style="width:16px;"> [Wymiar pionowy sfazowania](TechDraw_ExtensionCreateVertChamferDimension/pl.md), aby utworzyć rozmiar i wymiar kąta sfazowania.

<img alt="" src=images/TechDraw_ExampleDrawing-14.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleDrawing-15.png  style="width:300px;"> <img alt="" src=images/Button_right.svg  style="width:16px;"> <img alt="" src=images/TechDraw_ExampleDrawing-16.png  style="width:300px;">



*Po lewej: Wymiary sfazowania zastosowane do obiektu z poziomymi i pionowymi bokami → Środek: Ten sam widok obrócony o 10° → Po prawej: Obiekt przechylony o 10°, widok pod kątem 0.*

Narzędzia do sfazowania działają dobrze w przypadku obiektów o poziomych i pionowych bokach, o ile są one równoległe do osi X i Y widoku = strony, ale wiele części nie zrobi nam przysługi, aby były idealnie wyrównane.

Wartości kąta nie są parametryczne! Nie zmieniają się, gdy widok jest przechylony. Ostatnia strona pokazuje prawidłowe kąty, ale wymiary ustawione w ten sposób nie mają sensu.

Aby wyrównać wymiar sfazowania wzdłuż krawędzi, potrzebujemy punktu pomocniczego *(kosmetycznego)*, w którym spotykałyby się niefazowane krawędzie i musimy użyć <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Wymiar długości](TechDraw_LengthDimension/pl.md). Ale punkt kosmetyczny nie będzie podążał za krawędziami, jeśli widok jest przechylony. *(zobacz także akapit [Wymiar długości](#Wymiar_długości.md))*.



#### Wymiar promienia 

<img alt="" src=images/TechDraw_RadiusDimension.svg  style="width:32px;"> [Wstaw wymiar promienia](TechDraw_RadiusDimension/pl.md): dodaje wymiar promienia do okręgu lub łuku.

<img alt="" src=images/TechDraw_ExampleDrawing-20.png  style="width:300px;">



*Dwa sposoby dodania wymiaru promienia, czerwony z odwróconymi grotami strzałek.*

Aby zmienić kierunek strzałek, wystarczy ustawić wartość właściwości **Odwróć groty** na {{true/pl}}.



#### Wymiar średnicy 

Wymiary średnicy można dodać jako <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width:16px;"> [Wymiar średnicy](TechDraw_DiameterDimension/pl.md) lub jeden z wymiarów długości <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:16px;"> [Wymiar długości](TechDraw_LengthDimension/pl.md), <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:16px;"> [Wymiar poziomy](TechDraw_HorizontalDimension/pl.md), oraz <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> [Wymiar pionowy](TechDraw_VerticalDimension/pl.md) *(lub w połączeniu z linią odniesienia wskazującą na środek okręgu lub linię środkową - niewyświetlane)*.

<img alt="" src=images/TechDraw_ExampleDrawing-12.png  style="width:300px;">



*Kilka sposobów umieszczenia wymiaru średnicy ''(zignoruj brakującą linię środkową)''.*

-   Niebieski: <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> wymiar długości w widoku bocznym otworu wymaga przedrostka \"⌀\", aby odróżnić go od prostokątnego otworu.

:   <img alt="" src=images/TechDraw_ExtensionInsertDiameter.svg  style="width:16px;"> [Dodaj przedrostek \"⌀\"](TechDraw_ExtensionInsertDiameter/pl.md) jest łatwym sposobem na wykonanie tego, ale właściwość **Specyfikator formatu** może być również edytowana ręcznie.

-   Zielony: zwykły <img alt="" src=images/TechDraw_VerticalDimension.svg  style="width:16px;"> wymiar długości.

:   Wymaga pewnej geometrii pomocniczej *(punkty kosmetyczne)*, ponieważ nie można go zastosować bezpośrednio do okręgów.

-   Czerwony: <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width:16px;"> wymiar średnicy. Jeśli spojrzysz wzdłuż osi otworu i zobaczysz okrągły kształt otworu, \"⌀\" może zostać pominięte. Aby go usunąć, należy ręcznie edytować właściwość **Specyfikator formatu**.



#### Wymiar gwintu 

Wymiary gwintu mogą być stosowane tak samo jak wymiary średnicy, ale wymagają pewnej pomocniczej geometrii utworzonej wcześniej: <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width:16px;"> [Geometria pomocnicza dla otworu gwintowanego, widok z boku](TechDraw_ExtensionThreadHoleSide/pl.md), <img alt="" src=images/TechDraw_ExtensionThreadHoleBottom.svg  style="width:16px;"> [Geometria pomocnicza dla otworu gwintowanego, widok od dołu](TechDraw_ExtensionThreadHoleBottom/pl.md), <img alt="" src=images/TechDraw_ExtensionThreadBoltSide.svg  style="width:16px;"> [Geometria pomocnicza dla gwintu śruby, widok z boku](TechDraw_ExtensionThreadBoltSide/pl.md), lub <img alt="" src=images/TechDraw_ExtensionThreadBoltBottom.svg  style="width:16px;"> [Geometria pomocnicza dla gwintu śruby, widok od dołu](TechDraw_ExtensionThreadBoltBottom/pl.md).

<img alt="" src=images/TechDraw_ExampleDrawing-13.png  style="width:350px;">



*Gwint stożkowy z kilkoma sposobami umieszczenia wymiaru gwintu ''(i średnicy stożka)''*

Wszystkie wymiary gwintów są stosowane do linii pomocniczych *(kosmetycznych)* lub okręgów *(w połączeniu z punktami kosmetycznymi)*, a wszystkie właściwości **Specyfikator formatu** muszą być edytowane ręcznie, aby poprzedzić \"M\" dla gwintów metrycznych.



#### Tolerancja

Tolerancje określają, jak bardzo zmierzony wymiar może odbiegać od wartości wymiaru na rysunku. Aby dodać wartości tolerancji do wartości wymiaru, wystarczy ustawić właściwość **Powyżej tolerancji** na wartość inną niż {{Value|0}}, co skutkuje symetryczną tolerancją, taką jak {{Value|±0,5}}.

Dla asymetrycznej tolerancji ustaw wartość właściwość **Tolerancja symetryczna** na {{false/pl}} i określ niższą wartość dla właściwości **Poniżej tolerancji**.

Wartości można ustawić w [okienku dialogowym](TechDraw_LengthDimension/pl#Okno_dialogowe.md) lub bezpośrednio w [Edytorze właściwości](Property_editor/pl.md).



#### Pasowanie otwór / wał 

Tolerancje pasowania mogą być dodawane poprzez dodanie klas tolerancji do wymiaru. Klasa tolerancji składa się ze specyfikatora pola tolerancji *(duża litera dla otworów, mała litera dla wałków)* i specyfikatora klasy tolerancji *(liczba)* i może być dodana na trzy sposoby:

1.  Ustaw wartość właściwości **Tolerancja dowolna** na {{true}} i określ obie klasy tolerancji we właściwościach **Powyżej tolerancji** i **Poniżej tolerancji**.
2.  Użyj narzędzia <img alt="" src=images/TechDraw_HoleShaftFit.svg  style="width:16px;"> [Dodaj pasowanie otworu / wału](TechDraw_HoleShaftFit/pl.md). Ten sufiks dodaje tylko jedną klasę tolerancji, ale dodaje powiązane wartości do właściwości **Powyżej tolerancji** i **Poniżej tolerancji**.
3.  W przypadku pojedynczej tolerancji wystarczy dodać klasę tolerancji do specyfikatora formatu we właściwości **Specyfikator formatu**.



#### Pasowanie gwintu 

Tolerancje pasowania gwintu mogą być opatrzone przyrostkiem, jak opisano powyżej dla tolerancji pasowania otworu / wału, z wyjątkiem metody 2. Klasy tolerancji gwintu wyświetlają specyfikator stopnia tolerancji *(liczbę)* przed specyfikatorem pola tolerancji *(wielką literę dla gwintów wewnętrznych, małą literę dla gwintów zewnętrznych)*.



### Wymiary kontrolne 

Wymiary kontrolne (wymiary testowe) nie zostały jeszcze zaimplementowane. *(Może już przestarzałe. Zobacz temat [\...wymiar testowy został wycofany\...](https://forum.freecad.org/viewtopic.php?p=691914#p691914) na forum)*

Aby uzyskać pozorny wymiar kontrolny, ustawiamy właściwość **Specyfikator formatu** na \" \" *(jedna spacja - nie ma żadnego znaku i nie mielibyśmy żadnego uchwytu do chwycenia linii wymiaru, aby ją przesunąć)*, a następnie ustawiamy wartość właściwości **Dowolny** na {{TRUE/pl}}; skutkuje to wymiarem bez wartości. Wartość można teraz zastąpić dymkiem bez linii odniesienia. Działa to tylko w przypadku wymiarów poziomych, ponieważ nie możemy obracać dymków.

<img alt="" src=images/TechDraw_ExampleDrawing-21.png  style="width:300px;">



*Przykładowy element z wymiarem kontrolnym. W tym przypadku 100% elementów produkcyjnych musi zostać sprawdzonych, czy mieszczą się w tolerancji.*



### Wymiarowanie geometrii i tolerancja 

System [Wymiarowanie geometrii i tolerancja](TechDraw_Geometric_dimensioning_and_tolerancing/pl.md) *(GD&T)* ma na celu opisanie kształtów dokładniej niż mogą to zrobić same wymiary tolerowane. Opiera się na punktach odniesienia, teoretycznie dokładnych wymiarach i wskaźnikach tolerancji.



#### Odniesienia

Odniesienia to wirtualne powierzchnie, płaszczyzny, linie i punkty używane jako odniesienia do opisywania cech geometrycznych z teoretycznie dokładnymi wymiarami i wskaźnikami tolerancji. Można ich użyć do zbudowania teoretycznie dokładnego wirtualnego układu współrzędnych.



#### Cecha odniesienia 

Cecha odniesienia jest cechą geometryczną obiektu odpowiadającą pewnemu układowi odniesienia. Symbole punktów odniesienia są dodawane za pomocą <img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;"> [dymków](TechDraw_Balloon/pl.md) adnotacji.

<img alt="" src=images/TechDraw_ExampleDrawing-22.png  style="width:350px;">



*Przykładowy element z cechami odniesienia. Oba widoki wyświetlają dokładnie te same elementy odniesienia*

Wartość właściwości **Długość załamania** musi być ustawiona na {{Value|0}} dla pionowych linii odniesienia. W {{VersionMinus/pl|0.21}} skutkuje to wyświetleniem fragmentu linii w ramce.

<img alt="" src=images/TechDraw_ExampleDrawing-27.png  style="width:200px;">



*Teraz linia odniesienia zaczyna się na ramce, co jest idealne dla poziomych linii odniesienia, ale teraz niemożliwe jest prawidłowe narysowanie pionowych linii odniesienia*



#### Cel odniesienia 

Punkty odniesienia to punkty lub stosunkowo małe obszary, które wskazują miejsce, z którego należy wyprowadzić układ odniesienia. Najczęstszym zastosowaniem jest tworzenie teoretycznie dokładnego wirtualnego układu współrzędnych z zestawu sześciu punktów odniesienia.

<img alt="" src=images/TechDraw_ExampleDrawing-23.png  style="width:300px;">



*Ten rodzaj docelowego układu odniesienia nie został jeszcze zaimplementowany*

Obecnie nie jest znane żadne obejście tego problemu.

:   Specjalne symbole punktów wskazujące punkt odniesienia celu układu odniesienia nie są jeszcze uwzględnione w opcjach linii odniesienia.
:   Okręgi muszą pochodzić z geometrii 3D i są trudne w obsłudze w grupach rzutowania.



#### Wymiary teoretycznie dokładne 

Teoretycznie dokładne wymiary są dodawane w taki sam sposób jak [Wymiary podstawowe](#Wymiary_podstawowe.md), a różnicę zapewnia pole wyboru Teoretycznie dokładne: Ustawia ono wartość właściwości **W teorii dokładnie** na {{true/pl}}, która dodaje prostokątną ramkę do wartości wymiaru i dezaktywuje tolerancje oraz wszystkie ustawienia tolerancji.



### Wskaźnik tolerancji 

Wskaźnik tolerancji, nazywany również \"ramką kontrolną cech\", to ramka zawierająca informacje o tolerancji dotyczące:

-   wskazania która cecha geometryczna jest tolerowana,
-   kształtu i rozmiaru pola tolerancji,
-   układów odniesienia, do których należy się odnieść,
-   dodatkowych symboli opisujących cechy jeszcze dokładniej.

<img alt="" src=images/TechDraw_ExampleDrawing-24.png  style="width:300px;">



*Teoretycznie dokładne wymiary ''(czerwony)'' i wskaźniki tolerancji w odniesieniu do elementu odniesienia A ''(niebieski)''.*

Wskaźniki tolerancji są jak symbole punktów odniesienia dodane przy użyciu adnotacji <img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;"> [w dymkach](TechDraw_Balloon/pl.md), ale przy użyciu opcji {{value|Prostokąt}}. Użyj narzędzia <img alt="" src=images/TechDraw_ExtensionCustomizeFormat.svg  style="width:16px;"> [Dostosuj format etykiety](TechDraw_ExtensionCustomizeFormat/pl.md), aby wstawić znaki specjalne.

W większości przypadków wskaźniki tolerancji są wyrównane z linią wymiarową, co jest niemożliwe do zrealizowania w środowisku Rysunek Techniczny, z wyjątkiem wymiarów poziomych, ponieważ, jak już wspomniano, adnotacje w dymkach nie mogą być obracane. 

## Adnotacje



### Linia odniesienia 

<img alt="" src=images/TechDraw_LeaderLine.svg  style="width:16px;"> [Linia odniesienia](TechDraw_LeaderLine/pl.md) wskazuje na wierzchołek, krawędź lub ścianę, gdzie znajdują się dołączone informacje.

:   Narzędzia, które dostarczają informacji i dołączają do wstępnie wybranej linii odniesienia to <img alt="" src=images/TechDraw_RichTextAnnotation.svg  style="width:16px;"> [Opis z tekstem sformatowanym](TechDraw_RichTextAnnotation/pl.md), oraz <img alt="" src=images/TechDraw_WeldSymbol.svg  style="width:16px;"> [Symbol spawalniczy](TechDraw_WeldSymbol/pl.md).



### Dymki

<img alt="" src=images/TechDraw_Balloon.svg  style="width:16px;"> [Dymek](TechDraw_Balloon/pl.md) to połączenie linii odniesienia i krótkiego tekstu. Wymaga wstępnie wybranego widoku lub elementu należącego do widoku, w przeciwnym razie polecenie zwróci komunikat o błędzie. Linia odniesienia bez wyjątku zaczyna się poziomo i skręca w kierunku wybranego elementu po krótkiej odległości zdefiniowanej we właściwości **Długość zagięcia**. Jej wartość może być również ustawiona na {{Value|0}}.



### Tekst

Rysunek Techniczny udostępnia dwa narzędzia do dodawania tekstu do rysunku:

-   <img alt="" src=images/TechDraw_Annotation.svg  style="width:16px;"> [Wstaw adnotację](TechDraw_Annotation/pl.md) dodaje zwykły blok tekstu jako adnotację do strony. Adnotacje używają tych samych domyślnych ustawień co wymiary, niektóre parametry mogą być zmieniane, mogą być edytowane i obracane, ale nie mogą być dołączane.
-   <img alt="" src=images/TechDraw_RichTextAnnotation.svg  style="width:16px;"> [Wstaw adnotację w postaci tekstu sformatowanego](TechDraw_RichTextAnnotation/pl.md) dodaje blok tekstu sformatowanego jako adnotację do strony, linii odniesienia lub widoku. Adnotacje dołączone do linii odniesienia lub widoku przesuwają się synchronicznie z widokiem lub linią odniesienia, gdy zmienia się ich położenie.



### Symbol spawakniczy 

<img alt="" src=images/TechDraw_WeldSymbol.svg  style="width:16px;"> [Symbol spawalniczy](TechDraw_WeldSymbol/pl.md) dołącza się do wstępnie wybranej linii odniesienia i dodaje informacje o tym, jak utworzyć określony spaw między dwoma obiektami, aby uniknąć modelowania powierzchni szwu na surowych częściach. Tekst rozwidlenia określa, który proces spawania lub lutowania ma być użyty dla szwu.

:   Wygląda na to, że symbole spoin wymagają zintegrowanej linii odniesienia, aby uzyskać symbol rozwidlenia pasujący do rozmiaru tekstu, w przeciwnym razie symbole na linii odniesienia muszą być skalowalne.

<img alt="" src=images/TechDraw_ExampleDrawing-26.png  style="width:300px;">



*Symbol spoiny dla obwodowego szwu V, 111 oznaczający ręczne spawanie łukowe - Nie bij mnie, jeśli źle zacytowałem zasoby internetu.*



### Symbole wykończenia powierzchni 

<img alt="" src=images/TechDraw_SurfaceFinishSymbols.svg  style="width:16px;"> [Dodaj symbol wykończenia powierzchni](TechDraw_SurfaceFinishSymbols/pl.md) dodaje symbol wykończenia powierzchni do strony, co oznacza, że symbole te nie poruszają się wraz z geometrią, do której się odnoszą.

<img alt="" src=images/TechDraw_ExampleDrawing-25.png  style="width:300px;">



*Symbol wykończenia powierzchni w zestawieniu z wymiarem*

Symbole te nie mogą być dostosowywane pod względem szerokości linii i typu czcionki, aby pasowały do wymiarów i trudno je edytować po utworzeniu. {{Top}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw General Examples/pl
