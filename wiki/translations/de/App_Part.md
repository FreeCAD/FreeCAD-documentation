# App Part/de
## Einführung

<img alt="" src=images/Geofeaturegroup.svg  style="width:32px;">

Ein [Anwendung Teil](App_Part/de.md) Objekt oder formal ein `App::Part` ist ein Element, das die Gruppierung von Objekten im 3D Raum ermöglicht.

Es wurde für die Verwendung in Baugruppen entwickelt, da es über einen {{MenuCommand/de|Ursprung}} verfügt, der als Positionsreferenz für die gruppierten Objekte dient.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten im Programm. Die Klasse `App::Part* ist ein einfacher Container, der eine Position im 3D Raum hat und einen Ursprung zur Steuerung der Platzierung der darunter gruppierten Objekte besitzt.`

## Anwendung

1.  Drücke die **[<img src=images/Std_Part.svg style="width:16px"> [Std Part](Std_Part/de.md)** Schaltfläche. Es wird ein leeres Teil erstellt, das automatisch zu *[aktiv](Std_Part#Active_status.md)* wird.
2.  Um Objekte zu einem Teil hinzuzufügen, ziehe sie per Ziehen & Ablegen über das Teil in der [Baumansicht](tree_view/de.md).
3.  Um Objekte aus einem Teil zu entfernen, ziehe sie aus dem Teil heraus und auf die Dokumentbeschriftung oben in der [Baumansicht](tree_view/de.md).

Siehe die [Std Part](Std_Part/de.md) Seite findest du die vollständigen Informationen, einschließlich der Verwendung in [Skripten](Std_Part#Scripting/de.md).

## Eigenschaften

Eine [App Part](App_Part.md) (`App::Part` Klasse) wird von der Basisklasse [App GeoFeature](App_GeoFeature.md) (`App::GeoFeature` Klasse) abgeleitet, daher teilt sie alle Eigenschaften der letzteren.

Siehe die komplette Liste der Eigenschaften auf der [Std Part](Std_Part/de.md) Seite.


{{Std Base navi

}} {{Document objects navi}}

---
[documentation index](../README.md) > App Part/de
