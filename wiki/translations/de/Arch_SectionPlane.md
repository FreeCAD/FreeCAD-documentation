---
- GuiCommand:
   Name: Arch SectionPlane
   Name/de: Arch SchnittEbene
   MenuLocation: Arch -> Schnittebene
   Workbenches: Arch_Workbench/de
   Shortcut: **S** **P**
   SeeAlso: Draft_Shape2DView/de, TechDraw_ArchView/de
---

# Arch SectionPlane/de



## Beschreibung

Dieses Werkzeug platziert im aktuellen Dokument eine Schnittebene \"Ding\", die eine Schnitt- oder Ansichtsebene definiert. Das \"Ding\" wird entsprechend der aktuellen [Entwurf Arbeitsebene](Draft_SelectPlane/de.md) platziert und kann durch Verschieben und Drehen verschoben und neu ausgerichtet werden, bis es die 2D Ansicht beschreibt, die du erhalten möchtest. Das Objekt Schnittebene berücksichtigt nur einen bestimmten Satz von Objekten. Objekte, die beim Erstellen einer Schnittebene ausgewählt werden, werden automatisch zu diesem Satz hinzugefügt. Andere Objekte können später mit den [Arch Komponente hinzufügen](Arch_Add/de.md) und [Arch Komponente entfernen](Arch_Remove/de.md) Werkzeugen hinzugefügt oder daraus entfernt werden oder durch Doppelklicken auf die Schnittebene in der Baumansicht.

Die Schnittebene allein wird keine Ansicht der gesetzten Objekte erzeugen. Dazu musst du eine [TechDraw ArchAnsicht](TechDraw_ArchView/de.md) erzeugen, um eine Ansicht auf einer [TechDraw StandardSeite](TechDraw_Workbench/de.md) zu erzeugen.

<img alt="" src=images/Arch_SectionPlane_example.jpg  style="width:600px;">



## Anwendung


<div class="mw-translate-fuzzy">

1.  Setze wahlweise die [Entwurfsarbeitsebene](Draft_SelectPlane/de.md) so, dass sie die Ebene widerspiegelt, auf der du die Schnittebene platzieren möchtest.
2.  Wähle die Objekte aus, die in deiner Schnittansicht enthalten sein sollen.
3.  Drücke die **<img src="images/Arch_SectionPlane.svg" width=16px> [Schnittebene](Arch_SectionPlane.md)** Taste oder drücke **S** dann **P** Tasten.
4.  [Bewegen](Draft_Move/de.md)/[drehen](Draft_Rotate/de.md) der Schnittebene in die richtige Position, falls erforderlich.
5.  Wähle die Schnittebene aus, falls sie nicht bereits ausgewählt ist.
6.  Verwende entweder [Zeichnung EntwurfsAnsicht](Draft_Drawing/de.md), [Entwurf Form2DAnsicht](Draft_Shape2DView/de.md) oder [TechDraw ArchAnsicht](TechDraw_ArchView/de.md), um eine Ansicht zu erstellen.


</div>



## Optionen


<div class="mw-translate-fuzzy">

-   Das Schnittebenenobjekt berücksichtigt nur einen bestimmten Satz von Objekten, nicht alle Objekte des Dokuments. Objekte können einem Schnittebenenobjekt mit den [Arch Hinzufügen](Arch_Add/de.md) und [Arch Entfernen](Arch_Remove/de.md) Werkzeugen hinzugefügt oder entfernt werden, oder durch Doppelklicken auf die Schnittebene in der Baumansicht, Auswählen von Objekten entweder in der Liste oder in der 3D Szene und Drücken der Schaltflächen **hinzufügen\'\' oder**entfernen\'\'\'.


</div>

-   Wenn ein Schnittebenenobjekt ausgewählt ist, verwende das Werkzeug [Draft Form2DAnsicht](Draft_Shape2DView/de.md), um ein Formobjekt zu erstellen, das die Schnittansicht im Dokument darstellt.

<img alt="" src=images/Arch_Section_example2.jpg  style="width:600px;">

-   Eine [TechDraw Arch-Ansicht](TechDraw_ArchView/de.md) erstellen.

<img alt="" src=images/Arch_Section_example3.jpg  style="width:600px;">

-   Die Schnittebene kann auch verwendet werden, um die gesamte 3D Ansicht zu zeigen, die von einer unendlichen Ebene geschnitten wird. Dies ist nur visuell und hat keinen Einfluss auf die Geometrie der geschnittenen Objekte.

<img alt="" src=images/Arch_SectionPlane_CutView.jpg  style="width:600px;">



## Eigenschaften


<div class="mw-translate-fuzzy">

-    **Nur Festkörper**: Wenn dies True ist, werden nicht-feste Objekte in der Einstellung nicht berücksichtigt.

-    **Anzeige Länge**: Die Länge des Schnittebenen Gizmos in der 3D Ansicht. Hat keinen Einfluss auf die resultierende Ansicht

-    **Anzeige Höhe**: Die Höhe des Schnittebenen Gizmos in der 3D Ansicht. Hat keinen Einfluss auf die resultierende Ansicht

-    **Pfeilgröße**: Die Größe der Pfeile des Schnittebenen Gizmos in der 3D Ansicht. Hat keinen Einfluss auf die resultierende Ansicht

-    **Schnittansicht**: Wenn dies `True` ist, wird die gesamte 3D Ansicht an der Stelle dieser Schnittebene geschnitten.

-    **Clipansicht**: Wenn dies `True` ist, wird die Ansicht auf die Anzeigehöhe und -länge der Schnittebene zugeschnitten. Dadurch wird die Schnittebene effektiv zu einer orthografischen Kamera, wodurch das Sichtfeld begrenzt wird. <small>(v0.19)</small> 


</div>

<img alt="" src=images/Arch_SectionPlane_ClipView.png  style="width:600px;">



*Die Arch Schnittebene mit der Option Clip Ansicht verhält sich wie eine Kamera und begrenzt das Sichtfeld.*



## Kleine Verbesserungen 


<div class="mw-translate-fuzzy">

-   Das manuelle Hinzufügen einer Eigenschaft namens **RotateSolidRender** des Typs **App::PropertyAngle** zu den Schnittebene **Ansicht**-Eigenschaften (rechtsklicke in die Ansicht-Eigenschaften → Alle anzeigen, rechtsklicke erneut → Eigenschaft hinzufügen) erlaubt es, das Render-Objekt zu drehen, wenn der Volumenkörper-Modus benutzt wird. Dies ist sinnvoll, wenn eine gerenderte Ansicht bspw. sowohl Arch- als auch Draft-Element enthält und die Arch-Elemente im Verhältnis zu den Draft-Elementen gedreht sind. {{version/de|0.19}}


</div>

## Scripting


<div class="mw-translate-fuzzy">

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).


</div>


<div class="mw-translate-fuzzy">

Das SchnittEbene Werkzeug kann in [Makros](macros/de.md) und aus der [Python](Python/de.md) Konsole verwendet werden, in dem die folgende Funktion verwendet wird:


</div>


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
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch SectionPlane/de
