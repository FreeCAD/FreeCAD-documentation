# OpenCASCADE/pl
## Opis

**OpenCASCADE Technology**, w skrócie **OCC** lub **OCCT**, jest zbiorem bibliotek C++, które razem tworzą profesjonalne jądro komputerowego wspomagania projektowania *(CAD)* do modelowania obiektów 2D i 3D oraz budowania specjalistycznych narzędzi do produkcji, symulacji lub wizualizacji. OpenCASCADE jest sercem geometrycznych możliwości programu FreeCAD.

Klasy geometryczne OCCT są w większości zaimplementowane i udostępnione w programie FreeCAD za pośrednictwem środowiska pracy [Część](Part_Workbench/pl.md), od którego zależy większość innych [środowisk pracy](Workbenches/pl.md). Udostępnia on także wewnętrzne funkcje odczytu i zapisu różnych formatów plików, takich jak STEP i IGES, oraz wykonywania rzutów 2D, które mogą być używane do tworzenia rysunków technicznych w środowisku pracy [Rysunek Techniczny](TechDraw_Workbench/pl.md).

<img alt="" src=images/Part_Workbench_relationships.svg  style="width:600px;">



*OpenCASCADE dostarcza podstawowe klasy geometryczne i funkcje rysunkowe do środowiska pracy [Część](Part_Workbench/pl.md), które są następnie wykorzystywane przez wszystkie grupy robocze w programie FreeCAD.*

OpenCASCADE nie powinien być mylony z [OpenSCAD](https://www.openscad.org/), który jest innym projektem open source do budowy modeli 3D, dostępnym poprzez środowisko pracy [OpenSCAD](OpenSCAD_Workbench/pl.md).

OpenCASCADE jest wolnym oprogramowaniem podlegającym warunkom licencji GNU Lesser General Public License *(LGPL)* w wersji 2.1 z dodatkowym wyjątkiem.

## Instalacja

OpenCASCADE jest podstawowym komponentem FreeCAD, więc jeśli pobierzesz FreeCAD z jednego z linków na stronie [Pobierania](Download/pl.md), będziesz miał go zainstalowanego i żadna dalsza akcja instalacji nie jest konieczna.

Jednakże, jeśli chciałbyś rozwijać aplikacje, które używają OCCT, lub chciałbyś dodać kod C++ do FreeCAD, wtedy musisz zainstalować pliki programistyczne OCCT. W tym przypadku, procedura jest wyjaśniona na stronie [Kompilacja](Compiling/pl.md) dla każdego z głównych systemów, Linux, MacOS i Windows.

## Edycja społecznościowa 

Edycja społecznościowa\" OpenCASCADE, w skrócie OCE, została wydana w 2011 roku, w oparciu o oficjalne źródła OpenCASCADE *(OCCT)* w wersji 6.5. W teorii wydanie społecznościowe OCE powinno być kompatybilne z główną wersją OCCT w większości aspektów, jednocześnie posiadając pewien dodatkowy kod wniesiony przez społeczność.

Jednak ta alternatywna dystrybucja przestała aktywnie rozwijać się około 2017 roku i pozostała w tyle za główną wersją pod względem funkcji i poprawek błędów. Z tego powodu, od wersji FreeCAD v0.17, FreeCAD jest kompilowany wyłącznie z OCCT, a OCE nie jest testowany.

W niektórych starszych dystrybucjach Linuksa, FreeCAD jest kompilowany z OCE 0.18, odpowiednikiem OCCT 6.9.x, powodując różne problemy, które zostały już rozwiązane w głównych wydaniach OCCT 7.x. Jeśli tak jest, spróbuj usunąć OCE i zainstalować OCCT zamiast niego. Jeśli nie jest to możliwe, użyj kompilacji [AppImage](AppImage/pl.md) aby uzyskać nowoczesny FreeCAD z zaktualizowaną wersją OCCT.

## Historia

Jądro geometryczne Cas.CADE było pierwotnie zamknięte, ale stało się open source pod obecną nazwą około roku 2000. Niedługo potem rozpoczęto projekt FreeCAD, którego najstarsze pliki datowane są na styczeń 2001 roku. Czytaj więcej na stronie [Historia](History/pl.md).

OpenCASCADE w wersji 6.6 i wcześniejszych podlegał własnej \"licencji publicznej OCCT\", co sprawiało, że nie był w pełni \"wolnym oprogramowaniem\". Problem ten został rozwiązany wraz z wydaniem OCCT 6.7 *(2013)*, kiedy to przyjęto w nim licencję LGPL2.

## Koncepcje geometryczne OCCT 

W terminologii OpenCascade rozróżniamy geometryczne prymitywy i kształty powierzchniowe. Geometryczny prymityw może być punktem, linią, okręgiem, płaszczyzną itp. lub nawet bardziej skomplikowanymi typami, takimi jak krzywa złożona *(B-Spline)* lub powierzchnia. Kształt może być wierzchołkiem, krawędzią, obwodem, ścianą, bryłą lub składnikiem innych kształtów. Pierwotne elementy geometryczne nie są przeznaczone do bezpośredniego wyświetlania na scenie 3D, ale raczej do wykorzystania jako geometria konstrukcji kształtów. Na przykład, krawędź może być zbudowana z linii lub z fragmentu okręgu.

Podsumowując, prymitywy geometryczne to **bezkształtne** elementy konstrukcyjne, podczas gdy kształty [topologiczne](Part_TopoShape/pl.md) to realne obiekty zbudowane w ich oparciu.

Pełna lista wszystkich elementów pierwotnych i kształtów znajduje się w [dokumentacji OCC](https://dev.opencascade.org/resources/documentation) (Alternatywnie: [sourcearchive.com](https://www.opencascade.com/doc/occt-7.4.0/refman/html/)) i szukaj **Geom\_\*** *(dla prymitywów geometrycznych)* i **TopoDS\_\*** *(dla kształtów)*. Tam możesz również przeczytać więcej o różnicach między nimi. Należy pamiętać, że oficjalna dokumentacja OCC nie jest dostępna online (musisz pobrać archiwum) i jest skierowana głównie do programistów, a nie do użytkowników końcowych. Ale mam nadzieję, że znajdziesz wystarczająco dużo informacji, aby zacząć tutaj. Zobacz również [Podręcznik użytkownika danych modelowania](https://www.opencascade.com/doc/occt-7.0.0/overview/html/occt_user_guides__modeling_data.html).

> *Na bardzo wysokim poziomie topologia mówi, z jakich części składa się obiekt i jakie są logiczne relacje między nimi. Kształt tworzony jest z określonego zestawu powierzchni. Powierzchnia jest ograniczona pewnym zestawem krawędzi. Dwie powierzchnie sąsiadują ze sobą, jeśli mają wspólną krawędź.*

> *Sama topologia nie określa wielkości, krzywizny ani lokalizacji 3D żadnego z tych elementów. Jednak każdy element topologii wie o swojej podstawowej geometrii. Każda ściana wie, na jakiej powierzchni się znajduje. Krawędź wie, na jakiej krzywej leży. Geometria wie o krzywiznach i położeniu w przestrzeni.* - [Source](https://www.opencascade.com/content/geometry-and-topology)


<hr />

> *W ten sposób Topologia definiuje związek pomiędzy prostymi bryłami geometrycznymi, które mogą być łączone razem, aby reprezentować złożone kształty.* - [Podręcznik użytkownika danych modelowania](https://www.opencascade.com/doc/occt-7.0.0/overview/html/occt_user_guides__modeling_data.html)

![](images/ClassTopoDS_Shape_inherit_graph.png )

**Note:** Tylko 3 typy obiektów topologicznych mają reprezentacje geometryczne - wierzchołek, krawędź i powierzchnia *([źródło](https://opencascade.blogspot.com/2009/02/topology-and-geometry-in-open-cascade.html))*.

Typy geometryczne można podzielić na dwie główne grupy: krzywe i powierzchnie. Z krzywych *(linii, okręgu, \...)* można bezpośrednio zbudować krawędź, z powierzchni *(płaszczyzna, cylinder, \...)* można zbudować ścianę. Na przykład, pierwotna linia geometryczna jest nieograniczona, tzn. jest zdefiniowana wektorem bazowym i wektorem kierunku, podczas gdy jej reprezentacja kształtu musi być czymś ograniczonym np. przez punkt początkowy i końcowy. A kostka - bryła - może być utworzone przez sześć ograniczonych płaszczyzn.

Z krawędzi lub ściany można również powrócić do jej pierwotnego geometrycznego odpowiednika.

Zatem z kształtów można budować bardzo złożone części lub, odwrotnie, wyodrębniać wszystkie kształty podrzędne, z których składa się bardziej złożony kształt.

<img alt="" src=images/Part_TopoShape_relationships.svg  style="width:600px;">



*`Part::TopoShape* jest klasą obiektu geometrycznego, który jest widoczny na ekranie. Zasadniczo wszystkie Środowiska pracy wykorzystują te kształty [TopoShapes](Part_TopoShape.md) wewnętrznie, aby budować i wyświetlać krawędzie, ściany i bryły.`

## Powiązane

-   OpenCASCADE Technology (OCCT) [strona główna](http://www.opencascade.com)
-   OCCT [portal deweloperski](https://dev.opencascade.org/)
-   OCCT [najnowsze wydanie](https://www.opencascade.com/content/latest-release)
-   OCCT [repozytorium git](https://git.dev.opencascade.org/gitweb/?p=occt.git)
-   OpenCASCADE Community Edition (OCE) [repozytorium git](https://github.com/tpaviot/oce)
-   w Wikipedii [http://en.wikipedia.org/wiki/Open_Cascade_Technology Open Cascade Technology OCCT](http://en.wikipedia.org/wiki/Open_Cascade_Technology_Open_Cascade_Technology_OCCT.md)
-   Słownik pojęć, [Open CASCADE](Glossary/pl#Open_CASCADE.md)
-   Śledzenie błędów OCCT w bugtrackerze programu FreeCAD [*(wątek)*](https://forum.freecadweb.org/viewtopic.php?f=10&t=20264)



---
⏵ [documentation index](../README.md) > [Developer Documentation](Category_Developer%20Documentation.md) > OpenCASCADE/pl
