---
- GuiCommand:/de
   Name:TechDraw ProjectionGroup
   Name/de:TechDraw ProjektionsGruppe
   MenuLocation:TechDraw → Projektionsgruppe einfügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso:[TechDraw Ansicht einfügen](TechDraw_View/de.md), [TechDraw Schnitt Ansicht einfügen](TechDraw_SectionView/de.md)
---

## Beschreibung

Das <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:24px;"> [ProjektionsGruppe](TechDraw_ProjectionGroup/de.md) Werkzeug erstellt eine [Mehrfachansichtsprojektion](https://en.wikipedia.org/wiki/Multiview_projection) einer oder mehrerer 3D Objekte. Die isometrischen Ansichten der vier Frontecken können ebenfalls eingeschlossen werden.

Wenn du nur eine einzige Ansicht erzeugen möchtest, ist es nicht von Vorteil, ProjektionsGruppe zu verwenden; nutze statt dessen [Ansicht einfügen](TechDraw_View/de.md). Wenn du nicht die herkömmliche [first-](https://en.wikipedia.org/wiki/Multiview_orthographic_projection#First-angle_projection) / [1](https://en.wikipedia.org/wiki/Multiview_orthographic_projection#Third-angle_projection) verwenden möchtest, solltest du mehrere *Ansichten* ([Ansichten einfügen](TechDraw_View/de.md)) anstelle von *ProjektionsGruppe* verwenden.

<img alt="" src=images/TechDraw_ProjGroup_example.png  style="width:400px;"> 
*Drei orthogonale Ansichten und eine isometrische Ansicht eines Festkörperobjekts*

## Anwendung

1.  Wähle ein oder mehrere *Körper* und/oder *Part* Objekte im 3D Fenster oder Baum. Wenn du mehrere Zeichnungsseiten in deinem Dokument hast, musst du auch die gewünschte Seite in der Baumstruktur auswählen.
2.  Drücke die **<img src="images/TechDraw_ProjectionGroup.svg" width=16px> [Projektionsgruppe einfügen](TechDraw_ProjectionGroup/de.md)** Schaltfläche
3.  Ein Dialogfeld wird geöffnet, in dem du auswählen kannst, welche Ansichten in der Gruppe erscheinen sollen, den Maßstab der Gruppe und andere Parameter:

![](images/TaskProjGroup.png ) *Projektionsgruppe [Aufgabenkonsole](Task_panel/de.md). Das zentrale Feld zeigt die aktuelle Blickrichtung mit Prozentsätzen der x, y und z-Achse an.*

Nachdem du die Projektionsgruppe erstellt hast, kannst du die Gruppe als Ganzes durch Ziehen der zentralen Ansicht verschieben. Du kannst die Projektionsansichten auch durch Ziehen verschieben.

## Eigenschaften

-    {{PropertyData/de|Anker}}: Die zentrale Ansicht in der Projektionsgruppe. Normalerweise die Vorderansicht.

-    {{PropertyData/de|ProjektionsTyp}}: \"Erster Winkel\" oder \"Dritter Winkel\".

-    {{PropertyData/de|AutoVerteilung}}: Wenn true, werden einzelne Ansichten automatisch ausgeblendet. Verwende false zur manuellen Positionierung.

-    {{PropertyData/de|AbstandX}}: Horizontaler Abstand zwischen den Ansichten bei automatischer Positionierung. Beachte, dass auch der Maßstab und die Größe der anderen Ansichten in der Gruppe den Abstand beeinflussen.

-    {{PropertyData/de|AbstandY}}: Vertikaler Abstand zwischen den Ansichten bei automatischer Anordnung.

Die Projektionsgruppe als Ganzes erbt X, Y, MaßstabsTyp, Maßstab und Drehung aus der Basisansicht.

Einzelne Ansichten innerhalb der Gruppe erben alle Teilansichtseigenschaften, aber das ProjektionsGruppen Objekt steuert den Maßstab aller seiner Mitgliedsansichten.

Die Eigenschaft des Drehvectors jeder einzelnen Ansicht innerhalb der Gruppe ist veraltet seit v0.19. Verwende stattdessen XRichtung.

Beachte, dass der mittlere Kasten die aktuelle Projektionsrichtung der primären Ansicht anzeigt. Sie kann nicht dazu benutzt werden, die Richtung zu ändern.

## Skripten


**Siehe auch:**

[TechDraw API](TechDraw_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das NeueProjGruppe Werkzeug kann in [Makros](Macros/de.md) und von der [Python](Python/de.md) Konsole aus verwendet werden. Ein vollständiges Skript ist in der Quellverteilung in \"source-dir/src/Mod/TechDraw/TDTest/DProjGroupTest.py\" verfügbar.


```python
    #make a page
    print("making a page")
    page = FreeCAD.ActiveDocument.addObject('TechDraw::DrawPage','Page')
    FreeCAD.ActiveDocument.addObject('TechDraw::DrawSVGTemplate','Template')
    FreeCAD.ActiveDocument.Template.Template = templateFileSpec
    FreeCAD.ActiveDocument.Page.Template = FreeCAD.ActiveDocument.Template

    #make projection group
    group = FreeCAD.ActiveDocument.addObject('TechDraw::DrawProjGroup','ProjGroup')
    rc = page.addView(group)
    group.Source = [fusion]

    #add Front(Anchor) view
    frontView = group.addProjection("Front")               ##need an Anchor

    #update group
    group.Anchor.Direction = FreeCAD.Vector(0,0,1)
    group.Anchor.RotationVector = FreeCAD.Vector(1,0,0)

    #add more projections
    leftView = group.addProjection("Left")
    topView = group.addProjection("Top")
    rightView = group.addProjection("Right")
    rearView = group.addProjection("Rear")
    BottomView = group.addProjection("Bottom")

    #remove a view from projection group
    iv = group.removeProjection("Left")

```

Programmierhinweis: Die Projektionsgruppe sollte immer zur Seite hinzugefügt werden (z.B. page.addView(group), bevor Projektionen zur Gruppe hinzugefügt werden. Dies ermöglicht es der Projektionsgruppe, von der übergeordneten Seite abgeleitete Standardparameterwerte zu verwenden.





{{TechDraw Tools navi

}}  
