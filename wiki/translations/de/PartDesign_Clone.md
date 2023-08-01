---
- GuiCommand:
   Name:PartDesign Clone
   Name/de:PartDesign Klon
   MenuLocation:Part Design - Klon erzeugen
   Workbenches:[PartDesign](PartDesign_Workbench/de.md)
   Version:0.17
   SeeAlso:[Draft Klon](Draft_Clone/de.md)
---

# PartDesign Clone/de



## Beschreibung

**PartDesign Klon** erstellt eine verknüpfte Kopie eines ausgewählten Objekts, das allen zukünftigen Bearbeitungen des Originalobjekts (außer der Positionierung) folgt. Ein Anwendungsfall ist z.B., wenn [PartDesign boolesche Operationen](PartDesign_Boolean/de.md) für ein in einem anderen Arbeitsbereich erstelltes Objekt ausgeführt werden sollen. Die meisten Objektarten werden akzeptiert, solange es sich um einzelne Festkörper handelt. Sollen mehrere Objekte (d.h. Körper) oder ein [Part-Behälter](Std_Part/de.md) geklont werden, könnte man [Draft Klonen](Draft_Clone/de.md) verwenden. Ein Unterschied ist, dass der Klon des Arbeitsbereichs PartDesign die aktuelle Positionierung des Klons auf Null setzt (sowohl die kartesische Bewegung als auch die räumliche Orientierung), während der Klon des Arbeitsbereichs Draft die Zahlenwerte der aktuellen Positionierung und Orientierung der geklonten Objekte unter Berücksichtigung des Behälters für geklonte Objekte berechnet und einsetzt.

![*Clone of the inner gear while being translated in 3D space as an independent object*](images/clone.png ) 
*Klon des Innenzahnrades, der als eigenständiges Objekt im 3D-Raum bewegt wird*



## Anwendung

1.  Das zu klonenden Objekt im Modellbaum auswählen.
2.  Die Schaltfläche **[<img src=images/PartDesign_Clone.svg style="width:24px"> '''Klon erzeugen'''**.



## Eigenschaften

-    {{PropertyData/de|Base Feature}}: Bestimmt das Ausgangsobjekt, auf dem der Klon basiert. Um es auszutauschen klickt man auf die Schaltfläche **...** und erhält eine Liste vorhandener Objekte.

-    {{PropertyData/de|Placement}}: bestimmt die Ausrichtung und die Position des Klons im 3D-Raum. Siehe [Positionierung](Placement/de.md).

-    {{PropertyData/de|Label}}: Bezeichnung die dem Klon-Objekt gegeben wurde. Nach eigenem Bedarf änderbar.



## Begrenzungen

-   Nur ein einzelnes Objekt kann für einen PartDesign-Klon verwendet werden.
-   Nur Objekte, die aus einem einzelnen Festkörper bestehen, werden unterstützt. Deshalb werden [Verbunde](Glossary/de#Compound.md) wie [Part-Container](Std_Part/de.md), [Part-Verbund](Part_MakeCompound/de.md) oder [Draft RechtwinkligeAnordnung](Draft_OrthoArray/de.md) nicht unterstützt.





{{PartDesign_Tools_navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Clone/de
