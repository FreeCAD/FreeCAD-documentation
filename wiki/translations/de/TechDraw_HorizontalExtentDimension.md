---
- GuiCommand:/de
   Name:TechDraw Dimension Horizontal Extent
   Name/de:TechDraw Bemaßung Horizontale Ausdehnung
   MenuLocation:TechDraw → Bemaßungen → Maß für die horizontale Ausdehnung einfügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Version:0.19
   SeeAlso:[TechDraw Abmessung Länge](TechDraw_Dimension_Length/de.md), [TechDraw Abmessung Vertikale Ausdehnung](TechDraw_Dimension_Vertical_Extent/de.md)
---

# TechDraw HorizontalExtentDimension/de


</div>

## Beschreibung


<div class="mw-translate-fuzzy">

Das Werkzeug \"Horizontale Ausdehnung Bemaßen\" fügt einer Ansicht eine lineare Bemaßung hinzu. Die Bemaßung erstreckt sich vom äußersten linken Punkt auf den ausgewählten Objekten bis zum äußersten rechten Punkt. An jedem Punkt wird ein KosmetischerKnoten platziert.


</div>

<img alt="" src=images/TechDraw_Dimension_Horizontal_Extent_example.png  style="width:400px;"> 
*Horizontale Ausdehnung Bemaßen von BSpline Fläche*

## Anwendung


<div class="mw-translate-fuzzy">

1.  Wähle eine Ansicht oder eine Sammlung von Kanten in einer Ansicht aus.
2.  Drücke die **<img src="images/TechDraw_Dimension_Horizontal_Extent.svg" width=16px> [Bemaßen Horizontale Ausdehnung](TechDraw_Dimension_Horizontal_Extent/de.md)** Taste
3.  Eine Bemaßung wird der Ansicht hinzugefügt. Die Bemaßung kann an die gewünschte Position gezogen werden.


</div>

## Begrenzungen


<div class="mw-translate-fuzzy">

Bemaßungsobjekte sind anfällig für \"[topologische Benennungs](topological_naming_problem/de.md)\" Probleme. Siehe die Informationen im **<img src="images/TechDraw_Dimension_Length.svg" width=16px> [TechDraw Bemaßung Länge](TechDraw_Dimension_Length/de.md)** Werkzeug für weitere Informationen.


</div>

## Eigenschaften


<div class="mw-translate-fuzzy">

Dieses Objekt hat die gleichen Eigenschaften wie das [TechDraw Bemaßung Länge](TechDraw_Dimension_Length/de.md) Werkzeug. Siehe dieses Werkzeug für Einzelheiten. Ausnahmen vermerkt.


</div>

### Daten

-    {{PropertyData/de|MeasureType}}: `True` - basierend auf 3D Geometrie oder \"Projizierter Geometrie\" auf der Zeichnung. Normalerweise nicht direkt vom Endbenutzer beeinflusst. Noch nicht implementiert für Bemaßung Horizontale Ausdehnung.

## Skripten


**Siehe auch:**

[TechDraw Anwendungsschnittstelle](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


<div class="mw-translate-fuzzy">

Das Werkzeug Bemaßung Horizontale Ausdehnung kann in [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole durch Anwendung der folgenden Funktion verwendet werden:


</div>


```python
selection = [(view1, 'Edge1'), (view1, 'Edge2')]  #or [] for all
hExtentDim = TechDraw.Dimension.makeExtentDim(selection, HORIZONTAL)
rc = page.addView(hExtentDim)
```


<div class="mw-translate-fuzzy">





</div>


{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw HorizontalExtentDimension/de
