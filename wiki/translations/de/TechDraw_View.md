---
 GuiCommand:
   Name: TechDraw View
   Name/de: TechDraw Ansicht
   MenuLocation: TechDraw, TechDraw Ansichten , Ansicht einfügen
   Workbenches: TechDraw_Workbench/de
   SeeAlso: TechDraw_ProjectionGroup/de, TechDraw_SpreadsheetView/de, TechDraw_ArchView/de, TechDraw_Symbol/de, TechDraw_Image/de
---

# TechDraw View/de



## Beschreibung

Das Werkzeug **TechDraw Ansicht** fügt eine Darstellung eines oder mehrerer Objekte einer Zeichnungsseite hinzu. {{Version/de|1.0}}: Es kann [Elemente einer Ansichtengruppe (einzelne Ansichten)](#Properties_Projection_Group_Item.md), eine [Ansichtengruppe](TechDraw_ProjectionGroup/de.md), eine [Tabellenansicht](TechDraw_SpreadsheetView/de.md), eine [Arch-Ansicht](TechDraw_ArchView/de.md), ein [Symbol](TechDraw_Symbol/de.md) oder eine [Bildansicht](TechDraw_Image/de.md) erstellen.

In {{VersionMinus/de|0.21}} kann das Werkzeug nur eine [Bauteilansicht](#Properties_Part_View/de.md) erstellen, die einem Element der Ansichtengruppe sehr ähnlich ist.

![](images/TechDraw_View_example.png ) 
*Ansicht eines Würfel-Volmenkörpers mit verdeckten Kanten*



## Anwendung der Elemente einer Ansichtengruppe und der Ansichtengruppe 

1.  Wahlweise die [3D-Ansicht](3D_view/de.md) ausrichten. Die Richtung der Kamera in der 3D-Ansicht kann zum Festlegen der Projektionsrichtung der primären Ansicht eingesetzt werden.
2.  Ein oder mehrere Objekte mit einer {{PropertyData/de|Shape}} in der 3D-Ansicht oder der [Baumansicht](Tree_view/de.md) auswählen. Es können auch [Std Parts](Std_Part/de.md) oder [Std Gruppen](Std_Group/de.md) ausgewählt werden, die solche Objekte enthalten. Wird in der 3D-Ansicht ausgewählt, kann die erste ausgewählte Fläche zum Festlegen der Projektionsrichtung der primären Ansicht eingesetzt werden. Es sollte kein Objekt in der 3D-Ansicht ausgewählt werden, wenn die aktuelle Kameraausrichtung verwendet werden soll.
3.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind: Wahlweise das gewünschte Zeichnungsblatt durch Auswählen in der [Baumansicht](Tree_view/de.md) zur Auswahl hinzufügen.
4.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_View.svg" width=16px> [Ansicht einfügen](TechDraw_View/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → TechDraw Ansichten → <img src="images/TechDraw_View.svg" width=16px> Ansicht einfügen** auswählen.
5.  Wenn mehrere Zeichnungsblätter im Dokument vorhanden sind und kein Blatt im [Hauptansichtsbereich](Main_view_area/de.md) angezeigt wird und außerdem noch kein Blatt aktiviert wurde, wird das Dialogfeld **Blattauswahl** geöffnet:
    1.  Das gewünschte Zeichnungsblatt auswählen.
    2.  Die Schaltfläche **OK** drücken.
6.  Das Aufgaben-Fenster **Ansichtengruppe** wird geöffnet. {{Version/de|1.0}}
7.  Wahlweise die Parameter anpassen:
    -   **Skalieren**: {{Value|Seite}}, {{Value|Automatisch}} oder {{Value|Benutzerdefiniert}} auswählen. Wurde die letzte Möglichkeit ausgewählt: Zähler und Nenner des Maßstabs eingeben.
    -   **Richtung**: Mit den zur Verfügung stehenden Schaltflächen die Projektionsrichtung einstellen und die primäre Ansicht drehen:
        -   Die Schaltfläche **[#.## #.## #.##]** in der Mitte zeigt die aktuelle Projektionsrichtung an. Die anfänglichen Werte hängen von der [Voreinstellung](TechDraw_Preferences/de#Allgemeines.md) **3D-Kamerarichtung verwenden** ab. Die Schaltfläche drücken, um Ausrichtung und Drehung der Ansicht manuell einzustellen.
        -   Die Schaltfläche **<img src="images/Arrow-up.svg" width=16px>**, **<img src="images/Arrow-down.svg" width=16px>**, **<img src="images/Arrow-left.svg" width=16px>** oder **<img src="images/Arrow-right.svg" width=16px>** drücken, um die Projektionsrichtung in 90°-Schritten um die horizontale bzw. vertikale Achse der Ansicht zu drehen.
        -   Die Schaltfläche **<img src="images/Arrow-cw.svg" width=16px>** oder **<img src="images/Arrow-ccw.svg" width=16px>** drücken, um die Ansicht in 90°-Schritten um die Projektionsrichtung zu drehen.
        -   Die Schaltfläche **<img src="images/TechDraw_ProjFront.svg" width=16px>** drücken, um die Projektionsrichtung der primären Ansicht auf die normale [Vorderansicht](Std_ViewFront/de.md) einzustellen.
        -   Die Schaltfläche **<img src="images/TechDraw_CameraOrientation.svg" width=16px>** drücken, um die Projektionsrichtung auf die zuerst ausgewählte Fläche auszurichten, falls möglich, oder andernfalls entsprechend der aktuellen Kameraausrichtung.
    -   **Sekundäre Ansichten**: Wahlweise sekundäre Ansichten zusätzlich zu der Primären Ansicht erstellen. Es muss wenigstens eine sekundäre Ansicht aktiviert werden, damit alle Bedienelemente für diesen Bereich angezeigt werden.
8.  Wurden einige Parameter geändert, kann es erforderlich sein, die Schaltfläche **Anwenden** zu drücken, um die Ansicht(en) zu aktualisieren.
9.  Die Schaltfläche **OK** drücken.
10. Ein [Element der Ansichtengruppe](#Properties_Projection_Group_Item/de.md) wird eingefügt oder, wenn es eine oder mehrere sekundäre Ansichten gibt, eine [Ansichtengruppe](TechDraw_ProjectionGroup/de.md).

![](images/TechDraw_View_Taskpanel.png ) 
*[Ansicht-Fenster](Task_panel/de.md) Bauteilansicht*



## Anwendung der anderen Ansichtsarten 


{{Version/de|1.0}}

1.  Wahlweise eine [Kalkulationstabelle](Spreadsheet_CreateSheet/de.md) in der [Baumansicht](Tree_view/de.md) oder eine [Arch-Schnittebene](Arch_SectionPlane/de.md) in der [3D-Ansicht](3D_view/de.md) oder der Baumansicht auswählen.
2.  Die Schritte 3, 4 und 5 durchführen, wie [oben](#Anwendung_der_Elemente_einer_Ansichtengruppe_und_der_Ansichtengruppe.md) beschrieben.
3.  Wurde noch keine Tabelle oder Arch-Schnittebene ausgewählt:
    1.  Ein warnendes Dialogfenster wird geöffnet.
    2.  Die Checkbox **Do not show this message again** aktivieren, um dieses Dialogfenster in Zukunft zu vermeiden.
    3.  Die Schaltfläche **OK** drücken.
    4.  Ein Datei-Browser wird geöffnet.
    5.  Eine SVG- oder Bilddatei auswählen.
4.  Eine [Tabellenansicht](TechDraw_SpreadsheetView/de.md), eine [Arch-Ansicht](TechDraw_ArchView/de.md), ein [Symbol](TechDraw_Symbol/de.md) oder eine [Bildansicht](TechDraw_Image/de.md) wird eingefügt.
5.  Im Falle einer Tabellenansicht: Den Bereich der Zellen einstellen; hierfür ihre {{PropertyData/de|Cell Start}} und {{PropertyData/de|Cell End}} anpassen.
6.  Im Falle eines Symbols oder einer Bildansicht: Wahlweise die {{PropertyData/de|Scale}} anpassen, um die Größe einzustellen.



## Eigenschaften der Bauteilansicht 

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Eine Bauteilansicht, oder formal ein {{Incode|TechDraw::DrawViewPart}}-Objekt, besitzt die folgenden Eigenschaften:



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

-    {{PropertyData/de|Coarse View|Bool}}(Grobansicht): Wenn `True`, verwendet TechDraw eine Polygonnäherung zur Berechnung der Zeichnungsgeometrie. Wenn `False`, verwendet TechDraw einen Präzisionsalgorithmus. Eine Grobansicht kann bei komplexen Modellen sehr viel schneller sein. Die Qualität der Zeichnung wird verringert, da jede Kurve als eine Reihe kurzer Liniensegmente angenähert wird. Knoten werden in einer Grobansicht nicht angezeigt, da jedes kurze Segment zu zwei neuen Knoten führen würde und damit die Anzeige unübersichtlich werden ließe. Lineare Maße können einer Grobansicht hinzugefügt werden, sind aber wahrscheinlich nicht sinnvoll.

-    {{PropertyData/de|Smooth Visible|Bool}}: Sichtbare Flächenübergangslinien ein/aus.

-    {{PropertyData/de|Seam Visible|Bool}}: Sichtbare Seam-Lines on/off.

-    {{PropertyData/de|Iso Visible|Bool}}: Sichtbare isoparametrische (U-, V-) Linien ein/aus.

-    {{PropertyData/de|Hard Hidden|Bool}}: Verdeckte Kanten ein/aus.

-    {{PropertyData/de|Smooth Hidden|Bool}}: Verdeckte Flächenübergangslinien ein/aus.

-    {{PropertyData/de|Seam Hidden|Bool}}: Verdeckte Seam-Lines ein/aus.

-    {{PropertyData/de|Iso Hidden|Bool}}: Verdeckte isoparametrische (U-, V-) Linien ein/aus.

-    {{PropertyData/de|Iso Count|Integer}}: Anzahl der isoparametrischen (U-, V-) Linien, die auf jede Fläche gezeichnet werden.

-    **Scrub Count|Integer**: Die Anzahl der Versuche, die FreeCAD zur Bereinigung von HLR-Ergebnissen durchführen soll. {{Version/de|0.21}}


{{TitleProperty|Projection}}

-    {{PropertyData/de|Source|LinkList}}: Verweise auf die darstellbaren Objekte, die abgebildet werden sollen.

-    {{PropertyData/de|XSource|XLinkList}}: Verweise auf die darstellbaren Objekten in einer externen Datei.

-    {{PropertyData/de|Direction|Vector}}: Dieser Vektor steuert die Richtung, aus der das Objekt betrachtet wird. +X ist rechts, -X ist links, +Y ist hinten, -Y ist vorne (Blick auf den Bildschirm), +Z ist oben und -Z ist unten. Eine Vorderansicht ist also (0,-1,0) und eine isometrische Ansicht ist (1,-1,1).

-    {{PropertyData/de|XDirection|Vector}}: Dieser Vektor steuert die Rotation der Ansicht um die Blickrichtung (Direction).

-    {{PropertyData/de|Perspective|Bool}}: `True` für perspektivische Projektion `False` für orthogonale Projektion.

-    {{PropertyData/de|Focus|Distance}}: Abstand von der Kamera zur Projektionsebene für perspektivische Projektionen. Muss auf das Objekt eingestellt werden. Zu weit und die Perspektive geht verloren, zu nah und das Objekt wird verzerrt.



### Ansicht


{{TitleProperty|Basis}}

-    {{PropertyView/de|Keep Label|Bool}}: Zeigt die Bezeichnung (Label) der Ansicht immer an, wenn `True`. (1)

-    {{PropertyView/de|Stack Order|Integer}}: Liegt davor oder dahinter im Bezug auf andere Ansichten. (1) {{Version/de|0.21}}


{{TitleProperty|Broken View}}

-    {{PropertyView/de|Break Line Style|Enumeration}}: Legt die Linienart der Bruchlinien fest, falls anwendbar. {{Version/de|1.0}}

-    {{PropertyView/de|Break Line Type|Enumeration}}: Bestimmt die Darstellungsart der Bruchlinien in unterbrochenen Ansichten, falls anwendbar: {{Value|None}}, {{Value|ZigZag}} or {{Value|Simple}}. {{Version/de|1.0}}


{{TitleProperty|Decoration}}

-    {{PropertyView/de|Arc Center Marks|Bool}}: Markierungen der Kreisbogenmitten ein/aus.

-    {{PropertyView/de|Center Scale|Float}}: Größeneinstellung für Markierungen der Kreisbogenmitten, wenn aktiviert.

-    {{PropertyView/de|Horiz Center Line|Bool}}: Stellt eine horizontale Mittellinie durch die Ansicht dar.

-    {{PropertyView/de|Show All Edges|Bool}}: Stellt verdeckte Kanten zeitweise dar.

-    {{PropertyView/de|Vert Center Line|Bool}}: Stellt eine Vertikale Mittellinie durch die Ansicht dar.


{{TitleProperty|Faces}}

-    {{PropertyView/de|Face Color|Color}}: Legt die Farbe der Flächen fest. {{Version/de|1.0}}

-    {{PropertyView/de|Face Transparency|Percent}}: Legt die Transparenz der Flächen fest. {{Version/de|1.0}}


{{TitleProperty|Highlight}}

-    {{PropertyView/de|Highlight Adjust|Float}}: Passt die Drehung des Detail-Auswahlrahmens an, wenn vorhanden.

-    {{PropertyView/de|Highlight Line Color|Color}}: Bestimmt die Linienfarbe des Auswahlrahmens, wenn vorhanden.

-    {{PropertyView/de|Highlight Line Style|Enumeration}}: Bestimmt die Linienart des Auswahlrahmens, wenn vorhanden.


{{TitleProperty|Lines}}

-    {{PropertyView/de|Extra Width|Length}}: Noch nicht implementiert.

-    {{PropertyView/de|Hidden Width|Length}}: Linienstärke von verdeckten Kanten, wenn aktiviert.

-    {{PropertyView/de|Iso Width|Length}}: Die Linienstärke von isoparametrischen (U-, V-) Oberflächenl und Maßlinien.

-    {{PropertyView/de|Line Width|Length}}: Die Linienstärke von sichtbaren Kanten. Siehe [Liniengruppen](TechDraw_LineGroup/de.md).


{{TitleProperty|Section Line}}

-    {{PropertyView/de|Include Cut Line|Bool}}: Blendet nur die eigentliche Schnittlinie ein- bzw. aus, falls anwendbar. {{Version/de|1.0}}

-    {{PropertyView/de|Section Line Color|Color}}: Legt die Farbe der Schnittlinie fest, falls anwendbar.

-    {{PropertyView/de|Section Line Marks|Bool}}: Blendet die Markierungen an Richtungswechseln der Schnittlinie einer komplexen Schnittansicht ein- bzw. aus, falls anwendbar. {{Version/de|0.21}}

-    {{PropertyView/de|Section Line Style|Enumeration}}: Legt die Linienart der Schnittlinie fest, falls anwendbar.

-    {{PropertyView/de|Show Section Line|Bool}}: Blendet die Schnittlinie (alle Bestandteile) ein- bzw. aus, falls anwendbar.

\(1\) Diese Eigenschaften sind allen Ansichtstypen gemeinsam.



## Eigenschaften der Elemente einer Ansichtengruppe 

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Ein Element der Ansichtengruppe, formal ein {{Incode|TechDraw::DrawProjGroupItem}}-Objekt, wird von einer [Bauteilansicht](#Properties_Part_View/de.md), formal ein {{Incode|TechDraw::DrawViewPart}}-Objekt abgeleitet und erbt alle seine Eigenschaften. Es besitzt außerdem die folgenden Eigenschaften:



### Daten 


{{TitleProperty|Basis}}

-    {{PropertyData/de|Type|Enumeration}}: Die Art der Ansicht ({{Value|Vorderansicht}}, {{Value|Ansicht von links}} usw.).

-    {{PropertyData/de|Rotation Vector|Vector}}: Veraltet, stattdessen {{PropertyData/de|XDirection}} verwenden.



## Eigenschaften der Ansichtengruppe 

Siehe [TechDraw Ansichtengruppe](TechDraw_ProjectionGroup/de#Eigenschaften.md).



## Eigenschaften der Tabellenansicht 

Siehe [TechDraw Tabellenansicht](TechDraw_SpreadsheetView/de#Eigenschaften.md).



## Eigenschaften der Arch-Ansicht 

Siehe [TechDraw Arch-Ansicht](TechDraw_ArchView/de#Eigenschaften.md)



## Eigenschaften des Symbols 

Siehe [TechDraw Symbol](TechDraw_Symbol/de#Eigenschaften.md).



## Eigenschaften der Bildansicht 

Siehe [TechDraw Bild](TechDraw_Image/de#Eigenschaften.md).



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Eine Bauteilansicht kann mit [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen erstellt werden:


```python
import FreeCAD as App

doc = App.ActiveDocument
box = doc.addObject("Part::Box", "Box")

page = doc.addObject("TechDraw::DrawPage", "Page")
template = doc.addObject("TechDraw::DrawSVGTemplate", "Template")
template.Template = App.getResourceDir() + "Mod/TechDraw/Templates/A4_LandscapeTD.svg"
page.Template = template

# Toggle the visibility of the page to ensure its width and height are updated (hack):
page.Visibility = False
page.Visibility = True

view = doc.addObject("TechDraw::DrawViewPart", "View")
page.addView(view)
view.Source = [box]
view.Direction = (0, 0, 1)

view.X = page.PageWidth / 2
view.Y = page.PageHeight / 2

doc.recompute()
```





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw View/de
