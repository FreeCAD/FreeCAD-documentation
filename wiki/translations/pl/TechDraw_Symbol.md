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

Narzędzie **Wstaw symbol SVG** wstawia obiekt Symbol. Jest to okrojony widok, który zawiera tylko jeden plik [SVG](SVG/pl.md) zgodnie ze specyfikacją svg-tiny (zobacz [Rysunek Techniczny: Szablony](TechDraw_Templates/pl#Uwagi.md)).

Symbol może być czymkolwiek, co pomaga opisać rysunek i nie musi być dalej modyfikowane, ale może zawierać [edytowalny tekst](Svg_Namespace/pl#freecad_editable.md).


{{Version/pl|1.0}}

: Narzędzie [Wstaw widok](TechDraw_View/pl.md) również może utworzyć Symbol.

<img alt="" src=images/TechDraw_SymbolSVG_sample.png  style="width:250px;"> 
*Róża wiatrów dodana do strony rysunku; ten symbol jest dostępny po zainstalowaniu dodatku "symbols_library" za pomocą [Menadżera dodatków](Std_AddonMgr/pl.md).*



## Użycie

1.  Jeśli w dokumencie znajduje się wiele stron rysunku: opcjonalnie aktywuj żądaną stronę, wybierając ją w [Widoku drzewa](Tree_view.md).
2.  Wybierz opcję **Rysunek Techniczny → Widoki → <img src="images/TechDraw_Symbol.svg" width=16px> Wstaw symbol SVG** z menu.
3.  Jeśli w dokumencie znajduje się wiele stron rysunków, a strona nie została jeszcze aktywowana, otworzy się okno dialogowe **Wybór strony**:
    1.  Wybierz żądaną stronę.
    2.  Naciśnij przycisk **OK**.
4.  Zostanie otwarta przeglądarka plików.
5.  Wybierz plik SVG.
6.  Symbol zostanie wstawiony.
7.  Opcjonalnie można zmienić jego właściwość **Skala**, aby dostosować jego rozmiar.



## Uwagi

-    **Typ Skali**dla symboli jest zawsze ustawione na *Użytkownika* podczas tworzenia. Jest to wygodne, ponieważ symbole są prawie zawsze skalowane inaczej niż pozostałe obiekty na stronie.



## Właściwości

Zobacz również stronę: [Edytor właściwości](Property_editor/pl.md).

Symbol, formalnie obiekt {{Incode|TechDraw::DrawViewSymbol}} ma [właściwości](TechDraw_View/pl#Właściwości_-_Widok_części.md) wspólne dla wszystkich typów Widoków. Ma też następujące dodatkowe właściwości:



### Dane


{{TitleProperty|Widok rysunku}}

-    **Symbol|String|Hidden**: Kod SVG definiujący ten symbol.

-    **Editable Texts|StringList**: Wartości podstawienia dla edytowalnych ciągów w tym symbolu.

-    **Owner|Link**: Cecha, do której ten symbol jest dołączony. {{Version/pl|1.0}}



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





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Symbol/pl
