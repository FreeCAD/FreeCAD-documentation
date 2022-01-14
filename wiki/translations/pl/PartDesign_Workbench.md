# <img alt="Ikonka FreeCAD dla Środowiska pracy PartDesign" src=images/Workbench_PartDesign.svg  style="width:64px;"> PartDesign Workbench/pl


{{TOCright}}

## Wprowadzenie

<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;">[PartDesign](PartDesign_Workbench/pl.md) oferuje zaawansowane narzędzia do modelowania złożonych części brył. Głównie skupia się on na tworzeniu części mechanicznych, które mogą być produkowane i montowane w gotowy produkt. Niemniej jednak, utworzone bryły mogą być wykorzystywane ogólnie do wszelkich innych celów, takich jak [projekt architektoniczny](Arch_Workbench/pl.md), [analiza elementów skończonych](FEM_Workbench/pl.md) lub [obróbka CNC i drukowanie 3D](Path_Workbench/pl.md).

Środowisko pracy Projekt Części jest nierozerwalnie związane ze środowiskiem pracy [Szkicownik](Sketcher_Workbench/pl.md). Użytkownik zazwyczaj tworzy szkic, następnie używa narzędzia [Wyciągnij](PartDesign_Pad/pl.md), aby go wytłoczyć i utworzyć bryłę podstawową, a następnie modyfikuje tę bryłę.

Podczas gdy środowisko <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> [Część](Part_Workbench/pl.md) opiera się na [konstruktywnej geometrii bryły](constructive_solid_geometry/pl.md) *(CSG)* dla budowania kształtów, Projekt Części wykorzystuje metodę edycji parametrów i funkcji, co oznacza, że bryła podstawowa jest kolejno przekształcana przez dodanie elementów na górze, aż do uzyskania ostatecznego kształtu. Zobacz stronę [funkcje edycji](Feature_editing/pl.md), aby uzyskać pełniejsze wyjaśnienie tego procesu, a następnie zobacz [Tworzenie prostej części w środowisku Projekt Części](Creating_a_simple_part_with_PartDesign/pl.md), aby rozpocząć tworzenie brył.

Bardziej szczegółowa dyskusja na temat środowisk Part kontra Part Design znajduje się tutaj: [Część i Projekt części](Part_and_PartDesign/pl.md).

Korpusy utworzone w PartDesign często podlegają [problemom nazewnictwa według kolejności chronologicznej](topological_naming_problem.md), co powoduje zmianę nazw wewnętrznych cech podczas modyfikacji operacji parametrycznych. Problem ten można zminimalizować stosując najlepsze praktyki opisane na stronie [edycja funkcji](feature_editing.md) oraz wykorzystując obiekty odniesienia jako wsparcie dla szkiców i funkcji.

<img alt="" src=images/PartDesign_Example.png  style="width:500px;">

## Przybory

Narzędzia Part Design znajdują się w menu **Part Design** oraz na pasku narzędzi *PartDesign*, który pojawia się po załadowaniu Środowiska pracy Part Design.

### Narzędzia organizujące strukturę dokumentu 

Są to narzędzia, które nie są częścią Środowiska pracy **PartDesign**. Należą one do systemu [Std Base](Std_Base/pl.md). Zostały one opracowane w wersji **0.17** z zamiarem zorganizowania modelu i utworzenia [złożeń](Assembly.md). Jako takie, są bardzo przydatne przy pracy z bryłami stworzonymi przy pomocy tego stołu roboczego.

-   <img alt="" src=images/Std_Part.svg  style="width:32px;"> [Stwórz nową część \...](Std_Part/pl.md): dodaje kolejną pozycję części na drzewku do aktywnego dokumentu i czyni ją aktywną.

-   <img alt="" src=images/Std_Group.svg  style="width:32px;"> [Utwórz nową grupę \...](Std_Group.md): dodaje do aktywnego dokumentu pozycję grupy, co pozwala uporządkować obiekty w [widoku drzewa](Tree_view/pl.md).

### Narzędzia pomocnicze 

-   <img alt="" src=images/PartDesign_Body.svg  style="width:32px;"> [Stwórz nową zawartość \...](PartDesign_Body/pl.md): Tworzy obiekt [Body](Body.md) w aktywnym dokumencie i czyni go aktywnym.

-   <img alt="" src=images/Sketcher_NewSketch.svg  style="width:32px;"> [Utwórz nowy szkic](PartDesign_NewSketch.md): tworzy nowy szkic na wybranej ścianie lub płaszczyźnie. Jeśli podczas uruchamiania tego narzędzia nie zostanie wybrana żadna twarz, użytkownik zostanie poproszony o wybranie płaszczyzny z panelu Zadania. Następnie interfejs przełącza się na Środowisko pracy [Sketcher](Sketcher_Workbench/pl.md) w trybie edycji szkicu.

-   <img alt="" src=images/Sketcher_EditSketch.svg  style="width:32px;"> [Edycja wybranego szkicu](Sketcher_EditSketch.md): Uruchamia edycje szkicu wybranego na drzewku modelu.

-   <img alt="" src=images/Sketcher_MapSketch.svg  style="width:32px;"> [Mapuj szkic na powierzchnię](Sketcher_MapSketch/pl.md): Mapuje szkic do wcześniej wybranej płaszczyzny lub ściany aktywnej bryły.

### Narzędzia modelujące 

#### Narzędzia odniesienia 

-   <img alt="" src=images/PartDesign_Point.svg  style="width:32px;"> [Utwórz nowy punkt odniesienia](PartDesign_Point.md): tworzy punkt odniesienia w aktywnej części bryły. {{Version/pl|0.17}}

-   <img alt="" src=images/PartDesign_Line.svg  style="width:32px;"> [Utwórz nowa linię odniesienia](PartDesign_Line.md): tworzy linię odniesienia w aktywnej części bryły.

-   <img alt="" src=images/PartDesign_Plane.svg  style="width:32px;"> [Utwórz nową płaszczyznę odniesienia](PartDesign_Plane.md): tworzy płaszczyznę odniesienia w aktywnej części bryły.

-   <img alt="" src=images/PartDesign_CoordinateSystem.svg  style="width:32px;"> [Utwórz lokalny system współrzędnych](PartDesign_CoordinateSystem.md): tworzy lokalny układ odniesienia połączony z geometrią punktu odniesienia w aktywnej bryle.

-   <img alt="" src=images/PartDesign_ShapeBinder.svg  style="width:32px;"> [Utwórz spoiwo kształtu.](PartDesign_ShapeBinder.md): tworzy spoiwo kształtu w aktywnej bryle.

-   <img alt="" src=images/PartDesign_SubShapeBinder.svg  style="width:32px;"> [Utwórz spoiwo do elementu podrzędnego](PartDesign_SubShapeBinder.md): tworzy spoiwo kształtowe do elementu podrzędnego, jak krawędź lub powierzchnia z innej bryły, przy zachowaniu względnej pozycji tego elementu. {{Version/pl|0.19}}

-   <img alt="" src=images/PartDesign_Clone.svg  style="width:32px;"> [Stwórz nowego klona](PartDesign_Clone.md): tworzy klon wybranej bryły.

#### Narzędzia dodawania nowych elementów 

Są to narzędzia do tworzenia podstawowych właściwości lub dodawania materiału do istniejącej bryły.

-   <img alt="" src=images/PartDesign_Pad.png  style="width:32px;"> [Wyciągnij wybrany szkic](PartDesign_Pad.md): wybrany szkic wyciąga do bryły.

-   <img alt="" src=images/PartDesign_Revolution.svg  style="width:32px;"> [Wyciągnij przez obrót \...](PartDesign_Revolution.md): tworzy bryłę, obracając szkic wokół osi. Szkic musi tworzyć profil zamknięty.

-   <img alt="" src=images/PartDesign_Additive_Loft.svg  style="width:32px;"> [Lofuj wybrany profil \...](PartDesign_AdditiveLoft.md): tworzy bryłę, dokonując połączenia między dwoma lub więcej szkicami.

-   <img alt="" src=images/PartDesign_Additive_Pipe.svg  style="width:32px;"> [Rozciągnij wybrany rysunek wzdłuż ścieżki \...](PartDesign_AdditivePipe.md): tworzy bryłę poprzez przeciągnięcie jednego lub więcej szkiców wzdłuż otwartej lub zamkniętej ścieżki.

-   <img alt="" src=images/PartDesign_AdditiveHelix.svg  style="width:32px;"> [Addytywna helisa](PartDesign_AdditiveHelix.md): tworzy bryłę poprzez przeciągnięcie szkicu wzdłuż helisy. {{Version/pl|0.19}}

-   <img alt="" src=images/PartDesign_CompPrimitiveAdditive.png  style="width:48px;"> [Utwórz bryłę pierwotną do dodania](PartDesign_CompPrimitiveAdditive.md): dodaje do aktywnej bryły dodatek w postaci elementu pierwotnego.

:\*<img alt="" src=images/PartDesign_AdditiveBox.svg  style="width:32px;"> [Addytywny sześcian](PartDesign_AdditiveBox.md): dodaje do aktywnej bryły dodatek w postaci kostki.

:\*<img alt="" src=images/PartDesign_AdditiveCone.svg  style="width:32px;"> [Addytywny stożek](PartDesign_AdditiveCone.md): dodaje do aktywnej bryły dodatek w postaci stożka.

:\*<img alt="" src=images/PartDesign_AdditiveCylinder.svg  style="width:32px;"> [Addytywny walec](PartDesign_AdditiveCylinder.md): dodaje do aktywnej bryły dodatek w postaci walca.

:\*<img alt="" src=images/PartDesign_AdditiveEllipsoid.svg  style="width:32px;"> [Addytywna elipsoida](PartDesign_AdditiveEllipsoid.md): dodaje do aktywnej bryły dodatek w postaci elipsoidy obrotowej.

:\*<img alt="" src=images/PartDesign_AdditivePrism.svg  style="width:32px;"> [Addtytwny graniastosłup](PartDesign_AdditivePrism.md): dodaje do aktywnej bryły dodatek w postaci graniastosłupa.

:\*<img alt="" src=images/PartDesign_AdditiveSphere.svg  style="width:32px;"> [Addytywna sfera](PartDesign_AdditiveSphere.md): dodaje do aktywnej bryły dodatek w postaci sfery.

:\*<img alt="" src=images/PartDesign_AdditiveTorus.svg  style="width:32px;"> [Addytywny torus](PartDesign_AdditiveTorus.md): dodaje do aktywnej bryły dodatek w postaci torusa.

:\*<img alt="" src=images/PartDesign_AdditiveWedge.svg  style="width:32px;"> [Addytywny klin](PartDesign_AdditiveWedge.md): dodaje do aktywnej bryły dodatek w postaci klina.

#### Narzędzia do usuwania kształtów 

Są to narzędzia do odejmowania materiału z istniejącej bryły.

-   <img alt="" src=images/PartDesign_Pocket.svg  style="width:32px;"> [Utwórz kieszeń \...](PartDesign_Pocket.md): tworzy kieszeń z wybranego szkicu.

-   <img alt="" src=images/PartDesign_Hole.svg  style="width:32px;"> [Utwórz otwór \...](PartDesign_Hole.md): tworzy element otworu z wybranego szkicu. Szkic musi zawierać jeden lub kilka okręgów.

-   <img alt="" src=images/PartDesign_Groove.svg  style="width:32px;"> [Wytnij rowek](PartDesign_Groove.md): tworzy rowek, obracając szkic wokół osi.

-   <img alt="" src=images/PartDesign_Subtractive_Loft.svg  style="width:32px;"> [Odejmij wybrany profil\...](PartDesign_SubtractiveLoft.md): tworzy bryłę poprzez przejście pomiędzy dwoma lub więcej szkicami i odejmuje ją od aktywnego kształtu.

-   <img alt="" src=images/PartDesign_SubtractivePipe.svg  style="width:32px;"> [Rozciągnij wybrany szkic \... i usuń z zawartości](PartDesign_SubtractivePipe.md): tworzy bryłę poprzez przesuwanie jednego lub więcej szkiców wzdłuż otwartej lub zamkniętej ścieżki i odejmuje je od aktywowanego kształtu.

-   <img alt="" src=images/PartDesign_SubtractiveHelix.svg  style="width:32px;"> [Subtraktywna helisa](PartDesign_SubtractiveHelix.md): tworzy bryłę przez przeciągnięcie szkicu wzdłuż helisy i odejmuje ją od aktywnej bryły. <small>(v0.19)</small> 

-   <img alt="" src=images/PartDesign_CompPrimitiveSubtractive.png  style="width:48px;"> [Utwórz bryłę pierwotną do odjęcia](PartDesign_CompPrimitiveSubtractive.md): dodaje ubytek w kształcie elementu pierwotnego.

:\*<img alt="" src=images/PartDesign_Subtractive_Box.svg  style="width:32px;"> [Subtraktywny sześcian](PartDesign_SubtractiveBox.md): dodaje do aktywnej bryły ubytek w kształcie kostki.

:\*<img alt="" src=images/PartDesign_Subtractive_Cone.svg  style="width:32px;"> [Subtraktywny stożek](PartDesign_SubtractiveCone.md): dodaje do aktywnej bryły ubytek w kształcie stożka.

:\*<img alt="" src=images/PartDesign_SubtractiveCylinder.svg  style="width:32px;"> [Subtraktywny walec](PartDesign_SubtractiveCylinder.md): dodaje do aktywnej bryły ubytek w kształcie walca.

:\*<img alt="" src=images/PartDesign_Subtractive_Ellipsoid.svg  style="width:32px;"> [Subtraktywna ellipsoida](PartDesign_SubtractiveEllipsoid.md): dodaje do aktywnej bryły ubytek w kształcie elipsoidy.

:\*<img alt="" src=images/PartDesign_SubtractivePrism.svg  style="width:32px;"> [Subtraktywny graniastosłup](PartDesign_SubtractivePrism.md): dodaje do aktywnej bryły ubytek w kształcie graniastosłupa.

:\*<img alt="" src=images/PartDesign_SubtractiveSphere.svg  style="width:32px;"> [Subtraktywna sfera](PartDesign_SubtractiveSphere.md): dodaje do aktywnej bryły ubytek w kształcie sfery.

:\*<img alt="" src=images/PartDesign_SubtractiveTorus.svg  style="width:32px;"> [Subtraktywny torus](PartDesign_SubtractiveTorus.md): dodaje do aktywnej bryły ubytek w kształcie torusa.

:\*<img alt="" src=images/PartDesign_SubtractiveWedge.svg  style="width:32px;"> ‎[Subtraktywny klin](PartDesign_SubtractiveWedge.md): dodaje do aktywnej bryły ubytek w kształcie klina.

#### Narzędzia do przekształcania 

Są to narzędzia służące do przekształcania istniejących właściwości. Pozwalają one na wybór cech przeznaczonych do przeprowadzenia przekształceń.

-   <img alt="" src=images/PartDesign_Mirrored.svg  style="width:32px;"> [Utwórz kopie lustrzaną](PartDesign_Mirrored.md): jest lustrzanym odbiciem jednej lub kilku cech na płaszczyźnie lub ścianie.

-   <img alt="" src=images/PartDesign_LinearPattern.svg  style="width:32px;"> [Utwórz szyk liniowy](PartDesign_LinearPattern.md): tworzy wzór liniowy oparty na jednej lub kilku właściwościach.

-   <img alt="" src=images/PartDesign_PolarPattern.svg  style="width:32px;"> [Utwórz szyk kołowy](PartDesign_PolarPattern.md): tworzy układ kołowy złożony z jednej lub więcej właściwości.

-   <img alt="" src=images/PartDesign_MultiTransform.svg  style="width:32px;"> [Utwórz szyk kołowy](PartDesign_MultiTransform.md): tworzy układ kołowy złożony z jednej lub więcej właściwości.

#### Narzędzia do obróbki krawędzi 

Narzędzia te umożliwiają wykonanie określonej modyfikacji wybranych krawędzi lub powierzchni.

\_\*<img alt="" src=images/PartDesign_Fillet.svg  style="width:32px;"> [Utwórz zaokrąglenie na krawędzi](PartDesign_Fillet.md): tworzy zaokrąglenia na określonych krawędziach wybranego kształtu.

-   <img alt="" src=images/PartDesign_Chamfer.svg  style="width:32px;"> [Fazuj wybrane krawędzie \...](PartDesign_Chamfer.md): tworzy fazy na wybranych krawędziach aktywnej bryły.

-   <img alt="" src=images/PartDesign_Draft.svg  style="width:32px;"> [Utwórz szkic na obszarze](PartDesign_Draft.md): na wybrane powierzchnie aktywnej bryły stosuje szkic pod odpowiednim kątem.

-   <img alt="" src=images/PartDesign_Thickness.svg  style="width:32px;"> [Utwórz bryłę narzędziem grubość](PartDesign_Thickness.md): tworzy grubą powłokę z aktywnej bryły i powoduje otwarcie wybranych ścian.

#### Narzędzia do przeprowadzania operacji logicznych 

-   <img alt="" src=images/PartDesign_Boolean.svg  style="width:32px;"> [Operacje logiczne](PartDesign_Boolean.md): importuje jedną lub więcej brył lub klonów PartDesign do aktywnego elementu i przeprowadza operację logiczną.

#### Dodatki

Kilka dodatkowych funkcji, które można znaleźć w menu Part Design:

-   <img alt="" src=images/PartDesign_Migrate.svg  style="width:32px;"> [Przenieś](PartDesign_Migrate.md): migruje pliki utworzone w starszych wersjach FreeCAD. Jeśli plik jest oparty wyłącznie na funkcjach PartDesign, migracja powinna zakończyć się sukcesem. Jeśli plik zawiera mieszane obiekty Part/Part Design/Draft, konwersja najprawdopodobniej się nie powiedzie.

-   <img alt="" src=images/PartDesign_Sprocket.svg  style="width:32px;"> [Kreator projektowania kół łańcuchowych](PartDesign_Sprocket.md): tworzy profil koła zębatego, który może być użyty do wyciągnięcia. {{Version/pl|0.19}}

-   <img alt="" src=images/PartDesign_InternalExternalGear.svg  style="width:32px;"> [Kreator projektowania przekładni ewolwentowych](PartDesign_InvoluteGear.md): tworzy profil koła zębatego, który może być użyty do wyciągnięcia.

-   <img alt="" src=images/PartDesign_WizardShaft.svg  style="width:32px;"> [Twórca wałów](PartDesign_WizardShaft.md): tworzy wał z tabeli wartości i pozwala na analizę sił i momentów. Wał jest tworzony za pomocą szkicu obrotowego, który można edytować.

### Pozycje w menu kontekstowym 

-   <img alt="" src=images/_PartDesign_MoveTip.svg  style="width:32px;"> [Ustaw czubek](PartDesign_MoveTip.md): pozwala na przedefiniowanie czubka, który jest elementem eksponowanym na zewnątrz korpusu.

-   <img alt="" src=images/PartDesign_MoveFeature.svg  style="width:32px;"> [Przenieś obiekt do innej zawartości](PartDesign_MoveFeature.md): przenosi wybrany szkic, geometrię odniesienia lub element do innej zawartości

-   <img alt="" src=images/PartDesign_MoveFeatureInTree.svg  style="width:32px;"> [Przenieś obiekt za innym obiektem](PartDesign_MoveFeatureInTree.md): umożliwia zmianę kolejności obiektów drzewa zawartości poprzez przeniesienie wybranego szkicu, geometrii odniesienia lub elementu w inne miejsce na liście elementów.

#### Pozycje współdzielone ze Środowiskiem pracy Part 

-   <img alt="" src=images/Std_SetAppearance.svg  style="width:32px;"> [Wygląd zewnętrzny](Std_SetAppearance.md): określa wygląd całej części *(przezroczystość kolor itp.)*.

-   <img alt="" src=images/Part_FaceColors.svg  style="width:32px;"> [Ustaw kolor](Part_FaceColors.md): przypisuje kolory do poszczególnych powierzchni.

## Ustawienia

-   <img alt="" src=images/Preferences-part_design.svg  style="width:32px;"> [Ustawienia](PartDesign_Preferences.md): opcje dostępne w Narzędziach PartDesign.
-   [Ustawienia drobiazgowe](Fine-tuning.md): kilka dodatkowych parametrów, aby dopracować zachowanie PartDesign.

## Poradniki

-   [How to use FreeCAD](http://help-freecad-jpg87.fr/), strona internetowa opisująca przebieg pracy w zakresie projektowania mechanicznego.
-   [Projekt części: tworzenie podstawowych brył](Creating_a_simple_part_with_PartDesign/pl.md).
-   [Podstawy dla Środowiska pracy Projekt Części](Basic_Part_Design_Tutorial/pl.md).
-   [Poradnik: Projekt części uchwyt łożyska I](PartDesign_Bearingholder_Tutorial_I/pl.md) *(wymaga aktualizacji)*.
-   [Poradnik: Projekt części uchwyt łożyska II](PartDesign_Bearingholder_Tutorial_II/pl.md) *(wymaga aktualizacji)*.





 {{PartDesign Tools navi}}

[<img src="images/Property.png" style="width:16px"> Workbenches](Category_Workbenches.md)

---
[documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > PartDesign Workbench/pl
