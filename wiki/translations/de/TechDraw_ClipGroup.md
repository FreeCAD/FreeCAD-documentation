---
 GuiCommand:
   Name: TechDraw ClipGroup
   Name/de: TechDraw Ausschnittsgruppe
   MenuLocation: TechDraw , TechDraw Ansichten , Ausschnittsgruppe einfügen
   Workbenches: TechDraw_Workbench/de
   SeeAlso: 
---

# TechDraw ClipGroup/de



## Beschreibung

Das Werkzeug **TechDraw Ausschnittsgruppe** erstellt ein Ausschnittfenster, das Ansichten enthalten kann.

![](images/TechDraw_Clipview.png ) 
*Ausschnittfenster, das verschiedene vorhandene Ansichten beschneidet*



## Anwendung

1.  \# Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind: Wahlweise das gewünschte Zeichnungsblatt durch Auswahl in der [Baumansicht](Tree_view/de.md) aktivieren.
2.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_ClipGroup.svg" width=16px> [Ausschnittsgruppe einfügen](TechDraw_ClipGroup/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → TechDraw Ausschnittsgruppe → <img src="images/TechDraw_ClipGroup.svg" width=16px> Ausschnittsgruppe einfügen** auswählen.
3.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind und noch kein Blatt aktiviert wurde, wird das Dialogfeld **Blattauswahl** geöffnet:
    1.  Das gewünschte Blatt auswählen.
    2.  Die Schaltfläche **OK** drücken.
4.  Ansichten können durch Ziehen und Ablegen in der Baumansicht der Ausschnittsgruppe hinzugefügt und aus ihr entfernt werden. {{Version/de|1.0}}



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Eine Ausschnittsgruppe, oder formal ein {{Incode|TechDraw::DrawViewClip}}-Objekt, besitzt die gemeinsamen [Eigenschaften](TechDraw_View/de#Eigenschaften_der_Bauteilansicht.md) aller Ansichtsarten. Sie enthält außerdem die folgenden Eigenschaften:



### Daten


{{TitleProperty|Clip Group}}

-    {{PropertyData/de|Width|Length}}: Die Breite des Ausschnittfensters in Einheiten.

-    {{PropertyData/de|Height|Length}}: Die Höhe des Ausschnittfensters in Einheiten.

-    {{PropertyData/de|ShowFrame|Bool}}: Wenn `True`, wird ein Rahmen um das Ausschnittfenster herum dargestellt.

-    {{PropertyData/de|Views|LinkList}}: Die im Ausschnittfenster enthaltenen Ansichten.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ClipGroup/de
