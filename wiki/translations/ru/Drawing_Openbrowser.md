---
- GuiCommand:
   Name:Drawing Openbrowser
   Name/ru:Drawing Openbrowser
   Workbenches:[Drawing](Drawing_Workbench/ru.md), Complete
   MenuLocation:Чертёж - Открыть в браузере
   Shortcut:
---

# Drawing Openbrowser/ru

## Description

This command allows you to display a selected [Drawing page](Drawing_Landscape_A3.md) using FreeCAD\'s internal web browser. The normal Drawing page viewer of FreeCAD is based on [Qt\'s built-in SVG rendering module](http://qt-project.org/doc/qt-5.0/qtsvg/svgrendering.html), which only supports a tiny subset of the full SVG specification. As a result, some more advanced SVG features, such as pattern fills or multiline texts are not supported by this viewer. The FreeCAD internal web browser, however, is built on [webkit](http://en.wikipedia.org/wiki/WebKit), which is one of the best SVG renderers available, and will correctly render your page with all its features.

## Usage

1.  Create a [Drawing page](Drawing_Landscape_A3.md)
2.  Add some [views](Drawing_View.md) or other content to your page
3.  [Refresh](Std_Refresh.md) the view if a Drawing view wasn\'t opened
4.  Press the **<img src="images/Drawing_Openbrowser.png" width=16px> [[Drawing Openbrowser]]** button

## Limitations

-   A page opened in the web browser will not refresh automatically on changes. You must use right-click → reload manually.


{{docnav|[Clip](Drawing_Clip.md)|[Ortho Views](Drawing_Orthoviews.md)|[Drawing Workbench](Drawing_Workbench.md)|IconL=Drawing_Clip.png|IconC=Workbench_Drawing.svg|IconR=Drawing_Orthoviews.png}}


{{Drawing Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [Drawing](Category_Drawing.md) > Drawing Openbrowser/ru
