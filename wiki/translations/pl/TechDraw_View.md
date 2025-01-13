---
 GuiCommand:
   Name: TechDraw View
   Name/pl: Rysunek Techniczny: Wstaw widok
   MenuLocation: Rysunek Techniczny , Widoki , Wstaw widok
   Workbenches: TechDraw_Workbench/pl
   SeeAlso: TechDraw_ProjectionGroup/pl, TechDraw_SpreadsheetView/pl, TechDraw_ArchView/pl, TechDraw_Symbol/pl, TechDraw_Image/pl
---

# TechDraw View/pl



## Opis

Narzędzie **Wstaw widok** dodaje reprezentację jednego lub więcej obiektów do strony Rysunku. {{Version/pl|1.0}}: Może utworzyć [obiekt grupy rzutów (pojedynczy widok)](#Properties_Projection_Group_Item/pl.md), [grupę rzutów](TechDraw_ProjectionGroup/pl.md), [widok Arkusza Kalkulacyjnego](TechDraw_SpreadsheetView/pl.md), [obiekt środowiska Architektura](TechDraw_ArchView/pl.md), [symbol SVG](TechDraw_Symbol/pl.md) lub [obraz bitmapy](TechDraw_Image/pl.md).

W {{VersionMinus/pl|0.21}} to narzędzie może tylko utworzyć [Widok części](#Properties_Part_View/pl.md), który jest bardzo zbliżony do obiektu grupy rzutów.

![](images/TechDraw_View_example.png ) 
*Widok bryły sześcianu z ukrytymi liniami*



## Użycie - Obiekt grupy rzutów i Grupa rzutów 

1.  Opcjonalnie obróć [widok 3D](3D_view/pl.md). Kierunek kamery w widoku 3D może zostać użyty do ustawienia kierunku rzutowania głównego widoku.
2.  Wybierz jeden lub więcej obiektów z właściwością **Shape** w widoku 3D lub [widoku drzewa](Tree_view/pl.md). Możesz również wybrać obiekty[Std: Część](Std_Part/pl.md) lub [Std: Grupa](Std_Group/pl.md) zawierające takie obiekty. Podczas zaznaczania w widoku 3D, pierwsza zaznaczona ściana może zostać użyta do ustawienia kierunku rzutowania głównego widoku. Nie wybieraj obiektów przez zaznaczenie ścian w widoku 3D, jeśli chcesz użyć bieżącego kierunku kamery.
3.  Jeśli w dokumencie znajduje się wiele stron rysunku: opcjonalnie dodaj żądaną stronę do zaznaczenia, wybierając ją w [widoku drzewa](Tree_view/pl.md).
4.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_View.svg" width=16px> [Wstaw widok](TechDraw_View/pl.md)**.
    -   Wybierz opcję **Rysunek Techniczny → Widoki → <img src="images/TechDraw_View.svg" width=16px> Wstaw widok** z menu.
5.  Jeśli w dokumencie znajduje się wiele stron rysunku i jeśli żadna strona nie jest wyświetlana w [obszarze widoku głównego](Main_view_area/pl.md) i nie wybrałeś jeszcze strony, otworzy się okno dialogowe **Wybór strony**:
    1.  Wybierz żądaną stronę.
    2.  Naciśnij przycisk **OK**.
6.  Otworzy się panel zadań **Widok części**. {{Version/pl|1.0}}
7.  Opcjonalnie dostosuj parametry:
    -   **Skala**: wybierz {{Value|Strona}}, {{Value|Automatyczna}} lub {{Value|Użytkownika}}. Jeśli zostanie wybrana ostatnia opcja: wprowadź licznik i mianownik skali.
    -   **Kierunek**: użyj dostępnych przycisków, aby dostosować kierunek rzutowania i obrót głównego widoku:
        -   Przycisk **[#.## #.## #.##]** w środku pokazuje bieżący kierunek rzutowania. Wartość początkowa zależy od ustawienia [preferencji](TechDraw_Preferences/pl#Ogólne.md) **Użycie kierunku kamery 3D**. Naciśnij przycisk, aby ręcznie dostosować kierunek i obrót widoku.
        -   Naciśnij przycisk **<img src="images/Arrow-up.svg" width=16px>**, **<img src="images/Arrow-down.svg" width=16px>**, **<img src="images/Arrow-left.svg" width=16px>** lub **<img src="images/Arrow-right.svg" width=16px>**, aby obrócić kierunek rzutowania o 90° wokół osi poziomej lub pionowej widoku.
        -   Naciśnij przycisk **<img src="images/Arrow-cw.svg" width=16px>** lub **<img src="images/Arrow-ccw.svg" width=16px>**, aby obrócić widok o 90° wokół kierunku rzutowania.
        -   Naciśnij przycisk **<img src="images/TechDraw_ProjFront.svg" width=16px>**, aby ustawić kierunek rzutowania głównego widoku na standardowy [widok z przodu](Std_ViewFront/pl.md).
        -   Naciśnij przycisk **<img src="images/TechDraw_CameraOrientation.svg" width=16px>**, aby ustawić go na pierwszą zaznaczoną ścianę, jeśli jest dostępna, w przeciwnym razie na bieżący kierunek kamery.
    -   **Dodatkowe projekcje**: opcjonalnie utwórz dodatkowe projekcje oprócz głównego widoku. Co najmniej jedna dodatkowa projekcja musi być określona, aby wszystkie ustawienia w tej sekcji były wyświetlane.
8.  Po zmianie niektórych parametrów naciśnięcie przycisku **Zastosuj** może być wymagane do zaktualizowania widoku/widoków.
9.  Naciśnij przycisk **OK**.
10. Zostanie wstawiony [obiekt grupy rzutów](#Properties_Projection_Group_Item/pl.md) lub, jeśli istnieje jedna lub więcej dodatkowych projekcji, [Grupa rzutów](TechDraw_ProjectionGroup/pl.md).

![](images/TechDraw_View_Taskpanel.png ) 
*[Panel zadań](Task_panel/pl.md) Widok części*



## Użycie - inne typy widoków 


{{Version/pl|1.0}}

1.  Opcjonalnie wybierz [arkusz kalkulacyjny](Spreadsheet_CreateSheet/pl.md) w [widoku drzewa](Tree_view/pl.md) lub [płaszczyznę przekroju środowiska Architektura](Arch_SectionPlane/pl.md) w [widoku 3D](3D_view/pl.md) lub widoku drzewa.
2.  Postępuj zgodnie z krokami 3, 4 i 5 wyjaśnionymi [powyżej](#Użycie_-_Obiekt_grupy_rzutów_i_Grupa_rzutów.md).
3.  Jeśli nie wybrałeś arkusza kalkulacyjnego ani płaszczyzny przekroju środowiska Architektura:
    1.  Otwiera się okno dialogowe z ostrzeżeniem.
    2.  Zaznacz pole wyboru **Nie pokazuj tego komunikatu ponownie**, aby uniknąć wyświetlania tego okna w przyszłości.
    3.  Naciśnij przycisk **OK**.
    4.  Otworzy się przeglądarka plików.
    5.  Wybierz plik SVG lub plik z obrazem.
4.  Zostanie wstawiony [Widok Arkusza kalkulacyjnego](TechDraw_SpreadsheetView/pl.md), [obiekt środowiska Architektura](TechDraw_ArchView/pl.md), [Symbol SVG](TechDraw_Symbol/pl.md) lub [obraz bitmapy](TechDraw_Image/pl.md).
5.  W przypadku widoku arkusza kalkulacyjnego: dostosuj zakres komórek widoku, zmieniając jego właściwości **Cell Start** i **Cell End**.
6.  W przypadku symbolu lub obrazu bitmapy: opcjonalnie zmień jego właściwość **Scale**, aby dostosować jego rozmiar.



## Właściwości - Widok części 

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Widok części, formalnie obiekt {{Incode|TechDraw::DrawViewPart}}, ma następujące właściwości:



### Dane


{{TitleProperty|Podstawa}}

-    {{PropertyData/pl|Odległość X}}: Położenie widoku w poziomie na stronie. *(1)*

-    {{PropertyData/pl|Odległość Y}}: Położenie widoku w pionie na stronie. *(1)*

-    {{PropertyData/pl|Zablokuj pozycję|Bool}}: Gdy wartość wynosi {{True/pl}}, zapobiega przeciąganiu widoków w oknie GUI. Widok nadal może być przesuwany poprzez zmianę właściwości współrzędnych X,Y. *(1)*

-    {{PropertyData/pl|Obrót|Kąt}}: Obrót widoku strony w kierunku przeciwnym do ruchu wskazówek zegara w stopniach. *(1)*

-    {{PropertyData/pl|Typ skali|Enumeration}}: Typ skali. Opcje: *(1)*

    -   
        {{Value|Strona}}
        
        : Używa wartości z ustawień obiektu [Strony](TechDraw_PageDefault/pl.md).

    -   
        {{Value|Automatyczna}}
        
        : Dopasuje widok do rozmiaru strony.

    -   
        {{Value|Użytkownika}}
        
        : Użyj skali zdefiniowanej przez wartość **Skala**.

-    {{PropertyData/pl|Skala|FloatConstant}}: Widok zostanie wyrenderowany na stronie w stosunku Skala:1 w odniesieniu do źródła. *(1)*

-    {{PropertyData/pl|Podpis|String}}: Opcjonalny krótki podpis. *(1)*


{{Properties_Title/pl|Kosmetyczne}}

-    **Wierzchołek kosmetyczny|TechDraw::PropertyCosmeticVertexList|Ukryte**
    

-    **Krawędź kosmetyczna|TechDraw::PropertyCosmeticEdgeList|Ukryte**
    

-    **Linie środka|TechDraw::PropertyCenterLineList|Ukryte**
    

-    **Geom Formats|TechDraw::PropertyGeomFormatList|Ukryte**
    


{{Properties_Title/pl|Parametry HLR}}

-    **Widok zgrubny|Bool**: Jeśli wartość ta wynosi {{True/pl}}, Rysunek Roboczy użyje przybliżenia wielokąta do obliczenia geometrii rysunku. Jeżeli jest to {{False/pl}}, Rysunek Roboczy użyje algorytmu precyzyjnego. Widok zgrubny może być wyliczany znacznie szybciej dla złożonych modeli. Jakość rysunku jest obniżona, ponieważ każda krzywa jest aproksymowana jako seria krótkich odcinków linii. Wierzchołki nie są wyświetlane w trybie Widok zgrubny, ponieważ każdy krótki odcinek spowodowałby utworzenie dwóch nowych wierzchołków, co spowodowałoby bałagan na ekranie. Wymiary liniowe mogą zostać dodane do okna Widoku zgrubnego, ale ich użyteczność jest mało prawdopodobna.

-    **Wygładzanie widoczne|Bool**: Wyświetlanie wygładzonych linii włączone/wyłączone.

-    **Szew widoczny|Bool**: Wyświetlanie linii szwu włączone/wyłączone.

-    **Iso widoczne|Bool**: Wyświetlanie linii izometrycznych *(u,v)* włączone/wyłączone.

-    **Hard Hidden|Bool**: Wyświetlanie linii ukrytych włączone/wyłączone.

-    **Wygładzanie ukryte|Bool**: Ukrywanie wygładzonych linii włączone/wyłączone.

-    **Szew ukryty|Bool**: Ukrywanie linii szwu włączone/wyłączone.

-    **Iso ukryte|Bool**: Ukrywanie linii izometrycznych *(u,v)* włączone/wyłączone.

-    **Licznik Iso|Integer**: Liczba linii izometrycznych(u,v) do narysowania na każdej ścianie.

-    **Licznik przejść|Integer**: Ile razy FreeCAD powinien spróbować wyczyścić wynik algorytmu HLR. {{Version/pl|0.21}}


{{TitleProperty|Rzutowanie}}

-    {{PropertyData/pl|Pochodzenie|LinkList}}: Powiązania z obiektami rysunkowymi, które mają być przedstawione.

-    {{PropertyData/pl|XPochodzenie|XLinkList}}: Odnośniki do obiektów rysunkowych w pliku zewnętrznym.

-    {{PropertyData/pl|Kierunek|Vector}}: Wektor ten kontroluje kierunek, z którego patrzysz na obiekt. +X to prawo, -X to lewo, +Y to tył, -Y to przód *(patrząc w ekran)*, +Z to góra, a -Z to dół. Zatem widok z przodu to *(0,-1,0)*, a widok izometryczny to *(1,-1,1)*.

-    {{PropertyData/pl|XKierunek|Vector}}: ten wektor kontroluje obrót widoku, według wartości Kierunek.

-    {{PropertyData/pl|Perspektywa|Bool}}: Przyjmuje wartość {{True/pl}} dla projekcji perspektywicznej, {{False/pl}} dla projekcji ortogonalnej.

-    {{PropertyData/pl|Skupienie|Distance}}: Odległość od kamery do płaszczyzny projekcji dla rzutów perspektywicznych. Musi być dostosowana do obiektu. Odległość zbyt duża powoduje utratę perspektywy, odległość zbyt mała powoduje zniekształcenie obiektu.



### Widok


{{TitleProperty|Podstawa}}

-    **Utrzymaj etykietę|Bool**: Zawsze pokazuj etykietę widoku, jeśli parametr ma wartość {{TRUE/pl}}. *(1)*

-    **Kolejność na stosie|Integer**: Nad lub pod w stosunku do innych widoków. *(1)* {{Version/pl|0.21}}


{{TitleProperty|Widok z przerwaniem}}

-    **Styl linii przerwania|Enumeration**: Ustaw styl linii przerwania jeśli ma to zastosowanie. {{Version/pl|1.0}}

-    **Typ linii przerwania|Enumeration**: Dostosowuje typ przedstawienia linii przerwania na widokach z przerwaniem jeśli ma to zastosowanie: {{Value|Brak}}, {{Value|Zygzak}} lub {{Value|Proste}}. {{Version/pl|1.0}}


{{TitleProperty|Dekoracja}}

-    **Arc Center Marks|Bool**: Włączenie / wyłączenie znaczników środka łuku okręgu.

-    **Center Scale|Float**: Dostosowanie rozmiaru znacznika środka łuku okręgu, jeśli jest włączony.

-    **Horiz Center Line|Bool**: Pokaż poziomą oś symetrii w widoku.

-    **Show All Edges|Bool**: Tymczasowo pokaż niewidoczne linie.

-    **Vert Center Line|Bool**: Pokaż pionową oś symetrii w widoku.


{{TitleProperty|Ściany}}

-    **Kolor ścian|Color**: Ustaw kolor ścian. {{Version/pl|1.0}}

-    **Przezroczystość ścian|Percent**: Ustaw przezroczystość ścian. {{Version/pl|1.0}}


{{TitleProperty|Podświetlenie}}

-    **Highlight Adjust|Float**: W razie potrzeby dostosuj obrót podświetlenia szczegółu.

-    **Highlight Line Color|Color**: W razie potrzeby ustaw kolor podświetlonej linii.

-    **Highlight Line Style|Enumeration**: Ustaw styl podświetlonej linii, jeśli ma to zastosowanie.


{{TitleProperty|Linie}}

-    **Extra Width|Length**: Jeszcze nie wdrożone.

-    **Hidden Width|Length**: Grubość ukrytych linii, jeśli jest włączona.

-    **Iso Width|Length**: Grubość linii powierzchni izometrycznych *(u,v)* i linii wymiarowych.

-    **Line Width|Length**: Grubość widocznych linii. Zobacz informacje na stronie [Grupy linii](TechDraw_LineGroup/pl.md).


{{TitleProperty|Linia przekroju}}

-    **Uwzględnij linię cięcia|Bool**: Pokaż/ukryj linię cięcia przekroju, jeśli dotyczy. {{Version/pl|1.0}}

-    **Kolor linii przekroju|Color**: Ustaw kolor linii przekroju, jeśli dotyczy.

-    **Znaczniki linii przekroju|Bool**: Pokaż/ukryj znaczniki przy zmianach kierunku dla przekroju złożonego, jeśli dotyczy. {{Version/pl|0.21}}

-    **Styl linii przekroju|Enumeration**: Ustaw styl linii przekroju, jeśli dotyczy.

-    **Pokaż linię przekroju|Bool**: Pokaż/ukryj linię przekroju, jeśli dotyczy.

*(1)* właściwości te są wspólne dla wszystkich typów widoku.



## Właściwości - Obiekt grupy rzutów 

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt grupy rzutów, formalnie obiekt {{Incode|TechDraw::DrawProjGroupItem}}, wywodzi się z [Widoku części](#Właściwości_-_Widok_części.md), formalnie obiektu {{Incode|TechDraw::DrawViewPart}} i dziedziczy wszystkie jego właściwości. Ma również następujące dodatkowe właściwości:



### Dane 


{{TitleProperty|Podstawa}}

-    **Typ|Enumeration**: Typ widoku ({{Value|Z przodu}}, {{Value|Z lewej}}, itd.).

-    **Wektor obrotur|Vector**: Przestarzałe, użyj **KierunekX** zamiast tego.



## Właściwości - Grupa rzutów 

Zobacz stronę [Wstaw grupę rzutów](TechDraw_ProjectionGroup/pl#Właściwości.md).



## Właściwości - Widok Arkusza kalkulacyjnego 

Zobacz stronę [Wstaw widok Arkusza kalkulacyjnego](TechDraw_SpreadsheetView/pl#Właściwości.md).



## Właściwości - Wstaw obiekt środowiska Architektura 

Zobacz stronę [Wstaw obiekt środowiska Architektura](TechDraw_ArchView/pl#Właściwości.md).



## Właściwości - Symbol SVG 

Zobacz stronę [Wstaw Symbol SVG](TechDraw_Symbol/pl#Właściwości.md).



## Właściwości - Wstaw obraz bitmapy 

Zobacz stronę [Wstaw obraz bitmapy](TechDraw_Image/pl#Właściwości.md).



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Widok części można utworzyć za pomocą [makrodefinicji](Macros/pl.md) i z konsoli [Python](Python/pl.md) przy użyciu następujących funkcji:


```python
import FreeCAD as App

doc = App.ActiveDocument
box = doc.addObject("Part::Box", "Box")

page = doc.addObject("TechDraw::DrawPage", "Page")
template = doc.addObject("TechDraw::DrawSVGTemplate", "Template")
template.Template = App.getResourceDir() + "Mod/TechDraw/Templates/A4_LandscapeTD.svg"
page.Template = template

# Toggle the visibility of the page to ensure its width and height are updated (hack):
page.Visibility = False
page.Visibility = True

view = doc.addObject("TechDraw::DrawViewPart", "View")
page.addView(view)
view.Source = [box]
view.Direction = (0, 0, 1)

view.X = page.PageWidth / 2
view.Y = page.PageHeight / 2

doc.recompute()
```





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw View/pl
