---
- GuiCommand:/de
   Name:PartDesign Clone
   Name/de:PartDesign Klon
   MenuLocation:Part Design → Klon erzeugen
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[Entwurf Klon](Draft_Clone/de.md)
---

## Beschreibung

**PartDesign Clone** erzeugt eine verknüpfte Kopie eines gewählten Objekts, das allen zukünftigen Bearbeitungen des Originalobjekts (außer der Positionierung) folgt. Ein Anwendungsfall ist z.B., wenn du [PartDesign boolsche Opeartion](PartDesign_Boolean/de.md) für ein in einem anderen Arbeitsbereich erstelltes Objekt ausführen möchtest. Die meisten Objekttypen werden akzeptiert, solange es sich um einzelne Volumenkörper handelt. Wenn du mehrere Objekte (d.h. Körper) oder einen [Part Behälter](Std_Part/de.md) klonen musst, könntest du [Entwurf Arbeitsbereich Klon](Draft_Clone/de.md) verwenden. Ein Vorbehalt ist, dass der Klon des Part Design Arbeitsbereich die aktuelle Positionierung des Klons auf Null setzt (sowohl die kartesische Übersetzung als auch die räumliche Orientierung). Während der Klon des Entwurfs Arbeitsbereich berechnet und setzt die numerischen Werte der aktuellen Positionierung und Orientierung der geklonten Objekte in Bezug auf den geklonten Objektbehälter.

![*Clone of the inner gear while being translated in 3D space as an independent object*](images/clone.png ) *Klon des Innenzahnrades, während es im 3D Raum als eigenständiges Objekt übersetzt wird*

## Anwendung

1.  Wähle im Modellbaum das zu klonenden Objekt
2.  Drücke die Schaltfläche **<img src=images/PartDesign_Clone.svg style="width:24px"> '''Klon erstellen'''**.

## Eigenschaften

-    **Base Feature**: Bestimmt das Objekt, welches geklont wird. Um dies zu ändern klicke auf das **...** Icon und wähle ein Objekt aus der Liste

-    **Placement**: definiert die Ausrichtung und die Position des Klon im 3D Raum. Siehe [Platzierung](Placement/de.md).

-    **Label**: Benennung des Klon, beliebig.

## Begrenzungen


<div class="mw-translate-fuzzy">

-   Nur ein einzelnes Objekt kann für einen PartDesign Klon verwendet werden.
-   Nur Objekte, die aus einem einzelnen Volumenkörper bestehen, werden unterstützt. Deshalb werden [Teileverbünde](Glossary#Compound.md) wie [Part Container](Std_Part/de.md), [Part Compound](Part_MakeCompound/de.md) oder [Draft Array](Draft_Array/de.md) nicht unterstützt.


</div>





{{PartDesign Tools navi

}} 
