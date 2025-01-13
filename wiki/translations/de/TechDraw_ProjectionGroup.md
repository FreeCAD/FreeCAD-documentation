---
 GuiCommand:
   Name: TechDraw ProjectionGroup
   Name/de: TechDraw Ansichtengruppe
   MenuLocation: TechDraw, TechDraw Ansichten , Ansichtengruppe einfügen
   Workbenches: TechDraw_Workbench/de
   SeeAlso: TechDraw_View/de
---

# TechDraw ProjectionGroup/de



## Beschreibung

Das Werkzeug **TechDraw Ansichtengruppe** erstellt eine Mehrtafelprojektion eines oder mehrerer 3D-Objekte (Siehe [Normalprojektion](https://de.wikipedia.org/wiki/Normalprojektion)) unter Verwendung entweder der Projektionsmethode 1 (auch europäische Darstellung oder [First Angle Projection](https://en.wikipedia.org/wiki/Multiview_orthographic_projection#First-angle_projection) genannt) oder der Projektionsmethode 3 (auch europäische Darstellung oder [Third Angle Projection](https://en.wikipedia.org/wiki/Multiview_orthographic_projection#Third-angle_projection) genannt). Die isometrischen Ansichten der vier vorderen Ecken können ebenfalls enthalten sein.


{{Version/de|1.0}}

: Das Werkzeug [TechDraw Ansicht](TechDraw_View/de.md) kann auch eine Ansichtengruppe erstellen. Es wird empfohlen, jenes Werkzeug statt dieses zu verwenden.

<img alt="" src=images/TechDraw_ProjGroup_example.png  style="width:400px;"> 
*Drei orthogonale Ansichten und eine isometrische Ansicht eines Festkörperobjekts*



## Anwendung

Siehe [TechDraw Ansicht](TechDraw_View/de#Anwendung_der_Elemente_einer_Ansichtengruppe_und_der_Ansichtengruppe.md), aber zum Aufrufen des Befehles, den Menüeintrag **TechDraw → TechDraw Ansichten → <img src="images/TechDraw_ProjectionGroup.svg" width=16px> Ansichtengruppe einfügen** auswählen.



## Eigenschaften

Siehe auch: [Eigenschafteneditor](Property_editor/de.md).

Eine Ansichtengruppe, oder formal ein {{Incode|TechDraw::DrawProjGroup}}-Objekt, besitzt die gemeinsamen [Eigenschaften](TechDraw_View/de#Eigenschaften_der_Bauteilansicht.md) aller Ansichtsarten. Sie enthält außerdem die folgenden Eigenschaften:



### Daten


{{TitleProperty|Basis}}

-    {{PropertyData/de|Source|LinkList}}: Verweise zu den ableitbaren Objekten, die abgebildet werden sollen.

-    {{PropertyData/de|XSource|XLinkList}}: Verweise zu den ableitbaren Objekten in einer externen Datei.

-    {{PropertyData/de|Anchor|Link}}: Die zentrale Ansicht in der Gruppe; normalerweise die Vorderansicht.

-    {{PropertyData/de|ProjectionType|Enumeration}}: Legt die Projektionsmethode fest,{{Value|First Angle}} = Projektionsmethode 1 (europäisch) oder {{Value|Third Angle}} = Projektionsmethode 2 (amerikanisch).


{{TitleProperty|Collection}}

-    {{PropertyData/de|Views|LinkList}}: Verweise zu den Ansichten in dieser Ansichtengruppe.


{{TitleProperty|Distribute}}

-    {{PropertyData/de|Auto Distribute|Bool}}: Auf `True` gesetzt, werden die einzelnen Ansichten automatisch mit Abstand angeordnet. Auf `False` setzen, um sie manuell anzuordnen.

-    {{PropertyData/de|spacing X|Length}}: Horizontaler Abstand zwischen Ansichten, wenn sie automatisch angeordnet werden. Man beachte, dass auch der Maßstab und die Größe der anderen Ansichten in der Gruppe den Abstand beeinflussen.

-    {{PropertyData/de|spacing Y|Length}}: Vertikaler Abstand zwischen Ansichten, wenn sie automatisch angeordnet werden.



## Hinweise

Die Ansichtengruppe als Ganzes erbt X, Y, Scale Type, Scale und Rotation aus der Basisansicht.

Einzelne Ansichten innerhalb der Gruppe erben alle Eigenschaften der Bauteilansicht, aber das Objekt der Ansichtengruppe (ProjGroup-Objekt) steuert den Maßstab aller seiner enthaltenen Ansichten.

Die Eigenschaft RotationVector einzelner Ansichten innerhalb der Gruppe ist veraltet seit v0.19. Stattdessen wird XDirection verwendet.

Beachte, dass der mittlere Kasten die aktuelle Projektionsrichtung der primären Ansicht anzeigt. Sie kann nicht dazu benutzt werden, die Richtung zu ändern.



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Eine Ansichtengruppe kann mit [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen erstellt werden:


```python
import FreeCAD as App

doc = App.ActiveDocument
cyl = doc.addObject("Part::Cylinder", "Cylinder")
doc.recompute()

page = doc.addObject("TechDraw::DrawPage", "Page")
template = doc.addObject("TechDraw::DrawSVGTemplate", "Template")
template.Template = App.getResourceDir() + "Mod/TechDraw/Templates/A4_LandscapeTD.svg"
page.Template = template

# Toggle the visibility of the page to ensure its width and height are updated (hack):
page.Visibility = False
page.Visibility = True

group = doc.addObject("TechDraw::DrawProjGroup", "ProjGroup")
page.addView(group)
group.Source = [cyl]
group.ProjectionType = "Third Angle"

front_view = group.addProjection("Front") # First projection will become the Anchor.
group.Anchor.Direction = (0, 1, 0)
group.Anchor.RotationVector = (1, 0, 0)

left_view = group.addProjection("Left")
top_view = group.addProjection("Top")

group.X = page.PageWidth / 2
group.Y = page.PageHeight / 2

doc.recompute()
```

Hinweis: Die Ansichtengruppe sollte immer zum Zeichnungsblatt hinzugefügt werden,{{Incode|page.addView(group)}}, bevor Ansichten zur Gruppe hinzugefügt werden. Dies ermöglicht es der Ansichtengruppe, von der übergeordneten Seite übernommene Parameterwerte als Vorgaben zu verwenden.





{{TechDraw_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ProjectionGroup/de
