# App DocumentObjectGroup/de
## Einleitung

<img alt="" src=images/Folder.svg  style="width:32px;">

Das Objekt [App DocumentObjectGroup](App_DocumentObjectGroup.md), formell eine `App::DocumentObjectGroup`, ist ein einfaches Element, das ermöglicht, jede Art [Dokumentobjekt](App_DocumentObject/de.md) in der [Baumansicht](Tree_view/de.md) zu gruppieren, egal welcher Art von Daten.

Es wurde entwickelt, um Objekte in der [Baumansicht](Tree_view/de.md) für den Anwender logisch zu organisieren.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten im Programm. Die Klasse `App::DocumentObjectGroup* hat eine Erweiterung zum Gruppieren jeder Objektart. Die Gruppe selbst besitzt wenige Eigenschaften.`



## Anwendung

1.  Die Schaltfläche **[<img src=images/Std_Group.svg style="width:16px"> [Std Gruppe](Std_Group/de.md)** drücken. Eine leere Gruppe wird erzeugt.
2.  In der [Baumansicht](Tree_view/de.md) ein Objekt auswählen und mit Ziehen & Ablegen auf die Gruppe der Gruppe hinzufügen.
3.  Um Objekte aus der Gruppe zu entfernen, zieht man es aus der Gruppe heraus und legt es auf die Benennung (label) des Dokuments oben in der [Baumansicht](Tree_view/de.md) ab.

Siehe [Std Gruppe](Std_Group/de.md) für die vollständigen Informationen, einschließlich der Verwendung in [Skripten](Std_Group/de#Skripten.md).



## Eigenschaften

Eine [App DocumentObjectGroup](App_DocumentObjectGroup/de.md) (Klasse `App::DocumentObjectGroup`) wird von einem [App DocumentObject](App_DocumentObject/de.md) (Klasse `App::DocumentObject`) abgeleitet; daher besitzt es alle seine Eigenschaften.

Siehe die Eigenschaften auf der Seite [Std Gruppe](Std_Group/de.md).


{{Std Base navi

}} {{Document objects navi}}



---
⏵ [documentation index](../README.md) > App DocumentObjectGroup/de
