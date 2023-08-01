---
- GuiCommand:/pl
   Name:TechDraw DraftView
   Name/pl:Rysunek Techniczny: Wstaw obiekt środowiska Rysunek Roboczy
   MenuLocation:Rysunek Techniczny → Widoki → Wstaw obiekt środowiska Rysunek Roboczy
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md), [Rysunek Roboczy](Draft_Workbench/pl.md)
   SeeAlso:[Wstaw obiekt środowiska Architektura](TechDraw_ArchView/pl.md)
---

# TechDraw DraftView/pl



## Opis

Narzędzie **Wstaw obiekt środowiska Rysunek Roboczy** wstawia widok wybranego obiektu opartego na obiekcie [Część](Part_Workbench/pl.md) lub grupy do strony rysunku. W przeciwieństwie do standardowego <img alt="" src=images/TechDraw_View.svg  style="width:24px;"> [widoku](TechDraw_View/pl.md), widoki utworzone za pomocą tego narzędzia są obsługiwane przez środowisko <img alt="" src=images/Workbench_Draft.svg  style="width:24px;"> [Rysunek Roboczy](Draft_Workbench/pl.md) i specjalnie zaprojektowane do wyświetlania obiektów 2D. Zobacz [uwagi](#Uwagi.md).

![](images/TechDraw_DraftView_example.png ) 
*Elementy szkicu, takie jak okręgi i szyki, importowane do strony Rysunku Technicznego.*



## Użycie

1.  Opcjonalnie obróć [widok 3D](3D_view/pl.md). Kierunek ujęcia widoku w oknie [widoku 3D](3D_view/pl.md) określa początkową wartość właściwości widoku **Kierunek**.
2.  Wybierz jeden lub więcej obiektów w oknie [widoku 3D](3D_view/pl.md) lub [widoku drzewa](Tree_view/pl.md). Dla każdego obiektu zostanie utworzony osobny widok.
3.  Jeśli w dokumencie znajduje się wiele stron rysunku: opcjonalnie dodaj żądaną stronę do zaznaczenia, wybierając ją w oknie [widoku drzewa](Tree_view/pl.md).
4.  Istnieje kilka sposobów wywołania narzędzia:
5.  Naciśnij przycisk **<img src="images/TechDraw_DraftView.svg" width=16px> '''Wstaw obiekt środowiska Rysunek Roboczy'''**.
    -   Wybierz opcję z menu **Rysunek Techniczny → Widoki → <img src="images/TechDraw_DraftView.svg" width=16px> Wstaw obiekt środowiska Rysunek Roboczy**.
6.  Jeśli w dokumencie znajduje się wiele stron rysunku, a strona nie została jeszcze wybrana, otworzy się okno dialogowe **Wybór strony**: {{Version/pl|0.20}}.
    1.  Wybierz żądaną stronę.
    2.  Naciśnij przycisk **OK**.



## Opcje

-   Utworzenie warstwy DraftView będzie rekurencyjnie obsługiwać wszystkie obiekty znajdujące się w tej warstwie. Widok jest aktualizowany automatycznie po zmianie zawartości warstwy
-   Nie ma usuwania ukrytych linii. Każda ściana znaleziona w obsługiwanym obiekcie *(obiektach)* zostanie po prostu rzutowana wzdłuż wektora kierunku, nie są podejmowane żadne konkretne działania, gdy ściany nakładają się na siebie.
-   Widok szkicu obsługuje również wszystkie obiekty szkicu, które nie są oparte na częściach, takie jak wymiary i teksty.
-   Kolor, szerokość linii i wzór linii można określić we właściwościach. Wzory linii można precyzyjnie dostosować, bezpośrednio podając wartość [stroke-dasharray](https://www.w3.org/TR/SVG/painting.html#StrokeProperties), np. 3,5
-   Rzutowane ściany są wypełniane kolorem ściany.



## Uwagi

Widok Rysunku Roboczego jest renderowany w środowisku [Rysunek Roboczy](Draft_Workbench/pl.md), dlatego środowisko Rysunek Techniczny ma ograniczoną kontrolę nad jego wyglądem. Konieczne może być wprowadzenie zmian w środowisku pierwotnym, aby uzyskać pożądaną reprezentację.



## Właściwości

Zapoznaj się również informacjami na stronie [właściwości widoku](TechDraw_View/pl#Widok.md) środowiska Rysunek Techniczny.



### Dane


{{TitleProperty|Widok Rysunek Roboczy}}

-    **Źródło|Link**: Obiekt Draft do wyświetlenia.

-    **Szerokość linii|Float**: Szerokość linii, niezależnie od skali.

-    **Rozmiar czcionki|Float**: Rozmiar wszystkich tekstów pojawiających się w tym widoku *(tekstów i wymiarów)*.

-    **Kierunek |Vector**: Kierunek rzutowania do użycia.

-    **Kolor|Color**: Kolor linii.

-    **Styl linii|String**: Styl linii używany dla tego widoku. Może to być {{Value|Solid}}, {{Value|Kreskowana}}, {{Value|Kreska kropka}}, {{Value|Kropkowana}} lub wzór linii SVG, taki jak {{Value|0.20,0.20}}.

-    **odstęp wierszy|Float**: Odstęp między wierszami tekstu dla tekstów wielowierszowych.

-    **Nadpisz styl|Bool**: Jeśli parametr przyjmuje wartość {{TRUE/pl}}, kolor linii, szerokość i styl tego widoku będą zastępować kolory, szerokość i styl renderowanego obiektu.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Wstaw obiekt środowiska Rysunek Roboczy** może być używane w [makrodefinicjach](macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
dv = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDraft','TestDraft')
dv.Source = myDraftbject
rc = page.addView(dv)
```





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DraftView/pl
