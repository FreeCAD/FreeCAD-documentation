---
- GuiCommand:
   Name:TechDraw ComplexSection
   Name/pl:Rysunek Techniczny: Przekrój złożony
   MenuLocation:Rysunek Techniczny - Widoki - Wstaw przekrój złożony
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   Version:0.21
   SeeAlso:[Wstaw widok przekroju](TechDraw_SectionView/pl.md), [Wstaw widok](TechDraw_View/pl.md), [Wstaw grupę rzutów](TechDraw_ProjectionGroup/pl.md)
---

# TechDraw ComplexSection/pl



## Opis

Narzędzie **Wstaw przekrój złożony** wstawia widok przekroju na podstawie istniejącego widoku części i profilu.

<img alt="" src=images/TechDraw_QuarterSection_example.png  style="width:350px;"> 
*Widok przekroju ćwiartki utworzony za pomocą narzędzia Przekrój złożony.*

<img alt="" src=images/TechDraw_AlignedSection_example.png  style="width:350px;"> 
*Wyrównany widok przekroju utworzony za pomocą narzędzia Przekrój złożony.*

<img alt="" src=images/TechDraw_OffsetSection_example.png  style="width:350px;"> 
*Widok przekroju z przesunięciem utworzony za pomocą narzędzia Przekrój złożony*



## Użycie

1.  Wybierz widok części i obiekt profilu w oknie [widoku 3D](3D_view/pl.md) lub [widoku drzewa](Tree_view/pl.md). Profile to zazwyczaj Szkice, ale każdy obiekt, którego kształt można przekształcić w linię będzie działał.
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Nacisnąć przycisk **<img src="images/TechDraw_ComplexSection.svg" width=16px> '''Przekrój złożony'''**.
    -   Wybierz z menu opcję **Rysunek Techniczny → Widoki → <img src="images/TechDraw_ComplexSection.svg" width=16px> Wstaw przekrój złożony**.
3.  Otworzy się panel zadań, który pomoże obliczyć różne właściwości. Obliczane są rozsądne wartości dla widoku Kierunek, ale można je zmienić.

<img alt="" src=images/TechDraw_ComplexSection_Taskview1.png  style="width:" height="380px;"> <img alt="" src=images/TechDraw_ComplexSection_Taskview2.png  style="width:" height="380px;">



## Właściwości Przekroju złożonego 

Zapoznaj się również informacjami na stronie [właściwości widoku przekroju](TechDraw_SectionView/pl#Właściwości_widoku_przekroju.md) środowiska Rysunek Techniczny.



### Dane


{{TitleProperty|Narzędzie tnące}}

-    **Obiekt narzędzia tnącego linii łamanej**: Obiekt dokumentu, którego kształt zostanie użyty do wygenerowania profilu cięcia.

-    **Strategia rzutowania**: Kontroluje sposób, w jaki cięcie jest wykonywane i jak wynik jest wyświetlany na stronie:

    -   
        {{Value|Odsunięcie}}
        
        : Wykonuje proste cięcie kształtu źródłowego i rzutuje wynik.

    -   
        {{Value|Wyrównany}}
        
        : Wycina kształt źródłowy przy użyciu narzędzia utworzonego z każdego segmentu *(krawędzi)* profilu cięcia. Wyniki każdego cięcia są wyświetlane w układzie pionowym lub poziomym, w zależności od orientacji profilu cięcia.

    -   
        {{Value|Nierównoległe}}
        
        : Jak Wyrównany, ale segmenty profilu, które są równoległe do kierunku widoku, są pomijane.



## Uwagi

Zapoznaj się również informacjami na stronie [wstaw widoku przekroju](TechDraw_SectionView#Uwagi.md) środowiska Rysunek Techniczny.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie Wstaw przekrój złożony może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
doc = FreeCAD.ActiveDocument
box = doc.Box
profile = doc.Sketch
page = doc.Page

view = doc.addObject("TechDraw::DrawViewPart", "View")
page.addView(view)
view.Source = box
view.Direction = (0, 0, 1)

section = doc.addObject("TechDraw::DrawComplexSection", "ComplexSection")
page.addView(section)
section.BaseView = view
section.CuttingToolWireObject = profile
section.Direction = (0, 1, 0)
section.SectionNormal = (-1, 0, 0)
```



## Przykłady

Więcej informacji na temat widoków przekrojów i niektórych przypadków użycia można znaleźć na stronie [Przykłady przekrojów](TechDraw_Section_Examples/pl.md).

<img alt="" src=images/TechDraw_ExampleSection-10.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-13.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-15.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-17.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-34.png  style="width:80px;"> <img alt="" src=images/TechDraw_ExampleSection-35.png  style="width:80px;">





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ComplexSection/pl
