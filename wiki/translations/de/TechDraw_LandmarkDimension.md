---
 GuiCommand:
   Name: TechDraw LandmarkDimension
   Name/de: TechDraw MaßÜberOrientierungspunkte
   MenuLocation: TechDraw , Bemaßungen , Maß zwischen Orientierungspunkten einfügen - EXPERIMENTELL
   Workbenches: TechDraw_Workbench/de
   Version: 0.19
   SeeAlso: TechDraw_HorizontalDimension/de, TechDraw_VerticalDimension/de
---

# TechDraw LandmarkDimension/de



## Beschreibung

Das Werkzeug **TechDraw MaßÜberOrientierungspunkte** fügt einer Ansicht ein lineares Maß hinzu. Das Maß basiert auf zwei Punkten (Point-Objekte wie [Draft Punkt](Draft_Point/de.md), [Part Punkt](Part_Point/de.md) oder [PartDesign Punkt](PartDesign_Point/de.md)) aus dem 3D-Modell.

Der Zweck dieses Werkzeugs ist es, eine Abhilfe gegen die Beschädigung der Maße zu schaffen, die im Zusammenhang mit dem \"[Problem der topologischen Benennung](Topological_naming_problem/de.md)\" entsteht. Die Quellpunkte sollten [Ausdrücke](Expressions/de.md) verwenden oder andere Mechanismen enthalten, um ihre Position festzulegen. Da es sich bei den Punkten um [Dokumentobjekte](App_DocumentObject/de.md) und nicht um Formkomponenten handelt, ändert sich ihr Name bei Neuberechnungen nicht, so dass sie leicht gefunden werden können.

Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de#Begrenzungen.md) für Weiteres über Maße und topologische Benennung.



## Anwendung

1.  Zwei Punktobjekte in der [Baumansicht](Tree_view/de.md) oder der [3D-Ansicht](3D_view/de.md) auswählen.
2.  Die korrekte TechDraw-Ansicht zur Auswahl hinzufügen, indem sie in der [Baumansicht](Tree_view/de.md) ausgewählt wird.
3.  Es gibt mehrere Möglichkeiten, das Werkzeug aufzurufen:
    -   Die Schaltfläche **<img src="images/TechDraw_LandmarkDimension.svg" width=16px> [Maß zwischen Orientierungspunkten hinzufügen - EXPERIMENTELL](TechDraw_LandmarkDimension.md)** drücken.
    -   Den Menüeintrag **TechDraw → Maßeinträge  → <img src="images/TechDraw_LandmarkDimension.svg" width=16px> Maß zwischen Orientierungspunkten hinzufügen - EXPERIMENTELL** auswählen.
4.  Ein Maß wird zur Ansicht hinzugefügt.
5.  Das Maß kann an die gewünschte Position gezogen werden.
6.  Falls erforderlich, können Toleranzen, wie auf der [GD&T-Seite](TechDraw_Geometric_dimensioning_and_tolerancing/de#Toleranzen.md) beschrieben, hinzugefügt werden.



### Eigenschaften anpassen 

Um die Eigenschaften eines Maßes (Dimension-Objekt) zu ändern, wird es in der Zeichnung oder in der [Baumansicht](Tree_view/de.md) doppelt angeklickt. Dadurch wird der Dialog [Maßeintrag](TechDraw_LengthDimension/de#Dialog_Maßeintrag.md) geöffnet.



## Begrenzungen

Das Werkzeug MaßÜberOrientierungspunkte ist zunächst auf Maße für \"Abstände\" beschränkt. Andere Typen könnten hinzugefügt werden, wenn die Nachfrage dies rechtfertigt.



## Hinweise

Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de#Hinweise.md).



## Eigenschaften

Siehe [TechDraw Längenmaß](TechDraw_LengthDimension/de#Eigenschaften.md).



## Skripten

Siehe auch: [Autogenerierte API-Dokumentation](https://freecad.github.io/SourceDoc/) und [Grundlagen der Skripterstellung in FreeCAD](FreeCAD_Scripting_Basics/de.md).

Das Werkzeug MaßÜberOrientierungspunkte kann in [Makros](Macros/de.md) und von der [Python](Python/de.md)-Konsole aus mit den folgenden Funktionen verwendet werden:


```python
dim1 = FreeCAD.ActiveDocument.addObject("TechDraw::LandmarkDimension", "Landmark")
dim1.Type = "Distance"
dim1.References2D = [(TDView, "Vertex1")]
dim1.References3D = [(Point3d1, "Vertex1")]
dim1.References3D = [(Point3d2, "Vertex1")]
page.addView(dim1)
```





{{TechDraw Tools navi

}}



---
⏵ [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw LandmarkDimension/de
