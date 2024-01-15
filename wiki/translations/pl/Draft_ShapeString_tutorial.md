---
 TutorialInfo:l
   Topic: Projekt produktu
   Level: początkujący
   Time: 30 minut
   Author: r-frank oraz vocx
   FCVersion: 0.17 i nowszy
   Files: https://github.com/FreeCAD/Examples/blob/master/Draft_Shapestring_Tutorial_Examples/Draft_Shapestring_Tutorial_Text.FCStd?raw=true Draft_Shapestring_Text
---

# Draft ShapeString tutorial/pl







## Wprowadzenie

Ten poradnik został pierwotnie napisany przez Rolanda Franka *(†2017, r-frank)*, a następnie przepisany i zilustrowany przez vocx.

Ten samouczek opisuje metodę tworzenia tekstu 3D i używania go z obiektami bryłowymi w <img alt="" src=images/Workbench_Part.svg  style="width:24px;"> środowiska [Część](Part_Workbench/pl.md). Omówimy jak

-   wstawiać obrysowany tekst za pomocą narzędzia **<img src="images/Draft_ShapeString.svg" width=16px> [kształt z tekstu](Draft_ShapeString/pl.md)**,
-   wyciągnięcie go do postaci bryły 3D za pomocą narzędzia **[<img src=images/Part_Extrude.svg style="width:16px"> [Wyciągnij](Part_Extrude/pl.md)**,
-   pozycjonować go w przestrzeni 3D za pomocą [umiejscowienia](Placement.md), oraz **[<img src=images/Draft_Move.svg style="width:16px"> [przesunięcie](Draft_Move/pl.md)** *(używa szkicu jako geometrii pomocniczej)*, oraz
-   wygrawerować tekst poprzez zastosowanie funkcji logicznej **[<img src=images/Part_Cut.svg style="width:16px"> [Wytnij](Part_Cut/pl.md)**.

Aby użyć funkcji Kształt z tekstu wewnątrz środowiska pracy <img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [Projekt Części](PartDesign_Workbench/pl.md), proces jest zasadniczo taki sam jak w przypadku środowiska pracy Część, ale Kształt z tekstu jest umieszczany wewnątrz [Zawartości](PartDesign_Body/pl.md) środowiska Projekt Części w celu jego wyciągnięcia. Przejdź do końca tego samouczka, aby uzyskać więcej informacji.

![](images/08_T04_Part_ShapesString_Extrude_final_cut.png ) 
*Ostateczny model wygrawerowanego tekstu.*

Środowisko pracy [Szkicownik](Sketcher_Workbench/pl.md) jest krótko używane do narysowania linii pomocniczej. Więcej informacji o narzędziach tego środowiska pracy można znaleźć na stronach:

-   [Podstawy dla środowiska pracy Szkicownik](Basic_Sketcher_Tutorial/pl.md).
-   [Informator do szkicownika](Sketcher_reference/pl.md).



## Sposób postępowania 

1\. Otwórz FreeCAD, utwórz nowy pusty dokument za pomocą **Plik → [<img src=images/Std_New.svg style="width:16px"> [Nowy](Std_New/pl.md)** i przejdź do środowiska pracy [Część](Part_Workbench/pl.md).

:   1.1. Naciśnij przycisk **[<img src=images/Std_ViewIsometric.svg style="width:16px"> [Widok izometryczny](Std_ViewIsometric/pl.md)** lub naciśnij **0** na klawiaturze numerycznej, aby zmienić widok na izometryczny w celu lepszej wizualizacji brył 3D.
:   1.2. Naciśnij przycisk **[<img src=images/Std_ViewFitAll.svg style="width:16px"> [Dopasuj wszystko](Std_ViewFitAll/pl.md)** za każdym razem, gdy dodajesz obiekty, aby przesuwać i powiększać [widok 3D](3D_view/pl.md) tak, aby wszystkie elementy były widoczne w widoku.
:   1.3. Przytrzymaj **Ctrl** podczas klikania, aby zaznaczyć wiele elementów. Jeśli wybrałeś coś źle lub chcesz usunąć zaznaczenie, kliknij na puste miejsce w oknie [widoku 3D](3D_view/pl.md).



## Utwórz kształt podstawowy 

2\. Wstaw prostopadłościan, klikając **<img src="images/Part_Box.svg" width=16px> [Sześcian](Part_Box/pl.md)**.

:   2.1. Wybierz obiekt `Sześcian` w [widoku drzewa](Tree_view/pl.md).
:   2.2. Zmień wymiary w zakładce **Dane** [edytora właściwości](Property_editor/pl.md).
:   2.3. Zmień wartość **Szerokość** na `31 mm`.

3\. Utwórz fazę.

:   3.1. Wybierz górną krawędź ({{Incode|Edge6}}) na przedniej powierzchni {{Incode|sześcianu}} w oknie [widoku 3D](3D_view/pl.md).
:   3.2. Naciśnij **<img src="images/Part_Chamfer.svg" width=16px> [Sfazowanie ...](Part_Chamfer/pl.md)**.
:   3.3. W [panelu zadań](Task_panel/pl.md) **Fazowanie krawędzi** przejdź do **Zaznaczenie**, wybierz **Wybierz krawędzie**. Jako **Typ sfazowania** wybierz {{Incode|Wymiary równe}}, a następnie ustaw **Długość** na {{Incode|5 mm}}.
:   3.4. Naciśnij **OK**. Spowoduje to utworzenie obiektu {{Incode|Chamfer}}.
:   3.5. W [widoku drzewa](Tree_view/pl.md) wybierz obiekt `Chamfer`, w zakładce **Widok** zmień wartość **Szerokość linii** na `2.0`.

![](images/01_T04_Part_Cube_base_long.png ) 
*Obiekt bazowy utworzony z sześcianu i operacji fazowania.*



## Wstaw obiekt kształt z tekstu 

4\. Przełącz się do środowiska [Rysunek Roboczy](Draft_Workbench/pl.md).

:   4.1. Upewnij się, że nic nie jest zaznaczone w oknie [widoku drzewa](Tree_view/pl.md).
:   4.2. Ustal płaszczyznę roboczą na XY *(Góra)* klikając na **[<img src=images/Draft_SelectPlane.svg style="width:16px"> [Wyborze płaszczyzny roboczej](Draft_SelectPlane/pl.md)** i naciskając **[<img src=images/View-top.svg style="width:16px"> [Widok od góry (XY)](Std_ViewTop/pl.md)**.

5\. Wstaw tekst \"FreeCAD\".

:   5.1. Kliknij **[<img src=images/Draft_ShapeString.svg style="width:16px"> [Kształt z tekstu](Draft_ShapeString/pl.md)**.
:   5.2. Zmień **X** na `0 mm`.
:   5.3. Zmień **Y** na `0 mm`.
:   5.4. Zmień **Z** na `0 mm`.
:   5.5. Lub naciśnij **Zresetuj współrzędne punktu**.
:   5.6. Zmień **Ciąg znaków** na `FreeCAD`. Zmień **Wysokość** na `5 mm`. Zmień **Śledzenie** na `0 mm`.
:   5.7. Upewnij się, że **Plik czcionki** wskazuje na prawidłową czcionkę, na przykład `/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf`. Naciśnij przycisk wielokropka **…**, aby otworzyć okno dialogowe systemu operacyjnego w celu znalezienia czcionki.

    :   
        **Uwaga:**
        
        Więcej szczegółów na temat pracy z czcionkami można znaleźć na stronie [Kształt z tekstu](Draft_ShapeString/pl#Opcje.md).
:   5.8. Naciśnij **OK**. Spowoduje to utworzenie obiektu `Kształt z tekstu`.
:   5.9. Ponownie przelicz dokument, naciskając **[<img src=images/Std_Refresh.svg style="width:16px"> [Odśwież](Std_Refresh/pl.md)**.
:   5.10. W [widoku drzewa](Tree_view/pl.md) wybierz obiekt `Kształt z tekstu`, w zakładce **Widok** zmień wartość **Szerokość linii** na `2.0`.
:   5.11. W oknie [widoku drzewa](Tree_view/pl.md) wybierz obiekt `Chamfer`, w zakładce **Widok** zmień wartość **Widoczność** na {{false/pl}} lub naciśnij **Spacje** na klawiaturze. Spowoduje to ukrycie obiektu, dzięki czemu będzie lepiej widoczny obiekt {{Incode|Kształt z tekstu}}.
:   5.12. Aby zobaczyć Kształt z tekstu z góry, zmień widok, naciskając **[<img src=images/View-top.svg style="width:16px"> [Od góry (XY)](Std_ViewTop/pl.md)**, lub **2** na klawiaturze.
:   5.13. Aby przywrócić widok izometryczny, naciśnij **[<img src=images/Std_ViewIsometric.svg style="width:16px"> [Widok izometryczny](Std_ViewIsometric/pl.md)** lub **0** na klawiaturze.

![](images/02_T04_Part_ShapeString.png ) 
*Tekst utworzony jako obiekt Kształt z tekstu, czyli jako zbiór krawędzi na płaszczyźnie.*



## Utwórz bryłę tekstu 3D 

6\. Przełącz się z powrotem do środowiska [Część](Part_Workbench/pl.md).

:   6.1. W oknie [widoku drzewa](Tree_view/pl.md) wybierz obiekt `Kształt z tekstu`, a następnie naciśnij **[<img src=images/Part_Extrude.svg style="width:16px"> [Wyciągnij ...](Part_Extrude/pl.md)**.
:   6.2. W [Panelu zadań](Task_panel/pl.md) **Wyciągnięcie** przejdź do sekcji **Kierunek**, wybierz **Wzdłuz wektora normalnej**. W sekcji **Długość** ustaw **Wzdłuż** na `1 mm`. Zaznacz też opcję **Utwórz bryłę**.
:   6.3. Naciśnij **OK**. Spowoduje to utworzenie obiektu `Wyciągnięcie`.
:   6.4. W [widok drzewa](Tree_view/pl.md) wybierz `Wyciągnięcie`, w zakładce **Widok** zmień wartość **Szerokość linii** na `2.0`.

![](images/03_T04_Part_ShapeString_Extrude.png ) 
*Tekst utworzony jako Kształt z tekstu i przekształcony w bryłę przez wyciągnięcie.*



## Wstaw szkic pomocniczy do pozycjonowania 

Teraz narysujemy prosty szkic, który zostanie użyty jako geometria pomocnicza do pozycjonowania obiektu wytłoczenia kształtu z tekstu.

7\. W oknie [widoku drzewa](Tree_view/pl.md) wybierz obiekt `Wyciągnięcie` i naciśnij **Spacje** na klawiaturze, aby uczynić go niewidocznym.

8\. Przejdź do środowiska pracy [Szkicownik](Sketcher_Workbench/pl.md).

9\. W oknie [widoku drzewa](Tree_view/pl.md) wybierz obiekt {{Incode|Wyciągnięcie}} i naciśnij **Spacja** na klawiaturze, aby go wyświetlić.

:   9.1. Wybierz nachyloną powierzchnię utworzoną przez operację fazowania (`Face3`).
:   9.2. Kliknij **[<img src=images/Sketcher_NewSketch.svg style="width:16px"> [Utwórz szkic](Sketcher_NewSketch/pl.md)**. W oknie dialogowym **Dołączenie szkicu** wybierz `Płaska powierzchnia` i naciśnij **OK**.
:   9.3. Widok powinien automatycznie dostosować się tak, aby ujęcie widoku było równoległe do wybranej ściany.
:   9.4. Narysuj poziomą linię w ogólnym położeniu na górze ściany. Długość nie jest ważna, interesuje nas tylko jej położenie.
:   9.5. Zwiąż lewy punkt końcowy tak, aby znajdował się `2.5 mm` od lokalnej osi X i od lokalnej osi Y, używając **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Zwiąż w poziomie](Sketcher_ConstrainDistanceX/pl.md)** i **[<img src=images/Sketcher_ConstrainDistanceY.svg style="width:16px"> [Zwiąż w pionie](Sketcher_ConstrainDistanceY/pl.md)**.
:   9.6. Ponieważ szkic jest tylko obiektem pomocniczym, nie musimy go w pełni wiązać. Możesz to zrobić, jeśli chcesz, przypisując stałą odległość, powiedzmy `20 mm`, ponownie za pomocą **[<img src=images/Sketcher_ConstrainDistanceX.svg style="width:16px"> [Zwiąż w poziomie](Sketcher_ConstrainDistanceX/pl.md)**.
:   9.7. Zamknij szkic.

<img alt="" src=images/04_T04_Part_ShapeString_support_sketch.png  style="width:500px;"> 
*Linia z wiązaniami tworzona za pomocą szkicownika.*

<img alt="" src=images/05_T04_Part_ShapeString_support_sketch_3D.png  style="width:500px;"> 
*Linia szkicu utworzona na górnej powierzchni bryły, używana jako odniesienie do pozycjonowania wyciągniętego tekstu.*



## Pozycjonowanie bryły tekstu w przestrzeni 3D 

10\. W oknie [widoku drzewa](Tree_view/pl.md) wybierz obiekt `Wyciągnięcie` i naciśnij **Spacje** na klawiaturze, aby uczynić go niewidocznym.

11\. Po zaznaczeniu obiektu {{Incode|Wyciągnięcie}}, w zakładce **Dane** [edytora właściwości](Property_editor/pl.md), kliknij na wartość **Umiejscowienie**, aby po prawej stronie pojawił się przycisk trzykropka **…** i kliknij na ten przycisk.

:   11.1. Zaznacz opcję **Zastosuj zmiany przyrostowe**.
:   11.2. Zmień **Obrót** na `Oś obrotu z zadanym kątem`; **Oś** na `Z` (ustawiając wartości `X`, `Y` i `Z` pól wprowadzania wartości dla osi odpowiednio na `0`, `0` i `1`, `Z` jest trzecim polem wprowadzania) i **Kąt** na `90°`, a następnie kliknij **Zastosuj**. Spowoduje to zastosowanie obrotu wokół osi Z i wyzerowanie pola **Kąt**.
:   11.3. Zmień **Obrót** na `Oś obrotu z zadanym kątem`; **Oś** na `Y` (ustawiając wartości `X`, `Y` i `Z` pól wprowadzania osi odpowiednio na `0`, `1` i `0`) oraz **Kąt** na `45°`, a następnie kliknij **Zastosuj**. Spowoduje to zastosowanie obrotu wokół osi Y i wyzerowanie pola **Kąt**.
:   11.4. Kliknij przycisk **OK**, aby zamknąć okno dialogowe.

12\. Przełącz się ponownie do środowiska [Rysunek Roboczy](Draft_Workbench/pl.md).

:   12.1. Przełącz na styl rysowania \"Szkieletowy\" za pomocą pozycji z menu **Widok → [Styl kreślenia](Std_DrawStyle/pl.md) → [<img src=images/DrawStyleWireFrame.svg style="width:16px"> Szkieletowy**, lub naciśnij przycisk **[<img src=images/DrawStyleWireFrame.svg style="width:16px"> [Szkieletowy](Std_DrawStyle/pl.md)** na pasku narzędzi. Pozwoli to zobaczyć obiekty znajdujące się za innymi obiektami.
:   12.2. Upewnij się, że metoda [przyciągania](Draft_Snap/pl.md) \"Przyciągnij do punktu końcowego\" jest aktywna. Można to zrobić z menu **Rysunek Roboczy → Przyciąganie → [<img src=images/Draft_Snap_Lock.svg style="width:16px"> [Przełącz przyciąganie](Draft_Snap_Lock/pl.md)**, a następnie ** → [<img src=images/Draft_Snap_Endpoint.svg style="width:16px"> [Przyciągnij do punktu końcowego](Draft_Snap_Endpoint/pl.md)**, lub naciskając przycisk **[<img src=images/Draft_Snap_Lock.svg style="width:16px"> [Przełącz przyciąganie](Draft_Snap_Lock/pl.md)** i **[<img src=images/Draft_Snap_Endpoint.svg style="width:16px"> [Przyciągnij do punktu końcowego](Draft_Snap_Endpoint/pl.md)** na pasku narzędzi przyciągania.

13\. W oknie [widoku drzewa](Tree_view/pl.md) wybierz `Wyciągnięcie`.

:   13.1. Kliknij **[<img src=images/Draft_Move.svg style="width:16px"> [Przesuń](Draft_Move/pl.md)**.
:   13.2. W oknie [widoku 3D](3D_view/pl.md) kliknij w lewy górny róg obiektu `Wyciągnięcia` *(1)*, a następnie kliknij w skrajny lewy punkt linii narysowanej szkicownikiem *(2)*.
:   13.3. Jeśli opcja **[<img src=images/Draft_Snap_Endpoint.svg style="width:16px"> [Przyciągnij do punktu końcowego](Draft_Snap_Endpoint/pl.md)** jest aktywna, gdy tylko zbliżysz kursor do wierzchołka, powinieneś zobaczyć, że dokładnie do niego przylega.


**Uwaga:**

jeśli masz problemy z przyciąganiem do wierzchołków, upewnij się, że aktywne jest tylko narzędzie **[<img src=images/Draft_Snap_Endpoint.svg style="width:16px"> [Przyciągnij do punktu końcowego](Draft_Snap_Endpoint/pl.md)**. Posiadanie wielu metod przyciągania aktywnych w tym samym czasie może utrudnić wybór właściwej funkcji.

:   13.4. Wyciągnięty tekst powinien teraz znajdować się wewnątrz obiektu `Sfazowanie`.

![](images/06_T04_Part_ShapeString_move.svg ) 
*Wytłoczony kształt z tekstu powinien zostać przesunięty do pozycji naszkicowanej linii, która leży na powierzchni Zawartości podstawy.*

![](images/07_T04_Part_ShapesString_Extrude_in_place.png ) 
*Wyciągnięty Kształt z tekstu umieszczony w obiekcie `Sfazowanie*.`



## Tworzenie wygrawerowanego tekstu 

14\. Przełącz się z powrotem do środowiska pracy [Część](Part_Workbench/pl.md).

:   14.1. Przełącz na styl rysowania \"Domyślny\" za pomocą **Widok → [Styl kreślenia](Std_DrawStyle/pl.md) → [<img src=images/DrawStyleAsIs.svg style="width:16px"> Domyślny**, lub naciśnij przycisk **[<img src=images/DrawStyleAsIs.svg style="width:16px"> [Domyślny](Std_DrawStyle/pl.md)** na pasku narzędzi widoku. Spowoduje to wyświetlenie wszystkich obiektów z normalnym cieniowaniem i kolorem.
:   14.2. W oknie [widoku drzewa](Tree_view/pl.md) zaznacz `Szkic` i naciśnij klawisz **Spacja** na klawiaturze, aby uczynić go niewidocznym.

15\. W oknie [widoku drzewa](Tree_view/pl.md) wybierz najpierw obiekt `Sfazowanie`, a następnie `Wyciągnięcie`.

:   15.1. Następnie wciśnij **[<img src=images/Part_Cut.svg style="width:16px"> [Wytnij](Part_Cut/pl.md)**. Spowoduje to utworzenie obiektu `Wycięcie`. To jest ostateczny obiekt.

Kolejność zaznaczania obiektów jest ważna dla operacji cięcia. Obiekt bazowy jest zaznaczany jako pierwszy, a obiekt odejmowany na końcu.

:   15.2. W oknie [widoku drzewa](Tree_view/pl.md) wybierz obiekt `Wycięcie`, w zakładce **Widok** zmień wartość **Szerokość Linii** na `2.0`.

![](images/08_T04_Part_ShapesString_Extrude_final_cut.png ) 
*Końcowy model zaokrąglonego sześcianu z wyrzeźbionym tekstem utworzonym z operacji Kształt z tekstu, Wyciągnięcie i Wycięcie funkcją logiczną.*



## Grawerowanie tekstu 3D za pomocą środowiska Projekt Części 

Podobny proces do opisanego powyżej można wykonać za pomocą środowiska pracy [Projekt Części](PartDesign_Workbench/pl.md).

1.  Najpierw utwórz obiekt **[<img src=images/Draft_ShapeString.svg style="width:16px"> [Kształt z tekstu](Draft_ShapeString/pl.md)** jako pierwszy.
2.  Utwórz **[<img src=images/PartDesign_Body_Tree.svg style="width:16px"> [Zawartość](PartDesign_Body/pl.md)** środowiska pracy Projekt Części, uaktywnij ją i dodaj bryłę bazową poprzez dodanie Bryły pierwotnej lub użycie Szkicu i wyciągnięcie go za pomocą narzędzia **[<img src=images/PartDesign_Pad.svg style="width:16px"> [Wyciągnij](PartDesign_Pad/pl.md)** środowiska Projekt Części.
3.  Przenieś obiekt {{Incode|Kształt z tekstu}} do aktywnej zawartości.
4.  Dołącz obiekt {{Incode|Kształt z tekstu}} do jednej ze ścian bryły lub **[<img src=images/PartDesign_Plane.svg style="width:16px"> [Płaszczyzny](PartDesign_Plane/pl.md)**, używając narzędzia **[<img src=images/Part_EditAttachment.svg style="width:16px"> [Dołączenie](Part_EditAttachment/pl.md)**.
5.  Teraz utwórz **[<img src=images/PartDesign_Pad.svg style="width:16px"> [Wyciągnięcie](PartDesign_Pad/pl.md)** lub **[<img src=images/PartDesign_Pocket.svg style="width:16px"> [Kieszeń](PartDesign_Pocket/pl.md)** z obiektu `Kształt z tekstu`, w celu wytworzenia odpowiednio dodającej lub odejmującej [cechy](PartDesign_Feature/pl.md) podstawowej bryły.

Zobacz wątek na forum, [Jak używać obiektu Kształt z tekstu w środowisku Projekt Części](https://forum.freecadweb.org/viewtopic.php?f=3&t=36623).



## Uwagi

-   Aby utworzyć zakrzywiony tekst można użyć makropolecenia <img alt="" src=images/FCCircularTextButtom.png  style="width:32px;"> [FCCircularText](Macro_FCCircularText/pl.md).
-   Aby zaimportować tekst z pliku SVG, zapoznaj się z poradnikiem [Import tekstu i geometrii z programu Inkscape](Import_text_and_geometry_from_Inkscape/pl.md).


 {{PartDesign Tools navi}} {{Sketcher Tools navi}}



---
⏵ [documentation index](../README.md) > [Part](Category_Part.md) > [PartDesign](Category_PartDesign.md) > [Sketcher](Category_Sketcher.md) > [Draft](Draft_Workbench.md) > Draft ShapeString tutorial/pl
