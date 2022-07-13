---
- GuiCommand   */pl
   Name   *PartDesign PolarPattern
   Name/pl   *Projekt Części   * Szyk kołowy
   MenuLocation   *Projekt Części → Zastosuj szyk → Szyk kołowy
   Workbenches   *[Projekt Części](PartDesign_Workbench/pl.md)
   SeeAlso   *[Transformacja wielokrotna](PartDesign_MultiTransform/pl.md)
---

# PartDesign PolarPattern/pl

## Opis

Narzędzie <img alt="" src=images/PartDesign_PolarPattern.svg  style="width   *24px;"> **wzorca kołowego** tworzy wzorzec typu kołowego jednej lub wielu cech.

![](images/PartDesign_PolarPattern_example.png ) 
*Powyżej   * kieszeń w kształcie szczeliny ''(B)'' wykonana na bazie bryły ''(A, zwana również podstawą)'' jest używana do tworzenia wzoru biegunowego. Wynik ''(C)'' jest pokazany po prawej stronie.*

## Użycie

### Tworzenie

1.  Opcjonalnie [aktywuj](PartDesign_Body/pl#Aktywny_status.md) właściwą bryłę.
2.  Opcjonalnie wybierz jedną lub więcej cech w oknie [widoku drzewa](Tree_view/pl.md) lub w oknie [widoku 3D](3D_view/pl.md).
3.  Istnieje kilka sposobów wywołania narzędzia   *
    -   Naciśnij przycisk **<img src="images/PartDesign_PolarPattern.svg" width=16px> [Szyk kołowy](PartDesign_PolarPattern/pl.md)**,
    -   Wybierz opcję z menu **Projekt Części → Zastosuj wzór → <img src="images/PartDesign_PolarPattern.svg" width=16px> Szyk kołowy**.
4.  Jeśli nie ma aktywnej Zawartości, a w dokumencie są dwie lub więcej Zawartości, otworzy się okno dialogowe **Wymagana jest aktywna zawartość** i poprosi o uaktywnienie jednej z nich. Jeśli istnieje jedna Zawartość, zostanie ona aktywowany automatycznie.
5.  Jeśli nie wybrano żadnych cech, zostanie wyświetlone okno dialogowe **Wybierz cechę** otworzy się [panel zadań](Task_panel/pl.md)   * wybierz jedną lub więcej *(przytrzymaj klawisz **Ctrl**)* z listy i naciśnij przycisk **OK**.
6.  Parametry **Szyk kołowy** otwiera się [panel zadań](Task_panel/pl.md). Więcej informacji można znaleźć w sekcji [Opcje](#Opcje.md).
7.  Naciśnij przycisk **OK**, aby zakończyć.

### Edycja

1.  Wykonaj jedną z następujących czynności   *
    -   Kliknij dwukrotnie obiekt SzykKołowy w oknie [widoku drzewa](Tree_view/pl.md).
    -   Kliknij prawym przyciskiem myszy obiekt SzykKołowy w oknie [widoku drzewa](Tree_view/pl.md) i wybierz opcję **Edytuj SzykKołowy** z menu kontekstowego.
2.  Otworzy się [panel zadań](Task_panel/pl.md) **Parametry Szyku kołowego**. Więcej informacji można znaleźć w sekcji [Opcje](#Opcje.md).
3.  Naciśnij przycisk **OK**, aby zakończyć.

## Opcje

-   To add features   *
    1.  Press the **Add feature** button.
    2.  Select a feature in the [Tree view](Tree_view.md) or the [3D view](3D_view.md).
    3.  Repeat to add more features.
-   To remove features   *
    1.  Press the **Remove feature** button.
    2.  Do one of the following   *
        -   Select a feature in the [Tree view](Tree_view.md) or the [3D view](3D_view.md).
        -   Select a feature in the list and press the **Del** key.
        -   Right-click a feature in the list and select **Remove** from the context menu.
    3.  Repeat to remove more features.
-   If there are several features in the pattern, their order can be important. See [Ordering features](#Ordering_features.md).
-   Specify the **Axis** of the pattern   *
    -   
        **Normal sketch axis**
        
           * The Z axis of the sketch (only available for sketch-based features).

    -   
        **Vertical sketch axis**
        
           * The Y axis of the sketch (idem).

    -   
        **Horizontal sketch axis**
        
           * The X axis of the sketch (idem).

    -   
        **Construction line #**
        
           * A separate entry for each construction line in the sketch (idem).

    -   
        **Base X axis**
        
           * The X axis of the Body.

    -   
        **Base Y axis**
        
           * The Y axis of the Body.

    -   
        **Base Z axis**
        
           * The Z axis of the Body.

    -   
        **Select reference...**
        
           * Select a [Datum Line](PartDesign_Line.md) in the [Tree view](Tree_view.md) or a [Datum Line](PartDesign_Line.md) or edge in the [3D view](3D_view.md).
-   Check the **Reverse direction** checkbox to reverse the pattern.
-   Specify the **Angle** to be covered by the pattern.
-   Specify the number of **Occurrences** (including the original feature).
-   If the **Update view** checkbox is checked the view will update in real time.

## Oczekiwane funkcje 

Jeśli niektóre z wybranych cech są addytywne, a inne subtraktywne, ich kolejność może mieć wpływ na efekt końcowy. Kolejność można zmienić, przeciągając poszczególne cechy na liście. {{Version/pl|0.19}}

![](images/PartDesign_feature-order.gif ) 
*Efekty kolejności występowania elementów*

## Ograniczenia

-   Każdy kształt we wzorcu, który nie pokrywa się z elementem nadrzędnym, zostanie wykluczony. Zapewnia to, że bryła środowiska Projekt Części zawsze składa się z jednej, ciągłej bryły.
-   Wzorce Projektu Części nie są jeszcze tak zoptymalizowane jak ich odpowiedniki Rysunku Roboczego. Dlatego dla dużej liczby instancji powinieneś rozważyć użycie [Szyku biegunowego](Draft_PolarArray/pl.md) zamiast tego, w połączeniu z operacją logiczną środowiska Część. Może to wymagać poważnych zmian w twoim modelu, ponieważ opuszczasz środowisko Projekt Części i dlatego nie możesz po prostu kontynuować dalszych funkcji Projektu Części w tej samej Zawartości. Przykład pokazano na [Forum](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=55192).
-   Nie można zastosować wzorca bezpośrednio do innego wzorca, czy to kołowego, liniowego czy odbicia lustrzanego. Do tego potrzebna jest funkcja [Transformacji wielokrotnej](PartDesign_MultiTransform/pl.md).





{{PartDesign Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign PolarPattern/pl
