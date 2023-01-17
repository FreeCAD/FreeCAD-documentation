---
- GuiCommand:/de
   Name:TechDraw View
   Name/de:TechDraw Ansicht
   MenuLocation:TechDraw → Ansicht einfügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso:[TechDraw Projektionsgruppe einfügen](TechDraw_ProjectionGroup/de.md), [TechDraw Abschnittssansicht einfügen](TechDraw_SectionView/de.md)
---

# TechDraw View/de



## Beschreibung

Das Werkzeug Ansicht fügt eine Darstellung eines oder mehrerer Objekte einer Zeichnungsseite hinzu. Dies ist der Grundbaustein des TechDraw-Arbeitsbereichs. Die meisten anderen Ansichten werden in irgendeiner Weise von dieser Ansicht (dem View-Objekt) abgeleitet.

Ansicht wird versuchen, alles, was eine Eigenschaft `Shape` besitzt, zu zeichnen. Es können [Skizzen](Sketcher_Workbench/de.md), [PartDesign Bodies](PartDesign_Body/de.md), [Draft Objekte](Draft_Workbench/de.md) usw. ausgewählt werden. Ansicht extrahiert auch beliebige Formen aus Objekten innerhalb eines [Std Part](Std_Part/de.md) oder einer [Std Gruppe](Std_Group/de.md).

![](images/TechDraw_View_example.png ) 
*Ansicht eines Würfel-Volmenkörpers mit verdeckten Kanten*



## Anwendung

1.  Wahlweise die [3D-Ansicht](3D_view/de.md) ausrichten. Die Kamerarichtung in der [3D-Ansicht](3D_view/de.md) bestimmt die Startwerte der {{PropertyData/de|Direction}} der Ansicht.
2.  Ein oder mehrere Objekte in der [3D-Ansicht](3D_view/de.md) oder [Baumansicht](Tree_view/de.md) auswählen.
3.  Wenn das Dokument mehrere Zeichnungsblätter enthält: Wahlweise das gewünschte Blatt durch Auswahl in der [Baumansicht](Tree_view/de.md) zur Auswahl hinzufügen. Dies ist ein Muss für {{VersionMinus/de|0.19}}.
4.  Es gibr mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_View.svg" width=16px> [Ansicht einfügen](TechDraw_View/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → <img src="images/TechDraw_View.svg" width=16px> Ansicht einfügen** auswählen.
5.  Wenn das Dokument mehrere Zeichnungsblätter enthält und kein Blatt ausgewählt wurde, öffnet sich der Dialog **Blattauswahl**: {{Version/de|0.20}}
    1.  Das gewünschte Zeichnungsblatt auswählen.
    2.  Die Schaltfläche **OK** drücken.



## Eigenschaften



### Daten


{{TitleProperty|Basis}}

-    {{PropertyData/de|X|Distance}}: Die horizontale Position der Ansicht auf der Seite. (1)

-    {{PropertyData/de|Y|Distance}}: Die vertikale Position der Ansicht auf der Seite. (1)

-    {{PropertyData/de|Lock Position|Bool}}: Ist der Wert auf `True` gesetzt, wird verhindert, dass Ansichten mit der Benutzerschnittstelle (GUI) bewegt werden können. Die Ansicht kann weiterhin durch Ändern der X- und Y-Eigenschaften bewegt werden. (1)

-    {{PropertyData/de|Rotation|Angle}}: Drehung der Ansicht auf dem Zeichnungsblatt gegen den Uhrzeigersinn in Grad. (1)

-    {{PropertyData/de|Scale Type|Enumeration}}: Die Art der Skalierung. Optionen: (1)

    -   
        {{Value|Seite}}
        
        : Verwendet die Maßstabseinestellung des [Zeichnungsblattes](TechDraw_PageDefault/de.md).

    -   
        {{Value|Automatisch}}
        
        : Passt die Ansicht an die Blattgröße an.

    -   
        {{Value|Benutzerdefiniert}}
        
        : Verwendet den in der {{PropertyData/de|Scale}} definierten Maßstab.

-    {{PropertyData/de|Scale|FloatConstant}}: Die Ansicht wird auf dem Zeichnungsblatt im Verhältnis Scale:1 zur Quelle gerendert. (1)

-    {{PropertyData/de|Caption|String}}: Optionale kurze Textunterschrift. (1)


{{TitleProperty|Cosmetics}}

-    {{PropertyData/de|Cosmetic Vertexes|TechDraw::PropertyCosmeticVertexList|Hidden}}
    

-    {{PropertyData/de|Cosmetic Edges|TechDraw::PropertyCosmeticEdgeList|Hidden}}
    

-    {{PropertyData/de|Center Lines|TechDraw::PropertyCenterLineList|Hidden}}
    

-    {{PropertyData/de|Geom Formats|TechDraw::PropertyGeomFormatList|Hidden}}
    


{{TitleProperty|HLR Parameters}}

-    **Coarse View|Bool**(Grobansicht): Wenn `True`, verwendet TechDraw eine Polygonnäherung zur Berechnung der Zeichnungsgeometrie. Wenn `False`, verwendet TechDraw einen Präzisionsalgorithmus. Eine Grobansicht kann bei komplexen Modellen sehr viel schneller sein. Die Qualität der Zeichnung wird verringert, da jede Kurve als eine Reihe kurzer Liniensegmente angenähert wird. Knoten werden in einer Grobansicht nicht angezeigt, da jedes kurze Segment zu zwei neuen Knoten führen würde und damit die Anzeige unübersichtlich werden ließe. Lineare Maße können einer Grobansicht hinzugefügt werden, sind aber wahrscheinlich nicht sinnvoll.

-    **Smooth Visible|Bool**: Sichtbare Flächenübergangslinien ein/aus.

-    **Seam Visible|Bool**: Sichtbare Seam-Lines on/off.

-    **Iso Visible|Bool**: Sichtbare isoparametrische (U-, V-) Linien ein/aus.

-    **Hard Hidden|Bool**: Verdeckte Kanten ein/aus.

-    **Smooth Hidden|Bool**: Verdeckte Flächenübergangslinien ein/aus.

-    **Seam Hidden|Bool**: Verdeckte Seam-Lines ein/aus.

-    **Iso Hidden|Bool**: Verdeckte isoparametrische (U-, V-) Linien ein/aus.

-    **Iso Count|Integer**: Anzahl der isoparametrischen (U-, V-) Linien, die auf jede Fläche gezeichnet werden.


{{TitleProperty|Projection}}

-    {{PropertyData/de|Source|LinkList}}: Verweise auf die darstellbaren Objekte, die abgebildet werden sollen.

-    {{PropertyData/de|XSource|XLinkList}}: Verweise auf die darstellbaren Objekten in einer externen Datei. {{Version/de|0.19}}

-    {{PropertyData/de|Direction|Vector}}: Dieser Vektor steuert die Richtung, aus der das Objekt betrachtet wird. +X ist rechts, -X ist links, +Y ist hinten, -Y ist vorne (Blick auf den Bildschirm), +Z ist oben und -Z ist unten. Eine Vorderansicht ist also (0,-1,0) und eine isometrische Ansicht ist (1,-1,1).

-    {{PropertyData/de|XDirection|Vector}}: Dieser Vektor steuert die Rotation der Ansicht um die Blickrichtung (Direction). {{Version/de|0.19}}.

-    {{PropertyData/de|Perspective|Bool}}: `True` für perspektivische Projektion `False` für orthogonale Projektion.

-    {{PropertyData/de|Focus|Distance}}: Abstand von der Kamera zur Projektionsebene für perspektivische Projektionen. Muss auf das Objekt eingestellt werden. Zu weit und die Perspektive geht verloren, zu nah und das Objekt wird verzerrt.



### Ansicht


{{TitleProperty|Basis}}

-    {{PropertyView/de|Keep Label|Bool}}: Zeigt die Bezeichnung (Label) der Ansicht immer an, wenn `True`. (1)

-    {{PropertyView/de|Stack Order|Integer}}: Liegt davor oder dahinter im Bezug auf andere Ansichten. (1) {{Version/de|1.0}}


{{TitleProperty|Decoration}}

-    {{PropertyView/de|Arc Center Marks|Bool}}: Markierungen der Kreisbogenmitten ein/aus.

-    {{PropertyView/de|Center Scale|Float}}: Größeneinstellung für Markierungen der Kreisbogenmitten, wenn aktiviert.

-    {{PropertyView/de|Horiz Center Line|Bool}}: Stellt eine horizontale Mittellinie durch die Ansicht dar.

-    {{PropertyView/de|Section Line Color|Color}}: Legt die Farbe der Schnittlinien fest, wenn vorhanden.

-    {{PropertyView/de|Section Line Style|Enumeration}}: Legt die Linienart der Schnittlinien fest, wenn vorhanden.

-    {{PropertyView/de|Show All Edges|Bool}}: Stellt verdeckte Kanten zeitweise dar.

-    {{PropertyView/de|Show Section Line|Bool}}: Anzeigen/Ausblenden der Schnittlinien, wenn vorhanden.

-    {{PropertyView/de|Vert Center Line|Bool}}: Stellt eine Vertikale Mittellinie durch die Ansicht dar.


{{TitleProperty|Highlight}}

-    {{PropertyView/de|Highlight Adjust|Float}}: Passt die Drehung des Detail-Auswahlrahmens an, wenn vorhanden.

-    {{PropertyView/de|Highlight Line Color|Color}}: Bestimmt die Linienfarbe des Auswahlrahmens, wenn vorhanden.

-    {{PropertyView/de|Highlight Line Style|Enumeration}}: Bestimmt die Linienart des Auswahlrahmens, wenn vorhanden.


{{TitleProperty|Lines}}

-    **Extra Width|Length**: Noch nicht implementiert.

-    **Hidden Width|Length**: Linienstärke von verdeckten Kanten, wenn aktiviert.

-    **Iso Width|Length**: Die Linienstärke von isoparametrischen (U-, V-) Oberflächenl und Maßlinien.

-    **Line Width|Length**: Die Linienstärke von sichtbaren Kanten. Siehe [Liniengruppen](TechDraw_LineGroup/de.md).

\(1\) Diese Eigenschaften sind allen Ansichtstypen gemeinsam.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Ansicht kann mit [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden:


```python
view = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewPart', 'View')
rc = page.addView(view)
FreeCAD.ActiveDocument.View.Source = [App.ActiveDocument.Box]
FreeCAD.ActiveDocument.View.Direction = (0.0, 0.0, 1.0)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw View/de
