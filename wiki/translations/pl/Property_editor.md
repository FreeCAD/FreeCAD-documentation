# Property editor/pl
## Wprowadzenie

[Edytor właściwości](Property_editor/pl.md) pojawia się w dolnej części panelu **Model** (jeśli [widok łączony](Combo_view/pl.md) jest aktywny) lub jako niezależny panel nazwany **Widok właściwości**.

Ogólnie rzecz biorąc, Edytor właściwości jest przeznaczony do obsługi tylko jednego obiektu w tym samym czasie. Wartości wyświetlane w edytorze właściwości należą do wybranego obiektu. Mimo to, niektóre właściwości, takie jak kolory, mogą być ustawione dla wielu zaznaczonych obiektów. Jeśli nie ma zaznaczonych elementów, Edytor właściwości będzie pusty.

Nie wszystkie właściwości mogą być modyfikowane, niektóre są tylko do wyświetlania.

<img alt="" src=images/FreeCAD_Property_editor_Data.png  style="width:300px;"> 
*Właściwości Dane obiektu [Część: Sześcian](Part_Box/pl.md)*



## Typy właściwości 

Właściwość jest informacją taką jak numer lub ciąg znaków dołączony do dokumentu FreeCAD lub obiektu w dokumencie. Dostępnych jest wiele typów właściwości. Niektóre z najpopularniejszych to:


{{Code|lang=text|code=
App::PropertyAngle
App::PropertyBool
App::PropertyDistance
App::PropertyFloat
App::PropertyInteger
App::PropertyLength
App::PropertyPlacement
App::PropertyString
App::PropertyVector
}}



## Właściwości widoku i danych 

Istnieją dwie klasy właściwości obiektu dostępne poprzez zakładki w edytorze właściwości:

-   Właściwości **Dane** związane z parametrami \"fizycznymi\" obiektu. Właściwości **Dane** definiują podstawowe właściwości obiektu. Istnieją przez cały czas, nawet gdy FreeCAD jest używany w trybie konsolowym lub jako biblioteka. Oznacza to, że jeśli załadujesz dokument w trybie konsolowym, możesz edytować promień okręgu lub długość linii, nawet jeśli nie widzisz wyniku na ekranie.
-   Właściwości **Widok** związane z \"wizualnym\" wyglądem obiektu. Właściwości **Widok** są związane z `ViewObject` i są dostępne tylko wtedy, gdy załadowany jest graficzny interfejs użytkownika *(GUI)*. Nie są one dostępne przy korzystaniu z FreeCAD w trybie konsolowym lub jako biblioteka zasobów własnych. Domyślnie zmiany we właściwościach **Widok** nie są dodawane do stosu cofania i nie mogą być cofnięte ani przywrócone przy pomocy [Std: Cofnij](Std_Undo/pl.md) i [Std: Ponów](Std_Redo/pl.md). Ale można to zmienić ustawiając parametr [dostrajania](Fine-tuning/pl.md) **AutoTransactionView** na {{TRUE/pl}}.



### Właściwości podstawowe 

Różne obiekty mogą mieć różne właściwości. Jednak wiele obiektów ma te same właściwości, ponieważ wywodzą się z tej samej wewnętrznej klasy.

Większość obiektów geometrycznych, które mogą być tworzone i wyświetlane w [widoku 3D](3D_view.md) pochodzi z `Part::Feature`. Zobacz [Część: Cecha](Part_Feature/pl.md), aby dowiedzieć się, jakie podstawowe właściwości mają te obiekty.

Dla geometrii 2D większość obiektów pochodzi z `Part::Part2DObject` *(wywodzi się z `Part::Feature`)*, która jest podstawą [szkiców](Sketch/pl.md), i większości [obiektów środowiska Rysunek Roboczy](Draft_Workbench/pl.md). Zobacz [Część: Część na obiekt 2D](Part_Part2DObject/pl.md), aby zapoznać się z najbardziej podstawowymi właściwościami tych obiektów.



## Menu kontekstowe 

Aby wyświetlić menu kontekstowe Edytora właściwości, kliknij prawym przyciskiem myszy na tle edytora lub na właściwości.

Kliknięcie prawym przyciskiem myszy na tle pokazuje trzy opcje:

-    **Dodaj właściwość**: dodaje dynamiczną właściwość do obiektu.

-    **Pokaż ukryte**: jeśli aktywne, ukryte właściwości Dane i Widok są pokazane w edytorze.

-    **Automatycznie rozszerz**: jeśli aktywne, wszystkie węzły w edytorze są rozszerzone gdy obiekt jest wskazany.

Kliknięcie prawym przyciskiem myszy na właściwości daje dostęp do następujących dodatkowych opcji:

-    **Zmień nazwę grupy właściwości**: zmienia nazwę grupy właściwości wskazanych właściwości. Dostępne tylko dla właściwości dynamicznych. Właściwości dynamiczne to te dodawane przez użytkownika, jak również te dodawane przez kod w Python.

-    **Usuń właściwość**: usuwa wskazane właściwości. Dostępne tylko dla właściwości dynamicznych.

-    **Wyrażenie...**: wyświetla Edytor wyrażeń, który pozwala na użycie [wyrażeń](Expressions/pl.md) w wartości właściwości.

-    **Status**:

:   Jeśli po wartości statusu jest gwiazdka (*****) to jest on statyczny i nie może zostać zmieniony.

  - **Ukryte**: jeśli aktywne, ustawia właściwość jako ukrytą, co oznacza, że będzie wyświetlana w Edytorze właściwości tylko jeśli **Pokaż ukryte** jest aktywne.

  - **Wynik**: jeśli aktywne, ustawia właściwość jako wynik.

  - **Brak przeliczania**: jeśli aktywne, modyfikacja właściwości nie wpływa na jej kontener do przeliczenia.

  - **Tylko do odczytu**: jeśli aktywne, ustawia właściwość jako tylko do odczytu. Właściwość nie będzie edytowalna w Edytorze właściwości a opcja **Wyrażenie...** nie będzie dłużej dostępna. Może być jednak nadal możliwa zmiana właściwości przez okno dialogowe.

  - **Zmienna**: jeśli aktywne, właściwość jest ustawiana jako zmienna. Wartość zmiennej właściwości nie jest zapisywana do pliku. Przy otwieraniu pliku jest ona wstawiana z domyślną wartością.

  - **Naruszone**: jeśli aktywne, obiekt staje się naruszony i gotowy do przeliczenia.

  - **Ewaluacja przy przywróceniu**: jeśli aktywne, właściwość podlega ewaluacji przy przywracaniu dokumentu.

  - **Kopiuj przy zmianie**: jeśli aktywne, właściwość jest kopiowana gdy zmieniane jest Łącza. Właściwość **Link Copy on Change** Łącza musi być ustawiona na {{Value|Tracking}} lub {{Value|Enabled}} aby to działało. Jest to związane z [Variant Links](https://forum.freecad.org/viewtopic.php?p=738833#p738833).



## Tworzenie skryptów 

Zobacz [Właściwości niestandardowe funkcji Python](FeaturePython_Custom_Properties/pl.md).



## Właściwości

Zobacz [Widok połączony](Combo_view/pl#Ustawienia.md).





{{Interface_navi

}} {{Std_Base_navi}}



---
⏵ [documentation index](../README.md) > Property editor/pl
