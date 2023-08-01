---
- GuiCommand:/pl
   Name:TechDraw GeometricHatch
   Name/pl:Rysunek Techniczny: Zastosuj na powierzchni kreskowanie geometryczne
   MenuLocation:Rysunek Techniczny → Kreskowanie → Zastosuj na powierzchni kreskowanie geometryczne
   Workbenches:[Rysunek Techniczny](TechDraw_Workbench/pl.md)
   SeeAlso:[Kreskowanie powierzchni](TechDraw_Hatch/pl.md), [Kreskowanie](TechDraw_Hatching/pl.md)
---

# TechDraw GeometricHatch/pl



## Opis

Narzędzie **TechDraw GeometricHatch** wypełnia zamknięty obszar w widoku wzorem opartym na specyfikacji kreskowania AutoDesk PAT. Alternatywnie można użyć <img alt="" src=images/TechDraw_Hatch.svg  style="width:16px;"> [Kreskowanie powierzchni za pomocą pliku obrazu](TechDraw_Hatch/pl.md) wykorzystuje wzory kreskowania oparte na SVG. Aby uzyskać szczegółowe informacje, zobacz stronę [Kreskowanie](TechDraw_Hatching/pl.md).

<img alt="" src=images/TechDraw_GeomHatch_example.png  style="width:300px;"> 
*Geometryczny wzór kreskowania na powierzchni ściany.*



## Użycie

1.  Wybierz zamknięty obszar w widoku.
2.  Istnieje kilka sposobów na wywołanie tego narzędzia:
    -   Naciśnij przycisk **<img src="images/TechDraw_GeometricHatch.svg" width=16px> '''Zastosuj na powierzchni kreskowanie geometryczne'''**.
    -   Wybierz z menu **Rysunek Techniczny → Kreskowanie → <img src="images/TechDraw_GeometricHatch.svg" width=16px> Zastosuj na powierzchni kreskowanie geometryczne**.
3.  Otworzy się panel zadań **Zastosuj na powierzchni kreskowanie geometryczne**.
4.  Opcjonalnie można zmienić **Plik wzoru**, **Nazwa wzoru** **Skala wzoru**, **Grubość linii** i **Kolor linii**.
5.  Naciśnij przycisk **OK**.



## Uwagi

-   Obiekty kreskowania są podatne na problemy z *[nazewnictwem topologicznym](Topological_naming_problem/pl.md)*. Aby uzyskać więcej informacji, zobacz informacje w narzędziu [Rysunek techniczny: Wymiar długości](TechDraw_LengthDimension/pl.md). Zaleca się, aby kreskowanie było jednym z ostatnich kroków w procesie rysowania.

Niewielki zestaw przykładowych wzorów jest dostępny w prezentowanych lokalizacjach:


```python
$INSTALL_DIR/data/Mod/TechDraw/PAT/FCPAT.pat
```


`$INSTALL_DIR`

to katalog, w którym zainstalowano FreeCAD, na przykład:


```python
/usr/share/freecad/data/Mod/TechDraw/PAT/FCPAT.pat
```



## Właściwości

-    **Źródło**: Widok i ściana, które mają otrzymać wzór kreskowania.

-    **Plik wzoru**: Lokalizacja pliku PAT do użycia.

-    **Nazwa wzoru**: Nazwa specyfikacji PAT w ramach Pliku Wzorca.

-    **Skala wzoru**: Skala, która ma być zastosowana do wzorca *(wartość musi być większa od 0.0)*.

-    **Waga wzoru**: Grubość linii wzoru.

-    **Kolor wzoru**: Kolor linii wzoru.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Zastosuj na powierzchni kreskowanie geometryczne** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
hatch = FreeCAD.ActiveDocument.addObject("TechDraw::DrawGeomHatch", "GeomHatch")
hatch.Source = (view1, ["Face0"])
hatch.FilePattern = "path/to/myPATfile.pat"
hatch.NamePattern = "Diamond"
page.addView(hatch)
```

Możliwe jest również użycie silnika kreskowania geometrycznego środowiska Rysunek Techniczny do utworzenia złożonego obiektu w przestrzeni 3D. Należy zwrócić uwagę, aby ściana bazowa leżała na płaszczyźnie XY, ponieważ algorytm nie jest jeszcze dostosowany do innych przypadków:


```python
import TechDraw
face = Part.makePlane(10, 10)
patfile = "path/to/myPATfile.pat"
pattern = "Diamond"
scale = 10
hatch = TechDraw.makeGeomHatch(face, scale, pattern, patfile)
Part.show(hatch)
```





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw GeometricHatch/pl
