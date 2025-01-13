---
 GuiCommand:
   Name: TechDraw BrokenView
   Name/de: TechDraw UnterbrocheneAnsicht
   MenuLocation: TechDraw , TechDraw Ansichten , Unterbrochene Ansicht einfügen
   Workbenches: TechDraw_Workbench/de
   Version: 1.0
   SeeAlso: TechDraw_View/de
---

# TechDraw BrokenView/de



## Beschreibung

Das Werkzeug **TechDraw UnterbrocheneAnsicht** fügt eine unterbrochene Ansicht ein, die entweder auf einer bestehenden [Bauteilansicht](TechDraw_View/de.md) basiert oder auf einem oder Mehreren Objekten wie [Körpern](PartDesign_Body/de.md) oder [Part](Std_Part.md)-Behältern. Die unterbrochene Ansicht erfordert auch eine oder mehrere [Skizzen](Sketcher_NewSketch/de.md), die Lage und Größe des zu entfernenden Bereiches festlegen. Die unterbrochenen Ansicht verhält sich ähnlich wie andere Ansichten. Die Projektionsrichtung wird vom vorhandenen Bauteil, der 3D-Kamera-Ausrichtung oder der Normale einer ausgewählten Fläche abgeleitet.

<img alt="" src=images/TechDraw_BrokenView_example3d.png  style="width:350px;"> 
*Eine Form, die unterbrochen werden soll und die Skizzen, die die Unterbrechungen festlegen*

<img alt="" src=images/TechDraw_BrokenView_example2d.png  style="width:350px;"> 
*Das Ergebnis*



## Anwendung

1.  Wahlweise die [3D-Ansicht](3D_view/de.md) drehen. Die 3D-Ansicht bestimmt die Ausgangswerte der {{PropertyData/de|Direction}} und der {{PropertyData/de|XDirection}} der unterbrochenen Ansicht.
2.  Das Objekt auswählen, von dem eine unterbrochene Ansicht erstellt werden soll oder eine vorhandene TechDraw-Ansicht auswählen, die das Objekt enthält.
3.  Eine oder mehrere Skizzen in der [Baumansicht](Tree_view/de.md) auswählen, um sie zur Auswahl hinzuzufügen. Jede Skizze sollte nur zwei parallele Linien enthalten. Es können auch andere Objekte, die zwei parallele Kanten enthalten, verwendet werden
4.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_BrokenView.svg" width=16px> [Unterbrochene Ansicht einfügen](TechDraw_BrokenView/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → TechDraw Ansichten → <img src="images/TechDraw_BrokenView.svg" width=16px> Unterbrochene Ansicht einfügen** auswählen.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Eine unterbrochene Ansicht, formal ein {{Incode|TechDraw::DrawBrokenView}}-Objekt, wird von einer [Bauteilansicht](#Properties_Part_View/de.md), formal ein {{Incode|TechDraw::DrawViewPart}}-Objekt abgeleitet und erbt alle seine Eigenschaften. Es besitzt außerdem die folgenden Eigenschaften:



### Daten


{{TitleProperty|Broken View}}

-    {{PropertyData/de|Breaks|LinkList}}: Objekte in der 3D-Ansicht, die Start- und Endpunkte sowie die Ausrichtung der Unterbrechung in dieser Ansicht festlegen.

-    {{PropertyData/de|Gap|Length}}: Der Abstand der Bruchkanten in dieser Ansicht (nicht skalierte 3D-Länge).



## Hinweise

-   Unterbrechungen müssen vertikal oder horizontal sein. Beliebige Unterbrechungen werden nicht unterstützt.
-   Siehe auch [TechDraw Ansicht](TechDraw_View/de.md).



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Eine unterbrochene Ansicht kann mit [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen erstellt werden:


```python
doc = FreeCAD.ActiveDocument
box = doc.Box
profile = doc.Sketch
page = doc.Page

brokenView = doc.addObject("TechDraw::DrawBrokenView", "BrokenView")
page.addView(brokenView)
brokenView.Source= box
brokenView.Breaks = [doc.Sketch]
```





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw BrokenView/de
