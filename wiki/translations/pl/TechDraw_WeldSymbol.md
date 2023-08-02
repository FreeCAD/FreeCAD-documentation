---
- GuiCommand:
   Name: TechDraw WeldSymbol
   Name/pl: Rysunek Techniczny: Dodaj informacje spawalnicze do linii odniesienia
   MenuLocation: TechDraw -> Dodaj informacje spawalnicze do linii odniesienia
   Workbenches: TechDraw_Workbench/pl
   Version: 0.19
   SeeAlso: TechDraw_LeaderLine/pl
---

# TechDraw WeldSymbol/pl


</div>



## Opis

Narzędzie **Dodaj informacje spawalnicze do linii odniesienia** dodaje specyfikacje spawania do istniejącej linii prowadzącej.

<img alt="" src=images/TechDraw_WeldingSymbol_example.png  style="width:330px;"> 
*Specyfikacja spawania dodana do linii pomocniczej.*



## Użycie


<div class="mw-translate-fuzzy">

1.  Wybierz istniejącą [linię odniesienia](TechDraw_LeaderLine/pl.md).
2.  Naciśnij przycisk **<img src="images/TechDraw_WeldSymbol.svg" width=16px> '''Dodaj informacje spawalnicze do linii odniesienia'''**.
3.  Otworzy się panel zadań. Umożliwia on ustawienie poszczególnych symboli spawania i towarzyszącego im tekstu, które mają zostać dodane do linii odniesienia.
4.  Naciśnij przycisk **OK**, aby zamknąć okno dialogowe i zapisać zmiany.
5.  Po utworzeniu symbolu spawania można go edytować, klikając dwukrotnie symbol spawania w drzewie.


</div>

## Notes

-   After creation a welding symbol can be edited by double clicking it in the [Tree view](Tree_view.md).
-   There is a [preference parameter](TechDraw_Preferences.md) for the default welding symbol directory. You can add your own symbols in a personal directory.



## Właściwości



### Symbol spawu 

-    **Spoina dookoła**: Pokazuje symbol *Spoina dookoła* *(okrąg)* na załamaniu linii prowadzącej.

-    **Spawać na montażu**: Pokazuje symbol *Spawać na montażu* (flaga) na załamaniu linii odniesienia.

-    **Spoina naprzemienna**: Przesuwa dolny symbol, aby wskazać spoiny naprzemienne.

-    **Tekst ogona**: Tekst wyświetlany na końcu linii prowadzącej.



### Kafelek

Każdy pojedynczy symbol *(\"strona strzałki\" i \"druga strona\")* jest reprezentowany przez obiekt \"kafelek\". Symbol spawania ma 1 lub 2 powiązane z nim kafelki. Każdy z nich ma następujące właściwości:

-    **Kafelek nadrzędny**: Nadrzędny symbol spoiny

-    **Wiersz kafelka**: Wiersz kafelka. 0 oznacza powyżej linii, -1 poniżej linii. **Uwaga:** Jeśli zmienisz rząd jednego kafelka, musisz również zmienić kafelek dla drugiej strony! W ten sposób można odwrócić strony.

-    **Kolumna kafelka**: Kolumna kafelka. W tej chwili jest to zawsze 0, dlatego właściwość nie jest edytowalna.

-    **Plik symbolu**: Katalog i nazwa pliku SVG symbolu.

-    **Symbol dołączony**: Katalog i nazwa pliku SVG rzeczywistego dołączonego symbolu. *(Jest to katalog tymczasowy)*.

-    **Tekst z lewej**: Tekst wyświetlany po lewej stronie symbolu SVG.

-    **Tekst środkowy**: Tekst wyświetlany powyżej/poniżej symbolu SVG.

-    **Tekst z prawej**: Tekst wyświetlany po prawej stronie symbolu SVG.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Dodaj informacje spawalnicze do linii odniesienia** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
symbolName = "DrawWeldSymbol001")
symbolType = "TechDraw::DrawWeldSymbol"
App.activeDocument().addObject(symbolType, symbolName)
App.activeDocument().Page.addView(App.activeDocument().DrawWeldSymbol001)
App.activeDocument().DrawWeldSymbol001.Leader = myLeader
App.activeDocument().DrawWeldSymbol001.AllAround = True
App.activeDocument().DrawWeldSymbol001.FieldWeld = True
App.activeDocument().DrawWeldSymbol001.AlternatingWeld = True
App.activeDocument().DrawWeldSymbol001.TailText = "process text"

tileName = "DrawTileWeld001"
tileType = "TechDraw::DrawTileWeld"
App.activeDocument().addObject(tileType, tileName)
App.activeDocument().DrawTileWeld001.TileParent = App.activeDocument().DrawWeldSymbol001
App.activeDocument().DrawTileWeld001.TileRow = 0
App.activeDocument().DrawTileWeld001.TileColumn = 0
App.activeDocument().DrawTileWeld001.SymbolFile = fullPathToMySvgFile
App.activeDocument().DrawTileWeld001.LeftText = "left text"
App.activeDocument().DrawTileWeld001.RightText = "right text"
App.activeDocument().DrawTileWeld001.CenterText = "center text"
```



## Kafelki symboli SVG 

Poszczególne symbole są tworzone przez pliki SVG 64x64 pikseli. Dodatkowe symbole SVG można utworzyć w programie, takim jak [Inkscape](https://en.wikipedia.org/wiki/Inkscape), używając jednego z symboli dostarczonych przez FreeCAD jako szablonu.

<img alt="" src=images/Techdraw-WeldingSymbolLayoutArrow.svg  style="width:128px;"> <img alt="" src=images/Techdraw-WeldingSymbolLayoutOther.svg  style="width:128px;">

-   Poszczególne symbole są tworzone przez pliki SVG o rozmiarze 64x64 *(nominalnie)* pikseli. Kafelki mają w rzeczywistości \"obramowanie\" o rozmiarze 4px. Obramowanie zapewnia ładne połączenie linii prowadzącej i symbolu.
-   Symbol jest rysowany w kolorze czarnym na przezroczystym tle. Szerokość obrysu wynosi 0,5 mm.
-   Linia prowadząca przechodzi poniżej symboli po stronie strzałki *(patrz obrazek po lewej)* i powyżej symboli po \"drugiej\" stronie *(patrz obrazek po prawej)*.
-   Nie ma określonego standardu nazewnictwa innego niż dodanie \"Góra / Dół\" do symboli strzałki / drugiej strony.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw WeldSymbol/pl
