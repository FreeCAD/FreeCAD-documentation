---
 GuiCommand:
   Name: TechDraw DetailView
   Name/de: TechDraw Detailansicht
   MenuLocation: TechDraw, TechDraw Ansichten , Detailansicht einfügen
   Workbenches: TechDraw_Workbench/de
   Version: 0.19
   SeeAlso: TechDraw_View/de, TechDraw_ProjectionGroup/de
---

# TechDraw DetailView/de



## Beschreibung

Das Werkzeug **TechDraw Detailansicht** erstellt eine Ansicht eines kleinen Bereichs einer vorhandenen Ansicht.

![](images/ViewDetail.png ) 
*Detailansicht mit einem kreisförmigem Rahmen*



## Anwendung

1.  Eine Basisansicht für die Detailansicht auswählen.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_DetailView.svg" width=16px> [Detailansicht einfügen](TechDraw_DetailView/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → TechDraw Ansichten → <img src="images/TechDraw_DetailView.svg" width=16px> Detailansicht einfügen** auswählen.
3.  Ein Auswahlumriss wird zur Basisansicht hinzugefügt, eine Detailansicht zum Zeichnungsblatt hinzugefügt und ein Aufgaben-Bereich wird geöffnet.
4.  Für die Übersicht ist es am besten, die Detailansicht zu verschieben, sodass sie die Basisansicht nicht länger überlappt: Die linke Maustaste über ihrem Rahmen oder auf ihrer Benennung gedrückt halten und sie auf eine neue Position ziehen.
5.  Zum Ändern der Position des Auswahlumrisses gibt es folgende Möglichkeiten:
    -   Den Umriss ziehen:
        1.  Die Schaltfläche **Auswahl verschieben** drücken.
        2.  Der Umriss wird auf der Zeichnung markiert und die temporäre Benennung *drag* wird hinzugefügt.
        3.  Die linke Maustaste auf demUmriss selbst oder auf dieser Benennung gedrückt halten und den Umriss auf eine neue Position ziehen.
    -   Umriss durch Koordinateneingabe verschieben:
        1.  Die X- und Y-Koordinaten im Aufgaben-Bereich anpassen. Die Koordinaten beziehen sich auf den Mittelpunkt Basisansicht.
6.  Wahlweise den **Radius** der Detailansicht anpassen.
7.  Wahlweise den **Maßstab (Art)** und **Maßstab (Faktor)** der Detailansicht anpassen. Siehe [TechDraw Ansicht](TechDraw_View/de#Eigenschaften.md) für weitere Informationen.
8.  Eine Benennung unter **Referenz** angeben. Diese Benenung wird neben dem Auswahlumriss angezeigt.
9.  Die Schaltfläche **OK** drücken.



## Hinweise

-   Zum Bearbeiten wird eine Detaliansicht mit einem Doppelklick in der [Baumansicht](Tree_view/de.md) aktiviert.
-   Die Umrisse von Detailansichten können kreisförmig oder quadratisch sein. Dies wird mit der [Einstellung](TechDraw_Preferences/de#Anmerkung.md) **Umrissform für Detailansichten** gesteuert.
-   [Forum topic with a good discussion about setting the anchor.](https://www.forum.freecadweb.org/viewtopic.php?f=35&t=34055#p285281)



## Eigenschaften Detailansicht 

Siehe auch [TechDraw Ansicht](TechDraw_View/de#Eigenschaften.md).



### Daten


{{TitleProperty|Detail}}

-    {{PropertyData/de|Base View|Link}}: Die Ansicht auf der die Detailansicht basiert.

-    {{PropertyData/de|Anchor Point|Vector}}: Der Mittelpunkt der Detailansicht innerhalb der {{PropertyData/de|Base View}}.

-    {{PropertyData/de|Radius|Float}}: Die Größe des Bereichs in der {{PropertyData/de|Base View}}, der in der Detailansicht dargestellt wird.

-    {{PropertyData/de|Reference|String}}: Ein Bezeichner für die Detailansicht in der {{PropertyData/de|Base View}}.



## Eigenschaften Basisansicht 

Eine Detailansicht erbt alle anwendbaren Eigenschaften der unter {{PropertyData/de|Base View}} festgelegten Ansicht. In den Eigenschaften dieser Ansicht kann das Aussehen des Detailumrisses geändert werden:



### Ansicht


{{TitleProperty|Hightlight}}

-    {{PropertyView/de|Highlight Adjust|Float}}: Siehe [TechDraw Ansicht](TechDraw_View/de#Ansicht.md)

-    {{PropertyView/de|Highlight Line Color|Color}}: Wie vorher.

-    {{PropertyView/de|Highlight Line Style|Enumeration}}: Wie vorher.





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw DetailView/de
