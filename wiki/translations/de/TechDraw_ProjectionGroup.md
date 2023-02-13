---
- GuiCommand:/de
   Name:TechDraw ProjectionGroup
   Name/de:TechDraw Ansichtengruppe
   MenuLocation:TechDraw → Ansichtengruppe einfügen
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   SeeAlso:[TechDraw Ansicht einfügen](TechDraw_View/de.md), [TechDraw Schnitt Ansicht einfügen](TechDraw_SectionView/de.md)
---

# TechDraw ProjectionGroup/de



## Beschreibung

Das Werkzeug <img alt="" src=images/TechDraw_ProjectionGroup.svg  style="width:24px;"> [Ansichtengruppe](TechDraw_ProjectionGroup/de.md) erstellt eine Mehrtafelprojektion eines oder mehrerer 3D-Objekte (Siehe [Normalprojektion](https://de.wikipedia.org/wiki/Normalprojektion)). Die isometrischen Ansichten der vier Frontecken können ebenfalls enthalten sein.

Soll nur eine einzige Ansicht erzeugt werden, bringt die Verwendung von Ansichtengruppe keinen Vorteil; stattdessen sollte man [Ansicht](TechDraw_View/de.md) verwenden. Wenn man nicht die herkömmliche europäische Projektion: Erster Winkel (engl. [first-angle projection](https://en.wikipedia.org/wiki/Multiview_orthographic_projection#First-angle_projection)) bzw. amerikanische Projektion: Dritter Winkel (engl. [third-angle projection](https://en.wikipedia.org/wiki/Multiview_orthographic_projection#Third-angle_projection)) verwenden möchte, sollte man mehrmals [Ansicht](TechDraw_View/de.md) anstelle von *Ansichtengruppe* verwenden.

<img alt="" src=images/TechDraw_ProjGroup_example.png  style="width:400px;"> 
*Drei orthogonale Ansichten und eine isometrische Ansicht eines Festkörperobjekts*



## Anwendung

1.  Wahlweise die [3D-Ansicht](3D_view/de.md) zurechtdrehen. Die Blickrichtung der Kamera in der [3D-Ansicht](3D_view/de.md) legt den Anfangswert der **Hauptrichtung** der Ansichtengruppe (die {{PropertyData/de|Direction}} der zentralen Ansicht).
2.  Ein oder mehrere Objekte in der [3D-Ansicht](3D_view/de.md) oder [Baumansicht](Tree_view/de.md) auswählen.
3.  Wenn das Dokument mehrere Zeichnungsblätter enthält, kann das gewünschte Blatt wahlweise zur Auswahl hinzugefügt werden, indem es in der [Baumansicht](Tree_view/de.md) auswählt wird. Dies ist ein Muss für {{VersionMinus/de|0.19}}.
4.  Es gibt mehrere Möglichkeiten das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_ProjectionGroup.svg" width=16px> [Ansichtengruppe einfügen](TechDraw_ProjectionGroup/de.md)** drücken.
    -   Den Menüeintrag **TechDraw → <img src="images/TechDraw_ProjectionGroup.svg" width=16px> Ansichtengruppe einfügen** auswählen.
5.  Wenn das Dokument mehrere Zeichnungsblätter enthält und noch kein Blatt ausgewählt wurde, öffnet sich der **Seitenauswahl**-Dialog {{Version/de|0.20}}:
    1.  Die gewünscht Seite auswählen.
    2.  Die Schaltfläche **OK** drücken.
6.  Der Aufgabenbereich **Ansichtengruppe** wird geöffnet.
7.  Die Ansichten, die zur Ansichtengruppe hinzugefügt werden sollen sowie den Maßstab der Ansichtengruppe und andere Parameter auswählen.
8.  Die Schaltfläche **OK** drücken.
9.  Wahlweise kann die Ansichtengruppe, durch Ziehen der zentralen Ansicht, bewegt werden.
10. Wahlweise können die anderen Ansichten der Ansichtengruppe relativ zu der zentralen Ansicht bewegt werden, indem man sie jeweils einzeln zieht.

![](images/TaskProjGroup.png ) 
*[Aufgabenbereich](Task_panel/de.md) Ansichtengruppe. Das Feld ''Anpassen der Hauptrichtung'' zeigt die aktuelle Blickrichtung an.*



## Eigenschaften



### Daten


{{TitleProperty|Basis}}

-    **Source|LinkList**: Links to the drawable objects to be depicted.

-    **XSource|XLinkList**: Links to the drawable objects in an external file. <small>(v0.19)</small> 

-    **Anchor|Link**: The central view in the group. Normally the Front view.

-    **ProjectionType|Enumeration**: {{Value|First Angle}} or {{Value|Third Angle}}.

For the other properties in this group see [TechDraw View](TechDraw_View#Properties.md).


{{TitleProperty|Collection}}

-    **Views|LinkList**: Links to the views in this ProjectionGroup.


{{TitleProperty|Distribute}}

-    **Auto Distribute|Bool**: If `True`, space out individual views automatically. Use `False` to position manually.

-    **spacing X|Length**: Horizontal space between views when automatically positioned. Note that Scale and the size of other views in the group also influence the spacing.

-    **spacing Y|Length**: Vertical space between views when automatically positioned.

### View


{{TitleProperty|Basis}}

Siehe [TechDraw Ansicht](TechDraw_View/de#Eigenschaften.md)



## Hinweise

Die Ansichtengruppe als Ganzes erbt X, Y, Scale Type, Scale und Rotation aus der Basisansicht.

Einzelne Ansichten innerhalb der Gruppe erben alle Eigenschaften der Part-Ansicht, aber das Proj(ektion)Group-Objekt steuert den Maßstab aller seiner Elementansichten.

Die Eigenschaft RotationVector einzelner Ansichten innerhalb der Gruppe ist veraltet seit v0.19. Stattdessen wird XDirection verwendet.

Beachte, dass der mittlere Kasten die aktuelle Projektionsrichtung der primären Ansicht anzeigt. Sie kann nicht dazu benutzt werden, die Richtung zu ändern.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug Ansichtengruppe kann in [Makros](Macros/de.md) und von der [Python](Python/de.md) Konsole aus verwendet werden. Ein vollständiges Skript ist im Installationspaket im Verzeichnis \"source-dir/src/Mod/TechDraw/TDTest/DProjGroupTest.py\" enthalten.


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

Programmierhinweis: Die Ansichtengruppe sollte immer zum Zeichnungsblatt hinzugefügt werden (z.B. page.addView(group), bevor Ansichten zur Gruppe hinzugefügt werden. Dies ermöglicht es der Ansichtengruppe, von der übergeordneten Seite übernommene Parameterwerte als Vorgaben zu verwenden.





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ProjectionGroup/de
