# App DocumentObject/de
{{TOCright}}

## Einleitung

<img alt="" src=images/Px.svg  style="width:32px;">

Ein [App DocumentObject](App_DocumentObject/de.md) oder formal ein `App::DocumentObject` ist die Basisklasse aller im Dokument behandelten Objektklassen.

Allgemein ausgedrückt ist ein \"DocumentObject\" jedes \"Ding\", das in der [Baumansicht](Tree_view/de.md) erscheinen kann und das gespeichert und beim Öffnen eines Dokuments wiederhergestellt wird.

![](images/App_DocumentObject_example.png )



*Baumansicht, die verschiedene Objekte im Dokument anzeigt. Jedes von ihnen ist ein "Dokumentobjekt", das letztlich von der Basisklasse `App::DocumentObject* abgeleitet ist.`

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten in FreeCAD*

## Anwendung

Das [App DocumentObject](App_DocumentObject/de.md) ist eine interne Klasse, kann also weder von der grafischen Oberfläche aus erstellt werden, noch ist sie für sich selbst gedacht. Sie definiert lediglich das grundlegende Verhalten und die Eigenschaften von Objekten im Programm.

Einige der wichtigsten DocumentObjects sind die folgenden:

-   Die Klasse [App FeaturePython](App_FeaturePython/de.md), ein leeres Objekt, das je nach den hinzugefügten Eigenschaften für verschiedene Zwecke verwendet werden kann.
-   Die Klasse [App GeoFeature](App_GeoFeature/de.md), das Basisobjekt aller geometrischen Objekte, d.h. von Objekten, die eine Eigenschaft [Placement](Placement/de.md) haben, die ihre Position in der [3D-Ansicht](3D_view/de.md) definiert.
-   Die Klasse [Part Feature](Part_Feature/de.md) (Part Formelement), abgeleitet von App GeoFeature, und die übergeordnete Klasse von Objekten mit 2- und 3-dimensionalen [topologischen Formen](Part_TopoShape/de.md).
-   Die Klasse [Mesh Feature](Mesh_Feature/de.md) (Mesh Formelement), abgeleitet von App GeoFeature, und die übergeordnete Klasse von Objekten mit 2D- und 3D-[Polygonnetzen](Mesh_MeshObject/de.md).

## Eigenschaften

Siehe [Eigenschaft](Property/de.md) für alle Eigenschaftstypen, die geskriptete Objekte haben können.

Dies sind die grundlegenden Eigenschaften, die im Wesentlichen alle Objekte haben. Auf diese Eigenschaften kann über die [Python Konsole](Python_console/de.md) zugegriffen werden.

-    {{PropertyData/de|Label|String}}: Der vom Benutzer editierbare Name dieses Objekts, es ist ein beliebiger UTF8-String. Standardmäßig ist es derselbe wie der `Name`.

-    {{PropertyData/de|Label2|String}}: Eine längere, vom Benutzer editierbare Beschreibung dieses Objekts, es ist eine beliebige UTF8-Zeichenfolge, die Zeilenumbrüche enthalten kann. Standardmäßig ist es eine leere Zeichenfolge {{value|""}}.

-    {{PropertyData/de|Expression Engine|ExpressionEngine}}: Eine Liste von Ausdrücken.

-    {{PropertyData/de|Visibility|Bool}}: Entscheidet, ob das Objekt dargestellt werden soll oder nicht.

Für abgeleitete Objekte wird standardmäßig nur {{PropertyData/de|Label}} im [Eigenschafteneditor](property_editor/de.md) aufgelistet. Die anderen Eigenschaften werden ausgeblendet.

## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md), und [geskriptete Objekte](scripted_objects/de.md).

Siehe [Part Formelement](Part_Feature/de.md) für die allgemeinen Informationen über das Hinzufügen von Objekten zum Dokument.

Ein DocumentObject wird mit der Methode `addObject()` des Dokuments erstellt. Im Allgemeinen ist es jedoch nicht erforderlich, dieses Objekt von Hand zu erstellen. In der Regel ist es besser, eine der komplexeren Klassen unterzuordnen, z.B. [App FeaturePython](App_FeaturePython/de.md), [App GeoFeature](App_GeoFeature/de.md), [Part Feature](Part_Feature/de.md), [Part Part2DObjekt](Part_Part2DObject/de.md), usw.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::DocumentObject", "Name")
obj.Label = "Custom label"
```


{{Document_objects_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > App DocumentObject/de
