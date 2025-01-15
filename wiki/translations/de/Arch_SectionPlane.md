---
 GuiCommand:
   Name: Arch SectionPlane
   Name/de: Arch Schnittebene
   MenuLocation: Anmerkung , Schnittebene
   Workbenches: BIM_Workbench/de
   Shortcut: **S** **P**
   SeeAlso: Draft_Shape2DView/de
---

# Arch SectionPlane/de



## Beschreibung

Das Werkzeug **Arch Schnittebene** platziert im aktuellen Dokument eine Schnittebene \"Ding\", die eine Schnitt- oder Ansichtsebene definiert. Das \"Ding\" wird entsprechend der aktuellen [Entwurf Arbeitsebene](Draft_SelectPlane/de.md) positioniert und kann durch Verschieben und Drehen verschoben und neu ausgerichtet werden, bis es die 2D-Ansicht beschreibt, die du erhalten möchtest. Das Objekt Schnittebene berücksichtigt nur einen bestimmten Satz von Objekten. Objekte, die beim Erstellen einer Schnittebene ausgewählt werden, werden automatisch zu diesem Satz hinzugefügt. Andere Objekte können später mit den Werkzeugen [Arch Komponente hinzufügen](Arch_Add/de.md) und [Arch Komponente entfernen](Arch_Remove/de.md) hinzugefügt oder daraus entfernt werden oder durch Doppelklicken auf die Schnittebene in der Baumansicht.

Die Schnittebene allein wird keine Ansicht der gesetzten Objekte erzeugen. Dazu musst du eine [TechDraw ArchAnsicht](TechDraw_ArchView/de.md) erzeugen, um eine Ansicht auf einer [TechDraw StandardSeite](TechDraw_Workbench/de.md) zu erzeugen.

<img alt="" src=images/Arch_SectionPlane_example.jpg  style="width:600px;">



## Anwendung

1.  Wahlweise die [Draft-Arbeitsebene](Draft_SelectPlane/de.md) so ausrichten, dass sie die Ebene widerspiegelt, auf der die Schnittebene platziert werden soll.
2.  Die Objekte auswählen, die in der Schnittansicht enthalten sein sollen.
3.  Die Schaltfläche **<img src="images/Arch_SectionPlane.svg" width=16px> [Schnittebene](Arch_SectionPlane.md)** drücken oder Tastaturkürzel **S** dann **P**.
4.  Die Schnittebene in die richtige Position [verschieben](Draft_Move/de.md) und [drehen](Draft_Rotate/de.md), falls erforderlich.
5.  Die Schnittebene auswählen, falls sie nicht bereits ausgewählt ist.
6.  Entweder [Draft Form2DAnsicht](Draft_Shape2DView/de.md) oder [TechDraw ArchAnsicht](TechDraw_ArchView/de.md) verwenden, um eine Ansicht zu erstellen.



## Optionen

-   Das Schnittebenenobjekt berücksichtigt nur eine bestimmte Menge von Objekten, nicht alle Objekte des Dokuments. Objekte können einem Schnittebenenobjekt mit den Werkzeugen [Arch Hinzufügen](Arch_Add/de.md) und [Arch Entfernen](Arch_Remove/de.md) hinzugefügt oder entfernt werden oder durch Doppelklicken auf die Schnittebene in der Baumansicht, Auswählen von Objekten entweder in der Liste oder in der 3D-Szene und Drücken der Schaltflächen **hinzufügen** oder **entfernen**.

-   Wenn ein Schnittebenenobjekt ausgewählt ist, verwende das Werkzeug [Draft Form2DAnsicht](Draft_Shape2DView/de.md), um ein Formobjekt zu erstellen, das die Schnittansicht im Dokument darstellt.

<img alt="" src=images/Arch_Section_example2.jpg  style="width:600px;">

-   Eine [TechDraw Arch-Ansicht](TechDraw_ArchView/de.md) erstellen.

<img alt="" src=images/Arch_Section_example3.jpg  style="width:600px;">

-   Die Schnittebene kann auch verwendet werden, um die gesamte 3D Ansicht zu zeigen, die von einer unendlichen Ebene geschnitten wird. Dies ist nur visuell und hat keinen Einfluss auf die Geometrie der geschnittenen Objekte.

<img alt="" src=images/Arch_SectionPlane_CutView.jpg  style="width:600px;">



## Eigenschaften

-    {{PropertyData/de|Nur Festkörper}}: Wenn dies True ist, werden nicht-feste Objekte in der Einstellung nicht berücksichtigt.

-    {{PropertyView/de|Anzeige Länge}}: Die Länge des Schnittebenen-Gizmos in der 3D-Ansicht. Hat keinen Einfluss auf die resultierende Ansicht

-    {{PropertyView/de|Anzeige Höhe}}: Die Höhe des Schnittebenen-Gizmos in der 3D-Ansicht. Hat keinen Einfluss auf die resultierende Ansicht

-    {{PropertyView/de|Pfeilgröße}}: Die Größe der Pfeile des Schnittebenen-Gizmos in der 3D-Ansicht. Hat keinen Einfluss auf die resultierende Ansicht

-    {{PropertyView/de|Schnittansicht}}: Wenn dies `True` ist, wird die gesamte 3D-Ansicht an der Stelle dieser Schnittebene geschnitten.

-    {{PropertyView/de|Clipansicht}}: Wenn dies `True` ist, wird die Ansicht auf die Anzeigehöhe und -länge der Schnittebene zugeschnitten. Dadurch wird die Schnittebene effektiv zu einer orthografischen Kamera, wodurch das Sichtfeld begrenzt wird.

<img alt="" src=images/Arch_SectionPlane_ClipView.png  style="width:600px;">



*Die Arch Schnittebene mit der Option Clip Ansicht verhält sich wie eine Kamera und begrenzt das Sichtfeld.*



## Kleine Verbesserungen 

-   Das manuelle Hinzufügen einer Eigenschaft namens **RotateSolidRender** des Typs **App::PropertyAngle** zu den Schnittebene **Ansicht**-Eigenschaften (rechtsklicke in die Ansicht-Eigenschaften → Alle anzeigen, rechtsklicke erneut → Eigenschaft hinzufügen) erlaubt es, das Render-Objekt zu drehen, wenn der Festkörper-Modus benutzt wird. Dies ist sinnvoll, wenn eine gerenderte Ansicht bspw. sowohl Arch- als auch Draft-Elemente enthält und die Arch-Elemente im Verhältnis zu den Draft-Elementen gedreht sind.



## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug SchnittEbene kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden:


```python
Section = makeSectionPlane(objectslist=None, name="Section")
```

-   Erzeugt ein `Schnitt` Objekt aus `Objektliste`, die eine Liste von Objekten ist.

Beispiel:


```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
Structure = Arch.makeStructure(length=1000, width=1000, height=200)
FreeCAD.ActiveDocument.recompute()

BuildingPart = Arch.makeBuildingPart([Wall1, Wall2])

Floor = Arch.makeFloor([BuildingPart])
Building = Arch.makeBuilding([Floor, Structure])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()

Section1 = Arch.makeSectionPlane([Wall1, Wall2])
Section2 = Arch.makeSectionPlane([Structure])
Section3 = Arch.makeSectionPlane([Site])
FreeCAD.ActiveDocument.recompute()
```



---
⏵ [documentation index](../README.md) > Arch SectionPlane/de
