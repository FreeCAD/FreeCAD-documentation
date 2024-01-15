---
 GuiCommand:
   Name: TechDraw Symbol
   Name/pl: Rysunek Techniczny: Wstaw symbol SVG
   MenuLocation: Rysunek Techniczny , Widoki , Wstaw symbol SVG
   Workbenches: TechDraw_Workbench/pl
   SeeAlso: TechDraw_Templates/pl, Draft_SVG/pl
---

# TechDraw Symbol/pl



## Opis

Narzędzie **Wstaw symbol SVG** wstawia plik [SVG](SVG/pl.md) na stronę. Symbolem tym może być wszystko, co pomaga w dodawaniu adnotacji do rysunku i nie musi być potem modyfikowane.

<img alt="" src=images/TechDraw_SymbolSVG_sample.png  style="width:250px;"> 
*Róża wiatrów dodana do strony rysunku; ten symbol jest dostępny po zainstalowaniu dodatku "symbols_library" za pomocą [Menadżera dodatków](Std_AddonMgr/pl.md).*



## Użycie

1.  Jeśli w dokumencie znajduje się wiele stron rysunku: opcjonalnie aktywuj żądaną stronę, wybierając ją w [Widoku drzewa](Tree_view.md).
2.  Istnieje kilka sposobów wywołania narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_Symbol.svg" width=16px> '''Wstaw symbol SVG'''**.
    -   Wybierz z menu opcję **Rysunek Techniczny → Widoki → <img src="images/TechDraw_Symbol.svg" width=16px> Wstaw symbol SVG**.
3.  Jeśli w dokumencie znajduje się wiele stron rysunków, a strona nie została jeszcze aktywowana, otworzy się okno dialogowe **Wybór strony**: {{Version/pl|0.20}}.
    1.  Wybierz żądaną stronę.
    2.  Naciśnij przycisk **OK**.
4.  Zostanie otwarte okno dialogowe pliku.
5.  Wybierz lokalizację i nazwę pliku.
6.  Symbol zostanie wstawiony.
7.  Opcjonalnie można zmienić jego właściwość **Skala**, aby dostosować jego rozmiar.



## Uwagi

-    **Typ Skali**dla symboli jest zawsze ustawione na *Użytkownika* podczas tworzenia. Jest to wygodne, ponieważ symbole są prawie zawsze skalowane inaczej niż pozostałe obiekty na stronie.



## Właściwości

Zapoznaj się również informacjami na stronie [właściwości widoku](TechDraw_View/pl#Widok.md) środowiska Rysunek Techniczny.


{{TitleProperty|Widok rysunku}}

-    **Tekst edytowalny**: Lista edytowalnych tekstów, jeśli istnieją.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Wstaw symbol SVG** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
sym = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewSymbol','TestSymbol')
rc = page.addView(anno)
f = open(unicode(symbolFileSpec,'utf-8'),'r')
svg = f.read()
f.close()
sym.Symbol = svg
rc = page.addView(sym)
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Symbol/pl
