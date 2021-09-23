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

Das Werkzeug Ansicht fügt eine Darstellung eines oder mehrerer Objekte einer Zeichnungsseite hinzu. Dies ist der Grundbaustein des TechDraw-Arbeitsbereichs. Die meisten anderen Ansichten sind in irgendeiner Weise von NeueAnsicht abgeleitet.

![](images/TechDraw_View_example.png ) *Ansicht eines massiven Gehäuses mit unsichtbaren Linien*

## Anwendung

1.  Wähle eine oder mehrere Objekte (Körper, App::Part, Part::Formelement, Entwurfsobjekt, \...siehe Hinweise) im [3D Ansicht](3D_view/de.md) oder [Baumansicht](Tree_view/de.md).
2.  Wenn du mehrere Zeichnungsseiten in deinem Dokument hast, musst du auch die gewünschte Seite im Baum auswählen. Verwende die **Strg**, um mehrere Elemente im Baum auszuwählen.
3.  Drücke die **<img src="images/TechDraw_View.svg" width=16px> [Ansicht einfügen](TechDraw_View/de.md)** Schaltfläche

Ansicht wird versuchen, alles mit einer `Form` Eigenschaft zu zeichnen. Du kannst [Entwurf](Draft_Workbench/de.md) Objekte und [PartDesign Körper](PartDesign_Body/de.md) auch auswählen. Ansicht extrahiert auch beliebige Formen aus Objekten innerhalb eines [App::Part](Std_Part/de.md) Containers oder einer [Gruppe](Std_Group/de.md).

## Eigenschaften

### Daten


{{TitleProperty|Basis}}

-    {{PropertyData/de|X}}: Die horizontale Position der Ansicht auf der Seite. (1)

-    {{PropertyData/de|Y}}: Die vertikale Position der Ansicht auf der Seite. (1)

-    {{PropertyData/de|PositionSperren}}: Verhindert, dass Ansichten in die Gui gezogen werden, wenn sie true sind. Die Ansicht kann weiterhin durch Ändern der X,Y-Eigenschaften bewegt werden. (1)

-    {{PropertyData/de|Rotation}}: Drehung der Ansicht auf der Seite gegen den Uhrzeigersinn in Grad. (1)

-    {{PropertyData/de|SkalierungTyp}}: \"Dokument\": Verwende die Maßstabseinstellung der Seite. \"Benutzerdefiniert\": verwende einen für diese Ansicht einzigartigen Maßstab. \"Automatisch\": Ansicht an die Seite anpassen. (1)

-    {{PropertyData/de|Maßstab}}: Eine Ansicht wird auf der Seite im Verhältnis Maßstab:1 zur Quelle gerendert. (1)

-    {{PropertyData/de|Bildunterschrift}}: Optionale kurze Textunterschrift.


{{TitleProperty|Kosmetik}}


{{TitleProperty|HLR Parameters}}

-    **GrobAnsicht**: Wenn {{Incode|true}}, verwendet TechDraw eine Polygonnäherung zur Berechnung der Zeichnungsgeometrie. Wenn {{Incode|false}}, verwendet TechDraw einen Präzisionsalgorithmus. GrobAnsicht kann bei komplexen Modellen viel schneller sein. Die Qualität der Zeichnung wird verringert, da jede Kurve als eine Reihe kurzer Liniensegmente angenähert wird. Knoten werden in GrobAnsicht nicht angezeigt, da jedes kurze Segment zu zwei neuen Knoten führen würde und die Anzeige unübersichtlich wird. Lineare Bemaßungen können einer GrobAnsicht hinzugefügt werden, sind aber wahrscheinlich nicht sinnvoll.

:   
    **Hinweis:**GrobAnsicht ist von einem Upstream-Fehler in OCCT betroffen ([\#3332](https://www.freecadweb.org/tracker/view.php?id=3332)), was dazu führt, dass die Position der Ansicht auf der Seite leicht von den angegebenen X,Y-Werten abweicht.

-    **durchgehende Linie sichtbar**: Sichtbare durchgehende Linie ein/aus.

-    **Seam Visible**: Visible Seam lines on/off.

-    **Iso Sichtbar**: Sichtbare isometrische(u,v) Linien ein/aus.

-    **Hard Ausgeblendet**: Unsichtbare Linien ein/aus.

-    **Smooth Ausgeblendet**: Hidden Smooth Lines ein/aus.

-    **Seam Ausgeblendet**: Unsichtbare Seam Lines ein/aus.

-    **Iso Ausgeblendet**: Unsichtbare isometrische(u,v) Linien ein/aus.

-    **Iso Anzahl**: Anzahl der isometrischen(u,v) Linien, die auf jede Fläche gezeichnet werden sollen.


{{TitleProperty|Projektion}}

-    **Source**: Verweise auf die abgebildeten zeichenbaren Objekten.

-    **XSource**: Verweise auf die zeichenbaren Objekten in einer externen Datei. <small>(v0.19)</small> 

-    **Direction**: Dieser Vektor steuert die Richtung, aus der du das Objekt betrachtest. +X ist rechts, -X ist links, +Y ist hinten, -Y ist vorne (Blick in den Bildschirm), +Z ist oben und -Z ist unten. Eine Vorderansicht ist also (0,-1,0) und eine isometrische Ansicht ist (1,-1,1). (1)

-    **XDirection**: dieser Vektor steuert die Rotation der Ansicht um die Richtung. <small>(v0.19)</small> . (1)

-    **Perspective**: {{Incode|true}} bei perspektivischer Projektion, {{Incode|false}} bei orthogonaler Projektion.

-    **Focus**: Abstand von der Kamera zur Projektionsebene für perspektivische Projektionen. Muss an das Objekt angepasst werden. Zu weit und die Perspektive geht verloren, zu nah und das Objekt wird verzerrt.

\(1\) Diese Eigenschaften sind allen Ansichtstypen gemeinsam.

### Ansicht

-    {{PropertyView/de|Keep Label}}: »True» -- die Beschriftung (Untertitel) der Ansicht wird immer dargestellt..

-    {{PropertyView/de|LineWidth}}: Linienstärke der sichtbaren Linien. Siehe auch [Liniengruppen](TechDraw_LineGroup/de.md).

-    {{PropertyView/de|HiddenWidth}}: Lininienstärke der verdeckten Linien, wenn aktiviert.

-    {{PropertyView/de|IsoWidth}}: Linienstärke der isometrischen (u, v) Flächen- und Bemaßungslinien.

-    {{PropertyView/de|ExtraWidth}}: Noch nicht implementiert.

-    {{PropertyView/de|ShowCenters}}: Kreis- / Bogenmittelpunkte AN/AUS.

-    {{PropertyView/de|CenterScale}}: Größeneinstellung der Kreisbogenmarkierung, wenn aktiviert.

-    {{PropertyView/de|HorizCenterLine}}: Horizontale Mittellinie durch die Ansicht wird dargestellt.

-    {{PropertyView/de|VertCenterLine}}: Vertikale Mittellinie durch die Ansicht wird dargestellt.

-    {{PropertyView/de|ShowSectionLine}}: Schnittlinie ein- und ausblenden, falls vorhanden.

## Skripten


**Siehe auch:**

[TechDraw Anwendungsschnittstelle](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Neue Ansicht Werkzeug kann mit [Makros](Macros/de.md) und von der [Python](Python/de.md) Konsole aus mithilfe der folgenden Funktionen verwendet werden:


```python
view = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewPart','View')
rc = page.addView(view)
FreeCAD.ActiveDocument.View.Source = [App.ActiveDocument.Box]
FreeCAD.ActiveDocument.View.Direction = (0.0,0.0,1.0)
```





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw View/de
