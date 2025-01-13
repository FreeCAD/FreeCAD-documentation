---
 GuiCommand:
   Name: TechDraw ArchView
   Name/pl: Rysunek Techniczny: Wstaw obiekt środowiska Architektura
   MenuLocation: Rysunek Techniczny , Widoki , Wstaw obiekt środowiska BIM
   Workbenches: TechDraw_Workbench/pl, BIM_Workbench/pl
   SeeAlso: Arch_SectionPlane/pl
---

# TechDraw ArchView/pl



## Opis

Narzędzie **Wstaw obiekt środowiska Architektura** wstawia widok **<img src="images/Arch_SectionPlane.svg" width=16px> [przekroju](Arch_SectionPlane/pl.md)** na stronie [Rysunku Technicznego](TechDraw_PageDefault/pl.md).


{{Version/pl|1.0}}

: Narzędzie [Wstaw widok](TechDraw_View/pl.md) również może wstawić widok obiektu środowiska Architektura.

<img alt="" src=images/TechDraw_Arch_example.jpg  style="width:500px;">



## Użycie

1.  Wybierz płaszczyznę przekroju architektonicznego w oknie [widoku 3D](3D_view/pl.md) lub [widoku drzewa](Tree_view/pl.md).
2.  Jeśli w dokumencie znajduje się wiele stron rysunku: opcjonalnie dodaj żądaną stronę do zaznaczenia, wybierając ją w [Widoku drzewa](Tree_view/pl.md).
3.  Wybierz opcję **Rysunek Techniczny → Widoki z innych środowisk roboczych → <img src="images/TechDraw_ArchView.svg" width=16px> Wstaw obiekt środowiska pracy BIM** z menu.
4.  Jeśli w dokumencie znajduje się wiele stron rysunku i żadna strona nie jest wyświetlana w [obszarze widoku głównego](Main_view_area/pl.md), a strona nie została jeszcze wybrana, otworzy się okno dialogowe **Wybór strony**:
    1.  Wybierz żądaną stronę.
    2.  Naciśnij przycisk **OK**.



## Opcje

-   Widok Architektoniczny jest renderowany przez środowisko pracy [BIM](BIM_Workbench/pl.md).
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

Widok architektoniczny jest renderowany w środowisku [BIM](BIM_Workbench/pl.md), dlatego środowisko Rysunek Techniczny ma ograniczoną kontrolę nad jego wyglądem. Może być konieczne wprowadzenie zmian w środowisku pierwotnym, aby uzyskać pożądaną reprezentację.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt środowiska Architektura, formalnie obiekt {{Incode|TechDraw::DrawViewArch}} ma [właściwości](TechDraw_View/pl#Właściwości_-_Widok_części.md) wspólne dla wszystkich typów Widoków. Ma też następujące dodatkowe właściwości:



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

-    **Odstęp wierszy|Float**: Odstęp między wierszami do użycia dla tekstów wielowierszowych. {{Version/pl|1.0}}


{{TitleProperty|Widok rysunku}}

-    **Symbol|String|Hidden**: Kod SVG definiujący ten symbol.

-    **Editable Texts|StringList**: Wartości podstawienia dla edytowalnych ciągów w tym symbolu.

-    **Owner|Link**: Cecha, do której ten symbol jest dołączony. {{Version/pl|1.0}}



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
