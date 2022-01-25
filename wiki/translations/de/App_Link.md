# App Link/de
{{TOCright}}

## Einführung

<img alt="" src=images/Link.svg  style="width:32px;">

Eine [Anwendungsverknüpfung](App_Link/de.md) oder formal ein `App::Link`, ist ein Objekttyp, der auf ein anderes Objekt im selben Dokument oder in einem anderen Dokument verweist oder auf ein anderes Objekt verknüpft. Es wurde speziell entwickelt, um ein einzelnes Objekt effizient mehrfach zu duplizieren, was bei der Erstellung komplexer [Baugruppen](assembly/de.md) aus kleineren Unterbaugruppen und aus mehreren wiederverwendbaren Komponenten wie Schrauben, Muttern und ähnlichen Verbindungselementen hilfreich ist.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten im Programm. Das  `App::Link* Objekt ist eine Kernkomponente des Systems, es ist von keinem Arbeitsbereich abhängig, aber es kann mit den meisten Objekten verwendet werden, die in allen Arbeitsbereichen erstellt werden.`

## Anwendung

1.  Wähle ein Objekt in der [Baumansicht](tree_view/de.md) oder [3D Ansichtfür](3D_view/de.md) die du eine Verknüpfung erstellen möchtest.
2.  Drücke die **[<img src=images/Std_LinkMake.svg style="width:16px"> [Std LinkMake](Std_LinkMake.md)** Schaltfläche. Das produzierte Objekt hat dasselbe Symbol wie das Originalobjekt, ist jedoch mit einem Pfeil überlagert, der darauf hinweist, dass es sich um eine Verknüpfung handelt.

Siehe die [Std VerknüpfungErstellen](Std_LinkMake/de.md) Seite für die vollständige Informationen, einschließlich der Verwendung in [Skripten](Std_Part/de#Skripten.md).

## Eigenschaften

Eine [Anwendungsverknüpfung](App_Link.md) (`App::Link` Klasse) wird aus der [Anwendung DokumentObjekt](App_DocumentObject/de.md) (`App::DocumentObject` Klasse) abgeleitet. Daher haben sie die meisten gleichen Eigenschaften.

Siehe die vollständige Liste der Eigenschaften auf der [Std VerknüpfungHerstellen](Std_LinkMake/de.md) Seite.


{{Std Base navi

}} {{Document objects navi}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > App Link/de
