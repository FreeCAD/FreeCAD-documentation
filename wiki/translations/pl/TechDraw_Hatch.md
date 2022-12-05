---
- GuiCommand:/pl
   Name:TechDraw Hatch
   Name/pl:TechDraw: Zakreskuj
   MenuLocation:Rysunek techniczny → Kreskowanie na powierzchni za pomocą pliku obrazu
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   SeeAlso:[Zastosuj kreskowanie geometryczne na powierzchni](TechDraw_GeometricHatch/pl.md), [Kreskowanie](TechDraw_Hatching/pl.md)
---

# TechDraw Hatch/pl

## Opis

Narzędzie <img alt="" src=images/TechDraw_Hatch.svg  style="width:24px;"> **Kreskowanie** środowiska Rysunek Techniczny wypełnia zamknięty obszar w widoku wzorcem kreskowania, którym mogą być pliki [SVG](SVG/pl.md) lub [bitmap](Bitmap/pl.md) *({{Version/pl|1.0}})*. W odróżnieniu od tego, narzędzie <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:24px;"> [kreskowanie geometryczne](TechDraw_GeometricHatch/pl.md) wykorzystuje konkretny plik wzoru PAT, szczegółowe informacje znajdują się na stronie [kreskowanie](TechDraw_Hatching/pl.md).

<img alt="" src=images/TechDraw_Hatch_example.png  style="width:300px;">



*SVG hatch pattern on a face*

## Użycie

1.  Wybierz zamknięty obszar w widoku.
2.  Istnieje kilka sposobów na wywołanie tego narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_Hatch.svg" width=16px> [Kreskowanie powierzchni za pomocą pliku obrazu](TechDraw_Hatch/pl.md)**.
    -   Wybierz opcję **Rysunek Techniczny → <img src="images/TechDraw_Hatch.svg" width=16px> Kreskowanie powierzchni za pomocą pliku obrazu** z menu.
3.  Otworzy się panel zadań **Zastosuj kreskowanie na powierzchni**.
4.  Opcjonalnie zmień **Plik z wzorem**.
5.  Opcjonalnie zmień wartości w polach **Skala wzoru** i **Kolor linii**. Ustawienia te są ignorowane dla wzorów bitmapowych.
6.  Naciśnij przycisk **OK**.

## Uwagi

-   Obiekty kreskowania są podatne na problemy z *[nazewnictwem topologicznym](Topological_naming_problem/pl.md)*. Aby uzyskać więcej informacji, zobacz informacje w narzędziu [Rysunek techniczny: Wymiar długości](TechDraw_LengthDimension/pl.md). Zaleca się, aby kreskowanie było jednym z ostatnich kroków w procesie rysowania.
-   Przykładowe wzory [SVG](SVG/pl.md) są dostępne lokalnie w:

:   
    
```python
    $INSTALL_DIR/data/Mod/TechDraw/Patterns
    
```
    

\" Gdzie `$INSTALL_DIR` to katalog, w którym zainstalowano FreeCAD, na przykład:

:   
    
```python
    /usr/share/freecad/data/Mod/TechDraw/Patterns
    
```
    

:   Są one również dostępne na [GitHub](https://github.com/FreeCAD/FreeCAD/tree/master/src/Mod/TechDraw/Patterns).

## Właściwości

-    **Source**: Widok i ściana, aby otrzymać wzór kreskowania.

-    **Hatch Pattern**: Pełna ścieżka i nazwa pliku wzorca SVG.

-    **Hatch Color**: Wzór kreskowania zostanie wyświetlony w tym kolorze.

-    **Hatch Scale**: Modyfikator rozmiaru wzoru kreskowania.

## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie Hatch może być używane w [makrodefinicjach](macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
hatch = FreeCAD.ActiveDocument.addObject('TechDraw::DrawHatch','Hatch')
hatch.Source = (view1,["Face0"])
hatch.HatchPattern = hatchFileSpec
rc = page.addView(hatch)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Hatch/pl
