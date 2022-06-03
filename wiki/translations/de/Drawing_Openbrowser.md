---
- GuiCommand   */de
   Name   *Drawing Openbrowser
   Name/de   *Zeichen Openbrowser
   Workbenches   *[Zeichnung](Drawing_Workbench/de.md), Complete
   MenuLocation   *Drawing → Open Browser
   Shortcut   *none
---

# Drawing Openbrowser/de

## Beschreibung

Mit diesem Befehl kannst Du eine ausgewählte [Drawing page](Drawing_Landscape_A3.md) mit dem internen Webbrowser von FreeCAD anzeigen. Der normale Drawing Page Betrachter von FreeCAD basiert auf [Qt\'s eingebautem SVG Rendering Modul](http   *//qt-project.org/doc/qt-5.0/qtsvg/svgrendering.html), das nur eine winzige Teilmenge der vollständigen SVG Spezifikation unterstützt. Daher werden einige fortgeschrittenere SVG Funktionen wie Muster Füllen oder mehrzeilige Texte von diesem Betrachter nicht unterstützt. Der FreeCAD interne Webbrowser basiert jedoch auf [webkit](http   *//en.wikipedia.org/wiki/WebKit), einem der besten SVG Renderer auf dem Markt, der deine Seite mit all ihren Funktionen korrekt darstellt.

## Anwendung

1.  Erstelle eine [Drawing page](Drawing_Landscape_A3.md)
2.  Füge einige [Views](Drawing_View.md) oder andere Inhalte zu deiner Seite hinzu.
3.  [Refresh](Std_Refresh.md) Die Ansicht, wenn keine Zeichenansicht geöffnet wurde.
4.  Drücke die Taste **<img src="images/Drawing_Openbrowser.png" width=16px> [[Drawing Openbrowser]]** Schaltfläche

## Einschränkungen

-   Eine im Webbrowser geöffnete Seite wird bei Änderungen nicht automatisch aktualisiert. Du musst mit der rechten Maustaste auf → erneut laden.


{{docnav/de
|[Clip](Drawing_Clip.md)
|[Drawing OrthoViews](Drawing_Orthoviews/de.md)
|[Drawing Workbench](Drawing_Workbench.md)
|IconL=Drawing_Clip.png
|IconC=Workbench_Drawing.svg
|IconR=Drawing_Orthoviews.png
}}


{{Drawing Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Drawing](Drawing_Workbench.md) > Drawing Openbrowser/de
