# App FeaturePython/de
{{TOCright}}



## Einleitung

Ein <img alt="" src=images/Feature.svg  style="width:32px;"> [App FeaturePython](App_FeaturePython/de.md)-Objekt oder formal ein `App::FeaturePython`, ist eine einfache Instanz des [App DocumentObject](App_DocumentObject/de.md) in [Python](Python/de.md).

Hierbei handelt es sich um ein einfaches Objekt, das standardmäßig nicht viele Eigenschaften hat, z.B. hat es keine [Positionierung](Placement/de.md) und keine [topologische Form](Part_TopoShape/de.md). Abhängig von den Eigenschaften, die ihm zugeordnet sind, kann es zur Verwaltung verschiedener Datentypen verwendet werden.

<img alt="" src=images/FreeCAD_core_objects.svg  style="width:800px;">



*Vereinfachtes Diagramm der Beziehungen zwischen den Kernobjekten in FreeCAD*



## Anwendung

Das [App FeaturePython](App_FeaturePython/de.md)-Objekt ist ein internes Objekt, so dass es nicht über die grafische Oberfläche erstellt werden kann. Es ist dazu gedacht, von ihm Unterklassen abzuleiten, die unterschiedliche Arten von Daten verarbeiten.

Beispielsweise sind die Elemente [Draft Text](Draft_Text/de.md), [Draft Maß](Draft_Dimension/de.md), und [Arbeitsebenen Proxy](Draft_WorkingPlaneProxy/de.md) des Arbeitsbereichs [Draft](Draft_Workbench/de.md) `App::FeaturePython`-Objekte mit einem benutzerdefinierten Symbol und zusätzlichen Eigenschaften. Sie enthalten Daten, aber keine tatsächliche [Part TopoForm](Part_TopoShape/de.md).

Wenn das gewünschte Objekt eine Positionierung, eine Form, einen Anhang oder andere komplexe Eigenschaften haben soll, ist es besser, eine der komplexeren Klassen zu erstellen, zum Beispiel [App GeoFeature](App_GeoFeature/de.md), [Part Feature](Part_Feature/de.md), oder [Part Part2DObject](Part_Part2DObject/de.md).



## Eigenschaften

Siehe [ Objekteigenschaften](Property/de.md) für alle Arten von Eigenschaften, die skriptgenerierte Objekte besitzen können.

Das [App FeaturePython](App_FeaturePython/de.md)-Objekt (Klasse `App::FeaturePython`) wird von einem [App DocumentObject](App_DocumentObject/de.md) (Klasse `App::DocumentObject`) abgeleitet und erbt alle seine Eigenschaften. Es besitzt einige zusätzliche Eigenschaften.

Diese Eigenschaften stehen im [Eigenschafteneditor](Property_editor/de.md) zur Verfügung. Versteckte Eigenschaften werden durch den Befehl **Alle anzeigen** im Kontextmenü des [Eigenschafteneditors](Property_editor/de.md) angezeigt.



### Daten


{{TitleProperty|Basis}}

-    {{PropertyData/de|Proxy|PythonObject|Hidden}}: Eine spezielle, mit diesem Objekt verbundene Klasse.

-    {{PropertyData/de|Label|String}}: Die vom Anwender editierbare Bezeichnung dieses Objekts; es ist eine beliebige UTF8-Zeichenfolge.

-    {{PropertyData/de|Label2|String}}: Eine längere, vom Anwender editierbare Beschreibung dieses Objekts; es ist eine beliebige UTF8-Zeichenfolge, die Zeilenumbrüche enthalten kann. Standardmäßig ist es eine leere Zeichenkette {{value|""}}.

-    {{PropertyData/de|Expression_Engine|ExpressionEngine|Hidden}}: Eine Liste von Ausdrücken. a list of expressions. Standardmäßig ist sie leer {{value|[]}}.

-    {{PropertyData/de|Visibility|Bool|Hidden}}: Bestimmt, ob das Objekt angezeigt werden soll oder nicht.



### Ansicht


{{TitleProperty|Basis}}

-    {{PropertyView/de|Proxy|PythonObject|Hidden}}: Eine spezielle [Viewprovider](Viewprovider/de.md)-Klasse, die mit diesem Objekt verbunden ist.


{{TitleProperty|Display Options}}

-    {{PropertyView/de|Display Mode|Enumeration}}: ist standardmäßig leer.

-    {{PropertyView/de|Show In Tree|Bool}}: die Standardeinstellung ist `True`; in diesem Fall erscheint das Objekt in der [Baumansicht](Tree_view/de.md). Andernfalls wird das Objekt in der Baumansicht ausgeblendet. Ist ein Objekt unsichtbar in der Baumansicht, kann es wieder sichtbar gemacht werden, indem das Kontextmenü über den Namen des Dokuments geöffnet wird (Rechtsklick) und {{CheckBox|TRUE|Ausgeblendete Elemente anzeigen}} ausgewählt wird. Dann kann das ausgeblendete Element ausgewählt und die {{PropertyView/de|Show In Tree}} wieder auf `True` zurückgesetzt werden.

-    {{PropertyView/de|Visibility|Bool}}: auf `True` voreingestellt. In diesem Fall ist das Objekt in der [3D-Ansicht](3D_view/de.md) sichtbar, wenn es eine [Form](Part_TopoShape/de.md) hat, andernfalls ist es unsichtbar. Standardmäßig kann diese Eigenschaft ein- und ausgeschaltet werden, indem das Objekt ausgewählt und die **Leertaste** gedrückt wird.


{{TitleProperty|Auswahl}}

-    {{PropertyView/de|On Top When Selected|Enumeration}}: Sie steuert die Art und Weise, wie die Auswahl in der [3D-Ansicht](3D_view/de.md) erfolgt, wenn das Objekt eine [Form](Part_TopoShape/de.md) hat und es viele Objekte gibt, die teilweise von anderen abgedeckt werden. Die Standardeinstellung ist {{value|Disabled}}, was bedeutet, dass keine besondere Hervorhebung erfolgt; {{value|Enabled}} bedeutet, dass das Objekt über jedem anderen Objekt erscheint, wenn es ausgewählt wird; {{value|Object}} bedeutet, dass das Objekt nur dann oben erscheint, wenn das gesamte Objekt in der [Baumansicht](Tree_view/de.md) ausgewählt wird; {{value|Element}} bedeutet, dass das Objekt nur dann oben erscheint, wenn ein Unterelement (Knoten, Kante, Fläche) in der [3D-Ansicht](3D_view/de.md) ausgewählt wird.

-    {{PropertyView/de|Selection Style|Enumeration}}: steuert die Art und Weise, wie das Objekt hervorgehoben wird, wenn es eine [Form](Part_TopoShape/de.md) hat. Ist es {{value|Shape}}, wird die gesamte Form (Knoten, Kanten und Flächen) in der [3D-Ansicht](3D_view/de.md) hervorgehoben; ist es {{value| BoundBox}}, erscheint ein Begrenzungsrahmen um das Objekt herum und wird hervorgehoben.



## Skripten


**Siehe auch:**

[FreeCAD Grundlagen Skripten](FreeCAD_Scripting_Basics/de.md) und [Skriptgenerierte Objekte](Scripted_objects/de.md).

Siehe [Part Formelement](Part_Feature/de.md) für die allgemeinen Informationen über das Hinzufügen von Objekten zum Dokument.

Ein App-FeaturePython-Objekt wird mit der Methode `addObject()` des Dokuments erstellt.


```python
import FreeCAD as App

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::FeaturePython", "Name")
obj.Label = "Custom label"
```


{{Document_objects_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > App FeaturePython/de
