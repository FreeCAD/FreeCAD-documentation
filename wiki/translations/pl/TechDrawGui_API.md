# TechDrawGui API/pl
**''(Listopad 2018)'' Te informacje mogą być niekompletne i nieaktualne. Najnowsze API można znaleźć na stronie [https://www.freecadweb.org/api autogenerowana dokumentacja API].** Funkcje te są częścią środowiska pracy [Rysunek Roboczy](TechDraw_Workbench/pl.md) i mogą być używane w [makrodefinicjach](macros/pl.md) oraz z konsoli środowiska [Python](Python/pl.md) po zaimportowaniu modułu `TechDrawGui`.

Zobacz stronę [API](TechDraw_API/pl.md) aby poznać więcej funkcji.

Przykład: 
```python
import FreeCAD
import TechDrawGui

p = FreeCAD.ActiveDocument.Page

f = "/home/localuser/myPdfDirectory/savePage.pdf"
TechDrawGui.exportPageAsPdf(p, f)

f = "/home/localuser/mySvgDirectory/savePage.svg"
TechDrawGui.exportPageAsSvg(p, f)
```


{{APIFunction|exportPageAsPdf|pageObject, filePath|zapisz kopię pageObject w formacie PDF w lokalizacji filePath|}}


{{APIFunction|exportPageAsSvg|pageObject, filePath|zapisz kopię pageObject w formacie SVG w lokalizacji filePath|}}


{{APIFunction|copyActiveViewToSvgFile|document, filePath, ''(opcje)''|zapisz kopię aktywnego widoku dla "dokumentu" do pliku "filePath"|double ''(szacunkowa skala)''}}

Opcje:

-   width - float - szerokość generowanego svg w mm
-   height - float - wysokość generowanego svg w mm
-   paintBackground - bool - maluj / nie maluj tła
-   backgroundColor - tuple - (r,g,b,a)
-   lineWidth - float - szerokość linii
-   border - float - pusta przestrzeń wokół obrazu
-   mode - int - tryb renderowania (AS\_IS, WIREFRAME, POINTS, WIREFRAME\_OVERLAY, HIDDEN\_LINE, BOUNDING\_BOX)

{{APIFunction|addQGIToView|view, QGraphicsItem|add element QGraphicsItem ''(utworzony przy użyciu PySide)'' dla Widoku.|}}


{{TechDraw Tools navi

}}  

[<img src="images/Property.png" style="width:16px"> API](Category_API.md) [<img src="images/Property.png" style="width:16px"> Poweruser Documentation](Category_Poweruser_Documentation.md)

---
[documentation index](../README.md) > [API](Category_API.md) > TechDrawGui API/pl
