# App DocumentObjectGroup/de


## Einleitung

<img alt="" src=images/Folder.svg  style="width:32px;">

Ein Objekt [Anwendung DokumentObjektGruppe](App_DocumentObjectGroup.md), formell eine `App::DocumentObjectGroup`, ist ein einfaches Element zur Gruppierung jedes [DokumentObjekt](App_DocumentObject/de.md)-Typs in der [Baumansicht](tree_view/de.md) aus jedem Datentyp.

Es wurde entwickelt, um Objekte in der [Baumansicht](tree_view/de.md) für den Anwender logisch zu organisieren.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten im Programm. Die`App::DocumentObjectGroup* Klasse hat eine Erweiterung zur Gruppierung jedes Objekttyps. Die Gruppe selbst hat wenig Eigenschaften.`

## Anwendung

1.  Die Schaltfläche **<img src=images/Std_Group.svg style="width:16px"> [Standard Gruppe](Std_Group/de.md)** betätigen. Eine leere Gruppe wird erzeugt.
2.  In der [Baumansicht](tree_view/de.md) ein Objekt wählen und durch Drag & Drop auf die Gruppe ziehen, um es der Gruppe hinzuzufügen.
3.  Um Objekte aus der Gruppe zu entfernen, zieht man es per Drag & Drop aus der Gruppe auf die Dokumentenbeschriftung oben in der [Baumansicht](tree_view/de.md).

Siehe [Standard Gruppe](Std_Group/de.md) zu vollständigen Informationen, einschließlich der Verwendung in [Skripten](Std_Group/de#Skripten.md).

## Eigenschaften

Eine [Anwendung DokumentObjektGruppe](App_DocumentObjectGroup/de.md) (`App::DocumentObjectGroup` Klasse) stammt aus einer [Anwendung DokumentObjekt](App_DocumentObject/de.md) (`App::DocumentObject` Klasse). Deshalb hat es die meisten Eigenschaften mit letzterem gemein.

Siehe die Eigenschaften auf der [Standard Gruppe](Std_Group/de.md) Seite.


{{Std Base navi

}} {{Document objects navi}} 
