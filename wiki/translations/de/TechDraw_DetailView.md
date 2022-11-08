---
- GuiCommand   */de
   Name   *TechDraw DetailView
   Name/de   *TechDraw DetailAnsicht
   MenuLocation   *TechDraw → Detailansicht einfügen
   Workbenches   *[TechDraw](TechDraw_Workbench/de.md)
   Version   *0.19
   SeeAlso   *[TechDraw Ansicht](TechDraw_View/de.md), [TechDraw Projektionsgruppe](TechDraw_ProjectionGroup/de.md)
---

# TechDraw DetailView/de

## Beschreibung

Das Detailwerkzeug erstellt eine vergrößerte Ansicht eines kleinen Bereichs einer vorhandenen Ansicht.

![](images/ViewDetail.png ) 
*Detailansicht mit kreisförmiger Ansichtskasten einer vorhandenen Ansicht*

## Anwendung

-   Wähle eine Ansicht in der Zeichnung oder in der Baumansicht.
-   Klicke **<img src="images/TechDraw_DetailView.svg" width=16px> [Einfügen Detail Ansicht](TechDraw_DetailView/de.md)**, um die Detailansicht zu erstellen.
-   Im Dialogfenster der Combo-Box kann man die Position und Größe des anzuzeigenden Bereichs definieren.
    -   entweder durch Änderung der Koordinaten in X- und Y- Richtung
    -   oder durch Drücken der Schaltfläche ** Drag Highlight**. In diesem Fall wird der Rand des Detailursprungs fett und mit der Beschriftung *Ziehen* hervorgehoben. Klicke auf den Rand oder die Beschriftung, halte die Maustaste gedrückt und ziehe sie an die gewünschte Position.
    -   mit Änderung des Radius wird der vorgegebene Detailausschnitt im Detailursprung vergrößert oder verkleinert.
-   Zum späteren Ändern/Anpassen der Detailansicht kann man in der Baumsansicht mittels Doppelklick auf das betreffende \"Detail\" jederzeit Änderungen vornehmen.
-   Im Eigenschaftsfeld der Detailansicht **Scale** kann durch Ändern von \"Scale\" die Detailansicht auf der Zeichnung vergrößert und verkleinert werden.

Die Detailansicht kann innerhalb eines runden oder quadratischen Ansichtskastens angezeigt werden. Dies wird durch die [Einstellungen](TechDraw_Preferences#Annotation/de.md) Einstellung **Detailansicht Umrißform** gesteuert.

## Eigenschaften Detailansicht 

Siehe auch [TechDraw Ansicht](TechDraw_View/de#Eigenschaften.md).

### Daten


{{TitleProperty|Detail}}

-    {{PropertyData/de|Base View|Link}}   * Die Ansicht auf der diese Detailansicht basiert.

-    {{PropertyData/de|Anchor Point|Vector}}   * Der Mittelpunkt der Detailansicht innerhalb der {{PropertyData/de|Base View}}.

-    {{PropertyData/de|Radius|Float}}   * Die Größe des Bereichs in der {{PropertyData/de|Base View}}, der in der Detailansicht dargestellt wird.

-    {{PropertyData/de|Reference|String}}   * Ein Bezeichner für die Detailansicht in der {{PropertyData/de|Base View}}.

## Eigenschaften Basisansicht 

Eine Detailansicht erbt alle anwendbaren Eigenschaften der als {{PropertyData/de|Base View}} festgelegten Ansicht. In den Eigenschaften dieser Ansicht kann das Aussehen des Detailumrisses geändert werden   *

-    {{PropertyView/de|Einstellung Hervorheben}}   * Drehwinkel der Detailansicht im Uhrzeigersinn.

-    {{PropertyView/de|Linienfarbe Hervorheben}}   * Linienfarbe für die Umrissform. Die Standardeinstellung hierfür ist die Einstellung **Detail Hervorheben** in den [TechDraw Einstellungen](TechDraw_Preferences/de.md).

-    {{PropertyView/de|Linienstil Hervorheben}}   * Linienstil für die Umrissform. Die Standardeinstellung hierfür ist die Einstellung **Detail Hervorhebungsstil** in den [TechDraw Einstellungen](TechDraw_Preferences/de.md).

## Hinweise

-   [Eine gute Aussprache über das Setzen des Ankers](https   *//www.forum.freecadweb.org/viewtopic.php?f=35&t=34055#p285281)

## Skripten


**Siehe auch   ***

[TechDraw Anwendungsschnittstelle](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Detailwerkzeug kann mit [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole mit den folgenden Funktionen verwendet werden   *


```python
Detail = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewDetail','Detail')
...TBA
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DetailView/de
