# TechDraw Hatching/de
{{TOCright}}

## Beschreibung

Der **<img src="images/Workbench_TechDraw.svg" width=24px> [Techdraw Arbeitsbereich](TechDraw_Workbench/de.md)** verfügt über zwei Schraffierwerkzeuge:

-   <img alt="" src=images/TechDraw_Hatch.svg  style="width:32px;"> [Schraffierte Fläche unter Verwendung einer Bilddatei](TechDraw_Hatch/de.md) (kachelbasiert)
-   <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:32px;"> [Eine geometrische Schraffur auf einer Fläche anwenden](TechDraw_GeometricHatch/de.md) (zeilenbasiert)

## Anwendung

1.  Eine Fläche wählen

    :   <img alt="" src=images/SelectFace.png  style="width:150px;">
2.  Je nach Bedarf drücke entweder <img alt="" src=images/TechDraw_Hatch.svg  style="width:32px;"> [TechDraw Schraffur](TechDraw_Hatch/de.md) oder <img alt="" src=images/TechDraw_GeometricHatch.svg  style="width:32px;"> [TechDraw GeometrischeSchraffur](TechDraw_GeometricHatch/de.md).

**Ergebnis:** Die Fläche wird anfänglich mit Standardwerten schraffiert. **Hinweis:** Durch Ändern der Schraffureigenschaften kann das gewünschte Muster gewählt werden.

### Schraffierte Fläche unter Verwendung einer Bilddatei 


**<img src="images/TechDraw_Hatch.svg" width=24px> [Schraffur Fläche unter Verwendung einer  Bilddatei](TechDraw_Hatch/de.md)
**

verwendet [SVG](SVG/de.md) oder [bitmap](bitmap/de.md) basierte Kacheln, um die ausgewählte Fläche zu schraffieren.

[SVG](SVG/de.md) Kacheln sind typischerweise **64x64** Pixel Bilder. Alle in FreeCAD hinterlegten Dateien sind verfügbar unter [GitHub](https://github.com/FreeCAD/FreeCAD/tree/master/src/Mod/Draft/Resources/patterns).

Jede [Bitmap](bitmap/de.md) Datei (png, jpeg, usw\...) kann als Füllung verwendet werden. **Hinweis:** Die Ergebnisse sind am besten mit vielen kleinen sich wiederholenden Bildern und nicht mit wenigen großen Bildern.

Die Standard Schraffurmusterdatei kann in den [TechDraw Einstellungen](TechDraw_Preferences/de.md) festgelegt werden.

### Geometrische Schraffur 


**<img src="images/TechDraw_GeometricHatch.svg" width=24px> [Geometrische Schraffur auf eine Fläche anwenden](TechDraw_GeometricHatch/de.md)
**

bildet ein Muster von Linien basierend auf einer aus einer Datei gelesenen Spezifikation. Diese Datei ist im Allgemeinen **kompatibel mit dem weit verbreiteten AutoDesk® PAT Format**. Eine kleine Auswahl von Mustern ist in der Datei FCPAT.pat enthalten:


```python
; Standard PAT Muster

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





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Hatching/de
