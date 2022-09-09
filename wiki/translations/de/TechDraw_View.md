---
- GuiCommand   */de
   Name   *TechDraw View
   Name/de   *TechDraw Ansicht
   MenuLocation   *TechDraw → Ansicht einfügen
   Workbenches   *[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso   *[TechDraw Projektionsgruppe einfügen](TechDraw_ProjectionGroup/de.md), [TechDraw Abschnittssansicht einfügen](TechDraw_SectionView/de.md)
---

# TechDraw View/de

## Beschreibung

Das Werkzeug Ansicht fügt eine Darstellung eines oder mehrerer Objekte einer Zeichnungsseite hinzu. Dies ist der Grundbaustein des TechDraw-Arbeitsbereichs. Die meisten anderen Ansichten werden in irgendeiner Weise von dieser Ansicht (dem View-Objekt) abgeleitet.

Ansicht wird versuchen, alles, was eine Eigenschaft `Shape` besitzt, zu zeichnen. Es können [Skizzen](Sketcher_Workbench/de.md), [PartDesign Bodies](PartDesign_Body/de.md), [Draft Objekte](Draft_Workbench/de.md) usw. Ansicht extrahiert auch beliebige Formen aus Objekten innerhalb eines [Std Part](Std_Part/de.md) oder einer [Std Gruppe](Std_Group/de.md).

![](images/TechDraw_View_example.png ) 
*Ansicht eines Würfel-Volmenkörpers mit verdeckten Kanten*

## Anwendung

1.  Wahlweise die [3D-Ansicht](3D_view/de.md) ausrichten. Die Kamerarichtung in der [3D-Ansicht](3D_view/de.md) bestimmt die Startwerte der {{PropertyData/de|Direction}} der Ansicht.
2.  Ein oder mehrere Objekte in der [3D-Ansicht](3D_view/de.md) oder [Baumansicht](Tree_view/de.md) auswählen.
3.  Wenn das Dokument mehrere Zeichnungsblätter enthält   * Wahlweise das gewünschte Blatt durch Auswahl in der [Baumansicht](Tree_view/de.md) zur Auswahl hinzufügen. Dies ist ein Muss für {{VersionMinus/de|0.19}}.
4.  Es gibr mehrere Möglichkeiten das Werkzeug aufzurufen   *
    -   Die Schaltfläche **<img src="images/TechDraw_View.svg" width=16px> [Ansicht einfügen](TechDraw_View/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → <img src="images/TechDraw_View.svg" width=16px> Ansicht einfügen** auswählen.
5.  Wenn das Dokument mehrere Zeichnungsblätter enthält und kein Blatt ausgewählt wurde, öffnet sich der Dialog **Blattauswahl**   * {{Version/de|0.20}}
    1.  Das gewünschte Zeichnungsblatt auswählen.
    2.  Die Schaltfläche **OK** drücken.

## Eigenschaften

### Daten


{{TitleProperty|Basis}}

-    {{PropertyData/de|X}}   * Die horizontale Position der Ansicht auf der Seite. (1)

-    {{PropertyData/de|Y}}   * Die vertikale Position der Ansicht auf der Seite. (1)

-    {{PropertyData/de|Lock Position}}   * Ist der Wert auf true gesetzt, wird verhindert, dass Ansichten mit der Benutzerschnittstelle (GUI) bewegt werden können. Die Ansicht kann weiterhin durch Ändern der X- und Y-Eigenschaften bewegt werden. (1)

-    {{PropertyData/de|Rotation}}   * Drehung der Ansicht auf dem Zeichnungsblatt gegen den Uhrzeigersinn in Grad. (1)

-    {{PropertyData/de|ScaleType}}   * \"Dokument\"   * Verwendet die Maßstabseinstellung des Zeichnungsblattes. \"Benutzerdefiniert\"   * Verwendet einen abweichenden Maßstab für diese Ansicht. \"Automatisch\"   * Passt die Ansicht an die Blattgröße an. (1)

-    {{PropertyData/de|Scale}}   * Eine Ansicht wird auf dem Zeichnungsblatt im Verhältnis Scale   *1 zur Quelle gerendert. (1)

-    {{PropertyData/de|Caption}}   * Optionale kurze Textunterschrift.

\(1\) Diese Eigenschaften sind allen Ansichtstypen gemeinsam.


{{TitleProperty|Cosmetics}}


{{TitleProperty|HLR Parameters}}

-    {{PropertyData/de|Coarse View}}(Grobansicht)   * Wenn {{Incode|true}}, verwendet TechDraw eine Polygonnäherung zur Berechnung der Zeichnungsgeometrie. Wenn {{Incode|false}}, verwendet TechDraw einen Präzisionsalgorithmus. Eine Grobansicht kann bei komplexen Modellen sehr viel schneller sein. Die Qualität der Zeichnung wird verringert, da jede Kurve als eine Reihe kurzer Liniensegmente angenähert wird. Knoten werden in einer Grobansicht nicht angezeigt, da jedes kurze Segment zu zwei neuen Knoten führen würde und damit die Anzeige unübersichtlich werden ließe. Lineare Maße können einer Grobansicht hinzugefügt werden, sind aber wahrscheinlich nicht sinnvoll.

-    {{PropertyData/de|Smooth Visible}}   * Sichtbare Flächenübergangslinien ein/aus.

-    {{PropertyData/de|Seam Visible}}   * Sichtbare Seam-Lines on/off.

-    {{PropertyData/de|Iso Visible}}   * Sichtbare isoparametrische (U-, V-) Linien ein/aus.

-    {{PropertyData/de|Hard Hidden}}   * Verdeckte Kanten ein/aus.

-    {{PropertyData/de|Smooth Hidden}}   * Verdeckte Flächenübergangslinien ein/aus.

-    {{PropertyData/de|Seam Hidden}}   * Verdeckte Seam-Lines ein/aus.

-    {{PropertyData/de|Iso Hidden}}   * Verdeckte isoparametrische (U-, V-) Linien ein/aus.

-    {{PropertyData/de|Iso Count}}   * Anzahl der isoparametrischen (U-, V-) Linien, die auf jede Fläche gezeichnet werden.


{{TitleProperty|Projection}}

-    {{PropertyData/de|Source}}   * Verweise auf die darstellbaren Objekte, die abgebildet werden sollen.

-    {{PropertyData/de|XSource}}   * Verweise auf die darstellbaren Objekten in einer externen Datei. {{Version/de|0.19}}

-    {{PropertyData/de|Direction}}   * Dieser Vektor steuert die Richtung, aus der das Objekt betrachtet wird. +X ist rechts, -X ist links, +Y ist hinten, -Y ist vorne (Blick auf den Bildschirm), +Z ist oben und -Z ist unten. Eine Vorderansicht ist also (0,-1,0) und eine isometrische Ansicht ist (1,-1,1).

-    {{PropertyData/de|XDirection}}   * dieser Vektor steuert die Rotation der Ansicht um die Blickrichtung (Direction). {{Version/de|0.19}}.

-    {{PropertyData/de|Perspective}}   * {{Incode|true}} für perspektivische Projektion, {{Incode|false}} für orthogonale Projektion.

-    {{PropertyData/de|Focus}}   * Abstand von der Kamera zur Projektionsebene für perspektivische Projektionen. Muss auf das Objekt eingestellt werden. Zu weit und die Perspektive geht verloren, zu nah und das Objekt wird verzerrt.

### Ansicht

-    {{PropertyView/de|Keep Label}}   * Wenn True, wird die Bildunterschrift (Label) der Ansicht immer dargestellt.

-    {{PropertyView/de|LineWidth}}   * Strichstärke der sichtbaren Linien. Siehe auch [Liniengruppen](TechDraw_LineGroup/de.md).

-    {{PropertyView/de|HiddenWidth}}   * Strichstärke der verdeckten Linien, wenn aktiviert.

-    {{PropertyView/de|IsoWidth}}   * Strichstärke der isoparametrischen (U-, V-) Flächenlinien und der Maßlinien.

-    {{PropertyView/de|ExtraWidth}}   * Noch nicht implementiert.

-    {{PropertyView/de|ShowCenters}}   * Kreis-und Bogenmittelpunkte ein-/ausschalten.

-    {{PropertyView/de|CenterScale}}   * Größeneinstellung für Kreis- und Bogenmittelpunkte, wenn aktiviert.

-    {{PropertyView/de|HorizCenterLine}}   * Stellt eine horizontale Mittellinie durch die Ansicht dar.

-    {{PropertyView/de|VertCenterLine}}   * Stellt eine vertikale Mittellinie durch die Ansicht dar.

-    {{PropertyView/de|ShowSectionLine}}   * Schnittlinie ein-/ausblenden, falls anwendbar.

## Skripten


**Siehe auch   ***

[TechDraw Anwendungsschnittstelle](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Ansicht kann mit [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden   *


```python
view = FreeCAD.ActiveDocument.addObject('TechDraw   *   *DrawViewPart','View')
rc = page.addView(view)
FreeCAD.ActiveDocument.View.Source = [App.ActiveDocument.Box]
FreeCAD.ActiveDocument.View.Direction = (0.0,0.0,1.0)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw View/de
