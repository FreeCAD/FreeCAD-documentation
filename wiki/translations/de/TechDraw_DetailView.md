---
- GuiCommand:/de
   Name:TechDraw DetailView
   Name/de:TechDraw DetailAnsicht
   MenuLocation:TechDraw → Detailansicht einfügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Version:0.19
   SeeAlso:[TechDraw Ansicht](TechDraw_View/de.md), [TechDraw Projektionsgruppe](TechDraw_ProjectionGroup/de.md)
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

## Eigenschaften

### Detailansicht

-    {{PropertyData/de|BasisAnsicht}}: Die Ansicht, auf der diese Detailansicht basiert.

-    {{PropertyData/de|Ankerpunkt}}: Das Zentrum der Detailansicht innerhalb der {{PropertyData/de|BasisAnsicht}}.

-    {{PropertyData/de|Radius}}: Die Größe des Bereiches in der {{PropertyData/de|BasisAnsicht}} die in der Detailansicht angezeigt wird.

-    {{PropertyData/de|Maßstab}}: Vergrößerungsstufe.

-    {{PropertyData/de|Bezug}}: Eine Kennung zur Angabe des Bereichs der {{PropertyData/de|BasisAnsicht}} die angezeigt wird.

### Basisansicht

Eine Detailansicht erbt alle anwendbaren Eigenschaften der als {{PropertyData/de|BasisAnsicht}} festgelegten Ansicht. In den Eigenschaften dieser Ansicht kannst du das Aussehen des Detailumrisses ändern:

-    {{PropertyView/de|Einstellung Hervorheben}}: Drehwinkel der Detailansicht im Uhrzeigersinn.

-    {{PropertyView/de|Linienfarbe Hervorheben}}: Linienfarbe für die Umrissform. Die Standardeinstellung hierfür ist die Einstellung **Detail Hervorheben** in den [TechDraw Einstellungen](TechDraw_Preferences/de.md).

-    {{PropertyView/de|Linienstil Hervorheben}}: Linienstil für die Umrissform. Die Standardeinstellung hierfür ist die Einstellung **Detail Hervorhebungsstil** in den [TechDraw Einstellungen](TechDraw_Preferences/de.md).

## Skripten


**Siehe auch:**

[TechDraw Anwendungsschnittstelle](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Detailwerkzeug kann mit [Makros](Macros/de.md) und aus der [Python](Python/de.md) Konsole mit den folgenden Funktionen verwendet werden:


```python
Detail = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDetail','Detail')
...TBA
```

## Kniffe

-   Der Raum um den Ansichtsumriss und den Rand des Ansichtsobjekts ist standardmäßig ein weißer Bereich. Das heißt, er bedeckt alles dahinterliegende. Manchmal reicht der Platz auf der Seite nicht aus, und du kannst Platz sparen, indem du diesen unnötigen weißen Bereich reduzierst.

Dies wird erreicht, indem die Detailansicht in eine [Klipgruppe](TechDraw_ClipGroup/de.md) gesetzt wird:

![](images/TechDraw_DetailClipped.png ) 
*Detailansicht in einer Klipgruppe*

-   Bei Detailansichten mit einem runden Umriss kann die Position der Bezugskennzeichnung in der Basisansicht über die Basisansichtseigenschaft {{PropertyView/de|Einstellung Hervorheben}} geändert werden.

## Hinweise

-   [Eine gute Aussprache über das Setzen des Ankers](https://www.forum.freecadweb.org/viewtopic.php?f=35&t=34055#p285281)





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DetailView/de
