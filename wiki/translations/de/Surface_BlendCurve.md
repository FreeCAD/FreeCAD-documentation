---
 GuiCommand:
   Name: Surface BlendCurve
   Name/de: Surface Übergangskurve
   MenuLocation: Surface , Blend Curve
   Workbenches: Surface_Workbench/de
   Version: 0.21
---

# Surface BlendCurve/de



## Beschreibung


**[<img src=images/Surface_BlendCurve.svg style="width:16px"> [Surface Blend Curve](Surface_BlendCurve.md)**

Erzeugt eine Bezier Kurve zwischen zwei Kanten, mit der gewünschten Stetigkeit.

Die Basisgeometrie kann zu Kurven die mit dem [Draft Workbench](Draft_Workbench.md) oder dem [Sketcher Workbench](Sketcher_Workbench.md) erzeugt wurden gehören, kann aber auch zu festen Objekten die mit dem [Part Workbench](Part_Workbench.md) erzeugt wurden, gehören.

<img alt="" src=images/Surface_BlendCurve_G3_example.png  style="width:400px;"> <img alt="" src=images/Surface_BlendCurve_Comb.png  style="width:400px;"> 
*Flächen Übergangsurve die 2 Kanten mit G3 Kontinuität verbindet. Das orange Polygon repräsentiert die Kontrollpunkte. Der Kamm der Kurve (von [Curves addon](Curves_Workbench.md)) ist an den Kontaktpunkten glatt.*



## Anwendung

1.  Wähle zwei Kanten in [3D view](3D_view.md)
2.  Es gibt mehrere Wege den Befehl zu starten:
    -   Drücke die **<img src="images/Surface_BlendCurve.svg" width=16px> [Surface Blend Curve](Surface_BlendCurve.md)** Schaltfläche.
    -   Wähle die **Surface → <img src="images/Surface_BlendCurve.svg" width=16px> Blend Curve** Option aus dem Menü.
3.  Stelle die Form der Kurve in den Daten Eigenschaften des Objektes ein.



## Eigenschaften

Eine [Flächen Übergangskurve](Surface_BlendCurve.md) wird von der Basisklasse [Part Feature](Part_Feature.md) (`Part::Feature` durch die `Part::Spline` Unterklasse), abgeleitet, deshalb verwendet sie die Eigenschaften der Letzteren.

Zusätzlich zu den in [Part Feature](Part_Feature.md) beschriebenen Eigenschaften, hat die Oberflächen Übergangskurve im [Eigenschaften Editor](Property_editor.md) folgende Eigenschaften.



### Daten


{{TitleProperty|Übergangskurve}}

-    **Startkante|LinkSub**: Erste Eingangskante.

-    **Start Stetigkeit|Integer**: Grad der Stetigkeit.

-    **Start Parameter|Float**: Normalisierter Parameter entlang der Kante; von {{Value|0.0}}(Kantenstart) bis {{Value|1.0}}(Kantenende).

-    **Start Länge|Float**: Länge der Tangente.

-    **Endkante|LinkSub**: Zweite Eingangskante..

-    **Ende Stetigkeit|Integer**: Grad der Stetigkeit

-    **Ende Parameter|Float**: Normalisierter Parameter entlang der Kante; von {{Value|0.0}}(Kantenstart) bis {{Value|1.0}}(Kantenende).

-    **Ende Länge|Float**: Länge der Tangente.



### Ansicht


{{TitleProperty|Basis}}

-    **Kontrollpunkte|Bool**: Voreingestellt ist `False`; falls auf `True` gesetzt werden die Kontrollpunkte der Kurve überlagert dargestellt.



## Skripten


**Siehe auch:**

[FreeCAD Basis Scripten](FreeCAD_Scripting_Basics.md).

Das Werkzeug Übergangskurve kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus zum Einfügen von `Surface::FeatureBlendCurve`-Objekten verwendet werden.

-   Die dabei zur Definition der Kurve verwendeten Kanten müssen als [LinkSub](FeaturePython_Custom_Properties/de#App:_PropertyLinkSub.md) den `Startkante` und `Endkante` Eigenschaften des Objektes zugeordnet werden.
-   Alle Objekte mit Kanten müssen, bevor sie als Eingabe für die Eigenschaften der Übergangskurve verwendet werden können, berechnet werden.


```python
import FreeCAD as App
import Draft

doc = App.newDocument()

points1 = [App.Vector(-20, -20, 0), App.Vector(-20, -8, 0), App.Vector(-17, 7, 0), App.Vector(-18, 25, 0)]
obj1 = Draft.make_bspline(points1)

points2 = [App.Vector(60, 26, 0), App.Vector(37, 4, 0), App.Vector(33, -20, 0)]
obj2 = Draft.make_bspline(points2)

doc.recompute()

bcurve = doc.addObject("Surface::FeatureBlendCurve","BlendCurve")
bcurve.StartEdge = (obj1, 'Edge1')
bcurve.EndEdge = (obj2, 'Edge1')
bcurve.EndParameter = 1.00
bcurve.StartSize = -5.00
bcurve.EndSize = -5.00

doc.recompute()
```





{{Surface Tools navi

}}



---
⏵ [documentation index](../README.md) > [Surface](Surface_Workbench.md) > Surface BlendCurve/de
