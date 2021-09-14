# App DocumentObject/de

 {{TOCright}}

## Einführung

<img alt="" src=images/Px.svg  style="width:32px;">

Ein [Anwendung DokumentObjekt](App_DocumentObject/de.md) Objekt oder formal ein `App::DocumentObject` ist die Basisklasse aller im Dokument behandelten Objektklassen.

Allgemein ausgedrückt ist ein \"Dokumentobjekt\" jedes \"Ding\", das in der [Baumansicht](tree_view/de.md) erscheinen kann und das beim Öffnen eines Dokuments gespeichert und wiederhergestellt wird.

![](images/App_DocumentObject_example.png )


*Baumansicht, die verschiedene Objekte im Dokument anzeigt. Jedes von ihnen ist ein "Dokumentobjekt", das letztlich von der Basisklasse `App::DocumentObject* abgeleitet ist.`

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">


*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten im Programm. Die `App::DocumentObject* Klasse ist die Basisklasse von im Wesentlichen allen Objekten in der Software.`

## Anwendung

Das [Anwendung DokumentObjekt](App_DocumentObject/de.md) ist eine interne Klasse, kann also weder von der grafischen Oberfläche aus erstellt werden, noch ist sie für sich selbst gedacht. Sie definiert lediglich das grundlegende Verhalten und die Eigenschaften von Objekten in der Software.

Einige der wichtigsten DocumentObjects sind die folgenden:

-   Die Klasse [App FeaturePython](App_FeaturePython/de.md), ein leeres Objekt, das je nach den hinzugefügten Eigenschaften für verschiedene Zwecke verwendet werden kann.
-   Die Klasse [App GeoFeature](App_GeoFeature/de.md), das Basisobjekt aller geometrischen Objekte, d.h. von Objekten, die eine Eigenschaft [Platzierung](Placement/de.md) haben, die ihre Position in der [3D Ansicht](3D_view/de.md) definiert.
-   Die Klasse [Part Formelement](Part_Feature/de.md), abgeleitet von App GeoFeature, und die übergeordnete Klasse von Objekten mit 2D und 3D [topologische Formen](Part_TopoShape/de.md).
-   Die Klasse [Polygonnetz Formelement](Mesh_Feature/de.md), abgeleitet von App GeoFeature, und die übergeordnete Klasse von Objekten mit 2D und 3D [Polygonnetze](Mesh_MeshObject/de.md).

## Eigenschaften

Siehe [Eigenschaft](Property/de.md) für alle Eigenschaftstypen, die geskriptete Objekte haben können.

Dies sind die grundlegenden Eigenschaften, die im Wesentlichen alle Objekte haben. Auf diese Eigenschaften kann über die [Python Konsole](Python_console/de.md) zugegriffen werden.

-    {{PropertyData/de|Expression Engine|ExpressionEngine}}: eine Liste von Ausdrücken.

-    {{PropertyData/de|Label|String}}: der vom Benutzer editierbare Name dieses Objekts, es ist ein beliebiger UTF8-String. Standardmäßig ist es derselbe wie der `Name`.

-    {{PropertyData/de|Label2|String}}: eine längere, vom Benutzer editierbare Beschreibung dieses Objekts, es ist eine beliebige UTF8-Zeichenfolge, der Zeilenumbrüche enthalten kann. Standardmäßig ist es eine leere Zeichenfolge {{value|""}}.

-    {{PropertyData/de|Visibility|Bool}}: whether to display the object or not.

Für abgeleitete Objekte wird standardmäßig nur {{PropertyData/de|Label}} im [Eigenschafteneditor](property_editor/de.md) aufgelistet. Die anderen Eigenschaften werden ausgeblendet.

## Skripten


**Siehe auch:**

[FreeCAD Skripten Grundlagen](FreeCAD_Scripting_Basics/de.md), und [geskriptete Objekte](scripted_objects/de.md).

Siehe [Part Formelement](Part_Feature/de.md) für die allgemeinen Informationen über das Hinzufügen von Objekten zum Programm.

Ein DokumentObjekt wird mit der `addObject()` Methode des Dokuments erstellt. Im Allgemeinen ist es jedoch nicht erforderlich, dieses Objekt zu erstellen. In der Regel ist es besser, eine der komplexeren Klassen unterzuordnen, z.B. [App FeaturePython](App_FeaturePython/de.md), [App GeoFeature](App_GeoFeature/de.md), [Part Formelement](Part_Feature/de.md), [Part Teil2DObjekt](Part_Part2DObject/de.md), usw.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::DocumentObject", "Name")
obj.Label = "Custom label"
```


{{Document objects navi

}} 
