---
- GuiCommand:
   Name:TechDraw View
   Name/pl:Rysunek Techniczny: Widok
   MenuLocation:Rysunek Techniczny → Wstaw widok
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   SeeAlso:[Grupa rzutów](TechDraw_ProjectionGroup/pl.md), [Widok przekroju](TechDraw_SectionView/pl.md)
---

## Opis

Narzędzie Widok dodaje reprezentację jednego lub więcej obiektów do strony Rysunku. Jest to podstawowy element środowiska Rysunek Techniczny. Większość innych widoków pochodzi w jakiś sposób od metody Nowy widok.

![](images/TechDraw_View_example.png ) *Widok bryły sześcianu z ukrytymi liniami*

## Użycie

1.  Wybierz jeden lub więcej obiektów *(bryła, App::Part, Part::Feature, obiekt szkicu, \... Zobacz uwagi)* w oknie [widoku 3D](3D_view.md) lub [widoku drzewa](Tree_view/pl.md).
2.  Jeśli masz wiele stron rysunków w dokumencie, będziesz musiał również wybrać żądaną stronę na drzewku. Użyj przycisku **Ctrl**, aby wybrać wiele elementów w drzewie.
3.  Naciśnij przycisk **<img src="images/TechDraw_View.svg" width=16px> [Wstaw widok](TechDraw_View/pl.md)**.

Widok będzie próbował narysować cokolwiek z właściwością `kształt`. Możesz wybrać obiekty środowiska [Rysunek Roboczy](Draft_Workbench/pl.md) i również [Projekt Części: Zawartość](PartDesign_Body/pl.md). Widok wyodrębni również kształty z obiektów w kontenerze [App::Część](Std_Part.md) lub [Grupa](Std_Group/pl.md).

## Właściwości

### Dane


{{Properties_Title/pl|Podstawowe}}

-    {{PropertyData/pl|X}}: Położenie widoku w poziomie na stronie. *(1)*

-    {{PropertyData/pl|Y}}: Położenie widoku w pionie na stronie. *(1)*

-    {{PropertyData/pl|Zablokuj pozycję}}: Gdy wartość wynosi {{True}}, zapobiega przeciąganiu widoków w oknie GUI. Widok nadal może być przesuwany poprzez zmianę właściwości współrzędnych X,Y. *(1)*

-    {{PropertyData/pl|Obrót}}: Obrót widoku strony w kierunku przeciwnym do ruchu wskazówek zegara w stopniach. *(1)*

-    {{PropertyData/pl|Typ skali}}: **Dokument**: użyj skali strony. **Niestandardowy**: użyj skali własnej, unikalnej dla tego widoku. **Automatyczny**: dopasowanie rozmiaru widoku do strony. *(1)*

-    {{PropertyData/pl|Skala}}: Widok zostanie wyrenderowany na stronie w stosunku Skala:1 w odniesieniu do źródła. *(1)*

-    {{PropertyData/pl|Podpis}}: Opcjonalny krótki podpis.


{{Properties_Title/pl|Kosmetyczne}}


{{Properties_Title/pl|Parametry HLR}}

-    **Widok zgrubny**: Jeśli wartość ta wynosi {{True}}, Rysunek Roboczy użyje przybliżenia wielokąta do obliczenia geometrii rysunku. Jeżeli {{False}}, Rysunek Roboczy użyje algorytmu precyzyjnego. Widok zgrubny może być wyliczany znacznie szybciej dla złożonych modeli. Jakość rysunku jest obniżona, ponieważ każda krzywa jest aproksymowana jako seria krótkich odcinków linii. Wierzchołki nie są wyświetlane w trybie Widok zgrubny, ponieważ każdy krótki odcinek spowodowałby utworzenie dwóch nowych wierzchołków, co spowodowałoby bałagan na ekranie. Wymiary liniowe mogą zostać dodane do okna Widoku zgrubnego, ale ich użyteczność jest mało prawdopodobna.

:   
    **Uwaga:**Widok zgrubny jest podatny na błąd w OCCT *([\#3332](https://www.freecadweb.org/tracker/view.php?id=3332))*, który powoduje, że pozycja widoku na stronie jest nieco inna od podanych wartości X,Y.

-    **Wygładzanie widoczne**: Wyświetlanie wygładzonych linii włączone/wyłączone.

-    **Szew widoczny**: Wyświetlanie linii szwu włączone/wyłączone.

-    **Iso widoczne**: Wyświetlanie linii izometrycznych *(u,v)* włączone/wyłączone.

-    **Hard Hidden**: Wyświetlanie linii ukrytych włączone/wyłączone.

-    **Wygładzanie ukryte**: Ukrywanie wygładzonych linii włączone/wyłączone.

-    **Szew ukryty**: Ukrywanie linii szwu włączone/wyłączone.

-    **Iso ukryte**: Ukrywanie linii izometrycznych *(u,v)* włączone/wyłączone.

-    **Licznik Iso**: Liczba linii izometrycznych(u,v) do narysowania na każdej ścianie.


{{TitleProperty|Rzutowanie}}

-    {{PropertyData/pl|Pochodzenie}}: Powiązania z obiektami rysunkowymi, które mają być przedstawione.

-    {{PropertyData/pl|XPochodzenie}}: Odnośniki do obiektów rysunkowych w pliku zewnętrznym. {{Version/pl|0.19}}

-    {{PropertyData/pl|Kierunek}}: Wektor ten kontroluje kierunek, z którego patrzysz na obiekt. +X to prawo, -X to lewo, +Y to tył, -Y to przód *(patrząc w ekran)*, +Z to góra, a -Z to dół. Zatem widok z przodu to *(0,-1,0)*, a widok izometryczny to *(1,-1,1)*. *(1)*

-    {{PropertyData/pl|XKierunek}}: ten wektor kontroluje obrót widoku, według wartości Kierunek.{{Version/pl|0.19}}. *(1)*

-    {{PropertyData/pl|Perspektywa}}: Przyjmuje wartość {{True}} dla projekcji perspektywicznej, {{False}} dla projekcji ortogonalnej.

-    {{PropertyData/pl|Skupienie}}: Odległość od kamery do płaszczyzny projekcji dla rzutów perspektywicznych. Musi być dostosowana do obiektu. Odległość zbyt duża powoduje utratę perspektywy, odległość zbyt mała powoduje zniekształcenie obiektu.

*(1)* właściwości te są wspólne dla wszystkich typów widoku.

### Widok

-    {{PropertyView/pl|UtrzymujEtykietę}}: Zawsze pokazuj etykietę widoku jeśli wartość to {{True}}.

-    {{PropertyView/pl|SzerokośćLinii}}: Grubość widocznych linii. Zobacz stronę [GrupyLinii](TechDraw_LineGroup/pl.md).

-    {{PropertyView/pl|SzerokośćUkrytych}}: Grubość ukrytych linii, jeśli jest włączona.

-    {{PropertyView/pl|SzerokośćIso}}: Grubość izometrycznych *(u,v)* linii powierzchni i linii wymiarowych.

-    {{PropertyView/pl|SzerokośćDodatkowa}}: jeszcze nie wdrożone.

-    {{PropertyView/pl|PokażŚrodki}}: Włączanie / wyłączanie znaczników środka okręgu / łuku.

-    {{PropertyView/pl|SkalaŚrodka}}: Regulacja rozmiaru znacznika środka łuku po okręgu, jeśli jest włączona.

-    {{PropertyView/pl|PoziomąLinięŚrodka}}: Pokaż poziomą linię środkową w widoku.

-    {{PropertyView/pl|pionowąLinięŚrodka}}: Pokaż pionową linię środkową w widoku.

-    {{PropertyView/pl|PokażLinięPrzekroju}}: Pokaż / ukryj linię przekroju, jeśli dotyczy.

## Tworzenie skryptów {#tworzenie_skryptów}


**Zobacz również:**

[TechDraw API](TechDraw_API.md) i [Podstawy tworzenia skryptów FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie Nowy widok może być używane w [makrodefinicjach](macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
view = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewPart','View')
rc = page.addView(view)
FreeCAD.ActiveDocument.View.Source = [App.ActiveDocument.Box]
FreeCAD.ActiveDocument.View.Direction = (0.0,0.0,1.0)
```





{{TechDraw Tools navi

}}  
