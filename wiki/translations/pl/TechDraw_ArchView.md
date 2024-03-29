---
 GuiCommand:
   Name: TechDraw ArchView
   Name/pl: Rysunek Techniczny: Wstaw obiekt środowiska Architektura
   MenuLocation: Rysunek Techniczny , Widoki , Wstaw obiekt środowiska Architektura
   Workbenches: TechDraw_Workbench/pl, Arch_Workbench/pl
   SeeAlso: Arch_SectionPlane/pl
---

# TechDraw ArchView/pl



## Opis

Narzędzie **Wstaw obiekt środowiska Architektura** wstawia widok **<img src="images/Arch_SectionPlane.svg" width=16px> [przekroju](Arch_SectionPlane/pl.md)** na stronie [Rysunku Technicznego](TechDraw_PageDefault/pl.md).

![](images/TechDraw_Arch_example.jpg )



## Użycie

1.  Wybierz pojedynczą płaszczyznę przekroju architektonicznego w oknie [widoku 3D](3D_view/pl.md) lub [widoku drzewa](Tree_view/pl.md).
2.  Jeśli w dokumencie znajduje się wiele stron rysunku: opcjonalnie dodaj żądaną stronę do zaznaczenia, wybierając ją w [Widoku drzewa](Tree_view/pl.md).
3.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij **<img src="images/TechDraw_ArchView.svg" width=24px> '''Wstaw obiekt środowiska Architektura'''**.
    -   Wybierz opcję z menu **Rysunek Techniczny → Widoki → <img src="images/TechDraw_ArchView.svg" width=16px> Wstaw obiekt środowiska Architektura**.
4.  Jeśli w dokumencie znajduje się wiele stron rysunku, a strona nie została jeszcze wybrana, otworzy się okno dialogowe **Wybór strony**: {{Version/pl|0.20}}.
    1.  Wybierz żądaną stronę.
    2.  Naciśnij przycisk **OK**.



## Opcje

-   Widok Architektoniczny jest renderowany przez środowisko pracy [Architektura](Arch_Workbench/pl.md).
-   [Wymiary](Draft_Snap_Dimensions/pl.md), [teksty](Draft_Text/pl.md) i każdy inny obiekt 2D *(szkic lub rysunek)* uwzględniany przez płaszczyznę przekroju jest renderowany \"tak jak jest\" *(bez przecięć lub ukrytych linii)* na wierzchu geometrii bryłowej.
-   Objętość [kubatury](Arch_Space/pl.md) nie jest renderowana, renderowana jest tylko etykieta.
-   Linie przecięcia, linie rzutowane *(jeśli właściwość Pokaż ukryte jest ustawiona na {{True/pl}})* i linie 2D powyżej mogą być renderowane z różnymi szerokościami linii. Można to skonfigurować w preferencjach środowiska Architektura.
-   Widok Architektoniczny posiada dwa tryby renderowania:
    -   Szkielet, który wykorzystuje algorytmy OpenCasCade środowiska [Rysunek Techniczny](TechDraw_Workbench/pl.md), jest szybki i generuje tylko linie *(bez możliwości wypełniania ścian)*.
    -   Bryła, który jest oparty na algorytmie [Paintera](https://en.wikipedia.org/wiki/Painter%27s_algorithm) i jest w stanie renderować ściany wypełnione kolorem kształtu. Jest jednak znacznie wolniejszy i może zawieść w wielu sytuacjach.

:   Poniższy obraz ilustruje różnicę między tymi dwoma trybami renderowania:





:   ![](images/TechDraw_Arch_rendering.jpg )

-   Renderowana jest tylko linia bazowa [Rury](Arch_Pipe/pl.md), a nie cała objętość rury:

:   ![](images/TechDraw_Arch_piping.jpg )



## Uwagi

Widok architektoniczny jest renderowany w środowisku [Architektura](Arch_Workbench/pl.md), dlatego środowisko Rysunek Techniczny ma ograniczoną kontrolę nad jego wyglądem. Może być konieczne wprowadzenie zmian w środowisku pierwotnym, aby uzyskać pożądaną reprezentację.



## Właściwości

Zapoznaj się również informacjami na stronie [właściwości widoku](TechDraw_View/pl#Widok.md) środowiska Rysunek Techniczny.



### Dane


{{TitleProperty|Widok Architektury}}

-    **źródło|Link**: Obiekt płaszczyzny przekroju do wyświetlenia.

-    **Wszystko włączone|Bool**: Czy ukryte obiekty muszą być wyświetlane, czy nie. Jeśli parametr ma wartość `False`, renderowane są tylko obiekty widoczne w widoku 3D.

-    **Tryb renderowania|Enumeration**: Tryb renderowania do użycia, {{Value|Solid}} lub {{Value|Wireframe}}.

-    **Wypełnij przestrzenie|Bool**: Jeśli parametr ma wartość {{TRUE/pl}}, Arch Spaces są wyświetlane jako kolorowy obszar.

-    **Pokaż ukryte|Bool**: Czy ukryta geometria (część geometrii, która leży za płaszczyzną przekroju) jest pokazywana, czy nie. Będzie ona renderowana linią przerywaną, którą można skonfigurować w preferencjach środowiska Architektura.

-    **Pokaż wypełnienie|Bool**: Czy wycięte obszary muszą być wypełnione szarym kolorem, czy nie.

-    **Szerokość linii|Float**: Szerokość głównych linii. Współczynniki szerokości linii cięcia i linii rzutowanych/2D można skonfigurować w preferencjach Arch.

-    **Rozmiar czcionki|Float**: Rozmiar wszystkich tekstów wyświetlanych w tym widoku.

-    **Szerokość linii cięcia|Float**: Szerokość linii cięcia w tym widoku.

-    **Dołącz do Arch|Bool**: Jeśli parametr ma wartość {{TRUE/pl}}, ściany i struktury zostaną połączone materiałem.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Wstaw obiekt środowiska Architektura** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
dv = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewArch','TestArch')
dv.Source = mySectionPlane
rc = page.addView(dv)
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ArchView/pl
