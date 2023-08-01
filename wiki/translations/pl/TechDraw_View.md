---
- GuiCommand:
   Name:TechDraw View
   Name/pl:Rysunek Techniczny: Wstaw widok
   MenuLocation:Rysunek Techniczny - Widoki - Wstaw widok
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   SeeAlso:[Grupa rzutów](TechDraw_ProjectionGroup/pl.md), [Widok przekroju](TechDraw_SectionView/pl.md)
---

# TechDraw View/pl



## Opis

Narzędzie **Wstaw widok** dodaje reprezentację jednego lub więcej obiektów do strony Rysunku. Jest to podstawowy element środowiska Rysunek Techniczny. Większość innych widoków pochodzi w jakiś sposób od metody Widok.

Widok będzie próbował narysować cokolwiek z właściwością `kształt`. Możesz wybrać obiekty [szkicu](Draft_Workbench/pl.md) i również [Projekt Części: Zawartość](PartDesign_Body/pl.md), środowiska [Rysunek Roboczy](Draft_Workbench/pl.md). Widok wyodrębni również kształty z obiektów w kontenerze [Std: Część](Std_Part/pl.md) lub [Std: Grupa](Std_Group/pl.md).

![](images/TechDraw_View_example.png ) 
*Widok bryły sześcianu z ukrytymi liniami*



## Użycie

1.  Opcjonalnie obróć [widok 3D](3D_view/pl.md). O ile w następnym kroku nie zostanie wybrana ściana, kierunek ujęcia widoku w oknie [widoku 3D](3D_view/pl.md) określa początkową wartość właściwości **Kierunek** widoku.
2.  Wybierz jeden lub więcej obiektów w oknie [Widoku 3D](3D_view/pl.md) lub [Widoku drzewa](Tree_view/pl.md). Przy wyborze w oknie widoku 3D pierwsza wybrana ściana określa wartość początkową właściwości **Kierunek**.
3.  Jeśli w dokumencie jest wiele stron rysunku: opcjonalnie dodaj żądaną stronę do wyboru przez zaznaczenie jej w [widoku drzewa](Tree_view/pl.md). Nie jest to opcjonalne dla {{VersionMinus/pl|0.19}}.
4.  Istnieje kilka sposobów na wywołanie narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_View.svg" width=16px> [Wstaw widok](TechDraw_View/pl.md)**.
    -   Wybierz opcję **Rysunek Techniczny → Widoki → <img src="images/TechDraw_View.svg" width=16px> Wstaw widok** z menu.
5.  Jeśli w dokumencie jest wiele stron rysunków i nie została jeszcze wybrana żadna strona, zostanie otwarte okno dialogowe **Wybór strony**: {{Version/pl|0.20}}
    1.  Wybierz żądaną stronę.
    2.  Naciśnij przycisk **OK**.



## Właściwości



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


{{TitleProperty|Dekoracja}}

-    **Arc Center Marks|Bool**: Włączenie / wyłączenie znaczników środka łuku okręgu.

-    **Center Scale|Float**: Dostosowanie rozmiaru znacznika środka łuku okręgu, jeśli jest włączony.

-    **Horiz Center Line|Bool**: Pokaż poziomą oś symetrii w widoku.

-    **Section Line Color|Color**: Ustaw kolor linii przekroju, jeśli ma to zastosowanie.

-    **Section Line Style|Enumeration**: Ustaw styl linii przekroju, jeśli ma to zastosowanie.

-    **Show All Edges|Bool**: Tymczasowo pokaż niewidoczne linie.

-    **Show Section Line|Bool**: W razie potrzeby pokaż / ukryj linię przekroju.

-    **Vert Center Line|Bool**: Pokaż pionową oś symetrii w widoku.


{{TitleProperty|Podświetlenie}}

-    **Highlight Adjust|Float**: W razie potrzeby dostosuj obrót podświetlenia szczegółu.

-    **Highlight Line Color|Color**: W razie potrzeby ustaw kolor podświetlonej linii.

-    **Highlight Line Style|Enumeration**: Ustaw styl podświetlonej linii, jeśli ma to zastosowanie.


{{TitleProperty|Linie}}

-    **Extra Width|Length**: Jeszcze nie wdrożone.

-    **Hidden Width|Length**: Grubość ukrytych linii, jeśli jest włączona.

-    **Iso Width|Length**: Grubość linii powierzchni izometrycznych *(u,v)* i linii wymiarowych.

-    **Line Width|Length**: Grubość widocznych linii. Zobacz informacje na stronie [Grupy linii](TechDraw_LineGroup/pl.md).

*(1)* właściwości te są wspólne dla wszystkich typów widoku.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Widok można utworzyć za pomocą [makrodefinicji](Macros/pl.md) i z konsoli [Python](Python/pl.md) przy użyciu następujących funkcji:


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





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw View/pl
