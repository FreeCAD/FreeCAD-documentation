# PartDesign Feature/de
## Einleitung

Ein [PartDesign Formelement](PartDesign_Feature/de.md) verweist auf einen \"Schritt\" im Modellierungsprozess, der innerhalb eines [PartDesign Body](PartDesign_Body.md) stattfindet. Zum Beispiel jedes Mal, wenn du einen Festkörperquader mit [PartDesign Quader hinzufügen](PartDesign_AdditiveBox/de.md), fügst Du ein Formelement hinzu; wenn Du eine Fase zu einer Kante mit [PartDesign Fase](PartDesign_Chamfer/de.md) hinzufügst, fügst Du ein weiteres Formelement hinzu; wenn Du ein Loch mit [Skizze](Sketch/de.md) und [PartDesign Tasche](PartDesign_Pocket/de.md) schneidest, fügst Du ein weiteres Formelement hinzu.

<img alt="" src=images/PartDesign_Feature_example.png  style="width:600px;"> 
*Featurebearbeitung ein einem  [PartDesign Body](PartDesign_Body.md) mit drei aufeinanderfolgenden Features*

Es gibt viele Arten von Formelementen, die einem ursprünglichen Körper Volumen hinzufügen oder entfernen können. Das Wort \"Formelement\" bezieht sich auf die Bearbeitung selbst und auch auf den resultierenden Festkörper nach dieser Bearbeitung.

Um mehr über die Erstellung von Festkörperobjekten mit dem [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) zu erfahren, siehe [Formelementbearbeitung](feature_editing/de.md).

## Anwendung

Fast alle Werkzeuge im [PartDesign Arbeitsbereich](PartDesign_Workbench/de.md) sind dazu gedacht, einem [PartDesign Körper](PartDesign_Body/de.md) Formelemente hinzuzufügen. Diese Werkzeuge können über die Menü- und Werkzeugleisten-Schaltflächen aufgerufen werden, während ein Objekt oder Unterelement (Knoten, Kante, Fläche) ausgewählt ist.

Die Formelemente können in verschiedene Kategorien eingeteilt werden:

-   Formelement Basis: bezieht sich auf das Basis Formelementobjekt, das in einem [PartDesign Körper](PartDesign_Body/de.md) erstellt werden kann.
-   Additiv und subtraktiv
    -   Grundformen: [Quader](PartDesign_AdditiveBox/de.md), [Kegel](PartDesign_AdditiveCone/de.md), [Zylinder](PartDesign_AdditiveCylinder/de.md), [Ellipsoid](PartDesign_AdditiveEllipsoid/de.md), [Prisma](PartDesign_AdditivePrism/de.md), [Sphere](PartDesign_AdditiveSphere/de.md), [Torus](PartDesign_AdditiveTorus/de.md) und [Keil](PartDesign_AdditiveWedge/de.md).
    -   Grundformen subtraktiv:

[Subtraktionsbox](PartDesign_SubtractiveBox/de.md), [Subtraktionskegel](PartDesign_SubtractiveCone/de.md), [Subtraktionszylinder](PartDesign_SubtractiveCylinder/de.md), [Subtraktionsellipsoid](PartDesign_SubtractiveEllipsoid/de.md), [Subtraktives Prisma](PartDesign_SubtractivePrism/de.md), [Subtraktive Kugel](PartDesign_SubtractiveSphere/de.md), [Subtraktiver Torus](PartDesign_SubtractiveTorus/de.md) und [Subtraktiver Keil](PartDesign_SubtractiveWedge/de.md).

-   -   Profilbasiert: [Polster](PartDesign_Pad/de.md), [Drehung](PartDesign_Revolution/de.md), [Ausformung](PartDesign_AdditiveLoft/de.md), [Rohr](PartDesign_AdditivePipe/de.md).
    -   Profilbasierte Subtraktion: [Tasche](PartDesign_Pocket/de.md), [Bohrung](PartDesign_Hole/de.md), [Nut](PartDesign_Groove/de.md), [Subtraktion Ausformung](PartDesign_SubtractiveLoft/de.md), [Subtraktion Rohr](PartDesign_SubtractivePipe/de.md).

## Vererbung

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten im Programm. Die `PartDesign::Formelement* Objekte werden zum Aufbau parametrischer 3D Körper verwendet und sind somit vom Basisobjekt {{incode|Part::Formelement` abgeleitet.}}

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten ](FreeCAD_Scripting_Basics/de.md), und [geskriptete Objekte](scripted_objects/de.md).

Siehe [Part Formelemente](Part_Feature/de.md) für allgemeine Informationen über das Hinzufügen von Objekten aus der [Python Konsole](Python_console/de.md).

Siehe [PartDesign Körper](PartDesign_Body/de.md) für die allgemeinen Informationen zum Hinzufügen eines Körpers. Sobald ein Körper existiert, können Formelemente mit der Methode `addObject()` des Körpers angehängt werden.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject('PartDesign::Body', 'Body')
obj.Label = "Custom label"

feature = App.ActiveDocument.addObject('PartDesign::AdditiveBox', 'Box')
feature.Width = 200
feature.Length = 300
feature.Height = 500
obj.addObject(feature)
App.ActiveDocument.recompute()

feature2 = App.ActiveDocument.addObject('PartDesign::SubtractiveBox', 'Box')
feature2.Width = 50
feature2.Length = 200
feature2.Height = 400
obj.addObject(feature2)
App.ActiveDocument.recompute()
```


{{PartDesign Tools navi

}} {{Document objects navi}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Feature/de
