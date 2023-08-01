---
- GuiCommand:
   Name:TechDraw SectionView
   Name/pl:Rysunek Techniczny: Wstaw widok przekroju
   MenuLocation:Rysunek Techniczny → Widoki → Wstaw widok przekroju
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   SeeAlso:[Przekrój złożony](TechDraw_ComplexSection/pl.md), [Wstaw widok](TechDraw_View/pl.md), [Wstaw grupę rzutów](TechDraw_ProjectionGroup/pl.md)
---

# TechDraw SectionView/pl



## Opis

Narzędzie **Wstaw widok przekroju** wstawia widok przekroju na podstawie istniejącego widoku części.

<img alt="" src=images/TechDraw_section_ANSI.png  style="width:350px;">
<img alt="" src=images/TechDraw_section_ISO.png  style="width:350px;"> 
*Przekrój już umieszczonego widoku, który pokazuje wewnętrzne otwory i zakreskowaną powierzchnię cięcia.<br>
Górny obraz pokazuje format strzałki ANSI.<br>
Dolny obraz pokazuje format strzałki ISO.
*



## Użycie

1.  Wybierz widok części w oknie [widoku 3D](3D_view/pl.md) lub [widoku drzewa](Tree_view/pl.md).
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_SectionView.svg" width=16px> '''Wstaw widok przekroju'''**.
    -   Wybierz z menu opcję **Rysunek Techniczny → Widoki → <img src="images/TechDraw_SectionView.svg" width=16px> Wstaw widok przekroju**.
3.  Otworzy się panel zadań, który pomoże obliczyć różne właściwości. Rozsądne wartości dla widoku Kierunek są obliczane, ale można je zmienić.

![](images/TechDraw_Section_Taskview.png ) 
*Widok panelu zadania do definiowania widoku przekroju*



## Właściwości widoku przekroju 

Zapoznaj się również informacjami na stronie [właściwości widoku](TechDraw_View/pl#Widok.md) środowiska Rysunek Techniczny.



### Dane


{{TitleProperty|Operacja cięcia}}

-    **Połącz przed przecięciem|Bool**: Łączenie kształtów źródłowych przed wykonaniem cięcia przekroju.

-    **Przytnij po przecięciu|Bool**: Dodatkowo przycina wynikowy kształt po wycięciu przekroju w celu usunięcia niechcianych fragmentów.


{{TitleProperty|Format powierzchni cięcia}}

-    **Widok powierzchni cięcia|Enumeration**: Wygląd powierzchni cięcia. Opcje:

    -   
        {{Value|Ukryj}}
        
        : Ukrywa powierzchnię cięcia, wyświetlany jest tylko kontur.

    -   
        {{Value|Kolor}}
        
        : Koloruje powierzchnię cięcia przy użyciu ustawienia **Kolor powierzchni cięcia** w [ustawieniach](TechDraw_Preferences/pl.md).

    -   
        {{Value|SvgHatch}}
        
        : Wycina przekrój za pomocą [kreskowania](TechDraw_Hatch/pl.md).

    -   
        {{Value|PatHatch}}
        
        : Kreskowanie przekroju przy użyciu [kreskowanie geometryczne](TechDraw_GeometricHatch/pl.md).

    -   
        {{Value|PatHatch}}
        
        : Kreskuje wyciętą sekcję za pomocą [kreskowania geometrycznego](TechDraw_GeometricHatch/pl.md).

-    **Plik wzoru kreskowania|File**: Pełna ścieżka do pliku wzoru kreskowania SVG.

-    **Plik kreskowania geometrycznego|File**: Pełna ścieżka do pliku wzoru PAT.

-    **Dołączony plik Svg|FileIncluded**: Pełna ścieżka do dołączonego pliku wzorca kreskowania SVG.

-    **Dołączony plik Pat|FileIncluded**: Pełna ścieżka do dołączonego pliku wzoru PAT.

-    **Nazwa wzoru kreskowania geometrycznego|String**: Nazwa używanego wzorca PAT.

-    **Skala kreskowania|Float**: Dostosowanie rozmiaru wzorca kreskowania.


{{TitleProperty|Przekrój}}

-    **Symbol Przekroju|String**: Identyfikator dla tego przekroju.

-    **Widok Bazowy View|Link**: Widok, na którym opiera się przekrój.

-    **Normalna przekroju|Vector**: Wektor opisujący kierunek normalny do płaszczyzny cięcia.

-    **Punkt odniesienia przekroju|Vector**: Wektor opisujący punkt na płaszczyźnie przecięcia. Zazwyczaj jest to środek ciężkości oryginalnej części.

-    **Kierunek przekroju|Enumeration**: Kierunek w widoku podstawowym dla tego przekroju. Opcje: {{Value|Wyrównaj}}, {{Value|Z prawej}}, {{Value|Z lewej}}, {{Value|Z góry}} lub {{Value|Z dołu}}.



### Widok


{{TitleProperty|Płaszczyzna cięcia}}

-    **Kolor płaszczyzny przekroju|Color**: Stały kolor podświetlenia powierzchni. Używany, jeśli **Wyświetl płaszczyznę przekroju** jest ustawione na {{Value|Kolor}}.

-    **Wyświetl płaszczyznę przekroju|Bool|Hidden**: Pokaż / ukryj powierzchnię cięcia.


{{TitleProperty|Kreskowanie powierzchni}}

-    **Kolor kreskowania geometrycznego|Color**: Kolor wzoru kreskowania geometrycznego.

-    **Kolor kreskowania|Color**: Kolor wzoru kreskowania Svg.

-    **Kreskowanie powierzchni przekroju|Bool|Hidden**: Kreskowanie powierzchni cięcia.

-    **Waga kreskowania|Float**: Waga linii geometrycznego wzoru kreskowania.



## Właściwości widoku bazowego 

Obiekt **Widok przekroju** dziedziczy wszystkie odpowiednie właściwości widoku określonego jako **Widok bazowy**. We właściwościach tego widoku można zmienić wygląd linii przekroju:

-    **Kolor linii przekroju**: Kolor linii w przekroju.

-    **Styl linii przekroju**: Styl linii w przekroju.

Domyślne ustawienia tych parametrów są konfigurowane za pomocą ustawień **Linia przekroju** i **Styl linii przekroju** w [ustawieniach](TechDraw_Preferences/pl.md).



## Uwagi

-   **Format linii przekroju**: obsługiwane są dwa formaty linii przekroju (jak pokazano powyżej) i kontrolowane przez ustawienie preferencji \"Standard linii przekroju\" na karcie Adnotacja. Opcja {{Value|ANSI}} używa \"ciągnących strzałek\" *(znanych jako \"tradycyjny format\" w niektórych obszarach)*, a opcja {{Value|ISO}} używa \"pchających strzałek\" *(znanych również jako \"format strzałki odniesienia\")*.
-   \"Połącz przed wycięciem\": operacja przekroju czasami nie wycina kształtów źródłowych. Jeśli parametr \"Połącz przed wycięciem\" ma wartość true, kształty źródłowe są łączone w jeden kształt przed próbą wykonania operacji przekroju. Jeśli wystąpią problemy z operacją przekroju, należy spróbować zmienić tę wartość.
-   **Przytnij po wycięciu**: operacja przekroju czasami pozostawia część kształtu źródłowego. Jeśli parametr *Przytnij po cięciu* ma wartość true, na wyniku pierwszego cięcia wykonywana jest dodatkowa operacja cięcia, która powinna usunąć wszelkie niechciane elementy.
-   **Wyświetlanie powierzchni cięcia**: powierzchnia cięcia może być ukryta, pomalowana na jednolity kolor, zakreskowana przy użyciu wzoru Svg *(domyślnie)* lub zakreskowana przy użyciu wzoru PAT. Zobacz temat [kreskowanie](TechDraw_Hatching/pl.md).



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie Wstaw widok przekroju może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
doc = FreeCAD.ActiveDocument
box = doc.Box
page = doc.Page

view = doc.addObject("TechDraw::DrawViewPart", "View")
page.addView(view)
view.Source = box
view.Direction = (0, 0, 1)

section = doc.addObject("TechDraw::DrawViewSection", "Section")
page.addView(section)
section.Source = box
section.BaseView = view
section.Direction = (0, 1, 0)
section.SectionNormal = (-1, 0, 0)

doc.recompute()
```



## Przykłady

Więcej informacji na temat widoków przekrojów i niektórych przypadków użycia można znaleźć na stronie [Przykłady przekrojów](TechDraw_Section_Examples/pl.md).

<img alt="" src=images/TechDraw_ExampleSection-10.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-13.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-15.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-17.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-34.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-35.png  style="width:80px;">





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw SectionView/pl
