---
- GuiCommand:/de
   Name:Arch BuildingPart
   Name/de:Architektur GebäudeTeil
   MenuLocation:Arch → Gebäudeteil
   Workbenches:[Arch](Arch_Workbench.md)
   Version:0.18
   SeeAlso:[Arch Gebäude](Arch_Building/de.md), [Arch Baugrund](Arch_Site/de.md)
---

# Arch BuildingPart/de

## Beschreibung

Der GebäudeTeil ersetzt das alte [Arch Geschoss](Arch_Floor/de.md) und [Arch Gebäude](Arch_Building/de.md) Werkzeug durch eine leistungsfähigere Version, mit der nicht nur Geschosse/Etagen/Ebenen, sondern auch alle Arten von Situationen erstellt werden können, in denen verschiedene Architektur/BIM Objekte gruppiert werden sollen und das diese Gruppe als ein Objekt behandelt oder nachgebildet werden soll.

## Anwendung

1.  Wähle wahlweise ein oder mehrere Objekte, die in dein neues Gebäude Teil eingeschlossen werden sollen.
2.  Drücke die **<img src="images/Arch_BuildingPart.svg" width=16px> [Arch GebäudeTeil](Arch_BuildingPart/de.md)** Schaltfläche.

### Hinweise

GebäudeTeile haben eine eingebaute, implizite [Arch SchnittEbene](Arch_SectionPlane/de.md). <small>(v0.19)</small> 

Diese Ebene ist immer parallel zur GebäudeTeil Basisebene, aber du kannst den Versatz zwischen ihnen angeben. Daher arbeiten alle Werkzeuge, die mit einer Schnittebene arbeiten, wie z.B. [Entwurf Form2DAnsicht](Draft_Shape2DView/de.md) und [TechDraw ArchAnsicht](TechDraw_ArchView/de.md) auch mit GebäudeTeilen.

## Optionen

-   Nach der Erstellung eines GebäudeTeil kannst du weitere Objekte durch Ziehen und Ablegen in der Baumansicht oder mit dem **<img src="images/Arch_Add.svg" width=16px> [Arch Hinzufügen](Arch_Add/de.md)** Werkzeug verwenden.
-   Du kannst Objekte, durch Ziehen und Ablegen aus der Baumansicht heraus oder durch verwenden des **_ [Arch Entfernen](Arch_Remove.md)** Werkzeugs aus einem GebäudeTeil entfernen.
-   Durch doppelklicken auf das GebäudeTeil Objekt in der Baumansicht wird die [Working Plane](Draft_SelectPlane.md) auf dessen Stelle gesetzt, und das BuildingPart wird aktiv, was bedeutet daß neue Objekte automatisch dazu hinzugefügt werden.

Erneutes Doppelklicken auf das GebäudeTeil deaktiviert es und setzt die Arbeitsebene wieder auf die vorherige Position zurück (in Version 0.19, damit diese Option verfügbar ist, muss sie als true gesetzt werden, im Paneel Ansichtseigenschaften - Interaktion - Doppelklick aktiviert es).

-   Das GebäudeTeil kann in der 3D Ansicht eine Markierung mit einer Beschriftung und einer Niveauanzeige anzeigen.
-   Wenn ein GebäudeTeil verschoben/gedreht wird, werden alle seine Kinder, die entweder keine **Bewegen mit dem Bereitsteller** Eigenschaft haben oder diese aktiviert haben, gemeinsam verschoben/gedreht.
-   Gebäudeteile können [Entwurf Klone](Draft_Clone/de.md) sein.
-   Gebäudeteile können jeden IFC Typ annehmen. Ihre Eigenschaft **IFC Typ** bestimmt ihre Verwendung. Wenn du es auf **Gebäude Geschoss** setzt, verhält es sich wie ein Stockwerk. Wenn du es auf **Gebäude** setzt, verhält es sich wie ein Gebäude, und wenn du es auf **Element Baugruppe** setzt, verhält es sich wie eine Baugruppe. Das Symbol ändert sich entsprechend dieser Einstellung, aber ansonsten hat es keine weiteren Auswirkungen in FreeCAD. Der Export in IFC als der eine oder andere Typ kann jedoch Auswirkungen auf andere BIM Anwendungen haben.

## Eigenschaften

### Daten

-    {{PropertyData/de|Höhe}}: Die Höhe dieses Objekts und dessen Kinderobjekte. Die Kinderobjekte können z.B. [Arch Wände](Arch_Wall/de.md) sein. Jede Wandhöhe muss auf `0` (Null) gesetzt werden, so dass die Höheneigenschaft des GebäudeTeil Objekts auf die darin liegenden Objekte übertragen wird.

-    {{PropertyData/de|LevelOffset}}: Das Niveau des (0,0,0)-Punkts dieser Ebene

-    {{PropertyData/de|Area}}: Die berechnete Geschossfläche dieser Etage

-    {{PropertyData/de|IfcRole}}: Die Rolle dieses Objekts

-    {{PropertyData/de|Description}}: Eine optionale Beschreibung dieser Komponente

-    {{PropertyData/de|Tag}}: Eine optionale Kennzeichnung dieser Komponente

-    {{PropertyData/de|IfcAttributes}}: Benutzerdefinierte IFC-Eigenschaften und -Attribute

### Ansicht

-    {{PropertyView/de|LinienBreite}}: Die Linienbreite dieses Objekts

-    {{PropertyView/de|AufhebenEinheit}}: Eine optionale Einheit, um Niveaus auszudrücken

-    {{PropertyView/de|AnzeigeVersatz}}: Eine auf die Niveaumarkierung anzuwendende Transformation

-    {{PropertyView/de|ZeigeNiveau}}: Falls true, zeige das Niveau

-    {{PropertyView/de|ZeigeEinheit}}: Falls true, zeige die Einheit auf der Niveaumarkierung

-    {{PropertyView/de|SetzeArbeitsEbene}}: Falls true, wird bei Aktivierung die Arbeitsebene automatisch auf dieses Gebäudeteil angepasst

-    {{PropertyView/de|UrsprungVersatz}}: Falls true, wird bei Aktivierung der Ansichtsabstand auch die Ursprungsmarkierung beeinflussen

-    {{PropertyView/de|AnzeigeMarkierung}}: Falls true, wird bei Aktivierung die Objektkennzeichnung angezeigt

-    {{PropertyView/de|SchriftName}}: Die für Text zu benutzende Schriftart

-    {{PropertyView/de|SchriftGröße}}: Die Schriftgröße für Text

-    {{PropertyView/de|WiederherstellenAnsicht}}: Falls gesetzt, wird die in diesem Objekt gespeicherte Sicht bei Doppelklick wiederhergestellt

-    {{PropertyView/de|DiffuseFarbe}}: Die individuelle Flächenfarbe


<small>(v0.19)</small> 

-    **KinderAufhaben**: Wenn gesetzt, werden die folgenden Einstellungen die Kinder dieses Gebäudeteils beeinflussen

-    **KinderLinienBreite**: Die auf die Kinder des Gebäudeteils anzuwendende Linienbreite

-    **KinderLinienFarbe**: Die auf die Kinder des Gebäudeteils anzuwendende Linienfarbe

-    **KinderFormFarbe**: Die auf die Kinder des Gebäudeteils anzuwendende Formfarbe

-    **KinderTransparenz**: Die auf die Kinder des Gebäudeteils anzuwendende Transparenz

## Skripten


**Siehe auch:**

[Arch API](Arch_API/de.md) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Gebäudeteil-Werkzeug kann sowohl in [Makros](macros/de.md) als auch aus der [Python](Python/de.md)-Konsole heraus über folgende Funktion angesprochen werden:


```python
BuildingPart = makeBuildingPart(objectslist=None)
```

-   Erzeugt ein `Building`-Objekt aus `objectslist`, einer Liste von Objekten.

Beispiel: 
```python
import FreeCAD, Draft, Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(2000, 0, 0)
baseline = Draft.makeLine(p1, p2)
baseline2 = Draft.makeLine(p1, -1*p2)

Wall1 = Arch.makeWall(baseline, length=None, width=150, height=2000)
Wall2 = Arch.makeWall(baseline2, length=None, width=150, height=1800)
FreeCAD.ActiveDocument.recompute()

BuildingPart = Arch.makeBuildingPart([Wall1, Wall2])

Floor = Arch.makeFloor([BuildingPart])
Building = Arch.makeBuilding([Floor])
Site = Arch.makeSite(Building)
FreeCAD.ActiveDocument.recompute()
```

---
[documentation index](../README.md) > [Arch](Category_Arch.md) > [Arch](Arch_Workbench.md) > Arch BuildingPart/de
