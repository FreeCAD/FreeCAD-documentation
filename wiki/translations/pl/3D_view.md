# 3D view/pl
## Wprowadzenie


{{TOCright}}

[Widok 3D](3D_view/pl.md) programu FreeCAD jest przykładem [scenografii](Scenegraph/pl.md) Coin3D, tworzy również najważniejsze okno w [interfejsie użytkownika](interface/pl.md). Coin3D jest biblioteką, która implementuje standard opisu sceny OpenInventor 2.1.

Niektóre właściwości widoku, takie jak kolor tła, styl [nawigacja myszki](Mouse_navigation/pl.md) oraz kroki przybliżania, można skonfigurować w [etytorze preferencji](Preferences_Editor/pl.md).

<img alt="" src=images/FreeCAD_3D_view.png  style="width:600px;">


* [Widok 3D](3D_view/pl.md)jest komponentem [interfejsu](interface/pl.md) programu FreeCAD . Domyślnie pokazuje mały widżet z osiami współrzędnych, oraz kostkę nawigacyjną również z osiami współrzędnych. Siatka może być wyświetlana i konfigurowana przez załadowanie środowiska pracy [Rysunek roboczy](Draft_Workbench/pl.md).*

## Działania


**Note:**

działania związane z linkami zostały dodane w wersji <small>(v0.19)</small> .

Ponieważ [widok drzewa](tree_view/pl.md) wyszczególnia większość obiektów widocznych w oknie widoku 3D, wiele akcji pokrywa się z tymi, które mogą być wykonane z [widoku drzewa](tree_view/pl.md).

Gdy domyślne środowisko pracy [Start](Start_Workbench/pl.md) jest aktywne, kliknięcie prawym przyciskiem myszki w oknie [widoku 3D](3D_view/pl.md) pokazuje tylko jedno polecenie:

-    **[Style nawigacji](Mouse_navigation/pl.md)**: różne sposoby użycia przycisków za pomocą 3-przyciskowej myszy lub touchpada komputera przenośnego.

Jednak po załadowaniu dowolnego [Środowiska pracy](Workbenches.md), istnieją dodatkowe polecenia:

-    **Tworzenie dowiązania**: [Utwórz dowiązanie](Std_LinkMake.md).

    -   
        **Utwórz grupę dowiązań**
        
        : [Grupa podstawowa](Std_LinkMakeGroup.md), [Grupa dowiązań](Std_LinkMakeGroup.md), [Grupa linków przekształcających](Std_LinkMakeGroup.md).

-    **[Dopasuj rozmiar do okna](Std_ViewFitAll.md)**: Przybliża i powiększa widok, aby dopasować wszystkie obiekty dokumentu wyświetlane na ekranie.

-    **[Dopasuj widok do zaznaczenia](Std_ViewFitSelection.md)**: Przybliża i powiększa widok, aby ściśle dopasować aktualnie zaznaczony obiekt wyświetlany na ekranie.

-    **[Styl rysowania](Std_DrawStyle.md)**: tak jak jest, linie płaskie, zacieniony, szkielet, punkty, ukryta linia, brak zacienienia.

-    **[Standard views](Std_View_Menu.md)**: [Ustaw widok izometryczny](Std_ViewIsometric.md), [Widok z przodu](Std_ViewFront.md), [Widok z góry](Std_ViewTop.md), [Widok z prawej](Std_ViewRight.md), [Widok z tyłu](Std_ViewRear.md), [Widok z góry](Std_ViewBottom.md), [Widok z lewej](Std_ViewLeft.md), [Obróć w lewo](Std_ViewRotateLeft.md), [Obróć w prawo](Std_ViewRotateRight.md).

-    **Pomiar odległości**: [Przełącz pomiar](View_Measure_Toggle_All.md), [usuń poomiary](View_Measure_Clear_All.md).

-    **Okno dokumentów**: [zadokowany](Std_ViewDockUndockFullscreen.md), [oddokowany](Std_ViewDockUndockFullscreen.md), oraz [Pełny ekran](Std_ViewDockUndockFullscreen.md).

Dodatkowo, w zależności od aktywnego stanowiska pracy i aktywnego obiektu, mogą być dostępne inne polecenia kontekstowe.

Na przykład, w odniesieniu do [Part](Part_Workbench.md) i wybranego pojedynczego obiektu.

-    **[Wygląd](Std_SetAppearance.md)**: uruchamia okno dialogowe w celu zmiany koloru i rozmiaru linii i wierzchołków oraz koloru ścian.

-    **[Pokaż / ukryj](Std_ToggleVisibility.md)**: sprawia, że obiekt jest widoczny lub niewidoczny w oknie widoku 3D.

-    **[Przełącznik wyboru](Std_ToggleSelectability.md)**: sprawia, że obiekt nie może być dłużej zaznaczony w widoku 3D; użyj ponownie tego polecenia, aby anulować jego efekt. Pozwala przełączyć obiekt `Selectable` w przełaczając atrybuty na wartość `True` lub `False`. Zmień właściwość przez przełączanie **koloru kształtu** w [edytorze właściwości](property_editor.md).

-    **[Przełącz aktywną zawartość](Std_TreeSelection.md)**: rozwiń [widok drzewa](tree_view.md) aby wyświetlić wybrany obiekt w hierarchii.

-    **[Kolor losowy](Std_RandomColor.md)**: przypisuje obiektowi losowy kolor. Ustawia barwę obiektu. `Kolor kształtu` jest atrybutem złożonym `(r,g,b)` z drzewem o losowo wybranych wartościach pomiędzy 0 i 1. Zmień właściwość modyfikując **kolor kształtu** w [edytorze właściwości](property_editor.md).

-    **[Usuń](Std_Delete.md)**: usuwa obiekt z dokumentu, a także z widoku 3D, wywołując funkcję `removeObject()`.

Kolejny przykład, ze Środowiskiem pracy [Draft](Draft_Workbench.md) i jednym wybranym obiektem. Zawiera te same polecenia co menu Środowiska pracy [Part](Part_Workbench.md), oraz:

-    **Draft**: polecenia tworzenia i modyfikacji obiektów ze Środowiska pracy [Draft](Draft_Workbench.md).

-    **Narzędzia**: dodatkowe polecenia kontekstowe dostarczane przez Środowisko pracy [Draft](Draft_Workbench.md).

## Szczególy

FreeCAD korzysta z biblioteki Quarter do używania Coin3D w środowisku Qt.

Możliwa jest bezpośrednia interakcja z widokiem 3D z [Konsoli Pythona](Python_console.md) za pomocą biblioteki Pythona Pivy.

Więcej informacji można znaleźć w dokumentacji dla Power użytkowników:

-   [Scenografia](Scenegraph.md), opis Coin3D.
-   [Pivy](Pivy.md), użycie Coin3D z konsoli Pythona.
-   [Biblioteki zewnętrzne](Third_Party_Libraries.md) używane przez FreeCAD.
-   [Coin3D](https://grey.colorado.edu/coin3d/index.html) dokumentacja dla C++.


{{Interface navi

}}

---
[documentation index](../README.md) > 3D view/pl
