# TechDraw Hatching/de
{{TOCright}}

## Beschreibung


<div class="mw-translate-fuzzy">

Der Arbeitsbereich Techdraw verfügt über zwei Schraffierwerkzeuge:

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width:32px;"> [Fläche mit Muster aus einer Bilddatei schraffieren](TechDraw_Hatch/de.md) (kachelbasiert)
-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:32px;"> [ Fläche mit einer geometrischen Schraffur versehen](TechDraw_GeometricHatch/de.md) (linienbasiert)


</div>


<div class="mw-translate-fuzzy">

### Fläche mit Muster aus einer Bilddatei schraffieren 


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/TechDraw_Hatch.svg  style="width:24px;"> [Fläche mit Muster aus einer Bilddatei schraffieren](TechDraw_Hatch/de.md) verwendet [SVG-](SVG/de.md) oder [bitmap-](bitmap/de.md) basierte Kacheln, um die ausgewählte Fläche zu schraffieren.


</div>

[SVG](SVG/de.md)-Kacheln sind typischerweise **64x64** Pixel-Bilder. Alle Schraffurdateien, die mit FreeCAD ausgeliefert werden, sind verfügbar unter [GitHub](https://github.com/FreeCAD/FreeCAD/tree/master/src/Mod/Draft/Resources/patterns).

Die Standard-Schraffurmusterdatei kann in den [TechDraw Einstellungen](TechDraw_Preferences/de.md) festgelegt werden.

### Available patterns 

Image:Aluminium.svg\|aluminium Image:Brick01.svg\|brick01 Image:Concrete.svg\|concrete Image:Cross.svg\|cross Image:Cuprous.svg\|cuprous Image:Diagonal1.svg\|diagonal1 Image:Diagonal2.svg\|diagonal2 Image:Earth.svg\|earth Image:General\_steel.svg\|general\_steel Image:Glass.svg\|glass Image:Hatch45L.svg\|hatch45L Image:Hatch45R.svg\|hatch45R Image:Hbone.svg\|hbone Image:Line.svg\|line Image:Plastic.svg\|plastic Image:Plus.svg\|plus Image:Simple.svg\|simple Image:Solid.svg\|solid Image:Square.svg\|square Image:Steel.svg\|steel Image:Titanium.svg\|titanium Image:Wood.svg\|wood Image:Woodgrain.svg\|woodgrain Image:Zinc.svg\|zinc


<div class="mw-translate-fuzzy">

### Fläche mit einer geometrischen Schraffur versehen 


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:24px;"> [Geometrische Schraffur auf eine Fläche anwenden](TechDraw_GeometricHatch/de.md) bildet ein Muster von Linien basierend auf einer aus einer Datei gelesenen Spezifikation. Diese Datei ist im Allgemeinen **kompatibel mit dem weit verbreiteten AutoDesk® PAT-Format**. Eine kleine Auswahl von Mustern ist in der Datei FCPAT.pat enthalten:


</div>


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

Du kannst deine eigenen Muster hinzufügen, wenn du Schreibberechtigung für FCPAT.pat hast, oder du kannst deine eigene \*.pat Datei erstellen und in [TechDraw Einstellungen](TechDraw_Preferences/de.md) darauf verweisen.

### PAT Dateipfad 

Die Datei `FCPAT.pat` befindet sich im folgenden Verzeichnis:

-   **Windows**: `C:\Program Files\FreeCAD\data\Mod\TechDraw\PAT\`
-   **Mac**: `/Applications/FreeCAD.app/Contents/Mod/TechDraw/PAT/`
-   **Linux**: `/usr/share/freecad/Mod/TechDraw/PAT/`
    -   *freecad-daily PPA*: `/usr/share/freecad-daily/Mod/TechDraw/PAT/`





{{TechDraw_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Hatching/de
