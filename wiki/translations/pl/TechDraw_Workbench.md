# <img alt="Ikonka FreeCAD dla środowiska pracy Rysunek Techniczny" src=images/Workbench_TechDraw.svg  style="width:64px;"> TechDraw Workbench/pl

## Wprowadzenie

Środowisko pracy <img alt="" src=images/Workbench_TechDraw.svg  style="width:24px;"> [Rysunek Techniczny](TechDraw_Workbench/pl.md) służy do tworzenia podstawowych rysunków technicznych z modeli 3D tworzonych przy użyciu innego środowiska pracy, takich jak [Część](Part_Workbench/pl.md), [Projekt Części](PartDesign_Workbench/pl.md) lub [Architektura](Arch_Workbench/pl.md), lub importowanych z innych aplikacji. Każdy rysunek jest Stroną, która może zawierać różne widoki obiektów rysunkowych, takich jak Part::Features, PartDesign::Bodies, App::Part groups i Document Object groups. Powstałe w ten sposób rysunki mogą być wykorzystane do takich celów jak dokumentacja, instrukcje produkcyjne, umowy, pozwolenia, itp.

Wymiary, przekroje, zakreskowane obszary, adnotacje i symbole [SVG](SVG/pl.md) mogą być dodane do strony, która może być dalej eksportowana do różnych formatów, takich jak [DXF](DXF/pl.md), [SVG](SVG/pl.md), i [PDF](PDF/pl.md).

Rysunek Techniczny został oficjalnie włączony do FreeCAD począwszy od wersji **0.17**. ma on być następcą nieobsługiwanego już Środowiska pracy _.

Jeśli Twoim głównym celem jest tworzenie złożonych rysunków 2D i plików [DXF](DXF/pl.md), a nie potrzebujesz modelowania 3D, FreeCAD może nie być właściwym wyborem dla Ciebie. Możesz rozważyć zastosowanie dedykowanego programu do tworzenia projektów technicznych, takiego jak [LibreCAD](https://en.wikipedia.org/wiki/LibreCAD), [QCad](https://en.wikipedia.org/wiki/QCad), lub innego.


{{TOCright}}

<img alt="" src=images/TechDraw_Workbench_Example.png  style="width:600px;">

## Strony

Te narzędzia służą do tworzenia obiektów na stronie.

-   <img alt="" src=images/TechDraw_PageDefault.svg  style="width:32px;"> _.

-   <img alt="" src=images/TechDraw_PageTemplate.svg  style="width:32px;"> _.

-   <img alt="" src=images/TechDraw_RedrawPage.svg  style="width:32px;"> [Odśwież widok](TechDraw_RedrawPage/pl.md): wymusza aktualizację wybranej strony. {{Version/pl|0.19}}

## Widoki

Są to narzędzia do tworzenia obiektów widoku.

-   <img alt="" src=images/TechDraw_View.svg  style="width:32px;"> [Wstaw widok na stronę](TechDraw_View/pl.md): dodaje widok obiektu wyświetlany w formie projekcji 2D.

-   <img alt="" src=images/TechDraw_ActiveView.svg  style="width:32px;"> [Wstaw aktywny widok](TechDraw_ActiveView/pl.md): wstawia kopię widoku z okna 3D do strony rysunku. {{Version/pl|0.19}}

-   <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:32px;"> [Wstaw wiele połączonych widoków](TechDraw_ProjectionGroup/pl.md): otwiera okno dialogowe do tworzenia wielu widoków obiektu z wielu kierunków.

-   <img alt="" src=images/TechDraw_SectionView.svg  style="width:32px;"> [Wstaw widok sekcji na stronę](TechDraw_SectionView/pl.md): dodaje widok przekroju dla aktualnego widoku.

-   <img alt="" src=images/TechDraw_DetailView.svg  style="width:32px;"> [Wstaw widok szczegółu](TechDraw_DetailView/pl.md): dodaje widok szczegółu części wybranego widoku.

-   <img alt="" src=images/TechDraw_DraftView.svg  style="width:32px;"> _.

-   <img alt="" src=images/TechDraw_ArchView.svg  style="width:32px;"> _ ze środowiska pracy [Architektura](Arch_Workbench.md).

-   <img alt="" src=images/TechDraw_SpreadsheetView.svg  style="width:32px;"> _.

## Wycinki

Są to narzędzia do tworzenia i zarządzania obiektami wycinków *(przycięte widoki)*.

-   <img alt="" src=images/TechDraw_ClipGroup.svg  style="width:32px;"> [Wstaw grupę wycinków](TechDraw_ClipGroup/pl.md): wstawia do strony grupę wycinków.

-   <img alt="" src=images/TechDraw_ClipGroupAdd.svg  style="width:32px;"> [Dodaj widok do grupy wycinków](TechDraw_ClipGroupAdd/pl.md): dodaje istniejący widok do grupy wycinków.

-   <img alt="" src=images/TechDraw_ClipGroupRemove.svg  style="width:32px;"> [Usuń widok z grupy wycinków](TechDraw_ClipGroupRemove/pl.md): usuwa widok z grupy wycinków.

## Wymiary

Są to narzędzia do tworzenia i pracy z obiektami Wymiarowymi.

Wymiary liniowe mogą być wyznaczone w oparciu o dwa punkty, na jednej linii lub na dwóch liniach.

-   <img alt="" src=images/TechDraw_LengthDimension.svg  style="width:32px;"> [Wstaw wymiar długości](TechDraw_LengthDimension/pl.md): dodaje wymiar dotyczący odległości.

-   <img alt="" src=images/TechDraw_HorizontalDimension.svg  style="width:32px;"> [Wstaw wymiar poziomy](TechDraw_HorizontalDimension/pl.md): dodaje poziomy wymiar długości.

-   <img alt="" src=images/TechDraw_Dimension_Vertical.svg  style="width:32px;"> [Wstaw wymiar pionowy](TechDraw_Dimension_Vertical/pl.md): dodaje pionowy wymiar długości.

-   <img alt="" src=images/TechDraw_RadiusDimension.svg  style="width:32px;"> [Wstaw wymiar promienia](TechDraw_RadiusDimension/pl.md): dodaje wymiar promienia do okręgu lub łuku.

-   <img alt="" src=images/TechDraw_DiameterDimension.svg  style="width:32px;"> [Wstaw wymiar średnicy](TechDraw_DiameterDimension/pl.md): dodaje wymiar średnicy do okręgu lub łuku.

-   <img alt="" src=images/TechDraw_AngleDimension.svg  style="width:32px;"> [Wstaw wymiar kąta](TechDraw_AngleDimension/pl.md): dodaje wymiar kąta pomiędzy dwoma krawędziami prostymi.

-   <img alt="" src=images/TechDraw_3PtAngleDimension.svg  style="width:32px;"> [Wymiaruj kąt na podstawie 3 punktów](TechDraw_3PtAngleDimension/pl.md): dodaje wymiar kąta na podstawie trzech podanych punktów.

-   <img alt="" src=images/TechDraw_HorizontalExtentDimension.svg  style="width:32px;"> [Zakres poziomy](TechDraw_HorizontalExtentDimension/pl.md): dodaje wymiar poziomy. {{Version/pl|0.19}}

-   <img alt="" src=images/TechDraw_VerticalExtentDimension.svg  style="width:32px;"> [Zakres pionowy](TechDraw_VerticalExtentDimension/pl.md): dodaje wymiar pionowy {{Version/pl|0.19}}

-   <img alt="" src=images/TechDraw_LinkDimension.svg  style="width:32px;"> [Powiąż wymiar z geometrią 3D](TechDraw_LinkDimension/pl.md): umożliwia połączenie istniejącego wymiaru z geometrią 3D.

-   <img alt="" src=images/TechDraw_Balloon.svg  style="width:32px;"> [Wstaw adnotację w formie dymka](TechDraw_Balloon/pl.md): dodaje na stronie adnotację w *baloniku*. {{Version/pl|0.19}}

-   <img alt="" src=images/TechDraw_Dimension_Landmark.svg  style="width:32px;"> [Wstaw wymiar przestrzenny](TechDraw_Dimension_Landmark/pl.md): dodaje wymiar dystansu. {{Version/pl|0.19}}


<div class="mw-translate-fuzzy">

## Pakiet rozszerzeń 


</div>


<div class="mw-translate-fuzzy">

Pakiet rozszerzeń zawiera wiele przydatnych narzędzi do ulepszenia Twoich rysunków technicznych.


</div>


<div class="mw-translate-fuzzy">


**Niektóre z tych narzędzi nie zostały jeszcze wydane.**


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ExtensionCircleCenterLines.svg  style="width:32px;"> [Oś otworu](TechDraw_ExtensionCircleCenterLines/pl.md): dodaje linie środkowe do okręgów i łuków. {{Version/pl|0.20}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ExtensionThreadHoleSide.svg  style="width:32px;"> [Oś otworu, widok z boku](TechDraw_ExtensionThreadHoleSide/pl.md): dodaje symboliczną linię do bocznego widoku otworu. {{Version/pl|0.20}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ExtensionThreadBoltSide.svg  style="width:32px;"> [Symbol gwintu, widoku boczny śruby](TechDraw_ExtensionThreadBoltSide/pl.md): dodaje symbole gwintu do widoku bocznego śruby. {{Version/pl|0.20}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ExtensionThreadHoleBottom.svg  style="width:32px;"> [Otwór gwintowany, widok od dołu](TechDraw_ExtensionThreadHoleBottom.md): dodaje symboliczny gwint do widoku otworów od dołu. {{Version/pl|0.20}}


</div>


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/TechDraw_ExtensionThreadBoltBottom.svg  style="width:32px;"> [Symbol gwintu, widoku śruby od od dołu](TechDraw_ExtensionThreadBoltBottom/pl.md): dodaje symbol gwintu do widoku śruby od dołu. {{Version/pl|0.20}}


</div>


<div class="mw-translate-fuzzy">

## Import/Eksport


</div>

Są to narzędzia do eksportu zawartości stron do innych programów.

-   <img alt="" src=images/TechDraw_ExportPageSVG.svg  style="width:32px;"> _.

-   <img alt="" src=images/TechDraw_ExportPageDXF.svg  style="width:32px;"> _.

## Wystrój

Są to narzędzia do modyfikowania wyglądu stron lub widoków.

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width:32px;"> [Kreskowanie powierzchni \...](TechDraw_Hatch/pl.md): nakłada wzór kreskowania z pliku na ścianę.

-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:32px;"> [Geometryczne kreskowanie \...](TechDraw_GeometricHatch/pl.md): stosuje wzór kreskowania na powierzchni przy użyciu specyfikacji Autodesk PAT.

-   <img alt="" src=images/TechDraw_Symbol.svg  style="width:32px;"> _.

-   <img alt="" src=images/TechDraw_Image.svg  style="width:32px;"> _ do zawartości strony.

-   <img alt="" src=images/TechDraw_ToggleFrame.svg  style="width:32px;"> [Przełącz widoczność ramki](TechDraw_ToggleFrame/pl.md): włącza i wyłącza ramki oraz etykiety otaczające widok.

## Adnotacje

Narzędzia do nanoszenia adnotacji służą do \" oznaczania \" rysunku dodatkowymi informacjami.

-   <img alt="" src=images/TechDraw_Annotation.svg  style="width:32px;"> [Dodaj Adnotację](TechDraw_Annotation/pl.md): dodaje zwykły blok tekstowy, który służy jako adnotacja.

-   <img alt="" src=images/TechDraw_LeaderLine.svg  style="width:32px;"> [Dodaj linię odniesienia](TechDraw_LeaderLine/pl.md): narzędzie dodaje linię odniesienia do wyświetlanego widoku. {{Version/pl|0.19}}

-   <img alt="" src=images/TechDraw_RichTextAnnotation.svg  style="width:32px;"> _ lub widoku. {{Version/pl|0.19}}

-   <img alt="" src=images/TechDraw_CosmeticVertex.svg  style="width:32px;"> [Wstaw wierzchołek kosmetyczny](TechDraw_CosmeticVertex/pl.md): Narzędzie dodaje wierzchołek, który nie jest częścią geometrii źródłowej. {{Version/pl|0.19}}

-   <img alt="" src=images/TechDraw_Midpoints.svg  style="width:32px;"> [Dodaj wierzchołki punktu środkowego](TechDraw_Midpoints/pl.md): Narzędzie Punkty środkowe dodaje Punkty pomocnicze w punktach środkowych jednej lub kilku wybranych krawędzi. {{Version/pl|0.19}}

-   <img alt="" src=images/TechDraw_Quadrants.svg  style="width:32px;"> [Dodaj wierzchołki kwadrantu](TechDraw_Quadrants/pl.md): Narzędzie Kwadrant dodaje wierzchołki pomocnicze w punktach ćwiartki jednej lub więcej wybranych krawędzi *(okrągłych)*. {{Version/pl|0.19}}

-   <img alt="" src=images/TechDraw_FaceCenterLine.svg  style="width:32px;"> [Dodaj oś ściany](TechDraw_FaceCenterLine/pl.md): Narzędzie Oś ściany dodaje linię środkową do wybranej ściany *(ścian)*. {{Version/pl|0.19}}

-   <img alt="" src=images/TechDraw_2LineCenterLine.svg  style="width:32px;"> [Dodaj oś dwóch krawędzi](TechDraw_2LineCenterLine/pl.md): Narzędzie Oś dwóch krawędzi dodaje linię środkową pomiędzy dwoma krawędziami. {{Version/pl|0.19}}

-   <img alt="" src=images/TechDraw_2PointCenterLine.svg  style="width:32px;"> [Dodaj oś dwóch punktów](TechDraw_2PointCenterLine/pl.md): Narzędzie Oś dwóch punktów dodaje linię środkową pomiędzy 2 punktami. {{Version/pl|0.19}}

-   <img alt="" src=images/TechDraw_2PointCosmeticLine.svg  style="width:32px;"> [Dodaj linię kosmetyczną \...](TechDraw_2PointCosmeticLine/pl.md): dodaje linię estetyczną łączącą 2 wierzchołki. {{Version/pl|0.19}}

-   <img alt="" src=images/TechDraw_CosmeticEraser.svg  style="width:32px;"> [Usuń obiekt kosmetyczny](TechDraw_CosmeticEraser/pl.md): Narzędzie to usuwa obiekty kosmetyczne z danej strony. {{Version/pl|0.19}}

-   <img alt="" src=images/TechDraw_DecorateLine.svg  style="width:24px;"> [Zmień wygląd wybranych linii](TechDraw_DecorateLine/pl.md): Narzędzie to zmienia wygląd krawędzi. {{Version/pl|0.19}}

-   <img alt="" src=images/TechDraw_ShowAll.svg  style="width:32px;"> [Pokaż / ukryj niewidoczne krawędzie](TechDraw_ShowAll/pl.md): Narzędzie pokazuje / ukrywa niewidoczne krawędzie lub linie w widoku. {{Version/pl|0.19}}

-   <img alt="" src=images/TechDraw_WeldSymbol.svg  style="width:32px;"> [Dodaj informacje spawalnicze](TechDraw_WeldSymbol/pl.md): Narzędzie dodaje specyfikacje dotyczące spawania do istniejącej linii odniesienia. {{Version/pl|0.19}}

## Dodatkowe właściwości 

-   [Grupy linii](TechDraw_LineGroup/pl.md): domyślne wagi można przypisać do różnych typów linii.
-   [Szablony](TechDraw_Templates/pl.md): domyślne szablony zdefiniowane dla stron rysunku.
-   [Wypełnienie kreskowaniem](TechDraw_Hatching/pl.md): objaśnienie różnych technik kreskowania.

[Wymiarowanie geometrii i tolerancja](TechDraw_Geometric_dimensioning_and_tolerancing/pl.md): wyjaśnienie, jak osiągnąć wymiarowanie geometrii i tolerancji.

## Ustawienia

-   <img alt="" src=images/Preferences-techdraw.svg  style="width:32px;"> [Ustawienia](TechDraw_Preferences/pl.md): ustawienia domyślnych wartości strony rysunku, takich jak kąt projekcji, kolory, rozmiary tekstu i style linii.

## Tworzenie skryptów 

Narzędzi środowiska Rysunek Techniczny można używać w [makrodefinicjach](Macros/pl.md) oraz w konsoli [Python](Python/pl.md) przy użyciu dwóch interfejsów API.

-   [TechDraw API](TechDraw_API/pl.md)
-   [TechDrawGui API](TechDrawGui_API/pl.md)

## Ograniczenia

-   Rysunki środowiska Rysunek Techniczny i jego API nie są zamienne ze środowiskiem [Kreślenie](Drawing_Workbench/pl.md) i jego API. Możliwa jest konwersja Strony Kreślenie do Strony Rysunku Technicznego przy użyciu skryptu Pythona (`moveViews.py`).
-   Możliwe jest posiadanie zarówno Strony środowiska Rysunku Technicznego jak i Kreślenie w tym samym dokumencie FreeCAD, ponieważ każda strona jest całkowicie niezależna od siebie.
-   Istnieją niewielkie różnice w określaniu edytowalnych tekstów w szablonach [SVG](SVG.md) w porównaniu z modułem Kreślenie. W Rysunku Technicznym skalowanie dokumentu SVG wpływa na położenie edytowalnych pól tekstowych. Więcej szczegółów znajdziesz w dyskusji na forum [TechDraw templates scale](https://forum.freecadweb.org/viewtopic.php?f=3&t=24981&p=196271#p196271).
-   Nie wycinaj, nie kopiuj i nie wklejaj obiektów Rysunku Technicznego w widoku drzewa, ponieważ generalnie nie działa to dobrze.

## Poradniki


<div class="mw-translate-fuzzy">

-   [Poradnik: Podstawy dla Środowiska pracy Rysunek Techniczny](Basic_TechDraw_Tutorial/pl.md): wprowadzenie do tworzenia rysunków przy użyciu środowiska pracy TechDraw.
-   [Rysunek Techniczny: Jak wykonać nowy szablon ramki](TechDraw_TemplateHowTo/pl.md): instrukcja tworzenia nowego szablonu strony w programie Inkscape do użycia w środowisku pracy Rysunek Techniczny.
-   [Pomiar kątów na otworach](Measurement_Of_Angles_On_Holes/pl.md): instrukcje dotyczące dodawania linii centrujących i kolejnych oznaczeń kątowych na otworach.
-   [Rozmaitości](TechDraw_HowTo_Page/pl.md): instrukcje dotyczące różnych ustawień, takich jak znaki środka, itp.
-   [Tworzenie koła podziałowego](TechDraw_pitch_circle_tutorial/pl.md): instrukcja dodawania koła podziałowego.


</div>

Wideo poradniki przygotowane przez użytkownika sliptonic

-   Środowisko pracy Rysunek Techniczny [Część 1 *(Podstawy)*](https://www.youtube.com/watch?v=7LbOmSGW9F0), [Część 2 *(Wymiary)*](https://www.youtube.com/watch?v=z3w84RfvqaE), [Część 3 *(Wiele widoków)*](https://www.youtube.com/watch?v=uNjXg-m38aI).
-   Środowisko pracy Rysunek Techniczny [Part 4 *(Przekrój i detal)*](https://www.youtube.com/watch?v=3zSdeFV6I5o), [Part 5 *(Dostosowanie szablonu)*](https://www.youtube.com/watch?v=kcmdJ7xa7gg).





{{TechDraw Tools navi

}} 

_

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > TechDraw Workbench/pl
