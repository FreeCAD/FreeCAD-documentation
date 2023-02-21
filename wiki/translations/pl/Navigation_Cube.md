# Navigation Cube/pl
{{TOCright}}



## Wprowadzenie

**Kostka nawigacyjna** daje wizualną informację o orientacji ujęcia widoku kamery w bieżącym [widoku 3D](3D_view/pl.md) i może być użyta do jej zmiany. Domyślnie jest ona widoczna i znajduje się w prawym górnym rogu okna.

![](images/Navigation_Cube_Example.png )

Kostka nawigacyjna składa się z kilku części:

-   [Główny sześcian nawigacyjny](#G.C5.82.C3.B3wny_sze.C5.9Bcian_nawigacyjny.md).
-   [Strzałki kierunkowe](#Strza.C5.82ki_kierunkowe.md).
-   [Przycisk widoku do tyłu](#Przycisk_widoku_do_ty.C5.82u.md) *(u góry po prawej)* {{Version/pl|0.20}}
-   [Menu mini-kostki](#Menu_mini-kostki.md) *(na dole po prawej)*.
-   Wskaźniki osi X, Y i Z

Wszystkie elementy, z wyjątkiem wskaźników osi, można klikać.



## Użycie



### Główny sześcian nawigacyjny 

Główny sześcian posiada 26 ścian: 6 ścian głównych, 12 prostokątnych ścian brzegowych ({{Version/pl|0.20}}) i 8 ścian narożnych. Kliknięcie dowolnej z nich spowoduje zmianę ujęcia widoku kamery tak, aby jej kierunek był prostopadły do wybranej ściany.



### Strzałki kierunkowe 

Istnieje sześć strzałek kierunkowych: cztery trójkątne groty, jedna na górze, na dole, w lewo i w prawo; oraz dwie zakrzywione strzałki. Kliknięcie jednej z trójkątnych strzałek spowoduje obrót [widoku 3D](3D_view/pl.md) wokół linii prostopadłej do kierunku strzałki. Kliknięcie zakrzywionej strzałki spowoduje obrót [widoku 3D](3D_view/pl.md) wokół kierunku widoku.



### Przycisk widoku do tyłu 

Kliknięcie okrągłego przycisku w prawym górnym rogu kostki nawigacyjnej spowoduje obrócenie [widoku 3D](3D_view/pl.md) o 180° wokół pionowej osi widoku.



### Menu mini-kostki 

Kliknięcie małego sześcianu w prawym dolnym rogu Kostki nawigacji spowoduje wyświetlenie menu z następującymi opcjami:

-    **[Ortogonalny](Std_OrthographicCamera/pl.md)**: przełącza na widok ortogonalny.

-    **[Perspektywa](Std_PerspectiveCamera/pl.md)**: przełącza na widok perspektywiczny.

-    **[Isometryczny](Std_ViewIsometric/pl.md)**: przełącza na widok izometryczny.

-    **[Przybliż i dopasuj](Std_ViewFitAll/pl.md)**: powiększa i pochyla ujęcie widoku tak, aby wszystkie widoczne obiekty zmieściły się w aktualnym kadrze.



## Dostosowywanie



### Przesuwanie Kostki Nawigacyjnej 

Możesz przesunąć całą strukturę sterowania kostki nawigacyjnej w inne miejsce obrazu w oknie z widokiem 3D, naciskając myszą w dowolnym miejscu głównego sześcianu i przeciągając. Struktura zacznie się przesuwać dopiero po przesunięciu kursora poza jedną z krawędzi głównego sześcianu.



### Ustawienia

Sześcian nawigacyjny jest konfigurowalny, włącznie z dostosowaniem jego rozmiaru: **Edycja → Preferencje → Wyświetlanie → Nawigacja → Kostka nawigacyjna**. Zobacz [Edytor preferencji](Preferences_Editor/pl#Nawigacja.md).

### Advanced parameters 

Some advanced Navigation Cube parameters cannot be changed in the [Preferences Editor](Preferences_Editor#Navigation.md). These parameters can be set manually in the [Parameter editor](Std_DlgParameter.md) or via the [CubeMenu external workbench](Interface_Customization#CubeMenu.md). Changes will become visible when a new 3D view is created (with [Std New](Std_New.md), [Std Open](Std_Open.md) or [Std ViewCreate](Std_ViewCreate.md)).

To manually set colors:

1.  Start the <img alt="" src=images/Std_DlgParameter.svg  style="width:16px;"> [Parameter editor](Std_DlgParameter.md).
2.  In the panel on the left browse to **BaseApp → Preferences → NaviCube**.
3.  Right-click the panel on the right and select **New unsigned item** from the context menu.
4.  Enter the name of one of these colors:
    -   
        **BorderColor**
        
        : the lines separating the cube faces, default is {{Value|4281479730}} (hex: {{Value|ff323232}}).

    -   
        **ButtonColor**
        
        : all elements around the cube, default is {{Value|2162354671}} (hex: {{Value|80e2e9ef}}).

    -   
        **FrontColor**
        
        : all cube faces, default is {{Value|3236096495}} (hex: {{Value|c0e2e9ef}}).

    -   
        **HiliteColor**
        
        : the cube or arrow face that is currently highlighted, default is {{Value|4289389311}} (hex: {{Value|ffaae2ff}}).

    -   
        **TextColor**
        
        : the text on the cube faces, default is {{Value|4278190080}} (hex: {{Value|ff000000}}).
5.  The color value must be entered as a 32-bit unsigned integer. Translated to the hexadecimal format this integer has the form {{Value|AARRGGBB}}. Where {{Value|AA}} stands for the alpha channel (a measure for the transparency), and the other three digit pairs stand for red, green and blue. To convert a hexadecimal value to an unsigned integer you can use the [Python console](Python_console.md), enter for example {{Incode|int("ff323232", 16)}}, or an online service such as [this one](https://cryptii.com/pipes/integer-encoder).
6.  Optionally set more colors.
7.  Press the **Close** button.

To manually set the border width:

1.  Start the <img alt="" src=images/Std_DlgParameter.svg  style="width:16px;"> [Parameter editor](Std_DlgParameter.md).
2.  In the panel on the left browse to **BaseApp → Preferences → NaviCube**.
3.  Right-click the panel on the right and select **New float item** from the context menu.
4.  Enter the name **BorderWidth**, {{Value|default is 1.1}}.
5.  Enter the width.
6.  Press the **Close** button.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Navigation Cube/pl
