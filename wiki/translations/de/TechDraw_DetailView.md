---
- GuiCommand:
   Name: TechDraw DetailView
   Name/de: TechDraw Detailansicht
   MenuLocation: TechDraw - Detailansicht einfügen
   Workbenches: [TechDraw](TechDraw_Workbench/de.md)
   Version: 0.19
   SeeAlso: [TechDraw Ansicht](TechDraw_View/de.md), [TechDraw Projektionsgruppe](TechDraw_ProjectionGroup/de.md)
---

# TechDraw DetailView/de



## Beschreibung

Das Werkzeug **TechDraw Detailansicht** erstellt eine vergrößerte Ansicht eines kleinen Bereichs einer vorhandenen Ansicht.

![](images/ViewDetail.png ) 
*Detailansicht mit kreisförmigem Ansichtsrahmen einer vorhandenen Ansicht*



## Anwendung

-   Eine Ansicht in der Zeichnung oder in der Baumansicht auswählen.
-   Die Schaltfläche **<img src="images/TechDraw_DetailView.svg" width=16px> [Detailansicht einfügen](TechDraw_DetailView/de.md)** drücken, um die Detailansicht zu erstellen.
-   Im geöffneten Aufgaben-Dialog kann die Größe, die Position und der Maßstab des anzuzeigenden Bereichs definiert werden.
    -   entweder durch Änderung der Koordinaten in X- und Y- Richtung
    -   oder durch Drücken der Schaltfläche **Auswahl verschieben**. In diesem Fall wird der Rand des Detailauswahlrahmens fett und mit der Beschriftung *Ziehen* hervorgehoben. Auf den Rand oder die Beschriftung klicken, die Maustaste gedrückt halten und den Rahmen an die gewünschte Position ziehen. Zuletzt wird die Maustaste losgelassen, um die Änderung abzuschließen.

Die Detailansicht kann innerhalb eines runden oder quadratischen Ansichtsrahmens angezeigt werden. Dies wird durch die [Einstellung](TechDraw_Preferences/de#Anmerkung.md) **Umrißform für Detailansichten** gesteuert.



## Eigenschaften Detailansicht 

Siehe auch [TechDraw Ansicht](TechDraw_View/de#Eigenschaften.md).



### Daten


{{TitleProperty|Detail}}

-    {{PropertyData/de|Base View|Link}}: Die Ansicht auf der diese Detailansicht basiert.

-    {{PropertyData/de|Anchor Point|Vector}}: Der Mittelpunkt der Detailansicht innerhalb der {{PropertyData/de|Base View}}.

-    {{PropertyData/de|Radius|Float}}: Die Größe des Bereichs in der {{PropertyData/de|Base View}}, der in der Detailansicht dargestellt wird.

-    {{PropertyData/de|Reference|String}}: Ein Bezeichner für die Detailansicht in der {{PropertyData/de|Base View}}.



## Eigenschaften Basisansicht 

Eine Detailansicht erbt alle anwendbaren Eigenschaften der als {{PropertyData/de|Base View}} festgelegten Ansicht. In den Eigenschaften dieser Ansicht kann das Aussehen des Detailumrisses geändert werden:

-    {{PropertyView/de|Einstellung Hervorheben}}: Drehwinkel der Detailansicht im Uhrzeigersinn.

-    {{PropertyView/de|Linienfarbe Hervorheben}}: Linienfarbe für die Umrissform. Die Standardeinstellung hierfür ist die Einstellung **Detail Hervorheben** in den [TechDraw Einstellungen](TechDraw_Preferences/de.md).

-    {{PropertyView/de|Linienstil Hervorheben}}: Linienstil für die Umrissform. Die Standardeinstellung hierfür ist die Einstellung **Detail Hervorhebungsstil** in den [TechDraw Einstellungen](TechDraw_Preferences/de.md).



## Hinweise

-   [Eine gute Aussprache über das Setzen des Ankers](https://www.forum.freecadweb.org/viewtopic.php?f=35&t=34055#p285281)



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Detailansicht kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden:


```python
Detail = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewDetail','Detail')
...TBA
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DetailView/de
