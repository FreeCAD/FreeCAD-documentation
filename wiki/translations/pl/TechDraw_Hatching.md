# TechDraw Hatching/pl
{{TOCright}}



## Opis

Środowisko pracy TechDraw zawiera dwa narzędzia do kreskowania:

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width:32px;"> [Kreskowanie powierzchni za pomocą pliku obrazu](TechDraw_Hatch/pl.md) *(na podstawie kafelków SVG lub obrazów bitmapowych)*.
-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:32px;"> [Zastosuj na powierzchni kreskowanie geometryczne ](TechDraw_GeometricHatch/pl.md) *(na podstawie linii)*.



## Kreskowanie oparte na obrazie 

<img alt="" src=images/TechDraw_Hatch.svg  style="width:16px;"> [Kreskowanie powierzchni za pomocą pliku obrazu](TechDraw_Hatch/pl.md) używa kafelków [SVG](SVG/pl.md) lub obrazów bitmapowych ({{Version/pl|0.21}}) do pokrycia wybranej powierzchni. Początek siatki kafelków będzie odpowiadał geometrycznemu środkowi powierzchni.

Kafelki [SVG](SVG/pl.md) są zazwyczaj obrazami **64x64** pikseli. Wszystkie pliki wzorów dostarczane z FreeCAD są dostępne na stronie [GitHub](https://github.com/FreeCAD/FreeCAD/tree/master/src/Mod/TechDraw/Patterns).

Wzory oparte na mapach bitowych są wyświetlane ze stałą rozdzielczością 10 px/mm względem strony.

Domyślny plik wzoru kreskowania można określić w [Ustawieniach](TechDraw_Preferences/pl.md).



### Dostępne wzory SVG 

Image:Aluminium.svg\|aluminium Image:Brick01.svg\|brick01 Image:Concrete.svg\|concrete Image:Cross.svg\|cross Image:Cuprous.svg\|cuprous Image:Diagonal1.svg\|diagonal1 Image:Diagonal2.svg\|diagonal2 Image:Earth.svg\|earth Image:General_steel.svg\|general_steel Image:Glass.svg\|glass Image:Hatch45L.svg\|hatch45L Image:Hatch45R.svg\|hatch45R Image:Hbone.svg\|hbone Image:Line.svg\|line Image:Plastic.svg\|plastic Image:Plus.svg\|plus Image:Simple.svg\|simple Image:Solid.svg\|solid Image:Square.svg\|square Image:Steel.svg\|steel Image:Titanium.svg\|titanium Image:Wood.svg\|wood Image:Woodgrain.svg\|woodgrain Image:Zinc.svg\|zinc



## Kreskowanie geometryczne 

Narzędzie <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:16px;"> [Zastosuj na powierzchni kreskowanie geometryczne](TechDraw_GeometricHatch/pl.md) tworzy wzór linii na podstawie specyfikacji odczytanej z pliku. Plik ten jest ogólnie kompatybilny z szeroko stosowanym formatem AutoDesk® PAT. Niewielki wybór wzorów jest zawarty w pliku FCPAT.pat:


```python
; standard PAT patterns

*Diamond, 45 diagonals L & R, Solid, 1.0 mm separation
45,0,0,0,1.0
-45,0,0,0,1.0
*Diamond2, 45 diagonals L & R, Solid, 2.0 mm separation
45,0,0,0,2.0
-45,0,0,0,2.0
*Diamond4, 45 diagonals L & R, Solid, 4.0 mm separation
45,0,0,0,4.0
-45,0,0,0,4.0
*Diagonal4, 45 diagonal R, Solid, 4.0 mm separation
45,0,0,0,4.0
*Diagonal5, 45 diagonal L, Solid, 4.0 mm separation
-45,0,0,0,4.0
*Square, square grid, Solid, 5.0 mm separation 
90,1,1,0,5.0
0,0,0,1,5.0
*Horizontal5, horizontal lines, Solid 5.0 separation
0,0,0,0,5.0
*Vertical5, vertical lines, Solid, 5.0 separation
90,0,0,0,5.0
```

Możesz dodać własne wzorce, jeśli masz uprawnienia do zapisu do FCPAT.pat lub możesz utworzyć własny plik \*.pat i wskazać go w [ustawieniach](TechDraw_Preferences/pl.md).



### Ścieżka do pliku PAT 

Plik `FCPAT.pat` można znaleźć w następującej lokalizacji.

-   **Linux**: `/usr/share/freecad/Mod/TechDraw/PAT/`
    -   *freecad-daily PPA*: `/usr/share/freecad-daily/Mod/TechDraw/PAT/`
-   **Mac**: `/Applications/FreeCAD.app/Contents/Mod/TechDraw/PAT/`
-   **Windows**: `C:\Program Files\FreeCAD\data\Mod\TechDraw\PAT\`





{{TechDraw_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Hatching/pl
