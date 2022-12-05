---
- GuiCommand:
   Name:TechDraw ProjectShape
   MenuLocation:TechDraw → Project shape...
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Shortcut:
   Version:0.20
   SeeAlso:[Draft Shape2DView](Draft_Shape2DView/de.md)
---

# TechDraw ProjectShape/de

## Beschreibung

Das <img alt="" src=images/TechDraw_ProjectShape.svg  style="width:24px;"> **TechDraw ProjectShape** Werkzeug erzeugt Projektionen von Formstücken. Die Projektionen werden in [3D view](3D_view.md), und nicht in [TechDraw Page](TechDraw_PageDefault.md) erzeugt.

![](images/ProjectShape1_it.png )

## Verwendung

1.  Wähle eines oder mehrere Objekte. Für jedes Objekt wird eine eigene Projektion erzeugt.
2.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   Wähle die **<img src="images/TechDraw_ProjectShape.svg" width=16px> [Project shape...](TechDraw_ProjectShape.md)** Schaltfläche.
    -   Wähle die **TechDraw → <img src="images/TechDraw_ProjectShape.svg" width=16px> Project shape...** Option aus dem Menü.
3.  Das **Project shapes** Dialogfeld öffnet. Siehe [Properties](#Properties.md).
4.  Setze die gewünschten Optionen.
5.  Die gewählten Optionen sollten nicht zu einer leeren Projektion führen, weil das einen Fehler verursacht. Bei einem Objekt mit scharfen Kanten, wie etwa [Part Box](Part_Box.md), muss die **Visible sharp edges** und/oder die **Hidden sharp edges** Option gewählt werden.
6.  Wähle die **OK** Schaltfläche.

## Eigenschaften

Die Projektion wird von einem [Part Feature](Part_Feature.md) abgeleitet und erbt alle Eigenschaften. Sie hat zusätzlich folgende Eigenschaften:

### Daten


{{TitleProperty|Projection}}

-    **Source|Link**: Die zu projizierende Form.

-    **Direction|Vector**: Die Richtung der Projektion. Das ist der Normalvektor auf die Projektionsfläche.

-    **VCompound|Bool**: Wenn `True`, dann werden sichtbare scharfe Kanten gezeigt. Beispiel: alle Kanten einer [Part Box](Part_Box.md).

-    **Rg1 Line VCompound|Bool**: Wenn `True`, dann werden sichtbare glatte Kanten gezeigt. Beispiel: die Kanten zwischen einer Rundung und den benachbarten Flächen.

-    **Rg NLine VCompound|Bool**: Wenn `True`, dann werden sichtbare Nähte gezeigt. Beispiel: die Naht einer 360° zylindrischen Fläche.

-    **Out Line VCompound|Bool**: Wenn `True`, dann werden sichtbare Konturen (die nicht scharf sind) gezeigt. Beispiel: die Seitenansicht eines [Part Cylinder](Part_Cylinder.md) hat zwei solche Kanten.

-    **Iso Line VCompound|Bool**: Wenn `True`, dann werden sichtbare Isoparameter gezeigt. Dies funktioniert derzeit nicht.

-    **HCompound|Bool**: Wenn `True`, dann werden unsichtbare scharfe Kanten gezeigt.

-    **Rg1 Line HCompound|Bool**: Wenn `True`, dann werden unsichtbare glatte Kanten gezeigt.

-    **Rg NLine HCompound|Bool**: Wenn `True`, dann werden unsichtbare Nähte gezeigt.

-    **Out Line HCompound|Bool**: Wenn `True`, dann werden unsichtbare Konturen gezeigt.

-    **Iso Line HCompound|Bool**: Wenn `True`, dann werden unsichtbare Isoparameter gezeigt. Dies funktioniert derzeit nicht.

## Hinweise

Dieses Werkzeug gab es früher im Drawing Workbench.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ProjectShape/de
