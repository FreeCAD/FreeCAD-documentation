---
- GuiCommand:
   Name:TechDraw LandmarkDimension
   Name/de:TechDraw MaßÜberOrientierungspunkte
   MenuLocation:TechDraw - Bemaßungen - Maß zwischen Orientierungspunkten einfügen - EXPERIMENTELL
   Workbenches:[TechDraw](TechDraw_Workbench/de.md)
   Version:0.19
   SeeAlso:[TechDraw MaßHorizontal](TechDraw_HorizontalDimension/de.md), [TechDraw MaßVertikal](TechDraw_VerticalDimension/de.md)
---

# TechDraw LandmarkDimension/de



## Beschreibung

Das Werkzeug **TechDraw MaßÜberOrientierungspunkte** fügt einer Ansicht ein lineares Maß hinzu. Das Maß basiert auf zwei Punkt-**Elementen** (Draft.Point oder Part.Vertex) aus dem 3D-Modell. Man beachte, daß es sich bei den Punkten um **Formelement**-Objekte handeln muß, die in der [Baumansicht](Tree_view/de.md) des Modells erscheinen. Beliebige Knoten einer Form funktionieren nicht.

Der Zweck dieses Werkzeugs ist es, eine Abhilfe gegen die Beschädigung der Maße zu schaffen, die im Zusammenhang mit dem \"[Problem der topologischen Benennung](Topological_naming_problem/de.md)\" entsteht. Die Quellpunkte sollten [Ausdrücke](Expressions/de.md) verwenden oder andere Mechanismen enthalten, um ihre Position festzulegen. Da es sich bei den Punkten um [Dokumentobjekte](App_DocumentObject/de.md) und nicht um Formkomponenten handelt, ändert sich ihr Name bei Neuberechnungen nicht, so dass sie leicht gefunden werden können.

Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de#Begrenzungen.md) für Weiteres über Maße und topologische Benennung.

Das Maß zwischen Orientierungspunkten verhält sich im Allgemeinen wie jedes andere Maß.



## Anwendung

1.  2 Punktobjekte in der [Baumansicht](Tree_view/de.md) oder der [3D-Ansicht](3D_view/de.md) auswählen.
2.  Auch die Ansicht auswählen, zu der das Maß hinzugefügt werden soll.
3.  Die Schaltfläche **<img src="images/TechDraw_LandmarkDimension.svg" width=20px> [Maß zwischen Orientierungspunkten einfügen - EXPERIMENTELL](TechDraw_LandmarkDimension/de.md)
** drücken oder den Menüeintrag **TechDraw → Maßeinträge → Maß zwischen Orientierungspunkten einfügen - EXPERIMENTELL**
4.  Der Ansicht wird ein Maß hinzugefügt. Der Maßeintrag kann an die gewünschte Position gezogen werden.



## Begrenzungen

Das Werkzeug MaßÜberOrientierungspunkte ist zunächst auf Maße für \"Abstände\" beschränkt. Andere Typen könnten hinzugefügt werden, wenn die Nachfrage dies rechtfertigt.



## Eigenschaften

Das Werkzeug MaßÜberOrientierungspunkte führt keine neuen Eigenschaften ein.



## Skripten

Siehe auch: [Autogenerierte API Dokumentation](https://freecad.github.io/SourceDoc/) und [FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug MaßÜberOrientierungspunkte kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden:


```python
dim1 = FreeCAD.ActiveDocument.addObject('TechDraw::LandmarkDimension','Landmark')
dim1.Type = "Distance"
dim1.References2D=[(TDView, 'Vertex1')]
dim1.References3D=[(Point3d1, 'Vertex1')]
dim1.References3D=[(Point3d2, 'Vertex1')]
rc = page.addView(dim1)
```





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LandmarkDimension/de
