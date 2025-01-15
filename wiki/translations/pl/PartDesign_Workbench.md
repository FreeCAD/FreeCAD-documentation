# <img alt="Ikonka FreeCAD dla środowiska pracy Projekt Części" src=images/Workbench_PartDesign.svg  style="width:64px;"> PartDesign Workbench/pl






## Wprowadzenie

Środowisko pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> **Projekt Części** zapewnia zaawansowane narzędzia do modelowania komponentów bryłowych. Koncentruje się głównie na tworzeniu komponentów mechanicznych, które mogą być wytwarzane i składane w gotowy produkt. Niemniej jednak, utworzone bryły mogą być wykorzystywane do innych celów, takich jak: [projekt BIM](BIM_Workbench/pl.md), [analiza MES](FEM_Workbench/pl.md) lub [obróbka CNC i druk 3D](Path_Workbench/pl.md).

Środowisko pracy Projekt Części korzysta z podejścia opartego o cechy. Komponent jest reprezentowany przez kontener Zawartość. Definiuje on lokalny układ współrzędnych i zawiera kumulatywne cechy, które definiują komponent. Cechy są w większości oparte o parametryczne szkice i mogą być addytywne (dodające materiał) lub subtraktywne (odejmujące materiał). Przykładowo narzędzie [Wyciągnij](PartDesign_Pad/pl.md) dodaje wyciągany szkic do tworzonej bryły zaś narzędzie [Kieszeń](PartDesign_Pocket/pl.md) odejmuje wyciągany szkic. Każda cecha jest kumulatywna i budowana na wyniku poprzednich cech. Możliwe jest też używanie prymitywów ([Walec](PartDesign_AdditiveCylinder/pl.md), [Sfera](PartDesign_AdditiveSphere/pl.md) itd.) jak i brył tworzonych poza Zawartością jako cechy.

Zobacz stronę [Edycja cech](Feature_editing/pl.md) aby znaleźć bardziej kompletne wyjaśnienie tego procesu a następnie zobacz stronę [Projekt Części: tworzenie podstawowych brył](Creating_a_simple_part_with_PartDesign/pl.md) aby rozpocząć pracę z tworzeniem brył.

Środowisko pracy <img alt="" src=images/Workbench_Part.svg  style="width:16px;"> [Część](Part_Workbench/pl.md) zapewnia alternatywne podejście oparte o metologię [constructive solid geometry](constructive_solid_geometry/pl.md) (CSG) do tworzenia kształtów. Szczegółowe porównanie środowisk pracy Część i Projekt Części można znaleźć na stronie [Część i Projekt Części](Part_and_PartDesign/pl.md).

![](images/PartDesign_Workbench_Example.jpg )



## Przybory

Narzędzia Part Design znajdują się w menu **Part Design** oraz na pasku narzędzi *PartDesign*, który pojawia się po załadowaniu Środowiska pracy Part Design.



### Narzędzia pomocnicze 

-   <img alt="" src=images/PartDesign_Body.svg  style="width:32px;"> [Stwórz nową zawartość \...](PartDesign_Body/pl.md): Tworzy obiekt [Body](Body.md) w aktywnym dokumencie i czyni go aktywnym.

-   <img alt="" src=images/PartDesign_NewSketch.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Utwórz szkic:

  -<img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [Utwórz szkic](PartDesign_NewSketch/pl.md): tworzy nowy szkic na wybranej ścianie lub płaszczyźnie. Jeśli podczas uruchamiania tego narzędzia nie zostanie wybrana żadna ściana, użytkownik zostanie poproszony o wybranie płaszczyzny z panelu zadań. Następnie interfejs przełącza się na Środowisko pracy [Szkicownik](Sketcher_Workbench/pl.md) w trybie edycji szkicu.

  - <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [Mapuj szkic na powierzchnię](Sketcher_MapSketch/pl.md): dołącza szkic do geometrii wybranej z aktywnej bryły.

  - <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [Edycja wybranego szkicu](Sketcher_EditSketch/pl.md): Otwiera wybrany szkic do edycji.

-   <img alt="" src=images/Sketcher_ValidateSketch.svg  style="width:32px;"> [Sprawdź poprawność szkicu](Sketcher_ValidateSketch/pl.md): Sprawdza odchylenia różnych punktów i dopasowuje je.

-   <img alt="" src=images/Part_CheckGeometry.svg  style="width:32px;"> [Sprawdź geometrię](Part_CheckGeometry/pl.md): sprawdza geometrię wybranych obiektów pod kątem błędów.

-   <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:32px;"> [Utwórz łącznik kształtu](PartDesign_ShapeBinder/pl.md): tworzy łącznik kształtu odwołujący się do geometrii z jednego obiektu nadrzędnego.

-   <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:32px;"> [Utwórz łącznik kształtów podrzędnych](PartDesign_SubShapeBinder/pl.md): tworzy łącznik kształtu odwołujący się do geometrii z jednego lub więcej obiektów nadrzędnych.

-   <img alt="" src=images/PartDesign_Clone.svg  style="width:32px;"> [Stwórz nowego klona](PartDesign_Clone.md): tworzy klon wybranej bryły.

-   <img alt="" src=images/PartDesign_Plane.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Utwórz punkt odniesienia (

  -<img alt="" src=images/PartDesign_Plane.svg  style="width:32px;"> [Utwórz nową płaszczyznę odniesienia](PartDesign_Plane.md): tworzy płaszczyznę odniesienia w aktywnej części bryły. ({{VersionMinus/pl|1.0}})

  -<img alt="" src=images/PartDesign_Line.svg  style="width:32px;"> [Utwórz nowa linię odniesienia](PartDesign_Line.md): tworzy linię odniesienia w aktywnej części bryły. ({{VersionMinus/pl|1.0}})

  -<img alt="" src=images/PartDesign_Point.svg  style="width:32px;"> [Utwórz nowy punkt odniesienia](PartDesign_Point.md): tworzy punkt odniesienia w aktywnej części bryły. ({{VersionMinus/pl|1.0}})

  -<img alt="" src=images/PartDesign_CoordinateSystem.svg  style="width:32px;"> [Utwórz lokalny system współrzędnych](PartDesign_CoordinateSystem.md): tworzy lokalny układ odniesienia połączony z geometrią punktu odniesienia w aktywnej bryle. ({{VersionMinus/pl|1.0}})

:   
    {{Version/pl|1.1}}: te narzędzia zostały zastąpione nowymi [narzędziami do geometrii pomocniczych](Std_Base/pl#Part_Datums.md).



### Narzędzia modelujące 



#### Narzędzia dodawania nowych elementów 

Są to narzędzia do tworzenia elementów bazowych lub dodawania materiałów do istniejącej bryły.

-   <img alt="" src=images/PartDesign_Pad.png  style="width:32px;"> [Wyciągnij wybrany szkic](PartDesign_Pad.md): wybrany szkic wyciąga do bryły.

-   <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [Wyciągnij przez obrót \...](PartDesign_Revolution.md): tworzy bryłę, obracając szkic wokół osi. Szkic musi tworzyć profil zamknięty.

-   <img alt="" src=images/PartDesign_AdditiveLoft.svg  style="width:32px;"> [Lofuj wybrany profil \...](PartDesign_AdditiveLoft.md): tworzy bryłę, dokonując połączenia między dwoma lub więcej szkicami.

-   <img alt="" src=images/PartDesign_AdditivePipe.svg  style="width:32px;"> [Rozciągnij wybrany rysunek wzdłuż ścieżki \...](PartDesign_AdditivePipe.md): tworzy bryłę poprzez przeciągnięcie jednego lub więcej szkiców wzdłuż otwartej lub zamkniętej ścieżki.

-   <img alt="" src=images/PartDesign_AdditiveHelix.svg  style="width:32px;"> [Addytywna helisa](PartDesign_AdditiveHelix/pl.md): tworzy bryłę poprzez przeciągnięcie szkicu wzdłuż helisy.

-   <img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Utwórz bryłę pierwotną do dodania:

  -<img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:32px;"> [Addytywny sześcian](PartDesign_AdditiveBox.md): dodaje do aktywnej bryły dodatek w postaci kostki.

  -<img alt="" src=images/PartDesign_AdditiveCylinder.svg  style="width:32px;"> [Addytywny walec](PartDesign_AdditiveCylinder.md): dodaje do aktywnej bryły dodatek w postaci walca.

  -<img alt="" src=images/PartDesign_AdditiveSphere.svg  style="width:32px;"> [Addytywna sfera](PartDesign_AdditiveSphere.md): dodaje do aktywnej bryły dodatek w postaci sfery.

  -<img alt="" src=images/PartDesign_AdditiveCone.svg  style="width:32px;"> [Addytywny stożek](PartDesign_AdditiveCone.md): dodaje do aktywnej bryły dodatek w postaci stożka.

  -<img alt="" src=images/PartDesign_AdditiveEllipsoid.svg  style="width:32px;"> [Addytywna elipsoida](PartDesign_AdditiveEllipsoid.md): dodaje do aktywnej bryły dodatek w postaci elipsoidy obrotowej.

  -<img alt="" src=images/PartDesign_AdditiveTorus.svg  style="width:32px;"> [Addytywny torus](PartDesign_AdditiveTorus.md): dodaje do aktywnej bryły dodatek w postaci torusa.

  -<img alt="" src=images/PartDesign_AdditivePrism.svg  style="width:32px;"> [Addtytwny graniastosłup](PartDesign_AdditivePrism.md): dodaje do aktywnej bryły dodatek w postaci graniastosłupa.

  -<img alt="" src=images/PartDesign_AdditiveWedge.svg  style="width:32px;"> [Addytywny klin](PartDesign_AdditiveWedge.md): dodaje do aktywnej bryły dodatek w postaci klina.



#### Narzędzia do usuwania kształtów 

Są to narzędzia do odejmowania materiału z istniejącej bryły.

-   <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [Utwórz kieszeń \...](PartDesign_Pocket.md): tworzy kieszeń z wybranego szkicu.

-   <img alt="" src=images/PartDesign_Hole.svg  style="width:32px;"> [Utwórz otwór \...](PartDesign_Hole.md): tworzy element otworu z wybranego szkicu. Szkic musi zawierać jeden lub kilka okręgów.

-   <img alt="" src=images/PartDesign_Groove.svg  style="width:32px;"> [Wytnij rowek](PartDesign_Groove.md): tworzy rowek, obracając szkic wokół osi.

-   <img alt="" src=images/PartDesign_Subtractive_Loft.svg  style="width:32px;"> [Odejmij wybrany profil\...](PartDesign_SubtractiveLoft.md): tworzy bryłę poprzez przejście pomiędzy dwoma lub więcej szkicami i odejmuje ją od aktywnego kształtu.

-   <img alt="" src=images/PartDesign_SubtractivePipe.svg  style="width:32px;"> [Rozciągnij wybrany szkic \... i usuń z zawartości](PartDesign_SubtractivePipe.md): tworzy bryłę poprzez przesuwanie jednego lub więcej szkiców wzdłuż otwartej lub zamkniętej ścieżki i odejmuje je od aktywowanego kształtu.

-   <img alt="" src=images/PartDesign_SubtractiveHelix.svg  style="width:32px;"> [Subtraktywna helisa](PartDesign_SubtractiveHelix/pl.md): tworzy bryłę przez przeciągnięcie szkicu wzdłuż helisy i odejmuje ją od aktywnej bryły.

-   <img alt="" src=images/PartDesign_SubtractiveBox.svg  style="width:" height="32px;"><img alt="" src=images/Toolbar_flyout_arrow_blue_background.svg  style="width:" height="32px;"> Utwórz bryłę pierwotną do odjęcia:

  -<img alt="" src=images/PartDesign_Subtractive_Box.svg  style="width:32px;"> [Subtraktywny sześcian](PartDesign_SubtractiveBox.md): dodaje do aktywnej bryły ubytek w kształcie kostki.

  -<img alt="" src=images/PartDesign_SubtractiveCylinder.svg  style="width:32px;"> [Subtraktywny walec](PartDesign_SubtractiveCylinder.md): dodaje do aktywnej bryły ubytek w kształcie walca.

  -<img alt="" src=images/PartDesign_SubtractiveSphere.svg  style="width:32px;"> [Subtraktywna sfera](PartDesign_SubtractiveSphere.md): dodaje do aktywnej bryły ubytek w kształcie sfery.

  -<img alt="" src=images/PartDesign_Subtractive_Cone.svg  style="width:32px;"> [Subtraktywny stożek](PartDesign_SubtractiveCone.md): dodaje do aktywnej bryły ubytek w kształcie stożka.

  -<img alt="" src=images/PartDesign_Subtractive_Ellipsoid.svg  style="width:32px;"> [Subtraktywna ellipsoida](PartDesign_SubtractiveEllipsoid.md): dodaje do aktywnej bryły ubytek w kształcie elipsoidy.

  -<img alt="" src=images/PartDesign_SubtractiveTorus.svg  style="width:32px;"> [Subtraktywny torus](PartDesign_SubtractiveTorus.md): dodaje do aktywnej bryły ubytek w kształcie torusa.

  -<img alt="" src=images/PartDesign_SubtractivePrism.svg  style="width:32px;"> [Subtraktywny graniastosłup](PartDesign_SubtractivePrism.md): dodaje do aktywnej bryły ubytek w kształcie graniastosłupa.

  -<img alt="" src=images/PartDesign_SubtractiveWedge.svg  style="width:32px;"> ‎[Subtraktywny klin](PartDesign_SubtractiveWedge.md): dodaje do aktywnej bryły ubytek w kształcie klina.



#### Narzędzia do przeprowadzania operacji logicznych 

-   <img alt="" src=images/PartDesign_Boolean.svg  style="width:32px;"> [Operacje logiczne](PartDesign_Boolean.md): importuje jedną lub więcej brył lub klonów PartDesign do aktywnego elementu i przeprowadza operację logiczną.



### Narzędzia do wykańczania 

Narzędzia te umożliwiają wykonanie określonej modyfikacji krawędzi lub powierzchni.

\_\*<img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> [Utwórz zaokrąglenie na krawędzi](PartDesign_Fillet.md): tworzy zaokrąglenia na określonych krawędziach wybranego kształtu.

-   <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> [Fazuj wybrane krawędzie \...](PartDesign_Chamfer.md): tworzy fazy na wybranych krawędziach aktywnej bryły.

-   <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> [Utwórz szkic na obszarze](PartDesign_Draft.md): na wybrane powierzchnie aktywnej bryły stosuje szkic pod odpowiednim kątem.

-   <img alt="" src=images/PartDesign_Thickness.svg  style="width:32px;"> [Utwórz bryłę narzędziem grubość](PartDesign_Thickness.md): tworzy grubą powłokę z aktywnej bryły i powoduje otwarcie wybranych ścian.



### Narzędzia do przekształcania 

Są to narzędzia służące do przekształcania istniejących właściwości.

-   <img alt="" src=images/PartDesign_Mirrored.svg  style="width:32px;"> [Utwórz kopie lustrzaną](PartDesign_Mirrored.md): jest lustrzanym odbiciem jednej lub kilku cech.

-   <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [Utwórz szyk liniowy](PartDesign_LinearPattern.md): tworzy wzór liniowy oparty na jednej lub kilku właściwościach.

-   <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> [Utwórz szyk kołowy](PartDesign_PolarPattern.md): tworzy układ kołowy złożony z jednej lub więcej właściwości.

-   <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:32px;"> [Utwórz szyk kołowy](PartDesign_MultiTransform.md): tworzy układ kołowy złożony z jednej lub więcej właściwości, wspomniane powyżej, a także przekształcenie [Skali](PartDesign_Scaled/pl.md).
    -   <img alt="" src=images/PartDesign_Scaled.svg  style="width:32px;"> [Skaluj](PartDesign_Scaled/pl.md): skaluje jedną lub więcej funkcji. Funkcja nie jest dostępna jako osobne narzędzie do transformacji.



#### Dodatki

Kilka dodatkowych funkcji, które można znaleźć w menu Part Design:

-   <img alt="" src=images/PartDesign_Sprocket.svg  style="width:32px;"> [Kreator projektowania kół łańcuchowych](PartDesign_Sprocket/pl.md): tworzy profil koła zębatego, który może być użyty do wyciągnięcia.

-   <img alt="" src=images/PartDesign_InvoluteGear.svg  style="width:32px;"> [Koło zębate ewolwentowe](PartDesign_InvoluteGear/pl.md): tworzy profil koła zębatego, który może być użyty do wyciągnięcia.

-   <img alt="" src=images/PartDesign_WizardShaft.svg  style="width:32px;"> [Twórca wałów](PartDesign_WizardShaft.md): tworzy wał z tabeli wartości i pozwala na analizę sił i momentów. Wał jest tworzony za pomocą szkicu obrotowego, który można edytować.



### Pozycje w menu kontekstowym 

-   [Wygaszony](PartDesign_Suppressed/pl.md): pole, którego zaznaczenie wyłącza daną cechę bez usuwania jej. {{Version/pl|1.0}}

-   <img alt="" src=images/_PartDesign_MoveTip.svg  style="width:32px;"> [Ustaw czubek](PartDesign_MoveTip.md): pozwala na przedefiniowanie czubka, który jest elementem eksponowanym na zewnątrz korpusu.

-   <img alt="" src=images/PartDesign_MoveFeature.svg  style="width:32px;"> [Przenieś obiekt do innej zawartości](PartDesign_MoveFeature.md): przenosi wybrany szkic, geometrię odniesienia lub element do innej zawartości

-   <img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width:32px;"> [Przenieś obiekt za innym obiektem](PartDesign_MoveFeatureInTree.md): umożliwia zmianę kolejności obiektów drzewa zawartości poprzez przeniesienie wybranego szkicu, geometrii odniesienia lub elementu w inne miejsce na liście elementów.



#### Pozycje współdzielone ze Środowiskiem pracy Part 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Wygląd zewnętrzny](Std_SetAppearance.md): określa wygląd całej części *(przezroczystość kolor itp.)*.

-   <img alt="" src=images/Part_ColorPerFace.svg  style="width:32px;"> [Ustaw kolor ściany](Part_ColorPerFace.md): Przypisuje kolory do poszczególnych powierzchni obiektów.



### Narzędzia przestarzałe 

-   <img alt="" src=images/PartDesign_Migrate.svg  style="width:32px;"> [Przenieś ze starszej wersji](PartDesign_Migrate/pl.md): przenosi pliki z wersji programu FreeCAD poniżej 0.17 do wersji 0.17. To narzędzie nie jest dostępne w {{VersionPlus/pl|1.0}}.



## Ustawienia

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Ustawienia](PartDesign_Preferences/pl.md): opcje dostępne w Narzędziach PartDesign.
-   [Dostrajanie parametrów](Fine-tuning/pl.md): kilka dodatkowych parametrów, aby dopracować zachowanie PartDesign.



## Poradniki

-   [How to use FreeCAD](http://help-freecad-jpg87.fr/), strona internetowa opisująca przebieg pracy w zakresie projektowania mechanicznego.
-   [Projekt części: tworzenie podstawowych brył](Creating_a_simple_part_with_PartDesign/pl.md).
-   [Podstawy dla Środowiska pracy Projekt Części 019](Basic_Part_Design_Tutorial_019/pl.md).
-   [Poradnik: Projekt części uchwyt łożyska I](PartDesign_Bearingholder_Tutorial_I/pl.md) *(wymaga aktualizacji)*.
-   [Poradnik: Projekt części uchwyt łożyska II](PartDesign_Bearingholder_Tutorial_II/pl.md) *(wymaga aktualizacji)*.



## Przykłady

Aby uzyskać kilka pomysłów na to, co można osiągnąć za pomocą narzędzi środowiska Projekt Części, zajrzyj do: [przykładów](PartDesign_Examples/pl.md).

<img alt="" src=images/PartDesign_ExampleSphere-02.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleTorus-01.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExamplePad-09.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSweep-02.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSweep-05.png  style="width:80px;"> <img alt="" src=images/PartDesign_ExampleSpring-04.png  style="width:80px;">



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > [PartDesign](Category_PartDesign.md) > PartDesign Workbench/pl
