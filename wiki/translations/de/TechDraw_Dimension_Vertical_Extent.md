---
- GuiCommand:/de
   Name:TechDraw Dimension Vertical Extent
   Name/de:TechDraw Bemaßung Vertikale Ausdehnung
   MenuLocation:TechDraw → Bemaßung → Maß für die vertikale Ausdehnung einfügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Version:0.19
   SeeAlso:[TechDraw Bemaßung Länge](TechDraw_Dimension_Length/de.md), [TechDraw Bemaßung Horizontale Ausdehnung](TechDraw_Dimension_Horizontal_Extent/de.md)
---

## Beschreibung

Das Werkzeug Vertikale Ausdehnung Bemaßen fügt einer Ansicht eine lineare Bemaßung hinzu. Die Bemaßung erstreckt sich vom tiefsten Punkt auf den ausgewählten Objekten bis zum höchsten Punkt. An jedem Punkt wird ein kosmetischer Knoten platziert.

<img alt="" src=images/TechDraw_Dimension_Horizontal_Extent_example.png  style="width:400px;"> 
*Vertikale Ausdehnung Bemaßung von BSpline Fläche*

## Anwendung

1.  Wähle eine Ansicht oder eine Sammlung von Kanten in einer Ansicht aus.
2.  Drücke die **<img src="images/TechDraw_Dimension_Vertical_Extent.svg" width=16px> [Bemaßen Vertikale Ausdehnung](TechDraw_Dimension_Vertikal_Extent/de.md)** Taste
3.  Eine Bemaßung wird der Ansicht hinzugefügt. Die Bemaßung kann an die gewünschte Position gezogen werden.

## Begrenzungen

Bemaßungsobjekte sind anfällig für \"[topologische Benennungs](topological_naming_problem/de.md)\" Probleme. Siehe dazu die Informationen im **<img src="images/TechDraw_Dimension_Length.svg" width=16px> [TechDraw Bemaßung Länge](TechDraw_Dimension_Length/de.md)** Werkzeug für weitere Informationen.

## Eigenschaften

Dieses Objekt hat die gleichen Eigenschaften wie das [TechDraw Bemaßung Länge](TechDraw_Dimension_Length/de.md) Werkzeug. Siehe dieses Werkzeug für Einzelheiten. Ausnahmen vermerkt.

### Daten

-    {{PropertyData/de|MeasureType}}: `True` - basierend auf 3D Geometrie oder \"Projiziert\" - basierend auf der Zeichnung. Normalerweise nicht direkt vom Endanwender beeinflusst. Noch nicht implementiert für Bemaßung Vertikale Ausdehnung.

## Skripten


**Siehe auch:**

[TechDraw Anwendungsschnittstelle](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Bemaßung Vertikale Ausdehnung kann sowohl in [Makros](Macros/de.md) als auch aus der [Python](Python/de.md) Konsole mit den folgenden Funktionen verwendet werden:


```python
selection = [(view1, 'Edge1'), (view1, 'Edge2')]  #or [] for all
hExtentDim = TechDraw.Dimension.makeExtentDim(selection, VERTICAL)
rc = page.addView(hExtentDim)
```





{{TechDraw Tools navi

}}  
