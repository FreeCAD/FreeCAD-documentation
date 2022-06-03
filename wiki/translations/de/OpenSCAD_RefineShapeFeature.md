---
- GuiCommand   */de
   Name   *OpenSCAD RefineShapeFeature
   Name/de   *OpenSCAD RefineShapeFeature
   MenuLocation   *OpenSCAD → Form Feature verfeinern
   Workbenches   *[OpenSCAD](OpenSCAD_Workbench/de.md)
---

# OpenSCAD RefineShapeFeature/de

## Beschreibung

Entfernt unnötige Linien. Nach einer Booleschen Operation bleiben einige Linien sichtbar, die zur vorigen Form gehören. Dieses Werkzeug erstellt eine Kopie des bereinigten Körpers.

![](images/PartRefineShape_it.png )

## Anwendung

1.  Wähle die zu bereinigende Form.
2.  Klicke **OpenSCAD → Form Feature verfeinern** im Top-Menü.

-   Ein Eltern-Objekt wird erstellt und komplett bereinigt, das Original-Objekt wird verborgen gerendert.

## Einschränkungen


<div class="mw-translate-fuzzy">

## Beschränkungen

-   Der Bereinigungsalgorithmus arbeitet nur mit Hüllen. Dazu iteriert er über die Hüllen des ausgewählten Objektes und erstellt für jede Hülle eine neue Hülle mit zusammengelegten Flächen, wo immer es möglich ist. Das bedeutet, wenn das ausgewählte Objekt nur eine Fläche, ein Kantenzug, eine Kante oder ein Punkt ist, macht der Algorithmus nichts.
-   Anders als das [Form Feature verfeinern](OpenSCAD_RefineShapeFeature/de.md) im Arbeitsbereich OpenSCAD **wird** diese Funktion die erzeugte Hülle ändern, wenn sich die Elternhülle ändert.


</div>

## Hinweise

-   die Funktion wird nicht die existierende Form verändern, sondern eine neue Form erstellen
-   die Funktion wird normalerweise als letzter Schritt in der Modellierungshistorie verwendet
-   die Funktion kann helfen, schwierige Rundungen zu erstellen
-   die Funktion ist gedacht, um bei 3D-Druckern das Drucken unerwünschte Kanten zu vermeiden





{{OpenSCAD_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [OpenSCAD](OpenSCAD_Workbench.md) > OpenSCAD RefineShapeFeature/de
